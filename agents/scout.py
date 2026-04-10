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
from core.espn import fetch_scoreboard, fetch_injuries, fetch_standings, fetch_first_game_time_utc, fetch_advanced_stats, format_advanced_stats_for_prompt
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
                         advanced_stats: str,
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

OUTPUT RULE: Write the XML tags FIRST — no preamble, no analysis before the first tag.
Tags must appear in this exact order:

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
Brief summary only — slate quality, total picks drafted, key themes. 3-5 lines max.
DO NOT describe individual picks here — they are in draft_picks JSON above.
DO NOT list rejected games here — they are in rejected_games JSON above.
</scout_report>

CONSISTENCY CHECK (CRITICAL): Every pick you decide to draft MUST be in <draft_picks> JSON.
Picks written only in <scout_report> are silently lost — they will never be committed.
Before closing <draft_picks>, verify it contains every pick you intend to place.
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


def _standings_text(standings: dict, tonight_teams: list | None = None) -> str:
    seen = set()
    rows = []
    for name, s in standings.items():
        if len(name) <= 3 or name in seen:
            continue
        seen.add(name)
        rows.append((int(s.get("wins", 0)), int(s.get("losses", 0)), name, s))
    rows.sort(key=lambda x: -x[0])
    all_names = [r[2] for r in rows]
    # Include: tonight's teams + top-5 + bottom-5 for conf context
    include = set(tonight_teams or []) | set(all_names[:5]) | set(all_names[-5:])
    lines = []
    for w, l, name, s in rows:
        if name in include:
            l10 = s.get("l10", "")
            lines.append(f"{name}: {w}-{l}  L10:{l10}")
    return "\n".join(lines)


# ── L15 NetRtg from stored game log ────────────────────────────────────────────

