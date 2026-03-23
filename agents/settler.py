"""
agents/settler.py
Tobias — Settler Agent (10:00 UTC)

Responsibilities:
  1. Read pending_bets from state
  2. Fetch ESPN final scores for each bet's date
  3. Settle each bet (WON / LOST / still pending)
  4. Update state.bankroll, state.settled_bets, history entries
  5. Handle bust detection
  6. Write state + history + data.js back to GitHub
  7. Append to audit/settler_log.jsonl
"""

import json
import logging
from datetime import datetime, date, timezone

from core.validators import validate_all_bets
from core.espn import fetch_final_scores

log = logging.getLogger(__name__)

def _bust_reset_amount(state: dict) -> float:
    """Reset to the season starting bankroll, not an arbitrary small amount."""
    return float(state.get("bankroll_initial", 1000.0))

NBA_SEASON_START = {
    "2024-25": "2024-10-22",
    "2025-26": "2025-10-21",
}
BUST_THRESHOLD  = 2.0
BUST_RESET      = None   # resolved at runtime from state["bankroll_initial"]


# ── Bet evaluation ─────────────────────────────────────────────────────────────

def _evaluate(bet: dict, result: dict) -> bool:
    """Return True if bet WON given final scores."""
    pick  = bet.get("pick", "").lower()
    h     = result["home_score"]
    a     = result["away_score"]
    home  = result["home"].lower()
    away  = result["away"].lower()

    # Moneyline
    if "ml" in pick or pick in (home, away):
        winner = home if h > a else away
        return any(w in pick for w in winner.split())

    # Spread — format: "Team Name -X.X" or "Team Name +X.X"
    import re
    spread_m = re.search(r'([+-]?\d+\.?\d*)\s*$', pick)
    if spread_m:
        spread = float(spread_m.group(1))
        # Determine which team this pick is on
        if any(w in pick for w in home.split()):
            return (h + spread) > a
        elif any(w in pick for w in away.split()):
            return (a + spread) > h

    # Over / Under
    ou_m = re.search(r'(over|under)\s+(\d+\.?\d*)', pick)
    if ou_m:
        direction = ou_m.group(1)
        total_line = float(ou_m.group(2))
        total = h + a
        return total > total_line if direction == "over" else total < total_line

    log.warning(f"  Could not evaluate pick '{bet['pick']}' — leaving pending")
    return False


# ── Main bust logic ────────────────────────────────────────────────────────────

def _check_bust(state: dict, history: dict) -> tuple[dict, dict, bool]:
    """Check if bust condition is met. Handle reset if so."""
    bankroll = state["bankroll"]
    pending  = state.get("pending_bets", [])

    if bankroll >= BUST_THRESHOLD or pending:
        return state, history, False

    log.warning(f"BUST — bankroll EUR{bankroll:.2f} with no pending bets")
    now = datetime.now(timezone.utc).isoformat()

    # Close current game in history
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

    # Append bust entry to history
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

    # Reset state for new game
    new_game = game_n + 1
    state["game"]             = new_game
    reset_amt = _bust_reset_amount(state)
    state["bankroll"]         = reset_amt
    state["bankroll_initial"] = reset_amt
    state["bankroll_peak"]    = reset_amt
    state["bust"]             = True
    state["bust_at"]          = now
    state["settled_bets"]     = []
    state["pending_bets"]     = []

    # Open new game in history
    for s in history["seasons"]:
        if s["season"] == season:
            s["games"].append({
                "game":             new_game,
                "start_date":       now[:10],
                "end_date":         None,
                "initial_bankroll": reset_amt,
                "peak_bankroll":    reset_amt,
                "final_bankroll":   None,
                "net_pnl":          None,
                "total_bets":       0,
                "wins":             0,
                "losses":           0,
                "bust":             False,
            })

    return state, history, True


# ── Main run ───────────────────────────────────────────────────────────────────

