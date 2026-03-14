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

    # ── DATE-BASED IDEMPOTENCY GUARD (bulletproof) ─────────────────────────
    # If we already successfully committed today, never re-run regardless of
    # commit_status — this prevents double-staking if a GitHub write partially
    # failed and status didn't update cleanly.
    commit_date = state.get("commit_date", "")
    if commit_date == today:
        log.info(f"commit_if_ready: already committed on {today} — skipping")
        return

    # ── WINDOW GATE ────────────────────────────────────────────────────────
    first_game_time = state.get("first_game_time")
    if not first_game_time:
        log.info("commit_if_ready: no first_game_time in state — skipping")
        return

    try:
        fgt = datetime.fromisoformat(first_game_time.replace("Z", "+00:00"))
    except ValueError:
        log.warning(f"commit_if_ready: invalid first_game_time '{first_game_time}' — skipping")
        return

    window_open = fgt - timedelta(minutes=15)
    if now < window_open:
        remaining = int((window_open - now).total_seconds() / 60)
        log.info(f"commit_if_ready: {remaining}min until window — skipping")
        return

    # ── STATUS GATE (secondary — catches LLM errors that should retry) ─────
    # Only skip on "done" — "error" or "pending" should retry
    commit_status = state.get("commit_status", "pending")
    if commit_status == "done":
        # Shouldn't reach here normally (commit_date guard above catches it)
        # but kept as belt-and-suspenders
        log.info("commit_if_ready: status=done — skipping")
        return

    log.info(f"commit_if_ready: window open (first game {fgt.strftime('%H:%M')} UTC) — running commit")
    from agents.commit import run
    run(store, force=False)


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
