"""
agents/scout.py
Tobias — Scout Agent (14:00 UTC)

Responsibilities:
  1. Load current scout_skills.md (Analyst-maintained criteria)
  2. Fetch tonight's NBA slate via ESPN
  3. Fetch Betano odds via OddsPapi (+ DDG fallback)
  4. Fetch injuries + standings for context
  5. Call LLM to research and draft picks (no stakes committed yet)
  6. Validate all draft pick objects (all fields required)
  7. Store first_game_time for commit self-gating
  8. Write state + history + data.js to GitHub
  9. Append to audit/scout_log.jsonl
"""

import json
import re
import logging
from datetime import datetime, date, timezone

from core.llm import call_llm, call_llm_full, extract_tag, agent_model_name
from core.espn import fetch_scoreboard, fetch_injuries, fetch_standings, fetch_first_game_time_utc
from core.odds import fetch_betano_nba_odds, format_odds_for_prompt
from core.validators import validate_all_drafts, ValidationError

log = logging.getLogger(__name__)

# ── System prompt ──────────────────────────────────────────────────────────────

SCOUT_SYSTEM = """You are the Scout agent for Tobias, an autonomous NBA betting simulation.
You research tonight's NBA slate and draft picks for consideration.
NO stakes are committed in this phase — you only identify opportunities.
Stakes are committed at the Commit phase, 15 minutes before tip-off.

Read the skills file carefully — the Analyst updates it daily based on what is working.
Follow it precisely. It is your primary decision-making guide.

CRITICAL FORMATTING RULE: Your response MUST end with these exact XML tags.
No exceptions. Even if you find zero picks, output <draft_picks>[]</draft_picks>.
The system will FAIL and no picks will be saved if these tags are missing."""


def _build_scout_prompt(skills: str, games_text: str, odds_text: str,
                         injuries_text: str, standings_text: str,
                         state: dict, today: str) -> str:
    bankroll = state["bankroll"]
    season   = state["season"]
    game_n   = state["game"]

    return f"""## YOUR SKILLS (follow these criteria exactly)
{skills}

## TODAY: {today} | Season: {season} | Game: {game_n}
## BANKROLL: €{bankroll:.2f}

## TONIGHT'S NBA SLATE
{games_text}

## BETANO ODDS
{odds_text}

## INJURY REPORTS
{injuries_text}

## STANDINGS
{standings_text}

---

Research the slate above and produce draft picks.
Apply your skills criteria strictly. Only draft picks with confidence ≥ 40.
Draft 0 picks if nothing meets the bar — that is a valid result.

For each draft pick, you MUST include ALL fields:
  id, match, time, pick, odds, stake, potential_return,
  confidence, reasoning, anchor_players, drafted_at

Match string convention: always "HOME TEAM vs AWAY TEAM" (home first).
Pick: "Team Name ML" or "Team Name -X.X" or "Over X.X" etc.
Odds: decimal format (Betano style).
Stake: calculated from confidence tier and current bankroll (€{bankroll:.2f}).
Drafted_at: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}

Draft pick IDs: nba_draft_{today.replace('-','')}_{'{001, 002...}'}

IMPORTANT: You MUST end your response with ALL FOUR of these XML tags in this exact format.
Do not add any text after the closing </scout_report> tag.

<draft_picks>
[JSON array of draft pick objects — use [] if no picks meet criteria]
</draft_picks>

<first_game_time>
[ISO 8601 UTC of first tip-off, e.g. 2026-03-15T00:00:00Z]
</first_game_time>

<rejected_games>
[JSON array of games you reviewed but did NOT draft, format:
{{"match": "HOME vs AWAY", "reason": "why not picked (e.g. odds out of range, both teams tanking, confidence below 40, etc.)"}}
Use [] if all games were drafted or if no games tonight.]
</rejected_games>

<scout_report>
Write a structured scouting report covering EVERY game on tonight's slate.
For each game use this format:

### HOME vs AWAY
- **Edge assessment:** [why value exists or why it doesn't]
- **Key factors:** [B2B, injuries, tanking status, form, odds range]
- **Decision:** DRAFTED [pick @ odds] | REJECTED [reason] | NO EDGE [reason]

End with a brief summary of tonight's overall slate quality.
Even if 0 picks were drafted, the full per-game breakdown is required.
</scout_report>
"""


# ── Context builders ───────────────────────────────────────────────────────────

def _games_text(games: list[dict]) -> str:
    if not games:
        return "No games found for tonight."
    lines = []
    for g in games:
        t = g.get("time", "")[:16]
        lines.append(f"{g['away']} @ {g['home']}  |  {t} UTC  |  {g.get('venue','')}")
    return "\n".join(lines)


