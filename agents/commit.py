"""
agents/commit.py
Tobias — Commit Agent (self-gating, every 30 min)

Responsibilities:
  1. Self-gate: only run when now >= first_game_time - 30min
  2. Load commit_skills.md (Analyst-maintained criteria)
  3. Fetch live Betano odds for line movement check
  4. Fetch fresh injury reports for anchor player check
  5. Call LLM to: review draft picks, cancel/confirm, find new late picks
  6. Commit confirmed bets: deduct stakes from bankroll, move to pending_bets
  7. Clear draft_picks, set commit_status = "done"
  8. Handle bust detection
  9. Write state + history + data.js to GitHub
  10. Append to audit/commit_log.jsonl
"""

import json
import re
import logging
from datetime import datetime, date, timezone, timedelta

from core.llm import call_llm, call_llm_full, extract_tag, agent_model_name
from core.nba_injuries import fetch_official_nba_injuries, format_injuries_for_prompt as format_official_injuries
from core.odds import fetch_betano_nba_odds, format_odds_for_prompt, get_odds_failure_reasons
from core.validators import validate_all_bets, validate_all_drafts, ValidationError

log = logging.getLogger(__name__)

def _bust_reset_amount(state: dict) -> float:
    """Reset to the season starting bankroll, not an arbitrary small amount."""
    return float(state.get("bankroll_initial", 1000.0))

BUST_THRESHOLD = 2.0
BUST_RESET     = None    # resolved at runtime from state["bankroll_initial"]

# ── System prompt ──────────────────────────────────────────────────────────────

COMMIT_SYSTEM = """You are the Commit agent for Tobias, an autonomous NBA betting simulation.
This is the final decision point before games tip off.

You have two jobs:
1. Review the draft picks from the Scout phase and confirm or cancel each one.
2. Hunt for NEW late-breaking edges not visible at 14:00.

Read your skills file carefully — the Analyst updates it daily.
Stakes are committed NOW. Deduct from bankroll. This is real money in the simulation.

CRITICAL FORMATTING RULE: Your response MUST end with these exact XML tags.
The system will FAIL if <committed_bets> tag is missing. Even if all picks are cancelled, output <committed_bets>[]</committed_bets>."""


