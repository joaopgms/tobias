"""
agents/analyst.py
Tobias — Analyst Agent (11:00 UTC)

Responsibilities:
  1. Review yesterday's settlement results (from state)
  2. Fetch current NBA standings + injury landscape via ESPN
  3. Call LLM to reason about what's working, what's changed
  4. Apply patch/delta to scout_skills.md and commit_skills.md
  5. Write analyst_notes.md with today's meta-reasoning
  6. Append structured diff entry to audit/analyst_log.jsonl
  7. Write updated skills back to GitHub

Skill file format:
  Each file has YAML frontmatter (version, updated_at, etc.)
  and named sections: ## SECTION:name
  The LLM returns patches as JSON — each patch targets one section by name.
  Patch actions: "replace" (full section replacement) | "no_change"
"""

import json
import re
import logging
from datetime import datetime, date, timezone

from core.llm import call_llm, extract_tag, current_provider_name
from core.espn import fetch_standings, fetch_injuries

log = logging.getLogger(__name__)

# ── Skills patch helpers ───────────────────────────────────────────────────────

def _parse_frontmatter(content: str) -> tuple[dict, str]:
    """Split YAML frontmatter from body. Returns (meta_dict, body)."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    meta = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, parts[2].strip()


def _parse_sections(body: str) -> dict[str, str]:
    """Parse ## SECTION:name blocks into {name: content}."""
    sections = {}
    current_name = None
    current_lines = []
    for line in body.splitlines():
        m = re.match(r'^## SECTION:(\S+)', line)
        if m:
            if current_name:
                sections[current_name] = "\n".join(current_lines).strip()
            current_name  = m.group(1)
            current_lines = []
        else:
            current_lines.append(line)
    if current_name:
        sections[current_name] = "\n".join(current_lines).strip()
    return sections


def _build_skills_file(meta: dict, sections: dict[str, str]) -> str:
    """Reconstruct skills .md from meta + sections dict."""
    lines = ["---"]
    for k, v in meta.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    lines.append("")
    for name, content in sections.items():
        lines.append(f"## SECTION:{name}")
        lines.append(content)
        lines.append("")
    return "\n".join(lines)


def _apply_patches(current_content: str, patches: list[dict],
                   new_version: int, ts: str, llm_name: str) -> tuple[str, list[dict]]:
    """
    Apply a list of patch objects to a skills file.
    Each patch: {section, action, new_content, reason}
    Returns (new_file_content, applied_patches_with_before_after).
    """
    meta, body   = _parse_frontmatter(current_content)
    sections     = _parse_sections(body)
    applied      = []

    for patch in patches:
        section = patch.get("section", "")
        action  = patch.get("action", "no_change")
        reason  = patch.get("reason", "")
        new_sec = patch.get("new_content", "")

        if action == "no_change" or not section:
            continue

        before = sections.get(section, "[new section]")

        if action == "replace" and new_sec:
            sections[section] = new_sec.strip()
            applied.append({
                "section": section,
                "action":  "replace",
                "reason":  reason,
                "before":  before[:200],   # truncate for log compactness
                "after":   new_sec[:200],
            })
            log.info(f"  Patched [{section}]: {reason[:80]}")

        elif action == "add" and new_sec:
            sections[section] = new_sec.strip()
            applied.append({
                "section": section,
                "action":  "add",
                "reason":  reason,
                "before":  "[did not exist]",
                "after":   new_sec[:200],
            })
            log.info(f"  Added   [{section}]: {reason[:80]}")

    # Update frontmatter
    meta["version"]    = str(new_version)
    meta["updated_at"] = ts
    meta["updated_by"] = f"analyst_{ts[:10]}"
    meta["llm"]        = llm_name

    return _build_skills_file(meta, sections), applied


# ── Performance summary for LLM context ───────────────────────────────────────

def _perf_summary(state: dict) -> str:
    """Compact performance summary for the LLM prompt."""
    settled = state.get("settled_bets", [])
    pending = state.get("pending_bets", [])

    recent  = sorted(settled, key=lambda b: b.get("settled_at", ""), reverse=True)[:10]
    wins    = sum(1 for b in recent if b.get("result") == "WON")
    losses  = sum(1 for b in recent if b.get("result") == "LOST")
    pnl_l10 = sum(b.get("pnl", 0) or 0 for b in recent)

    lines = [
        f"Bankroll: €{state['bankroll']:.2f} | Peak: €{state.get('bankroll_peak', 0):.2f}",
        f"Net P&L: €{state.get('net_pnl', 0):.2f}",
        f"Last 10 settled: {wins}W / {losses}L | P&L: €{pnl_l10:+.2f}",
        f"Pending: {len(pending)} bets",
        "",
        "Recent settled bets:",
    ]
    for b in recent[:5]:
        result = b.get("result", "?")
        icon   = "✅" if result == "WON" else "❌"
        lines.append(
            f"  {icon} {b.get('match','?')} | {b.get('pick','?')} @ {b.get('odds','?')} "
            f"| conf={b.get('confidence','?')} | pnl=€{b.get('pnl',0):+.2f}"
        )
    return "\n".join(lines)