def run(store) -> None:
    now      = datetime.now(timezone.utc)
    today    = date.today()
    now_iso  = now.isoformat()

    # ── 1. Load state & history ────────────────────────────────────────────────
    state, history = store.read_state_and_history()
    pending = state.get("pending_bets", [])

    if not pending:
        log.info("Settler: no pending bets — nothing to settle")
        state["agent_models"] = state.get("agent_models", {})
        state["agent_models"]["settler"] = "no-llm"
        state["settler_updated_at"] = now_iso
        state["last_updated"]       = now_iso
        store.write_json("state", state, f"settler: no pending bets {today}")
        _append_audit(store, now_iso, state, history, settled=[], skipped=[], bust=False,
                      bankroll_before=state["bankroll"],
                      bankroll_after=state["bankroll"])
        store.write_data_js(state, history, config=store.read_config())
        return

    log.info(f"Settler: {len(pending)} pending bets to check")

    # ── 2. Fetch scores — flat dict across all relevant dates ─────────────────
    # ID format: nba_bet_YYYYMMDD_NNN (YYYYMMDD is UTC date of commit run)
    # ESPN uses Eastern Time dates — a post-midnight UTC commit (e.g. 00:04 UTC Mar 21)
    # is still a Mar 20 ET game. So we fetch both the ID date AND the previous day.
    from datetime import timedelta

    def _bet_date(bet):
        try:
            return bet["id"].split("_")[2]          # YYYYMMDD
        except Exception:
            return (today - timedelta(days=1)).strftime("%Y%m%d")

    def _d_obj(d_str):
        return date.fromisoformat(f"{d_str[:4]}-{d_str[4:6]}-{d_str[6:8]}")

    dates_to_fetch: set[str] = set()
    for b in pending:
        d_str = _bet_date(b)
        dates_to_fetch.add(d_str)
        try:                                        # also try previous day (ET vs UTC gap)
            dates_to_fetch.add((_d_obj(d_str) - timedelta(days=1)).strftime("%Y%m%d"))
        except Exception:
            pass

    all_scores: dict[str, dict] = {}               # flat match->result across all dates
    for d_str in sorted(dates_to_fetch):
        try:
            d_obj = _d_obj(d_str)
            if d_obj <= today:
                fetched = fetch_final_scores(d_obj)
                log.info(f"  Fetched scores for {d_str}: {len(fetched)} keys")
                all_scores.update(fetched)
            else:
                log.info(f"  Skipping {d_str} — games not final yet")
        except Exception as e:
            log.warning(f"  Could not fetch scores for {d_str}: {e}")

    # ── 2b. Update team game log (all games from fetched dates) ──────────────
    game_log = state.get("team_game_log", {})
    recorded = set(state.get("game_log_recorded", []))
    seen_games: set = set()
    for result in all_scores.values():
        h, a = result.get("home", ""), result.get("away", "")
        if not h or not a:
            continue
        game_key = f"{a}@{h}"
        if game_key in seen_games or game_key in recorded:
            continue
        seen_games.add(game_key)
        home_margin = result["home_score"] - result["away_score"]
        for team, margin in [(h, home_margin), (a, -home_margin)]:
            entries = game_log.setdefault(team, [])
            entries.append(margin)
            if len(entries) > 25:
                game_log[team] = entries[-25:]
        recorded.add(game_key)
    state["team_game_log"] = game_log
    state["game_log_recorded"] = list(recorded)[-200:]
    if seen_games:
        log.info(f"Settler: game log updated — {len(seen_games)} new games, {len(game_log)} teams tracked")

    # ── 3. Settle each bet ────────────────────────────────────────────────────
    settled_ids: list[str] = []
    still_pending: list[dict] = []
    newly_settled: list[dict] = []
    bankroll_before = state["bankroll"]

    for bet in pending:
        match  = bet.get("match", "")

        # Try to find result in flat scores dict
        result = all_scores.get(match)
        if result is None:
            # Try partial match
            for key, res in all_scores.items():
                if res.get("home", "") in match or res.get("away", "") in match:
                    result = res
                    break

        if result is None:
            log.info(f"  [{bet['id']}] No final score found — keeping pending")
            still_pending.append(bet)
            continue

        # Evaluate
        won     = _evaluate(bet, result)
        stake   = float(bet["stake"])
        odds    = float(bet["odds"])
        returned = round(stake * odds, 2) if won else 0.0
        pnl      = round(returned - stake, 2)

        bet["result"]     = "WON" if won else "LOST"
        bet["returned"]   = returned
        bet["pnl"]        = pnl
        bet["settled_at"] = now_iso

        if won:
            state["bankroll"]      = round(state["bankroll"] + returned, 2)
            state["total_returned"] = round(state.get("total_returned", 0) + returned, 2)
            log.info(f"  WON  {match} | +EUR{pnl:.2f} | bankroll EUR{state['bankroll']:.2f}")
        else:
            log.info(f"  LOST {match} | -EUR{stake:.2f} | bankroll EUR{state['bankroll']:.2f}")

        state["net_pnl"] = round(
            state.get("net_pnl", 0) + pnl, 2)

        if state["bankroll"] > state.get("bankroll_peak", 0):
            state["bankroll_peak"] = state["bankroll"]

        newly_settled.append(bet)

    # ── 4. Update state bets lists ────────────────────────────────────────────
    state["pending_bets"]  = still_pending
    state["settled_bets"]  = state.get("settled_bets", []) + newly_settled
    state["last_updated"]      = now_iso
    state["settler_updated_at"] = now_iso
    state["bust"]               = False   # reset flag (rechecked below)

    # ── 5. Update history entries with settlement results ─────────────────────
    settled_by_id = {b["id"]: b for b in newly_settled}
    for entry in history.get("entries", []):
        if entry.get("type") != "bets_placed":
            continue
        for eb in entry.get("bets", []):
            if eb["id"] in settled_by_id:
                sb = settled_by_id[eb["id"]]
                eb["result"]     = sb["result"]
                eb["returned"]   = sb["returned"]
                eb["pnl"]        = sb["pnl"]
                eb["settled_at"] = sb["settled_at"]

    # Update game-level stats in history
    wins   = sum(1 for b in newly_settled if b["result"] == "WON")
    losses = sum(1 for b in newly_settled if b["result"] == "LOST")
    season = state["season"]
    game_n = state["game"]
    for s in history["seasons"]:
        if s["season"] == season:
            for g in s["games"]:
                if g["game"] == game_n:
                    g["wins"]          = g.get("wins", 0) + wins
                    g["losses"]        = g.get("losses", 0) + losses
                    g["peak_bankroll"] = max(g.get("peak_bankroll", 0), state["bankroll"])

    # ── 6. Bust check ─────────────────────────────────────────────────────────
    state, history, busted = _check_bust(state, history)

    # ── 7. Validate & write ────────────────────────────────────────────────────
    try:
        validate_all_bets(state["pending_bets"],  "settler/pending")
        validate_all_bets(state["settled_bets"],  "settler/settled")
    except Exception as e:
        log.error(f"Validation error: {e}")
        # Write error state to GitHub so dashboard shows it
        state["scout_error"] = str(e)
        store.write_json("state", state, "settler: validation error")
        return

    commit_msg = f"settler: {len(newly_settled)} settled ({wins}W/{losses}L), {len(still_pending)} pending"
    store.write_json("state",   state,   commit_msg)
    store.write_json("history", history, commit_msg)

    # ── 8. Audit log ──────────────────────────────────────────────────────────
    _append_audit(store, now_iso, state, history,
                  settled=newly_settled,
                  skipped=[b["id"] for b in still_pending],
                  bust=busted,
                  bankroll_before=bankroll_before,
                  bankroll_after=state["bankroll"])

    log.info(f"Settler done: {wins}W / {losses}L | bankroll €{bankroll_before:.2f} → €{state['bankroll']:.2f}")


def _append_audit(store, ts: str, state: dict, history: dict,
                  settled: list, skipped: list,
                  bust: bool, bankroll_before: float, bankroll_after: float):
    wins   = sum(1 for b in settled if b.get("result") == "WON")
    losses = sum(1 for b in settled if b.get("result") == "LOST")
    entry = {
        "ts":              ts,
        "agent":           "settler",
        "settled_count":   len(settled),
        "wins":            wins,
        "losses":          losses,
        "skipped":         skipped,
        "bust":            bust,
        "bankroll_before": round(bankroll_before, 2),
        "bankroll_after":  round(bankroll_after, 2),
        "pnl_today":       round(bankroll_after - bankroll_before, 2),
    }
    try:
        store.append_jsonl("settler_log" if "settler_log" in store.FILES else "scout_log", entry)
    except Exception as e:
        log.warning(f"Audit log append failed: {e}")
    store.write_data_js(state, history, config=store.read_config())