def _build_commit_prompt(skills: str, draft_picks: list, rejected_games: list,
                          games_text: str, odds_text: str,
                          injuries_text: str, injuries_source: str,
                          netrtg_l15_text: str, standings_text: str,
                          adv_stats_text: str,
                          state: dict, today: str,
                          season_phase: str = "regular",
                          playoff_context: str = "",
                          future_picks_count: int = 0) -> str:
    bankroll = state["bankroll"]
    now_iso  = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    is_postseason = season_phase in ("playoffs", "playin")
    phase_label = {"regular": "Regular Season", "playin": "Play-In Tournament",
                   "playoffs": "Playoffs", "preseason": "Preseason"}.get(season_phase, season_phase)
    playoff_block = ""
    if is_postseason and playoff_context:
        playoff_block = f"""
## PLAYOFF / PLAY-IN CONTEXT (replaces tanking and B2B rules this phase)
{playoff_context}
"""

    picks_json     = json.dumps(draft_picks, separators=(',', ':'))
    rejected_json  = json.dumps(rejected_games, separators=(',', ':')) if rejected_games else "[]"
    future_note    = (f" ({future_picks_count} pick(s) for later games are already queued and will be committed separately.)"
                      if future_picks_count > 0 else "")

    return f"""## YOUR SKILLS (follow these criteria exactly)
{skills}
{playoff_block}
## NOW: {now_iso} | Bankroll: €{bankroll:.2f} | Phase: {phase_label}

## TONIGHT'S FULL SLATE
{games_text}

## DRAFT PICKS TO REVIEW
{picks_json}

## SCOUT REJECTED GAMES (from 14:00 Scout run — re-evaluate for late changes)
{rejected_json}

## NETRTG L15 (primary signal — last 15 games)
{netrtg_l15_text}

## LIVE BETANO ODDS (check for line movement vs Scout odds in draft picks)
{odds_text}

## STANDINGS
{standings_text}

## ADVANCED STATS (season — tonight's teams)
{adv_stats_text}

## FRESH INJURY REPORTS (NBA official PDF — verify anchor players)
Source: {injuries_source}
{injuries_text}

---

## YOUR TASKS

### Task 1 — Review each draft pick
For each pick, check:
- Anchor player confirmed OUT? → cancel
- Line moved against by > 0.10? → investigate, may cancel
- Line moved in your favour? → note improvement, confirm
- New injury info changes the edge? → re-evaluate

### Task 2 — Late scout
Re-examine ALL games from tonight's slate, especially Scout's rejected games above.
Check what has changed since 14:00 Scout:
- Any anchor player status changed? (Questionable → OUT, or OUT → Available)
- Significant line movement on any game?
- Any game Scout rejected that now has value at current odds?
Apply the same rules as Scout: only add picks with genuine edge (conf ≥ 60, EV ≥ 0.05, odds in range).
Max 3 new picks. Only add games where tip-off is within the next 90 minutes — later games will be evaluated at their own commit window.{future_note}

### Task 3 — Confirm final list and commit
- Recalculate stakes based on current bankroll (€{bankroll:.2f})
- Ensure total stake ≤ 70% of bankroll
- Apply all required fields to every bet object

Bet IDs: nba_bet_{today.replace('-','')}_{'{001, 002...}'} (continuing from {len(state.get('pending_bets', []))} existing)
All bet objects MUST have ALL fields:
  id, match, time, pick, odds, stake, potential_return,
  reasoning, confidence, anchor_players,
  result (null), returned (null), pnl (null), settled_at (null)

Match convention: "HOME TEAM vs AWAY TEAM" (home first).
Committed_at: {now_iso}

Output these XML tags at the very end:

<committed_bets>
[JSON array of confirmed bet objects — [] if all cancelled]
</committed_bets>

<cancelled_picks>
[JSON array of {{"id": "...", "match": "...", "pick": "...", "reason": "..."}} for each draft pick you cancelled]
</cancelled_picks>

<late_scout_rejections>
[JSON array of games you checked in late scout but did NOT add as new bets, format:
{{"match": "HOME vs AWAY", "reason": "why not picked"}}
Use [] if you found no new edges to evaluate.]
</late_scout_rejections>

<commit_report>
Structure your report with one section per bet decision.

For each CONFIRMED bet write:
### CONFIRMED — [pick name]
- Match: [HOME vs AWAY] | Tip: [time]
- Pick: [pick] | Scout odds: [scout_odds] | Commit odds: [current_odds] | Move: [delta]
- ML: [ml_home]/[ml_away] | ATS: [spread_pt] ([sp_h]/[sp_a]) | O/U: [total] (O:[over]/U:[under])
- Stake: [stake] | Pot: [potential_return] | Conf: [confidence]/100 | EV: [ev]
- Decision: [reason for confirming]

For each CANCELLED pick write:
### CANCELLED — [pick name]
- Reason: [specific reason]
- Odds at cancel: [current_odds] (was [scout_odds] at scout time)

End with 2-3 sentence slate summary.
</commit_report>
"""


# ── Bust handling ──────────────────────────────────────────────────────────────