def _injuries_text(injuries: dict) -> str:
    if not injuries:
        return "No injury reports available."
    lines = []
    for team, players in injuries.items():
        notable = [p for p in players
                   if p["status"] in ("Out", "Doubtful", "Questionable", "Game-Time Decision")]
        if notable:
            parts = []
            for p in notable[:4]:
                parts.append(f"{p['name']} ({p['pos']}, {p['status']})")
            lines.append(f"{team}: {', '.join(parts)}")
    return "\n".join(lines[:30]) if lines else "No notable injuries."


def _standings_text(standings: dict) -> str:
    seen = set()
    rows = []
    for name, s in standings.items():
        if len(name) <= 3 or name in seen:
            continue
        seen.add(name)
        rows.append((int(s.get("wins", 0)), int(s.get("losses", 0)), name, s))
    rows.sort(key=lambda x: -x[0])
    lines = []
    for w, l, name, s in rows[:30]:
        l10 = s.get("l10", "")
        lines.append(f"{name}: {w}-{l}  L10:{l10}")
    return "\n".join(lines)


# ── Same-day guard ─────────────────────────────────────────────────────────────

def _already_scouted_today(state: dict, today: str) -> bool:
    """Return True if draft picks already exist for today."""
    for pick in state.get("draft_picks", []):
        if pick.get("drafted_at", "")[:10] == today:
            return True
    return False


# ── Main run ───────────────────────────────────────────────────────────────────

