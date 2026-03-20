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
from core.espn import fetch_scoreboard, fetch_injuries, fetch_standings, fetch_first_game_time_utc, fetch_advanced_stats, fetch_netrtg_l15, format_advanced_stats_for_prompt
from core.nba_injuries import fetch_official_nba_injuries
from core.odds import fetch_betano_nba_odds, format_odds_for_prompt, odds_available, get_odds_failure_reasons
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
                         advanced_stats: str, netrtg_l15_text: str,
                         injuries_source: str,
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
Source: {injuries_source}
{injuries_text}

## STANDINGS
{standings_text}

## ADVANCED STATS (OffRtg / DefRtg / NetRtg / Pace — tonight's teams only)
{advanced_stats}

---

Research the slate above and produce draft picks.
Apply your skills criteria strictly. Only draft picks with confidence ≥ 40.
Draft 0 picks if nothing meets the bar — that is a valid result.

For each draft pick, you MUST include ALL fields:
  id, match, time, pick, odds, stake, potential_return,
  confidence, reasoning, anchor_players, drafted_at, market_type

market_type: "ml" | "spread" | "total"
  - "ml" = moneyline (Team X to win)
  - "spread" = ATS (Team X -7.5 or +7.5)
  - "total" = over/under (Over/Under X.X)

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
[REQUIRED — JSON array for EVERY game NOT drafted.
Format: {{"match": "HOME vs AWAY", "reason": "brief", "ml_home": 1.85, "ml_away": 2.10, "decision": "rejected|anomaly|no_edge|deferred"}}
Use [] only if ALL games were drafted. Every non-drafted game MUST appear here.]
</rejected_games>

<scout_report>
Write a structured scouting report covering EVERY game listed in TONIGHT'S GAMES above.
Use the ESPN slate as the authoritative game list — not the odds feed (odds may be incomplete).

For each game use this format:

### HOME vs AWAY
- **Edge assessment:** [value exists or not]
- **Key factors:** [B2B, injuries, tanking status, form, line]
- **Odds:** [list available odds or "no odds available for this game"]
- **Decision:** DRAFTED [pick @ odds] | REJECTED [reason] | NO ODDS — DEFERRED | NO EDGE [reason]