def _check_bust(state: dict, history: dict) -> tuple[dict, dict, bool]:
    bankroll = state["bankroll"]
    pending  = state.get("pending_bets", [])
    if bankroll >= BUST_THRESHOLD or pending:
        return state, history, False

    log.warning(f"BUST — bankroll EUR{bankroll:.2f}")
    now = datetime.now(timezone.utc).isoformat()
    season = state["season"]
    game_n = state["game"]

    for s in history["seasons"]:
        if s["season"] == season:
            for g in s["games"]:
                if g["game"] == game_n:
                    g["end_date"]       = now[:10]
                    g["final_bankroll"] = round(bankroll, 2)
                    g["net_pnl"]        = round(bankroll - g["initial_bankroll"], 2)
                    g["bust"]           = True

    history["entries"].append({
        "entry_id":        f"bust_{now[:10]}_game{game_n}",
        "season":          season,
        "game":            game_n,
        "timestamp":       now,
        "type":            "bust",
        "bankroll_before": round(bankroll, 2),
        "bankroll_after":  _bust_reset_amount(state),
        "summary":         f"Game {game_n} bust at EUR{bankroll:.2f}. Resetting to EUR{_bust_reset_amount(state):.0f}.",
    })

    new_game = game_n + 1
    reset_amt = _bust_reset_amount(state)
    state.update({
        "game": new_game, "bankroll": reset_amt,
        "bankroll_initial": reset_amt, "bankroll_peak": reset_amt,
        "bust": True, "bust_at": now,
        "settled_bets": [], "pending_bets": [],
    })

    for s in history["seasons"]:
        if s["season"] == season:
            s["games"].append({
                "game": new_game, "start_date": now[:10], "end_date": None,
                "initial_bankroll": reset_amt, "peak_bankroll": reset_amt,
                "final_bankroll": None, "net_pnl": None,
                "total_bets": 0, "wins": 0, "losses": 0, "bust": False,
            })

    return state, history, True


# ── Main run ───────────────────────────────────────────────────────────────────

def should_run(state: dict) -> bool:
    """Returns True if at least one draft pick's commit window is open."""
    now = datetime.now(timezone.utc)
    for p in state.get("draft_picks", []):
        try:
            t = datetime.fromisoformat(p["time"].replace("Z", "+00:00"))
            if now >= t - timedelta(minutes=30):
                return True
        except Exception:
            continue
    return False


