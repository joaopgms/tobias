"""
run.py — Tobias entry point

Usage:
  python run.py settle           → Settler agent (10:00 UTC)
  python run.py analyst          → Analyst agent (11:00 UTC)
  python run.py scout            → Scout agent   (14:00 UTC)
  python run.py commit_if_ready  → Commit agent  (every 30 min, self-gating)
  python run.py commit           → Force commit  (manual override)
"""

import sys
import os
import logging
from datetime import datetime, timezone, timedelta
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    handlers=[logging.StreamHandler()],
)
log = logging.getLogger("tobias")


def _store():
    from core.github_store import GitHubStore
    return GitHubStore(os.environ["GITHUB_TOKEN"], os.environ["GITHUB_REPO"])


def run_settle():
    log.info("=" * 60)
    log.info(f"TOBIAS — SETTLER — {datetime.now(timezone.utc).isoformat()}")
    log.info("=" * 60)
    from agents.settler import run
    run(_store())


def run_analyst():
    log.info("=" * 60)
    log.info(f"TOBIAS — ANALYST — {datetime.now(timezone.utc).isoformat()}")
    log.info("=" * 60)
    from agents.analyst import run
    run(_store())


def run_scout():
    log.info("=" * 60)
    log.info(f"TOBIAS — SCOUT — {datetime.now(timezone.utc).isoformat()}")
    log.info("=" * 60)
    from agents.scout import run
    run(_store())


def run_commit(force: bool = False):
    log.info("=" * 60)
    log.info(f"TOBIAS — COMMIT{'(FORCED)' if force else ''} — {datetime.now(timezone.utc).isoformat()}")
    log.info("=" * 60)
    from agents.commit import run
    run(_store(), force=force)


def run_commit_if_ready():
    store = _store()
    state, _ = store.read_state_and_history()
    now   = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")

    commit_date   = state.get("commit_date", "")
    commit_status = state.get("commit_status", "pending")

    # ── WINDOW GATE — per pick or approaching slate game ───────────────────
    draft_picks  = state.get("draft_picks", [])
    slate_times  = state.get("slate_game_times", [])

    # Picks within the 45-min tip-off window
    window_picks = []
    soonest_future = None
    for p in draft_picks:
        try:
            t = datetime.fromisoformat(p["time"].replace("Z", "+00:00"))
            delta_min = (t - now).total_seconds() / 60
            if delta_min <= 45:
                window_picks.append(p)
            elif soonest_future is None or t < soonest_future:
                soonest_future = t
        except Exception:
            continue

    # Any slate game (including Scout-rejected) approaching tip-off?
    # Opens a late-scout window even when draft_picks is empty.
    approaching_game = False
    for ts in slate_times:
        try:
            t = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            delta_min = (t - now).total_seconds() / 60
            if -30 <= delta_min <= 45:   # window: up to 30 min past tip
                approaching_game = True
                break
        except Exception:
            continue

    # Skip if done AND no game is approaching (nothing left to late-scout)
    # commit_date == today guard preserves UTC midnight boundary behaviour:
    # Scout resets commit_status to "pending" for the next day's slate.
    if commit_date == today and commit_status == "done" and not approaching_game:
        log.info("commit_if_ready: status=done and no approaching games — skipping")
        return

    # Skip if no picks in window AND no game approaching
    if not window_picks and not approaching_game:
        if soonest_future:
            remaining = int((soonest_future - timedelta(minutes=45) - now).total_seconds() / 60)
            log.info(f"commit_if_ready: {remaining}min until next window — skipping")
        else:
            log.info("commit_if_ready: no picks or approaching games — skipping")
        return

    log.info(f"commit_if_ready: {len(window_picks)} pick(s) in window | approaching_game={approaching_game} — running commit")
    from agents.commit import run
    run(store, force=False, window_picks=window_picks)


# ── Entry ──────────────────────────────────────────────────────────────────────

COMMANDS = {
    "settle":           run_settle,
    "analyst":          run_analyst,
    "scout":            run_scout,
    "commit":           lambda: run_commit(force=True),
    "commit_if_ready":  run_commit_if_ready,
}

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd not in COMMANDS:
        print(f"Usage: python run.py [{' | '.join(COMMANDS)}]")
        sys.exit(1)

    try:
        COMMANDS[cmd]()
    except Exception as e:
        log.exception(f"TOBIAS FATAL ERROR in '{cmd}': {e}")
        sys.exit(0)