End with a 3-5 sentence summary of tonight's overall slate quality.
ALL games must appear — missing a game from the report is not acceptable.
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
    games        = fetch_scoreboard()
    adv_stats    = fetch_advanced_stats()
    # NetRtg L15 — use Analyst-cached value if available (saves 30 API calls)
    # If Analyst hasn't run yet today, fetch fresh
    netrtg_l15 = state.get("netrtg_l15") or {}
    if not netrtg_l15:
        log.info("Scout: NetRtg L15 not in state — fetching fresh")
        netrtg_l15 = fetch_netrtg_l15()
    else:
        log.info(f"Scout: NetRtg L15 loaded from state ({len(netrtg_l15)} teams)")
    # Primary: NBA official injury report (PDFs updated every 15min, legally required)
    injuries = fetch_official_nba_injuries()
    if not injuries:
        log.warning("Scout: NBA official injuries unavailable — falling back to ESPN")
        injuries = fetch_injuries()
        injuries_source = "espn"
    else:
        injuries_source = "nba_official"
    standings = fetch_standings()
    odds      = fetch_betano_nba_odds()
    odds_failures = get_odds_failure_reasons()  # capture before anything else
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
    if injuries_source == "nba_official":
        from core.nba_injuries import format_injuries_for_prompt as _fmt_official
        tonight_teams = [g["home"] for g in games] + [g["away"] for g in games]
        injuries_str = _fmt_official(injuries, tonight_teams=tonight_teams)
    else:
        injuries_str = _injuries_text(injuries)
    standings_str = _standings_text(standings)

    adv_str       = format_advanced_stats_for_prompt(adv_stats, games)
    adv_available = bool(adv_stats)
    # Format NetRtg L15 for prompt
    netrtg_l15_str = _format_netrtg_l15_for_prompt(netrtg_l15, games) if netrtg_l15 else ""
    if not adv_available:
        log.warning("Scout: advanced stats unavailable — session limited to ML only (spreads/totals banned)")
        adv_str = "ADVANCED STATS UNAVAILABLE — ML only session. Spreads and totals cannot be evaluated."
    log.info(f"Scout: {len(games)} games | odds source: {odds[0].get('odds_source','?') if odds else 'none'} | adv_stats: {'ok' if adv_available else 'MISSING'}")

    # ── 6. Call LLM ───────────────────────────────────────────────────────────
    log.info("Scout: calling LLM…")
    llm_result = None
    try:
        llm_result = call_llm_full(
            SCOUT_SYSTEM,
            _build_scout_prompt(skills, games_str, odds_str, injuries_str,
                                 standings_str, adv_str, injuries_source, state, today),
            max_tokens=12000,
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
    rejected_raw  = extract_tag(raw, "rejected_games")
    retry_count   = 0  # will increment if retries needed

    if draft_raw is None:
        log.error("Scout: <draft_picks> tag missing — attempting retries")
        prompt_full = _build_scout_prompt(skills, games_str, odds_str, injuries_str,
                                           standings_str, adv_str, netrtg_l15_str,
                                           injuries_source, state, today)
        prompt_minimal = (
            f"You are the Scout agent. Today: {today} | Bankroll: €{state['bankroll']:.2f}\n"
            f"Output ONLY these XML tags — nothing else before or after:\n\n"
            f"<scout_report>\n[2-3 sentence summary of tonight slate]\n</scout_report>\n\n"
            f"<draft_picks>\n[JSON array of picks, or [] if none]\n</draft_picks>\n\n"
            f"<first_game_time>\n[ISO UTC of first tip-off]\n</first_game_time>\n\n"
            f"<rejected_games>\n[]\n</rejected_games>"
        )
        retries = [
            ("Attempt 2 — full prompt", prompt_full, 10000),
            ("Attempt 3 — minimal prompt", prompt_minimal, 2048),
        ]
        succeeded = False
        retry_count = 0
        for attempt_label, retry_prompt, retry_tokens in retries:
            retry_count += 1
            try:
                log.info(f"Scout: {attempt_label}")
                retry_result = call_llm_full(SCOUT_SYSTEM, retry_prompt,
                                             max_tokens=retry_tokens, agent="scout")
                draft_raw_r = extract_tag(retry_result.text, "draft_picks")
                if draft_raw_r is not None:
                    draft_raw  = draft_raw_r
                    fgt_raw    = extract_tag(retry_result.text, "first_game_time") or fgt_raw
                    new_report   = extract_tag(retry_result.text, "scout_report") or ""
                    new_rejected = extract_tag(retry_result.text, "rejected_games")
                    if new_rejected is not None:
                        rejected_raw = new_rejected
                    # Only use retry report if it's not the fallback placeholder
                    FALLBACK_MSG = "No analysis available"
                    if new_report and FALLBACK_MSG not in new_report:
                        report_raw = new_report
                    elif not report_raw or FALLBACK_MSG in report_raw:
                        report_raw = ""  # blank is better than the error string
                    # accumulate tokens
                    if llm_result:
                        llm_result.tokens_in  += retry_result.tokens_in
                        llm_result.tokens_out += retry_result.tokens_out
                        llm_result.cost_usd   += retry_result.cost_usd
                    else:
                        llm_result = retry_result
                    log.info(f"Scout: {attempt_label} succeeded")
                    succeeded = True
                    break
                log.warning(f"Scout: {attempt_label} — still missing <draft_picks>")
            except Exception as e:
                log.warning(f"Scout: {attempt_label} failed: {e}")

        if not succeeded:
            log.error("Scout: all 3 attempts failed — giving up")
            state["scout_status"] = "unavailable"
            state["scout_error"]  = "Missing <draft_picks> tag after 3 attempts"
            state["last_updated"] = now_iso
            store.write_json("state", state, f"scout: parse error {today}")
            llm_meta = llm_result.to_audit_dict() if llm_result else {}
            _append_audit(store, now_iso, llm, state, history, "",
                          error="Missing <draft_picks> after 3 attempts",
                          bankroll=state["bankroll"],
                          retry_count=retry_count,
                          llm_meta=llm_meta)
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
    state["scout_odds_source"]= odds[0].get("odds_source", "none") if odds else "none"
    state["scout_status"]     = "live"
    # Store full scout report data — persists even after commit clears draft_picks
    state["scout_report_data"] = {
        "date":             today,
        "picks":            draft_picks,
        "rejected":         json.loads(rejected_raw) if rejected_raw else [],
        "report":           report_raw,
        "odds_source":      odds[0].get("odds_source", "none") if odds else "none",
        "injuries_source":  injuries_source,
        "updated_at":       now_iso,
    }
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
        log.info(f"  PICK: {p['match']} — {p['pick']} @ {p['odds']} (conf={p['confidence']})")

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
                  injuries_source=injuries_source,
                  bankroll=state["bankroll"],
                  retry_count=retry_count,
                  odds_failures=odds_failures,
                  llm_meta=llm_result.to_audit_dict() if llm_result else {})

    # ── 14. Store report for Scout tab history ───────────────────────────────
    report_entry = {
        "ts":          now_iso,
        "date":        today,
        "llm":         llm,
        "odds_source": odds[0].get("odds_source", "?") if odds else "none",
        "draft_count": len(draft_picks),
        "picks":       draft_picks,
        "rejected":    state.get("rejected_games", []),
        "report":      report_raw,
        "retries":     retry_count,
        **(llm_result.to_audit_dict() if llm_result else {}),
    }
    try:
        store.append_report("scout", report_entry)
    except Exception as e:
        log.warning(f"Scout: failed to store report: {e}")

    log.info(f"Scout done — {len(draft_picks)} picks | first game: {fgt}")


def _append_audit(store, ts, llm, state, history, report_raw="",
                  draft_count=0, picks=None,
                  first_game_time="", odds_source="", bankroll=0, error="",
                  retry_count=0, odds_failures=None, injuries_source="unknown",
                  llm_meta=None):
    entry = {
        "ts":               ts,
        "agent":            "scout",
        "llm":              llm,
        "draft_count":      draft_count,
        "picks":            picks or [],
        "first_game_time":  first_game_time,
        "odds_source":      odds_source,
        "odds_failures":    odds_failures or [],
        "injuries_source":  injuries_source,
        "bankroll":         round(bankroll, 2),
        "error":            error,
        "retries":          retry_count,
        **(llm_meta or {}),
    }
    try:
        store.append_jsonl("scout_log", entry)
    except Exception as e:
        log.warning(f"Scout audit log failed: {e}")
    store.write_data_js(state, history, scout_report=report_raw, config=store.read_config())