def run(store, force: bool = False, window_picks: list = None) -> None:
    now     = datetime.now(timezone.utc)
    now_iso = now.isoformat()
    today   = now.strftime("%Y-%m-%d")
    llm     = agent_model_name("commit")

    # ── 1. Load state ──────────────────────────────────────────────────────────
    state, history = store.read_state_and_history()

    # ── 2. Guard: already committed today? ────────────────────────────────────
    if state.get("commit_status") == "done" and not force:
        log.info("Commit: already committed today — skipping")
        return

    # ── 3. Load draft picks (commit always runs — late scout may find new edges) ─
    draft_picks = state.get("draft_picks", [])
    # When called from commit_if_ready, only process picks in the current window;
    # force=True (manual override) processes all picks regardless of time.
    picks_to_process = window_picks if window_picks is not None else draft_picks

    # ── 4. Load skills ────────────────────────────────────────────────────────
    skills = store.read_md("commit_skills")

    # ── 4b. Season phase + playoff context ────────────────────────────────────
    from core.espn import fetch_season_phase
    season_phase = fetch_season_phase()
    playoff_context = ""
    if season_phase in ("playoffs", "playin"):
        playoff_context = store.read_md("playoff_context") or ""
        log.info(f"Commit: season phase={season_phase} — playoff context loaded")
    else:
        log.info(f"Commit: season phase={season_phase} — regular season mode")

    # ── 5. Fetch live data ────────────────────────────────────────────────────
    log.info("Commit: fetching live odds + injuries…")
    odds      = fetch_betano_nba_odds()
    odds_failures = get_odds_failure_reasons()
    # Primary: NBA official injury report PDF
    injuries = fetch_official_nba_injuries()
    if not injuries:
        log.warning("Commit: NBA official injuries unavailable — falling back to ESPN")
        injuries = fetch_injuries()
        injuries_source = "espn"
    else:
        injuries_source = "nba_official"
    # Filter injuries to tonight's teams only, use official formatter if available
    from core.espn import fetch_scoreboard, fetch_injuries, fetch_first_game_time_utc, fetch_standings, fetch_advanced_stats
    scoreboard = fetch_scoreboard()
    tonight_teams = set([g["home"] for g in scoreboard] + [g["away"] for g in scoreboard])
    odds_filtered = [g for g in odds if g.get("home") in tonight_teams or g.get("away") in tonight_teams]
    odds_str = format_odds_for_prompt(odds_filtered)
    if injuries_source == "nba_official":
        injuries_str = format_official_injuries(injuries, tonight_teams=tonight_teams)
    else:
        injuries_str = _injuries_text({t: p for t, p in injuries.items() if t in tonight_teams})

    # ── 6. Build context — reuse Scout cache where possible ───────────────────
    cached = state.get("cached_context", {})
    cache_fresh = cached.get("cached_at") == today

    if cache_fresh:
        log.info("Commit: using Scout-cached games/standings/adv_stats (no re-fetch)")
        games_str     = cached["games_str"]
        standings_str = cached["standings_str"]
        adv_str       = cached["adv_str"]
    else:
        log.info("Commit: no Scout cache for today — fetching games/standings/adv_stats fresh")
        games_str     = _games_text(scoreboard)
        standings_str = _format_standings(fetch_standings())
        adv_str       = _format_adv_stats(fetch_advanced_stats(), scoreboard)

    # NetRtg L15 — computed from Settler-maintained game log (no API calls)
    from agents.scout import _compute_netrtg_l15
    netrtg_l15 = _compute_netrtg_l15(state.get("team_game_log", {}))
    if netrtg_l15:
        log.info(f"Commit: NetRtg L15 from game log ({len(netrtg_l15)} teams)")
    else:
        log.info("Commit: NetRtg L15 not yet available (game log accumulating)")
    netrtg_l15_str = _format_netrtg_l15_commit(netrtg_l15, scoreboard)
    rejected_games = state.get("rejected_games", [])
    future_picks_count = len(draft_picks) - len(picks_to_process)
    log.info(f"Commit: {len(scoreboard)} games tonight | {len(picks_to_process)} in window | {future_picks_count} pending future | {len(rejected_games)} rejected | injuries: {injuries_source}")
    log.info(f"Commit: injuries source: {injuries_source} — calling LLM for final decision…")
    llm_result = None
    try:
        llm_result = call_llm_full(
            COMMIT_SYSTEM,
            _build_commit_prompt(skills, picks_to_process, rejected_games,
                                  games_str, odds_str,
                                  injuries_str, injuries_source,
                                  netrtg_l15_str, standings_str,
                                  adv_str, state, today,
                                  season_phase=season_phase,
                                  playoff_context=playoff_context,
                                  future_picks_count=future_picks_count),
            max_tokens=12000,
            agent="commit",
        )
        raw = llm_result.text
    except Exception as e:
        log.error(f"Commit: LLM call failed: {e}")
        state["commit_status"] = "error"
        state["scout_error"]   = str(e)
        state["last_updated"]  = now_iso
        store.write_json("state", state, f"commit: LLM error {today}")
        store.write_data_js(state, history, config=store.read_config())
        return

    # ── 7. Extract tags ────────────────────────────────────────────────────────
    bets_raw            = extract_tag(raw, "committed_bets")
    cancelled_raw       = extract_tag(raw, "cancelled_picks") or "[]"
    late_rejections_raw = extract_tag(raw, "late_scout_rejections") or "[]"
    report_raw          = extract_tag(raw, "commit_report") or ""

    if bets_raw is None:
        log.error("Commit: <committed_bets> tag missing")
        state["commit_status"] = "error"
        state["scout_error"]   = "Missing <committed_bets> tag"
        state["last_updated"]  = now_iso
        store.write_json("state", state, f"commit: parse error {today}")
        store.write_data_js(state, history, config=store.read_config())
        return

    # ── 8. Parse ──────────────────────────────────────────────────────────────
    try:
        committed_bets = json.loads(bets_raw)
        cancelled_picks = json.loads(cancelled_raw)
    except json.JSONDecodeError as e:
        log.error(f"Commit: JSON parse error: {e}")
        state["commit_status"] = "error"
        state["scout_error"]   = f"JSON parse error: {e}"
        state["last_updated"]  = now_iso
        store.write_json("state", state, f"commit: JSON error {today}")
        store.write_data_js(state, history, config=store.read_config())
        return

    # ── 8b. Normalise match strings — same as scout ───────────────────────────
    venue_to_team = {g.get("venue","").lower(): g["home"] for g in scoreboard if g.get("venue")}
    espn_home_set = {g["home"].lower() for g in scoreboard}
    espn_away_set = {g["away"].lower() for g in scoreboard}
    def _normalise_match(match_str: str) -> str:
        if " @ " in match_str:
            parts = match_str.split(" @ ", 1)
            away_part, home_part = parts[0].strip(), parts[1].strip()
        elif " vs " in match_str:
            parts = match_str.split(" vs ", 1)
            home_part, away_part = parts[0].strip(), parts[1].strip()
        else:
            return match_str
        home_norm = venue_to_team.get(home_part.lower(), home_part)
        away_norm = venue_to_team.get(away_part.lower(), away_part)
        return f"{home_norm} vs {away_norm}"
    for b in committed_bets:
        if "match" in b:
            b["match"] = _normalise_match(b["match"])
    for c in cancelled_picks:
        if "match" in c:
            c["match"] = _normalise_match(c["match"])
    late_rejs = json.loads(late_rejections_raw) if late_rejections_raw else []
    for r in late_rejs:
        if "match" in r:
            r["match"] = _normalise_match(r["match"])
    state["late_scout_rejections"] = late_rejs

    # ── 9. Validate bets ──────────────────────────────────────────────────────
    try:
        validate_all_bets(committed_bets, "commit")
    except ValidationError as e:
        log.error(f"Commit: validation failed: {e}")
        state["commit_status"] = "error"
        state["scout_error"]   = str(e)
        state["last_updated"]  = now_iso
        store.write_json("state", state, f"commit: validation error {today}")
        store.write_data_js(state, history, config=store.read_config())
        return

    # ── 10. Deduct stakes, update bankroll ────────────────────────────────────
    bankroll_before = state["bankroll"]
    total_staked    = 0.0

    for bet in committed_bets:
        stake = float(bet["stake"])
        state["bankroll"]      = round(state["bankroll"] - stake, 2)
        state["total_staked"]  = round(state.get("total_staked", 0) + stake, 2)
        total_staked          += stake
        log.info(f"  BET: {bet['match']} — {bet['pick']} @ {bet['odds']} | EUR{stake:.2f}")

    # ── 11. Update state ──────────────────────────────────────────────────────
    state["agent_models"] = state.get("agent_models", {})
    state["agent_models"]["commit"] = llm
    state["pending_bets"]      = state.get("pending_bets", []) + committed_bets
    # Remove only picks processed in this window; future-game picks stay for their own window
    committed_ids = {b["id"] for b in committed_bets}
    cancelled_ids = {c["id"] for c in cancelled_picks if isinstance(c, dict) and "id" in c}
    processed_ids = committed_ids | cancelled_ids
    remaining_picks = [p for p in state.get("draft_picks", []) if p.get("id") not in processed_ids]
    state["draft_picks"]   = remaining_picks
    # NOTE: rejected_games intentionally kept — Scout tab needs them until next Scout run
    state["commit_status"] = "done" if not remaining_picks else "partial"
    state["commit_date"]   = today
    state["commit_updated_at"] = now_iso
    state["last_updated"]      = now_iso
    state["last_report"]       = report_raw
    # Store commit report data for dashboard Commit tab
    state["commit_report_data"] = {
        "date":            today,
        "ts":              now_iso,
        "bets":            committed_bets,
        "cancelled":       cancelled_picks,
        "late_rejections": state.get("late_scout_rejections", []),
        "total_staked":    round(total_staked, 2),
        "bankroll_before": round(bankroll_before, 2),
        "report":          report_raw,
        "tokens_in":       llm_result.tokens_in if llm_result else 0,
        "tokens_out":      llm_result.tokens_out if llm_result else 0,
        "cost_usd":        llm_result.cost_usd if llm_result else 0,
    }
    # ── 12. Update history ────────────────────────────────────────────────────
    season = state["season"]
    game_n = state["game"]
    entry  = {
        "entry_id":        f"nba_entry_{today.replace('-','')}",
        "season":          season,
        "game":            game_n,
        "timestamp":       now_iso,
        "type":            "bets_placed",
        "bankroll_before": round(bankroll_before, 2),
        "total_staked":    round(total_staked, 2),
        "bankroll_after":  round(state["bankroll"], 2),
        "cancelled_picks": cancelled_picks,
        "bets":            committed_bets,
        "summary": (
            f"Day {today} commit — {len(committed_bets)} bets totalling "
            f"€{total_staked:.2f}. "
            f"{len(cancelled_picks)} cancelled. "
            f"Bankroll: €{bankroll_before:.2f} → €{state['bankroll']:.2f}."
        ),
    }
    history["entries"].append(entry)

    # Update game stats
    for s in history["seasons"]:
        if s["season"] == season:
            for g in s["games"]:
                if g["game"] == game_n:
                    g["total_bets"] = g.get("total_bets", 0) + len(committed_bets)

    # ── 13. Bust check ────────────────────────────────────────────────────────
    state, history, busted = _check_bust(state, history)

    # ── 14. Write to GitHub ───────────────────────────────────────────────────
    commit_msg = (
        f"commit: {len(committed_bets)} bets staked €{total_staked:.2f} "
        f"({len(cancelled_picks)} cancelled) {today}"
    )
    store.write_json("state",   state,   commit_msg)
    store.write_json("history", history, commit_msg)

    # ── 15. Audit log ─────────────────────────────────────────────────────────
    _append_audit(store, now_iso, llm, state, history, report_raw,
                  committed=committed_bets,
                  cancelled=cancelled_picks,
                  total_staked=total_staked,
                  bankroll_before=bankroll_before,
                  bankroll_after=state["bankroll"],
                  bust=busted,
                  injuries_source=injuries_source,
                  llm_meta=llm_result.to_audit_dict() if llm_result else {})

    # ── 16. Store report for Commit tab ──────────────────────────────────────
    commit_entry = {
        "ts":              now_iso,
        "date":            today,
        "llm":             llm,
        "committed_count": len(committed_bets),
        "cancelled_count": len(cancelled_picks),
        "total_staked":    round(total_staked, 2),
        "bankroll_before": round(bankroll_before, 2),
        "bankroll_after":  round(state["bankroll"], 2),
        "bets":            committed_bets,
        "cancelled":       cancelled_picks,
        "late_rejections": state.get("late_scout_rejections", []),
        "report":          report_raw,
        "odds_failures":   odds_failures,
        **(llm_result.to_audit_dict() if llm_result else {}),
    }
    try:
        store.append_report("commit", commit_entry)
        log.info("Commit: report stored to commit_reports.js")
    except Exception as e:
        log.warning(f"Commit: failed to store report: {e}")

    log.info(
        f"Commit done — {len(committed_bets)} bets, €{total_staked:.2f} staked | "
        f"bankroll €{bankroll_before:.2f} → €{state['bankroll']:.2f}"
    )