# ── LLM prompt ────────────────────────────────────────────────────────────────

ANALYST_SYSTEM = """You are the Analyst agent for Tobias, an autonomous NBA betting simulation.
Your job is to review performance data and current NBA context, then decide which sections
of the scouting and commit skills files need updating.

You output structured JSON patches — nothing else.
Be conservative: only patch sections where you have clear evidence the current guidance is wrong or outdated.
Reasoning quality matters more than frequency of changes."""


def _build_analyst_prompt(perf: str, standings_text: str,
                           injuries_text: str,
                           scout_content: str, commit_content: str) -> str:
    return f"""## PERFORMANCE REVIEW
{perf}

## CURRENT NBA STANDINGS (top/bottom relevant teams)
{standings_text}

## CURRENT INJURY LANDSCAPE
{injuries_text}

## CURRENT scout_skills.md
{scout_content}

## CURRENT commit_skills.md
{commit_content}

---

Review the above and return a JSON object with patches for both skills files.
Only include sections that genuinely need updating based on evidence above.

Output ONLY valid JSON in this exact structure:

{{
  "scout_patches": [
    {{
      "section": "section_name",
      "action": "replace",
      "new_content": "full replacement text for this section",
      "reason": "one sentence explaining the evidence for this change"
    }}
  ],
  "commit_patches": [
    {{
      "section": "section_name",
      "action": "replace",
      "new_content": "full replacement text for this section",
      "reason": "one sentence explaining the evidence for this change"
    }}
  ],
  "analyst_notes": "2-3 sentences summarising today's key findings and any macro NBA trends worth watching",
  "no_change_reason": "if no patches needed, explain why here — otherwise leave empty"
}}

Rules:
- "action" must be "replace" or "add" (add = new section) — never delete sections
- "new_content" must be the COMPLETE replacement text for that section (not a diff)
- Only patch what the evidence supports — 0 patches is a valid and good answer
- Keep new_content compact — these files are fed to agents as context tokens
"""


# ── Standings + injuries → compact text ───────────────────────────────────────

def _standings_text(standings: dict) -> str:
    if not standings:
        return "Standings unavailable."
    # Deduplicate (standings indexed by both name and abbr)
    seen = set()
    rows = []
    for name, s in standings.items():
        if len(name) <= 3:   # abbr — skip
            continue
        key = (s.get("wins"), s.get("losses"))
        if name in seen:
            continue
        seen.add(name)
        rows.append((int(s.get("wins", 0)), int(s.get("losses", 0)), name, s))

    rows.sort(key=lambda x: -x[0])
    lines = []
    for w, l, name, s in rows[:30]:
        streak = s.get("streak", "")
        l10    = s.get("l10", "")
        lines.append(f"{name}: {w}-{l}  L10:{l10}  streak:{streak}")
    return "\n".join(lines)


def _injuries_text(injuries: dict) -> str:
    if not injuries:
        return "No injury reports."
    lines = []
    for team, players in injuries.items():
        out_players = [p for p in players if p["status"] in ("Out", "Doubtful")]
        if out_players:
            names = ", ".join(f"{p['name']} ({p['status']})" for p in out_players[:3])
            lines.append(f"{team}: {names}")
    return "\n".join(lines[:25]) if lines else "No significant injuries."


# ── Main run ───────────────────────────────────────────────────────────────────

