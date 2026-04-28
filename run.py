"""
run.py — Tobias entry point

Usage:
  python run.py settle           → Settler agent (10:00 UTC)
  python run.py analyst          → Analyst agent (11:00 UTC)
  python run.py scout            → Scout agent   (14:00 UTC)
  python run.py commit_if_ready  → Commit agent  (every 30 min, fires once at first_game_time - 45min)
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
    run(_store())


def run_commit_if_ready():
    store = _store()
    state, _ = store.read_state_and_history()
    now   = datetime.now(timezone.utc)
    today = now.strftime("%Y-%m-%d")

    # Skip if already committed today
    if state.get("commit_date") == today and state.get("commit_status") == "done":
        log.info("commit_if_ready: already committed today — skipping")
        return

    # Wait until 45 min before first game
    fgt = state.get("first_game_time")
    if not fgt:
        log.info("commit_if_ready: no first_game_time yet (Scout hasn't run) — skipping")
        return

    try:
        t = datetime.fromisoformat(fgt.replace("Z", "+00:00"))
    except Exception:
        log.info(f"commit_if_ready: could not parse first_game_time '{fgt}' — skipping")
        return

    if now < t - timedelta(minutes=45):
        remaining = int((t - timedelta(minutes=45) - now).total_seconds() / 60)
        log.info(f"commit_if_ready: {remaining}min until commit window — skipping")
        return

    log.info("commit_if_ready: commit window open — running commit")
    from agents.commit import run
    run(store)


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