def run(store) -> None:
    now     = datetime.now(timezone.utc)
    now_iso = now.isoformat()
    today   = now.strftime("%Y-%m-%d")
    llm     = agent_model_name("scout")

    # ── 1. Load state ──────────────────────────────────────────────────────────
    state, history = store.read_state_and_history()

    # ── 2. Same-day guard ─────────────────────────────────────────────────────
    if _already_scouted_today(state, today):
        log.info(f"Scout: draft picks already exist for {today} — skipping")
        return

    # ── 3. Load skills ────────────────────────────────────────────────────────
    skills = store.read_md("scout_skills")
    if not skills:
        log.warning("Scout: scout_skills.md is empty — using defaults")

    # ── 4. Fetch data ─────────────────────────────────────────────────────────
    log.info("Scout: fetching NBA data…")
    games     = fetch_scoreboard()
    injuries  = fetch_injuries()
    standings = fetch_standings()
    odds      = fetch_betano_nba_odds()
    first_game_time = fetch_first_game_time_utc()

    if not games:
        log.warning("Scout: no games found tonight — writing no-games state")
        state["scout_status"]     = "no_games"
        state["scout_updated_at"] = now_iso
        state["last_updated"]     = now_iso
        store.write_json("state", state, f"scout: no games {today}")
        store.write_data_js(state, history, config=store.read_config())
        return

    # ── 5. Build prompt ───────────────────────────────────────────────────────
    games_str    = _games_text(games)
    odds_str     = format_odds_for_prompt(odds)
    injuries_str = _injuries_text(injuries)
    standings_str = _standings_text(standings)

    log.info(f"Scout: {len(games)} games | odds source: {odds[0].get('odds_source','?') if odds else 'none'}")

    # ── 6. Call LLM ───────────────────────────────────────────────────────────
    log.info("Scout: calling LLM…")
    llm_result = None
    try:
        llm_result = call_llm_full(
            SCOUT_SYSTEM,
            _build_scout_prompt(skills, games_str, odds_str, injuries_str,
                                 standings_str, state, today),
            max_tokens=4096,
            agent="scout",
        )
        raw = llm_result.text
    except Exception as e:
        log.error(f"Scout: LLM call failed: {e}")
        state["scout_status"] = "unavailable"
        state["scout_error"]  = str(e)
        state["last_updated"] = now_iso
        store.write_json("state", state, f"scout: LLM error {today}")
        _append_audit(store, now_iso, state.get("llm_provider","claude"),
                      error=str(e), bankroll=state["bankroll"])
        store.write_data_js(state, history, config=store.read_config())
        return

    # ── 7. Extract tags ────────────────────────────────────────────────────────
    draft_raw     = extract_tag(raw, "draft_picks")
    fgt_raw       = extract_tag(raw, "first_game_time")
    report_raw    = extract_tag(raw, "scout_report") or ""

    if draft_raw is None:
        log.error("Scout: <draft_picks> tag missing — retrying with stricter prompt")
        # One automatic retry with a simpler, more direct prompt
        try:
            retry_prompt = (
                f"CRITICAL: You forgot to include the required XML tags.\n"
                f"Today: {today} | Bankroll: €{state['bankroll']:.2f}\n\n"
                f"You MUST output EXACTLY these XML tags and nothing else:\n\n"
                f"<draft_picks>\n[]\n</draft_picks>\n\n"
                f"<first_game_time>\n{now_iso}\n</first_game_time>\n\n"
                f"<rejected_games>\n[]\n</rejected_games>\n\n"
                f"<scout_report>\nNo analysis available — retry required due to missing XML tags.\n</scout_report>\n\n"
                f"If you do have picks from your analysis, include them in draft_picks now. "
                f"Otherwise output empty arrays. DO NOT write anything except these XML tags."
            )
            retry_result = call_llm_full(SCOUT_SYSTEM, retry_prompt, max_tokens=2048, agent="scout")
            draft_raw = extract_tag(retry_result.text, "draft_picks")
            fgt_raw   = extract_tag(retry_result.text, "first_game_time") or fgt_raw
            report_raw = extract_tag(retry_result.text, "scout_report") or report_raw or ""
            if draft_raw is None:
                raise ValueError("Retry also missing <draft_picks>")
            log.info("Scout: retry succeeded")
        except Exception as retry_err:
            log.error(f"Scout: retry failed: {retry_err}")
            state["scout_status"] = "unavailable"
            state["scout_error"]  = "Missing <draft_picks> tag after retry"
            state["last_updated"] = now_iso
            store.write_json("state", state, f"scout: parse error {today}")
            llm_meta = llm_result.to_audit_dict() if llm_result else {}
            _append_audit(store, now_iso, state.get("llm_provider","claude"),
                          error="Missing <draft_picks> tag after retry",
                          bankroll=state["bankroll"], llm_meta=llm_meta)
            store.write_data_js(state, history, config=store.read_config())
            return

    # ── 8. Parse draft picks ──────────────────────────────────────────────────
    try:
        draft_picks = json.loads(draft_raw)
    except json.JSONDecodeError as e:
        log.error(f"Scout: draft_picks JSON invalid: {e}")
        state["scout_status"] = "unavailable"
        state["scout_error"]  = f"JSON parse error: {e}"
        state["last_updated"] = now_iso
        store.write_json("state", state, f"scout: JSON error {today}")
        store.write_data_js(state, history, config=store.read_config())
        return

    # ── 9. Validate picks ─────────────────────────────────────────────────────
    try:
        validate_all_drafts(draft_picks, "scout")
    except ValidationError as e:
        log.error(f"Scout: validation failed: {e}")
        state["scout_status"] = "unavailable"
        state["scout_error"]  = str(e)
        state["last_updated"] = now_iso
        store.write_json("state", state, f"scout: validation error {today}")
        store.write_data_js(state, history, config=store.read_config())
        return

    # ── 10. Determine first_game_time ─────────────────────────────────────────
    fgt = fgt_raw or first_game_time
    if fgt:
        state["first_game_time"] = fgt
    log.info(f"Scout: first game time = {fgt}")

    # ── 11. Update state ──────────────────────────────────────────────────────
    state["draft_picks"]      = draft_picks
    state["agent_models"] = state.get("agent_models", {})
    state["agent_models"]["scout"] = llm
    state["scout_status"]     = "live"
    # Store rejected games for dashboard display
    try:
        state["rejected_games"] = json.loads(rejected_raw) if rejected_raw else []
    except Exception:
        state["rejected_games"] = []
    state["scout_error"]      = ""
    state["scout_updated_at"] = now_iso
    state["commit_status"]    = "pending"   # reset for today's commit
    state["last_updated"]     = now_iso
    state["last_report"]      = report_raw

    log.info(f"Scout: {len(draft_picks)} draft picks drafted")
    for p in draft_picks:
        log.info(f"  📋 {p['match']} — {p['pick']} @ {p['odds']} (conf={p['confidence']})")

    # ── 12. Validate & write ──────────────────────────────────────────────────
    commit_msg = f"scout: {len(draft_picks)} draft picks for {today}"
    store.write_json("state",   state,   commit_msg)
    store.write_json("history", history, commit_msg)

    # ── 13. Audit log ─────────────────────────────────────────────────────────
    _append_audit(store, now_iso, llm, state, history, report_raw,
                  draft_count=len(draft_picks),
                  picks=[{"id": p["id"], "match": p["match"],
                          "pick": p["pick"], "odds": p["odds"],
                          "confidence": p["confidence"]}
                         for p in draft_picks],
                  first_game_time=fgt or "",
                  odds_source=odds[0].get("odds_source", "?") if odds else "none",
                  bankroll=state["bankroll"],
                  llm_meta=llm_result.to_audit_dict() if llm_result else {})

    log.info(f"Scout done — {len(draft_picks)} picks | first game: {fgt}")


def _append_audit(store, ts, llm, state, history, report_raw="",
                  draft_count=0, picks=None,
                  first_game_time="", odds_source="", bankroll=0, error="",
                  llm_meta=None):
    entry = {
        "ts":               ts,
        "agent":            "scout",
        "llm":              llm,
        "draft_count":      draft_count,
        "picks":            picks or [],
        "first_game_time":  first_game_time,
        "odds_source":      odds_source,
        "bankroll":         round(bankroll, 2),
        "error":            error,
        **(llm_meta or {}),
    }
    try:
        store.append_jsonl("scout_log", entry)
    except Exception as e:
        log.warning(f"Scout audit log failed: {e}")
    store.write_data_js(state, history, scout_report=report_raw, config=store.read_config())