def run(store) -> None:
    now     = datetime.now(timezone.utc)
    now_iso = now.isoformat()
    today   = now.strftime("%Y-%m-%d")
    llm     = current_provider_name()

    # ── 1. Load state ──────────────────────────────────────────────────────────
    state, history = store.read_state_and_history()

    # ── 2. Fetch NBA context ───────────────────────────────────────────────────
    log.info("Analyst: fetching standings + injuries…")
    standings = fetch_standings()
    injuries  = fetch_injuries()

    perf           = _perf_summary(state)
    standings_str  = _standings_text(standings)
    injuries_str   = _injuries_text(injuries)

    # ── 3. Load current skills files ──────────────────────────────────────────
    scout_content  = store.read_md("scout_skills")
    commit_content = store.read_md("commit_skills")

    # ── 4. Parse current version numbers ──────────────────────────────────────
    scout_meta,  _ = _parse_frontmatter(scout_content)
    commit_meta, _ = _parse_frontmatter(commit_content)
    scout_ver  = int(scout_meta.get("version", 1))
    commit_ver = int(commit_meta.get("version", 1))

    # ── 5. Call LLM ───────────────────────────────────────────────────────────
    log.info("Analyst: calling LLM for skills review…")
    system = ANALYST_SYSTEM
    user   = _build_analyst_prompt(perf, standings_str, injuries_str,
                                    scout_content, commit_content)
    raw = call_llm(system, user, max_tokens=2048)

    # ── 6. Parse LLM response ─────────────────────────────────────────────────
    try:
        # Strip markdown code fences if present
        clean = re.sub(r'^```(?:json)?\s*', '', raw.strip(), flags=re.MULTILINE)
        clean = re.sub(r'\s*```$', '', clean.strip(), flags=re.MULTILINE)
        result = json.loads(clean)
    except json.JSONDecodeError as e:
        log.error(f"Analyst: LLM returned invalid JSON: {e}\nRaw: {raw[:400]}")
        _append_audit(store, now_iso, llm, error=str(e),
                      scout_patches=[], commit_patches=[], notes="JSON parse error")
        return

    scout_patches  = result.get("scout_patches", [])
    commit_patches = result.get("commit_patches", [])
    analyst_notes  = result.get("analyst_notes", "")
    no_change      = result.get("no_change_reason", "")

    log.info(f"Analyst: {len(scout_patches)} scout patches, {len(commit_patches)} commit patches")

    # ── 7. Apply patches ──────────────────────────────────────────────────────
    scout_changed = commit_changed = False
    scout_applied = commit_applied = []

    if scout_patches:
        new_scout, scout_applied = _apply_patches(
            scout_content, scout_patches, scout_ver + 1, now_iso, llm)
        if scout_applied:
            store.write_md("scout_skills", new_scout,
                           f"analyst: patch scout_skills v{scout_ver+1} ({today})")
            scout_changed = True

    if commit_patches:
        new_commit, commit_applied = _apply_patches(
            commit_content, commit_patches, commit_ver + 1, now_iso, llm)
        if commit_applied:
            store.write_md("commit_skills", new_commit,
                           f"analyst: patch commit_skills v{commit_ver+1} ({today})")
            commit_changed = True

    # ── 8. Write analyst_notes.md ─────────────────────────────────────────────
    notes_content = f"""---
date: {today}
llm: {llm}
scout_patches: {len(scout_applied)}
commit_patches: {len(commit_applied)}
---

## Today's Analysis — {today}

{analyst_notes}

{"## No changes this run" + chr(10) + no_change if no_change and not scout_applied and not commit_applied else ""}

## Scout patches applied
{chr(10).join(f"- [{p['section']}] {p['reason']}" for p in scout_applied) or "None"}

## Commit patches applied
{chr(10).join(f"- [{p['section']}] {p['reason']}" for p in commit_applied) or "None"}
"""
    store.write_md("analyst_notes", notes_content,
                   f"analyst: notes {today}")

    # ── 9. Audit log ──────────────────────────────────────────────────────────
    _append_audit(store, now_iso, llm, error="",
                  scout_patches=scout_applied,
                  commit_patches=commit_applied,
                  notes=analyst_notes,
                  no_change=no_change,
                  bankroll=state["bankroll"],
                  net_pnl=state.get("net_pnl", 0))

    log.info(f"Analyst done — scout changed={scout_changed}, commit changed={commit_changed}")
    if analyst_notes:
        log.info(f"Notes: {analyst_notes[:120]}")


def _append_audit(store, ts: str, llm: str, error: str = "",
                  scout_patches: list = None, commit_patches: list = None,
                  notes: str = "", no_change: str = "",
                  bankroll: float = 0, net_pnl: float = 0):
    entry = {
        "ts":               ts,
        "agent":            "analyst",
        "llm":              llm,
        "error":            error,
        "bankroll":         round(bankroll, 2),
        "net_pnl":          round(net_pnl, 2),
        "scout_patches":    scout_patches or [],
        "commit_patches":   commit_patches or [],
        "notes":            notes,
        "no_change_reason": no_change,
    }
    try:
        store.append_jsonl("analyst_log", entry)
    except Exception as e:
        log.warning(f"Analyst audit log failed: {e}")
