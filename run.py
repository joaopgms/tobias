"""
run.py — Tobias entry point

Usage:
  python run.py settle   → Settler agent (10:00 UTC)
  python run.py analyst  → Analyst agent (11:00 UTC)
  python run.py scout    → Scout agent   (14:00 UTC)
  python run.py commit   → Commit agent  (16:30 UTC)
"""

import sys
import os
import logging
from datetime import datetime, timezone
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


def run_commit():
    log.info("=" * 60)
    log.info(f"TOBIAS — COMMIT — {datetime.now(timezone.utc).isoformat()}")
    log.info("=" * 60)
    from agents.commit import run
    run(_store())


# ── Entry ──────────────────────────────────────────────────────────────────────

COMMANDS = {
    "settle":  run_settle,
    "analyst": run_analyst,
    "scout":   run_scout,
    "commit":  run_commit,
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