def _format_standings(standings) -> str:
    """standings is a dict {team_name: {wins, losses, streak, last_10, ...}}"""
    if not standings:
        return "Standings unavailable."
    lines = []
    # standings is a dict keyed by team name
    items = standings.items() if isinstance(standings, dict) else [(t.get("team","?"), t) for t in standings]
    for team_name, t in sorted(items):
        wins  = t.get("wins", t.get("w", 0))
        losses= t.get("losses", t.get("l", 0))
        l10   = t.get("last_10", t.get("l10", ""))
        strk  = t.get("streak", "")
        lines.append(f"  {team_name}: {wins}-{losses} | L10: {l10} | Streak: {strk}")
    return "STANDINGS:\n" + "\n".join(lines)


def _format_adv_stats(adv_stats: dict, games: list) -> str:
    if not adv_stats:
        return "Advanced stats unavailable."
    tonight = set()
    for g in games:
        tonight.add(g.get("home",""))
        tonight.add(g.get("away",""))
    lines = ["ADVANCED STATS (season — OffRtg/DefRtg/NetRtg/Pace):"]
    for team in sorted(tonight):
        s = adv_stats.get(team)
        if s:
            lines.append(
                f"  {team}: OffRtg={s.get('off_rtg',0):.1f} DefRtg={s.get('def_rtg',0):.1f} "
                f"NetRtg={s.get('net_rtg',0):.1f} Pace={s.get('pace',0):.1f}"
            )
    return "\n".join(lines) if len(lines) > 1 else "Advanced stats unavailable."