def _compute_netrtg_l15(team_game_log: dict) -> dict:
    """
    Compute approximate L15 NetRtg from Settler-maintained game log.
    1pt avg margin ≈ 2.85 NetRtg points (empirical NBA calibration).
    Requires ≥5 games to return a value.
    """
    result = {}
    for team, margins in team_game_log.items():
        last15 = margins[-15:]
        if len(last15) >= 5:
            result[team] = round(sum(last15) / len(last15) * 2.85, 1)
    return result


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
    # NetRtg L15 — computed from Settler-maintained game log (no API calls)
    netrtg_l15 = _compute_netrtg_l15(state.get("team_game_log", {}))
    if netrtg_l15:
        log.info(f"Scout: NetRtg L15 computed from game log ({len(netrtg_l15)} teams)")
    else:
        log.info("Scout: NetRtg L15 not yet available (game log accumulating)")
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
    # Filter odds to tonight's ESPN slate only — The-Odds-API returns all upcoming
    # games (no date filter), so without this LLM would analyse tomorrow's games too.
    tonight_teams_set = {g["home"].lower() for g in games} | {g["away"].lower() for g in games}
    odds_tonight = [o for o in odds if o.get("home","").lower() in tonight_teams_set
                    or o.get("away","").lower() in tonight_teams_set]
    if len(odds_tonight) < len(odds):
        log.info(f"Scout: odds filtered {len(odds)} -> {len(odds_tonight)} games (tonight's ESPN slate only)")
    # Re-align home/away in odds to match ESPN — The-Odds-API sometimes swaps them.
    # ESPN is authoritative for venue/home assignment.
    espn_home_map = {g["home"].lower(): g["home"] for g in games}
    espn_away_map = {g["away"].lower(): g["away"] for g in games}
    aligned_odds = []
    for o in odds_tonight:
        oh, oa = o.get("home",""), o.get("away","")
        # Check if The-Odds-API has home/away swapped vs ESPN
        if oh.lower() in espn_away_map and oa.lower() in espn_home_map:
            # Swap: flip home/away and their respective ML/spread odds
            log.info(f"Scout: odds home/away swapped for '{oh} vs {oa}' — re-aligning to ESPN")
            o = {**o,
                 "home": oa, "away": oh,
                 "ml_home_dec": o.get("ml_away_dec"), "ml_away_dec": o.get("ml_home_dec"),
                 "spread": o.get("spread") and -o["spread"],
                 "spread_odds_home": o.get("spread_odds_away"), "spread_odds_away": o.get("spread_odds_home"),
            }
        aligned_odds.append(o)
    odds_str     = format_odds_for_prompt(aligned_odds)
    if injuries_source == "nba_official":
        from core.nba_injuries import format_injuries_for_prompt as _fmt_official
        tonight_teams = [g["home"] for g in games] + [g["away"] for g in games]
        injuries_str = _fmt_official(injuries, tonight_teams=tonight_teams)
    else:
        injuries_str = _injuries_text(injuries)
    tonight_teams = [g["home"] for g in games] + [g["away"] for g in games]
    standings_str = _standings_text(standings, tonight_teams=tonight_teams)

    adv_str       = format_advanced_stats_for_prompt(adv_stats, games, netrtg_l15 or None)
    adv_available = bool(adv_stats)
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
                                 standings_str, adv_str,
                                 injuries_source, state, today),
            max_tokens=14000,
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
                      state, history,
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
                                           standings_str, adv_str,
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
            ("Attempt 2 — full prompt", prompt_full, 6000),
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

    # ── 8b. Enforce confidence threshold ─────────────────────────────────────
    before_filter = len(draft_picks)
    draft_picks = [p for p in draft_picks if p.get("confidence", 0) >= 40]
    if len(draft_picks) < before_filter:
        log.info(f"Scout: dropped {before_filter - len(draft_picks)} picks below confidence 40")

    # ── 8c. Fix LLM inconsistencies ───────────────────────────────────────────
    bankroll = state["bankroll"]
    for p in draft_picks:
        # Correct market_type from pick text if LLM contradicted itself
        pick_lower = (p.get("pick") or "").lower()
        if " ml" in pick_lower or pick_lower.endswith(" ml"):
            p["market_type"] = "ml"
        elif any(x in pick_lower for x in ["-", "+", "spread", "ats"]):
            p["market_type"] = "spread"
        elif any(x in pick_lower for x in ["over", "under", "o/u"]):
            p["market_type"] = "total"
        # Recalculate stake if LLM left it at 0
        conf = p.get("confidence", 0)
        if not p.get("stake") and conf >= 40:
            if conf >= 70:   stake = round(bankroll * 0.15, 2)
            elif conf >= 55: stake = round(bankroll * 0.10, 2)
            else:            stake = round(bankroll * 0.08, 2)
            pick_odds = float(p.get("odds") or 1.0)
            p["stake"] = stake
            p["potential_return"] = round(stake * pick_odds, 2)
            log.info(f"Scout: fixed stake for {p['id']}: conf={conf} → €{stake}")

    # ── 8d. Enforce odds range ────────────────────────────────────────────────
    # ML: 1.60–2.50 | Spread: 1.75–2.35 | Total: 1.75–2.10
    ODDS_RANGE = {"ml": (1.60, 2.50), "spread": (1.75, 2.35), "total": (1.75, 2.10)}
    valid_picks = []
    post_filter_rejected = []  # picks dropped by 8d/8e — added to rejected_games later
    for p in draft_picks:
        pick_odds = float(p.get("odds") or 0)
        mtype = p.get("market_type", "ml")
        lo, hi = ODDS_RANGE.get(mtype, (1.65, 2.50))
        if pick_odds < lo or pick_odds > hi:
            reason = f"Post-filter: {mtype} odds {pick_odds} outside [{lo}–{hi}] target range"
            log.info(f"Scout: dropped {p['id']} — {reason}")
            post_filter_rejected.append({"match": p.get("match",""), "reason": reason})
        else:
            valid_picks.append(p)
    if len(valid_picks) < len(draft_picks):
        log.info(f"Scout: odds-range filter removed {len(draft_picks)-len(valid_picks)} pick(s)")
    draft_picks = valid_picks

    # ── 8e. Enforce minimum EV ────────────────────────────────────────────────
    # EV = (confidence/100 × odds) - 1 must be ≥ 0.05 (5% floor)
    ev_picks = []
    for p in draft_picks:
        conf_pct = p.get("confidence", 0) / 100
        pick_odds = float(p.get("odds") or 0)
        ev = round(conf_pct * pick_odds - 1, 4)
        if ev >= 0.05:
            ev_picks.append(p)
        else:
            reason = f"Post-filter: EV {ev:.2%} below 5% floor (conf={p.get('confidence')} odds={pick_odds})"
            log.info(f"Scout: dropped {p['id']} — {reason}")
            post_filter_rejected.append({"match": p.get("match",""), "reason": reason})
    if len(ev_picks) < len(draft_picks):
        log.info(f"Scout: EV filter removed {len(draft_picks)-len(ev_picks)} pick(s)")
    draft_picks = ev_picks

    # ── 8f. Smart retry — extract picks the LLM wrote in text but not JSON ──────
    # Fire whenever draft_picks is empty but report is non-empty (cheap call).
    # Catches all variants: "3-pick slate", "two picks", "picks drafted", etc.
    import re as _re
    report_has_content = bool(report_raw and len(report_raw.strip()) > 50)
    report_mentions_picks = report_has_content and bool(
        _re.search(r'\d+-pick|\bpick(s)?\b.*draft|\bdraft.*pick|\bpicked\b', report_raw or "", _re.IGNORECASE)
    )
    if not draft_picks and report_mentions_picks:
        log.warning("Scout: draft_picks empty but report mentions picks — firing extraction retry")
        extraction_prompt = (
            f"You are the Scout agent. Today: {today} | Bankroll: €{state['bankroll']:.2f}\n\n"
            f"Your previous analysis identified draft picks but they were NOT included in the "
            f"<draft_picks> JSON tag. Here is your analysis:\n\n{report_raw}\n\n"
            f"Extract EVERY pick you decided to draft from the analysis above and output ONLY:\n\n"
            f"<draft_picks>\n"
            f"[JSON array — one object per pick with: id, match, time, pick, odds, stake, "
            f"potential_return, confidence, reasoning, anchor_players, drafted_at, market_type]\n"
            f"</draft_picks>\n\n"
            f"CRITICAL: 'pick' field format must be '<Team Name> <value>' — e.g. "
            f"'San Antonio Spurs +2.0' or 'San Antonio Spurs -18.5' or 'San Antonio Spurs ML'. "
            f"NEVER use words like '-spread' or '-total' — always use the actual numeric line.\n\n"
            f"Draft pick IDs: nba_draft_{today.replace('-', '')}_{{001, 002...}}\n"
            f"drafted_at: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}\n"
            f"If no picks should be drafted, output <draft_picks>[]</draft_picks>.\n"
            f"Output ONLY the tag — nothing else."
        )
        try:
            extraction_result = call_llm_full(SCOUT_SYSTEM, extraction_prompt,
                                              max_tokens=3000, agent="scout")
            extracted_raw = extract_tag(extraction_result.text, "draft_picks")
            if extracted_raw:
                extracted_picks = json.loads(extracted_raw)
                log.info(f"Scout: extraction retry raw picks: {len(extracted_picks)}")
                for p in extracted_picks:
                    log.info(f"  extracted: {p.get('pick')} @ {p.get('odds')} conf={p.get('confidence')} mtype={p.get('market_type')}")
                # Apply same filters with logging
                after_conf = [p for p in extracted_picks if p.get("confidence", 0) >= 40]
                if len(after_conf) < len(extracted_picks):
                    log.info(f"Scout: extraction — {len(extracted_picks)-len(after_conf)} dropped conf<40")
                extracted_picks = after_conf
                for p in extracted_picks:
                    pick_lower = (p.get("pick") or "").lower()
                    if " ml" in pick_lower or pick_lower.endswith(" ml"):
                        p["market_type"] = "ml"
                    elif any(x in pick_lower for x in ["-", "+", "spread", "ats"]):
                        p["market_type"] = "spread"
                    elif any(x in pick_lower for x in ["over", "under", "o/u"]):
                        p["market_type"] = "total"
                # Odds range filter
                ODDS_RANGE = {"ml": (1.65, 2.50), "spread": (1.75, 2.35), "total": (1.75, 2.10)}
                after_odds = [p for p in extracted_picks
                              if ODDS_RANGE.get(p.get("market_type","ml"), (1.65, 2.50))[0]
                              <= float(p.get("odds") or 0)
                              <= ODDS_RANGE.get(p.get("market_type","ml"), (1.65, 2.50))[1]]
                if len(after_odds) < len(extracted_picks):
                    log.info(f"Scout: extraction — {len(extracted_picks)-len(after_odds)} dropped odds-range")
                extracted_picks = after_odds
                # EV filter
                after_ev = [p for p in extracted_picks
                            if p.get("confidence",0)/100 * float(p.get("odds") or 0) - 1 >= 0.05]
                if len(after_ev) < len(extracted_picks):
                    log.info(f"Scout: extraction — {len(extracted_picks)-len(after_ev)} dropped EV<5%")
                extracted_picks = after_ev
                # ESPN is authoritative — overwrite match string AND time from fetched games.
                # LLM guesses on home/away and time are never trusted.
                espn_game_map = {}  # any team-pair key -> {"match": "HOME vs AWAY", "time": iso}
                for g in games:
                    home = g.get("home", "")
                    away = g.get("away", "")
                    t    = g.get("time", "")
                    if home and away:
                        canonical = {"match": f"{home} vs {away}", "time": t or fgt_raw or ""}
                        espn_game_map[f"{home} vs {away}".lower()] = canonical
                        espn_game_map[f"{away} vs {home}".lower()] = canonical
                for p in extracted_picks:
                    match_key = (p.get("match") or "").lower()
                    espn = espn_game_map.get(match_key)
                    if espn:
                        p["match"] = espn["match"]
                        p["time"]  = espn["time"]
                        log.info(f"Scout: ESPN override — match='{p['match']}' time='{p['time']}'")
                    else:
                        log.warning(f"Scout: no ESPN match found for '{p.get('match')}' — keeping LLM value")
                if extracted_picks:
                    draft_picks = extracted_picks
                    log.info(f"Scout: extraction retry recovered {len(draft_picks)} pick(s)")
                    if llm_result:
                        llm_result.tokens_in  += extraction_result.tokens_in
                        llm_result.tokens_out += extraction_result.tokens_out
                        llm_result.cost_usd   += extraction_result.cost_usd
                else:
                    log.info("Scout: extraction retry ran but all picks filtered out")
            else:
                log.warning("Scout: extraction retry returned no <draft_picks> tag")
        except Exception as e:
            log.warning(f"Scout: extraction retry failed: {e}")

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
    state["netrtg_l15"]       = netrtg_l15   # cache for Commit + Analyst
    # Cache pre-formatted context for Commit — avoids re-fetching static data 2-3h later
    state["cached_context"] = {
        "cached_at":    today,
        "games_str":    games_str,
        "standings_str": standings_str,
        "adv_str":      adv_str,
    }
    state["agent_models"] = state.get("agent_models", {})
    state["agent_models"]["scout"] = llm
    state["scout_odds_source"]= odds[0].get("odds_source", "none") if odds else "none"
    state["scout_status"]     = "live"
    # Store full scout report data — persists even after commit clears draft_picks
    state["scout_report_data"] = {
        "date":             today,
        "updated_at":       now_iso,
        "picks":            draft_picks,
        "rejected":         json.loads(rejected_raw) if rejected_raw else [],
        "report":           report_raw,
        "odds_source":      odds[0].get("odds_source", "none") if odds else "none",
        "injuries_source":  injuries_source,
        "tokens_in":        llm_result.tokens_in if llm_result else 0,
        "tokens_out":       llm_result.tokens_out if llm_result else 0,
        "cost_usd":         llm_result.cost_usd if llm_result else 0,
    }
    # Store rejected games for dashboard display
    try:
        state["rejected_games"] = json.loads(rejected_raw) if rejected_raw else []
    except Exception:
        state["rejected_games"] = []
    # Append picks dropped by post-parse filters (8d/8e) — not in LLM rejected_games
    if post_filter_rejected:
        seen_matches = {r.get("match","") for r in state["rejected_games"]}
        for r in post_filter_rejected:
            if r["match"] not in seen_matches:
                state["rejected_games"].append(r)
                seen_matches.add(r["match"])
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
