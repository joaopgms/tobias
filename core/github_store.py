"""
core/github_store.py
All GitHub read/write operations for Tobias.
GitHub is the entire data store — no database, no persistent disk.
"""

import json
import base64
import logging
from datetime import datetime, timezone
from github import Github, GithubException

log = logging.getLogger(__name__)


class GitHubStore:
    """Read and write all Tobias files to a GitHub repo."""

    # Files managed by Tobias
    FILES = {
        "state":       "data/state.json",
        "history":     "data/history.json",
        "data_js":     "data/data.js",
        "config":      "data/config.json",
        "scout_skills":      "skills/scout_skills.md",
        "commit_skills":     "skills/commit_skills.md",
        "analyst_notes":     "skills/analyst_notes.md",
        "analyst_rules":     "skills/analyst_rules.md",
        "playoff_context":   "skills/playoff_context.md",
        "analyst_log":    "audit/analyst_log.jsonl",
        "scout_log":      "audit/scout_log.jsonl",
        "commit_log":     "audit/commit_log.jsonl",
        "settler_log":       "audit/settler_log.jsonl",
        "scout_archive":     "data/scout_archive.json",
        "commit_archive":    "data/commit_archive.json",
    }

    def __init__(self, token: str, repo_name: str):
        self._gh = Github(token)
        self._repo = self._gh.get_repo(repo_name)
        self._shas: dict[str, str] = {}   # path → sha (needed for updates)
        log.info(f"GitHubStore ready → {repo_name}")

    # ── low-level ──────────────────────────────────────────────────────────────

    def _get_file(self, path: str) -> tuple[str, str]:
        """Returns (content_str, sha). Raises FileNotFoundError if missing."""
        try:
            f = self._repo.get_contents(path)
            content = base64.b64decode(f.content).decode("utf-8")
            self._shas[path] = f.sha
            return content, f.sha
        except GithubException as e:
            if e.status == 404:
                raise FileNotFoundError(f"GitHub: {path} not found")
            raise

    def _put_file(self, path: str, content: str, message: str) -> None:
        """Create or update a file on GitHub."""
        sha = self._shas.get(path)
        if sha is None:
            # Try to fetch SHA if we haven't cached it yet
            try:
                _, sha = self._get_file(path)
            except FileNotFoundError:
                sha = None

        if sha:
            self._repo.update_file(path, message, content, sha)
            log.info(f"  ↑ updated {path}")
        else:
            self._repo.create_file(path, message, content)
            log.info(f"  ↑ created {path}")

        # Invalidate SHA cache so next write re-fetches
        self._shas.pop(path, None)

    # ── JSON helpers ───────────────────────────────────────────────────────────

    def read_json(self, key: str) -> dict | list:
        path = self.FILES[key]
        content, _ = self._get_file(path)
        return json.loads(content)

    def write_json(self, key: str, data: dict | list, message: str) -> None:
        path = self.FILES[key]
        content = json.dumps(data, indent=2, ensure_ascii=False)
        self._put_file(path, content, message)


    def append_report(self, report_type: str, entry: dict) -> None:
        """Append a report entry to the archive .json only (append-only, permanent record).
        Rolling .js files were removed — archive.json is the sole record."""
        import json as _json
        now_ts = entry.get("ts", "")
        archive_key = f"{report_type}_archive"
        try:
            existing_arch, _ = self._get_file(self.FILES[archive_key])
            archive = _json.loads(existing_arch) if existing_arch.strip() else []
        except Exception:
            archive = []
        archive.append(entry)
        self._put_file(self.FILES[archive_key],
                       _json.dumps(archive, indent=2, ensure_ascii=False),
                       f"{report_type}: archive {now_ts[:10]}")


    def read_config(self) -> dict:
        """Read agent model config. Returns defaults if file missing."""
        try:
            return self.read_json("config")
        except FileNotFoundError:
            return {
                "analyst_model": "claude-sonnet-4-6",
                "scout_model":   "claude-sonnet-4-6",
                "commit_model":  "claude-sonnet-4-6",
                "settler_model": "claude-haiku-4-5-20251001",
                "llm_provider":  "claude",
            }

    def write_config(self, config: dict, message: str = "config: update agent models") -> None:
        self.write_json("config", config, message)

    # ── Markdown helpers ───────────────────────────────────────────────────────

    def read_md(self, key: str) -> str:
        path = self.FILES[key]
        try:
            content, _ = self._get_file(path)
            return content
        except FileNotFoundError:
            return ""

    def write_md(self, key: str, content: str, message: str) -> None:
        path = self.FILES[key]
        self._put_file(path, content, message)

    # ── JSONL helpers (append-only audit logs) ─────────────────────────────────

    def append_jsonl(self, key: str, entry: dict) -> None:
        """Append one JSON object as a new line to a .jsonl audit log."""
        path = self.FILES[key]
        try:
            existing, _ = self._get_file(path)
            # Ensure file ends with newline
            if existing and not existing.endswith("\n"):
                existing += "\n"
        except FileNotFoundError:
            existing = ""

        line = json.dumps(entry, ensure_ascii=False) + "\n"
        new_content = existing + line
        ts = entry.get("ts", datetime.now(timezone.utc).isoformat())
        self._put_file(path, new_content, f"audit: {key} {ts}")

    def read_jsonl(self, key: str, last_n: int = 50) -> list[dict]:
        """Read last N entries from a .jsonl file."""
        path = self.FILES[key]
        try:
            content, _ = self._get_file(path)
        except FileNotFoundError:
            return []
        lines = [l for l in content.strip().splitlines() if l.strip()]
        entries = []
        for line in lines[-last_n:]:
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue
        return entries

    # ── Convenience: read all core state at once ───────────────────────────────

    def read_state_and_history(self) -> tuple[dict, dict]:
        state = self.read_json("state")
        history = self.read_json("history")
        return state, history

    # ── data.js generator ─────────────────────────────────────────────────────

    def write_data_js(self, state: dict, history: dict,
                      scout_report: str = "", commit_report: str = "",
                      config: dict = None) -> None:
        """Regenerate data.js from current state + history."""
        ts = datetime.now(timezone.utc).isoformat()
        state_json  = json.dumps(state,   indent=2, ensure_ascii=False)
        history_json = json.dumps(history, indent=2, ensure_ascii=False)
        draft_json  = json.dumps(state.get("draft_picks", []), indent=2, ensure_ascii=False)

        cfg = config or {}
        # Read skills files for live export to dashboard
        scout_skills_text = ""
        commit_skills_text = ""
        try:
            scout_skills_text = self._get_file(self.FILES["scout_skills"])[0]
        except Exception:
            pass
        try:
            commit_skills_text = self._get_file(self.FILES["commit_skills"])[0]
        except Exception:
            pass
        def js_str(s: str) -> str:
            return json.dumps(s)  # safe JS string with escaping

        # Read analyst notes + rules for export
        analyst_notes_text = ""
        analyst_rules_text = ""
        try:
            analyst_notes_text = self._get_file(self.FILES["analyst_notes"])[0]
        except Exception:
            pass
        try:
            analyst_rules_text = self._get_file(self.FILES["analyst_rules"])[0]
        except Exception:
            pass

        # Read audit logs for export
        analyst_log = []
        scout_log   = []
        commit_log  = []
        settler_log = []
        try: analyst_log  = self.read_jsonl("analyst_log",  last_n=50)
        except Exception: pass
        try: scout_log    = self.read_jsonl("scout_log",    last_n=50)
        except Exception: pass
        try: commit_log   = self.read_jsonl("commit_log",   last_n=50)
        except Exception: pass
        try: settler_log  = self.read_jsonl("settler_log",  last_n=50)
        except Exception: pass
        audit_log = sorted(
            analyst_log + scout_log + commit_log + settler_log,
            key=lambda e: e.get("ts", "")
        )

        content = f"""// Auto-generated by Tobias agents -- do not edit manually
// Last updated: {ts}

const STATE_DATA = {state_json};
const HISTORY_DATA = {history_json};
const DRAFT_PICKS = {draft_json};
const SCOUT_STATUS = {js_str(state.get('scout_status', 'pending'))};
const SCOUT_ERROR = {js_str(state.get('scout_error', ''))};
const SCOUT_UPDATED_AT = {js_str(state.get('scout_updated_at') or '')};
const COMMIT_STATUS = {js_str(state.get('commit_status', 'pending'))};
const COMMIT_UPDATED_AT = {js_str(state.get('commit_updated_at') or '')};
const LLM_PROVIDER = {js_str(state.get('llm_provider', 'claude'))};
const CONFIG_DATA = {json.dumps(cfg, indent=2, ensure_ascii=False)};
const SCOUT_SKILLS = {js_str(scout_skills_text)};
const COMMIT_SKILLS = {js_str(commit_skills_text)};
const ANALYST_RULES = {js_str(analyst_rules_text)};
const AUDIT_LOG = {json.dumps(audit_log, ensure_ascii=False)};
const ANALYST_NOTES = {js_str(analyst_notes_text)};
"""
        path = self.FILES["data_js"]
        self._put_file(path, content, f"data.js: auto-update {ts[:10]}")
        log.info("  ↑ data.js regenerated")