def _format_netrtg_l15_commit(netrtg_l15: dict, games: list) -> str:
    """Format NetRtg L15 for ALL 30 teams — Commit needs full picture for late scout."""
    if not netrtg_l15:
        return "NetRtg L15 unavailable."
    lines = ["NETRTG L15 (last 15 games — primary signal, all teams):"]
    for team in sorted(netrtg_l15.keys()):
        val = netrtg_l15[team]
        sign = "+" if val >= 0 else ""
        lines.append(f"  {team}: {sign}{val}")
    return "\n".join(lines)


def _games_text(games: list) -> str:
    """Format tonight's scoreboard for Commit prompt."""
    if not games:
        return "No games scheduled."
    lines = []
    for g in games:
        t = g.get("time", "")
        time_str = ""
        if t:
            try:
                from datetime import datetime, timezone
                dt = datetime.fromisoformat(t.replace("Z", "+00:00"))
                time_str = dt.strftime("%H:%M UTC")
            except Exception:
                time_str = t
        lines.append(f"{g.get('home','?')} vs {g.get('away','?')} — {time_str}")
    return "\n".join(lines)


def _injuries_text(injuries: dict) -> str:
    if not injuries:
        return "No injury reports."
    lines = []
    for team, players in injuries.items():
        notable = [p for p in players
                   if p["status"] in ("Out", "Doubtful", "Questionable", "Game-Time Decision")]
        if notable:
            parts = [f"{p['name']} ({p['status']})" for p in notable[:4]]
            lines.append(f"{team}: {', '.join(parts)}")
    return "\n".join(lines[:30]) if lines else "No notable injuries."


def _append_audit(store, ts, llm, state, history, report_raw="",
                  committed=None, cancelled=None,
                  total_staked=0, bankroll_before=0, bankroll_after=0, bust=False,
                  injuries_source="unknown", llm_meta=None):
    entry = {
        "ts":              ts,
        "agent":           "commit",
        "llm":             llm,
        "committed_count": len(committed or []),
        "cancelled_count": len(cancelled or []),
        "bets": [{"id": b["id"], "match": b["match"], "pick": b["pick"],
                  "odds": b["odds"], "stake": b["stake"],
                  "confidence": b["confidence"]}
                 for b in (committed or [])],
        "cancelled": cancelled or [],
        "total_staked":    round(total_staked, 2),
        "bankroll_before": round(bankroll_before, 2),
        "bankroll_after":  round(bankroll_after, 2),
        "bust":            bust,
        "injuries_source":  injuries_source,
        **(llm_meta or {}),
    }
    try:
        store.append_jsonl("commit_log", entry)
    except Exception as e:
        log.warning(f"Commit audit log failed: {e}")
    store.write_data_js(state, history, commit_report=report_raw, config=store.read_config())
