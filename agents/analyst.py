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

from core.llm import call_llm, call_llm_full, call_llm_full, extract_tag, agent_model_name
from core.espn import (fetch_standings, fetch_injuries, fetch_advanced_stats,
                        fetch_franchise_player_statuses, fetch_season_phase,
                        fetch_playoff_series, format_playoff_series_for_prompt)

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
                "before":  before,
                "after":   new_sec,
            })
            log.info(f"  Patched [{section}]: {reason[:80]}")

        elif action == "add" and new_sec:
            sections[section] = new_sec.strip()
            applied.append({
                "section": section,
                "action":  "add",
                "reason":  reason,
                "before":  "[did not exist]",
                "after":   new_sec,
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
        icon   = "W" if result == "WON" else "L"
        lines.append(
            f"  {icon} {b.get('match','?')} | {b.get('pick','?')} @ {b.get('odds','?')} "
            f"| conf={b.get('confidence','?')} | pnl=€{b.get('pnl',0):+.2f}"
        )
    return "\n".join(lines)


# ── Performance stats (pre-computed — no LLM arithmetic) ──────────────────────

def _compute_performance_stats(state: dict, history: dict) -> dict:
    """
    Compute dimensional performance stats from all settled bets.
    Python does the math — LLM only interprets.
    """
    # Pull all-time settled bets from history.json entries (survives bust resets)
    # history entries of type "bets_placed" have bets with results filled in by settler
    seen: set[str] = set()
    bets: list[dict] = []
    for entry in history.get("entries", []):
        if entry.get("type") != "bets_placed":
            continue
        for b in entry.get("bets", []):
            bid = b.get("id", "")
            if bid and bid not in seen and b.get("result") in ("WON", "LOST"):
                seen.add(bid)
                bets.append(b)
    # Also include state["settled_bets"] for anything not yet in history
    for b in state.get("settled_bets", []):
        bid = b.get("id", "")
        if bid and bid not in seen and b.get("result") in ("WON", "LOST"):
            seen.add(bid)
            bets.append(b)

    total = len(bets)
    if total == 0:
        return {"total": 0}

    wins   = sum(1 for b in bets if b["result"] == "WON")
    losses = total - wins
    total_pnl  = sum(b.get("pnl", 0) or 0 for b in bets)
    avg_odds   = sum(float(b.get("odds", 0) or 0) for b in bets) / total
    avg_conf   = sum(float(b.get("confidence", 0) or 0) for b in bets) / total

    def _breakdown(key_fn: callable, cats: list[str]) -> dict:
        out = {}
        for cat in cats:
            group = [b for b in bets if key_fn(b) == cat]
            if not group:
                continue
            w   = sum(1 for b in group if b["result"] == "WON")
            pnl = sum(b.get("pnl", 0) or 0 for b in group)
            out[cat] = {
                "n": len(group), "w": w, "l": len(group) - w,
                "wr": round(w / len(group) * 100, 1),
                "pnl": round(pnl, 2),
            }
        return out

    def _market(b: dict) -> str:
        mt = (b.get("market_type") or "").lower()
        if mt in ("ml", "moneyline"):   return "ml"
        if mt in ("spread", "ats"):     return "spread"
        if mt in ("total", "ou"):       return "total"
        # infer from pick string
        pick = (b.get("pick") or "").lower()
        if "over " in pick or "under " in pick: return "total"
        import re
        if re.search(r'[+-]\d+\.?\d*\s*$', pick): return "spread"
        return "ml"

    def _tier(b: dict) -> str:
        c = float(b.get("confidence", 0) or 0)
        if c >= 70: return "high"
        if c >= 55: return "medium"
        return "speculative"

    def _odds_range(b: dict) -> str:
        o = float(b.get("odds", 0) or 0)
        if o < 1.90: return "1.70-1.89"
        if o < 2.10: return "1.90-2.09"
        return "2.10-2.50"

    recent = sorted(bets, key=lambda b: b.get("settled_at") or "", reverse=True)[:20]
    r_wins = sum(1 for b in recent if b["result"] == "WON")
    r_pnl  = sum(b.get("pnl", 0) or 0 for b in recent)

    return {
        "total":          total,
        "wins":           wins,
        "losses":         losses,
        "win_rate":       round(wins / total * 100, 1),
        "total_pnl":      round(total_pnl, 2),
        "avg_odds":       round(avg_odds, 2),
        "avg_confidence": round(avg_conf, 1),
        "by_market":      _breakdown(_market,     ["ml", "spread", "total"]),
        "by_confidence":  _breakdown(_tier,       ["high", "medium", "speculative"]),
        "by_odds_range":  _breakdown(_odds_range, ["1.70-1.89", "1.90-2.09", "2.10-2.50"]),
        "recent": {
            "n":       len(recent),
            "wins":    r_wins,
            "losses":  len(recent) - r_wins,
            "win_rate": round(r_wins / len(recent) * 100, 1) if recent else 0,
            "pnl":     round(r_pnl, 2),
        },
    }


def _format_stats_block(stats: dict, milestone_type: str, total_settled: int) -> str:
    """Format computed stats into a clean text block for the LLM prompt."""
    if stats.get("total", 0) == 0:
        return "No settled bets yet — statistical analysis not available."

    lines = [f"ALL-TIME: {stats['wins']}W / {stats['losses']}L | "
             f"Win rate: {stats['win_rate']}% | P&L: €{stats['total_pnl']:+.2f} | "
             f"Avg odds: {stats['avg_odds']} | Avg conf: {stats['avg_confidence']}/100"]

    r = stats["recent"]
    if r["n"]:
        lines.append(f"RECENT {r['n']}: {r['wins']}W / {r['losses']}L | "
                     f"{r['win_rate']}% WR | P&L: €{r['pnl']:+.2f}")

    bm = stats.get("by_market", {})
    if bm:
        lines.append("By market:      " + "  |  ".join(
            f"{k.upper()} {v['n']}bets {v['w']}W/{v['l']}L {v['wr']}% €{v['pnl']:+.2f}"
            for k, v in bm.items()
        ))

    bc = stats.get("by_confidence", {})
    if bc:
        lines.append("By confidence:  " + "  |  ".join(
            f"{k.capitalize()} {v['n']}bets {v['w']}W/{v['l']}L {v['wr']}% €{v['pnl']:+.2f}"
            for k, v in bc.items()
        ))

    bo = stats.get("by_odds_range", {})
    if bo:
        lines.append("By odds range:  " + "  |  ".join(
            f"{k} {v['n']}bets {v['w']}W/{v['l']}L {v['wr']}% €{v['pnl']:+.2f}"
            for k, v in bo.items()
        ))

    if milestone_type == "milestone":
        lines.append(f"\n[MILESTONE — {total_settled} bets reached. "
                     f"Systematic review required. Confidence gate 0.85 for any strategic changes "
                     f"(ev_requirement, confidence_staking, b2b_rules, odds_targets). "
                     f"Cite specific stat rows as evidence for every patch.]")
    elif milestone_type == "checkpoint":
        lines.append(f"\n[CHECKPOINT — {total_settled} bets (25-bet read zone). "
                     f"Analysis only — no strategic patches unless win_rate < 25%.]")

    return "\n".join(lines)


def _detect_milestone(state: dict) -> tuple[str, int, int]:
    """
    Returns (milestone_type, milestone_n, total_settled).
    milestone_type: "milestone" | "checkpoint" | ""
    """
    settled       = state.get("settled_bets", [])
    total         = sum(1 for b in settled if b.get("result") in ("WON", "LOST"))
    last_milestone = int(state.get("analyst_last_milestone", 0))

    if total >= 50:
        current = (total // 50) * 50
        if current > last_milestone:
            return "milestone", current, total

    if 25 <= total < 50 and not state.get("analyst_checkpoint_done"):
        return "checkpoint", 25, total

    return "", 0, total


# ── LLM prompt ────────────────────────────────────────────────────────────────

ANALYST_SYSTEM = "You are the Analyst agent for Tobias. Follow your rules file exactly."
# Full instructions loaded from skills/analyst_rules.md at runtime


def _build_analyst_prompt(stats_block: str, milestone_instructions: str,
                           standings_text: str,
                           injuries_text: str, advanced_stats: str,
                           franchise_status: str,
                           scout_content: str, commit_content: str,
                           analyst_rules: str = "",
                           season_phase: str = "regular",
                           playoff_context: str = "",
                           playoff_series_str: str = "") -> str:

    is_postseason = season_phase in ("playoffs", "playin")
    phase_label = {"regular": "Regular Season", "playin": "Play-In Tournament",
                   "playoffs": "Playoffs", "preseason": "Preseason"}.get(season_phase, season_phase)

    playoff_section = ""
    playoff_patch_instructions = ""
    playoff_output_field = ""
    if is_postseason:
        playoff_section = f"""
## LIVE PLAYOFF SERIES (from ESPN — use this as ground truth for series_context patches)
{playoff_series_str or "No series data retrieved — patch series_context based on standings and injury data only."}

## CURRENT playoff_context.md
{playoff_context or "(empty — populate this session)"}
"""
        playoff_patch_instructions = f"""
## PLAYOFF CONTEXT PATCHES (PRIORITY — update every session during {phase_label})
You MUST update playoff_context.md every session during playoffs/play-in.
Sections to update:
- series_context: Current series scores (e.g. "OKC leads SAS 2-1 — Game 4 tonight at OKC").
  Include home court team for the series and which team has the advantage.
- elimination_flags: Any team facing elimination (down 3-0 or 3-1 in a series, or play-in loser-out game).
- h2h_playoff: Regular season H2H records for each active series. Format: "OKC vs SAS: OKC 3-1 (regular season)".
  Flag if any H2H games were played without key players — discount those results.
  Clear completed series and add new ones as bracket advances.
- playoff_rest: Update if rest days between games change (e.g. 3-day break before a Game 5).
- no_tanking: Keep as-is — no tanking exists in playoffs.
DO NOT patch tanking_teams or b2b_rules in scout_skills during {phase_label} — they are irrelevant.
DO patch franchise_player_rules — injuries still matter critically in playoffs.
"""
        playoff_output_field = """
  "playoff_context_patches": [
    {
      "section": "section_name",
      "action": "replace",
      "new_content": "full replacement text for this section",
      "reason": "one sentence"
    }
  ],"""

    regular_patch_note = "" if is_postseason else "- Always update tanking_teams and franchise_player_rules if data changed"
    b2b_note = "" if is_postseason else "- b2b_rules: B2B impact rules. Only change with performance evidence (5+ B2B bets settled)."
    tanking_note = "" if is_postseason else "- tanking_teams: Confirmed tanks, tank-watch, hot streaks. Update every session with standings."

    return f"""## YOUR RULES (from analyst_rules.md — follow exactly)
{analyst_rules}

---

## SEASON PHASE: {phase_label}

## PERFORMANCE STATS (pre-computed — trust these numbers)
{stats_block}
{milestone_instructions}

## CURRENT NBA STANDINGS (top/bottom relevant teams)
{standings_text}

## CURRENT INJURY LANDSCAPE
{injuries_text}

## VERIFIED FRANCHISE PLAYER STATUSES (ESPN roster + NBA injury feed cross-reference)
{franchise_status}

## ADVANCED STATS (OffRtg / DefRtg / NetRtg / Pace — all 30 teams)
{advanced_stats}

## CURRENT scout_skills.md
{scout_content}

## CURRENT commit_skills.md
{commit_content}
{playoff_section}
---

## NOW
You maintain two skills files that govern Scout (14:00 daily) and Commit (pre tip-off).
You have two jobs:
1. Keep factual data current — franchise player absences, hot/cold streaks, standings{", series scores and elimination flags" if is_postseason else ", tanking teams"}
2. When performance data exists — connect win/loss patterns to specific sections and tighten rules
{playoff_patch_instructions}
## SCOUT SKILLS SECTIONS YOU CAN PATCH
- odds_targets: ML/spread/O-U target ranges. Only change with strong market evidence.
- priority_stats: Scouting priority order including line anomaly check. Only restructure with evidence.
- ev_requirement: EV floor (currently 0.05). Only tighten/loosen based on settled bet patterns.
- franchise_player_rules: Current player absences + confidence adjustments. Update every session with injury feed.
{tanking_note}
{b2b_note}
- confidence_staking: Staking tiers. Only change after 20+ settled bets show a pattern.
- selectivity: Draft criteria. Only tighten/loosen based on pick quality evidence.

## COMMIT SKILLS SECTIONS YOU CAN PATCH
- odds_validation: Confirmation odds floor/ceiling. Only change with evidence of missed value.
- line_movement_rules: Movement thresholds. Only tighten after confirmed bad confirms on moving lines.
- injury_check_rules: Injury response rules. Update if new injury patterns emerge.
- line_anomaly_check: Anomaly thresholds. Tighten if anomalies keep producing losses.
- late_scout_triggers: Late pick criteria. Only loosen/tighten with evidence.
- cancel_criteria: Cancellation rules. Only tighten after bad confirms.
- commit_staking: Same as scout staking. Keep in sync with scout confidence_staking.

## PERFORMANCE FEEDBACK RULE
If settled bets exist: for each losing pattern (3+ losses on same signal type), identify which section
governed those picks and propose a targeted tightening. Be specific — cite the losing picks.
If no settled bets: focus only on factual data updates (franchise_player_rules{", series context" if is_postseason else ", tanking_teams"}).
Never patch strategic sections (ev_requirement, confidence_staking, b2b_rules) without performance evidence.

## STATISTICAL EVIDENCE STANDARD
Use the pre-computed PERFORMANCE STATS above when referencing numbers — do not estimate.
- Daily light pass: patch only if a clear recent pattern (last 10-20 bets) supports it (confidence >= 0.70)
- Milestone run (flagged above): full systematic review across all dimensions required.
  confidence gate raises to 0.85 for any strategic section. Every patch must cite a specific stat row.
  Add a milestone summary to analyst_notes: which signals are working, which aren't, what changed.
- Checkpoint run (flagged above): read-only. Only patch franchise_player_rules{" and series_context" if is_postseason else " and tanking_teams"}.
  Note patterns in analyst_notes for future reference. Do NOT touch strategic sections.

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
  ],{playoff_output_field}
  "analyst_notes": "2-3 sentences summarising today's key findings and macro NBA trends",
  "no_change_reason": "if no patches needed, explain why — otherwise leave empty",
  "intelligence_gaps": [
    {{
      "gap": "one sentence describing missing data, stat, or rule",
      "why": "why it matters — what decision it would have changed or improved",
      "suggestion": "proposed action (e.g. add pace to scout context, add section X, fetch stat Y)",
      "not_patched_reason": "one sentence — why no patch was produced (e.g. 'infrastructure fix needed', 'confidence 0.65 below 0.70 threshold', 'insufficient data — only 3 bets on this market')"
    }}
  ]
}}

Rules:
- "action" must be "replace" or "add" — never delete sections
- "new_content" must be the COMPLETE replacement text (not a diff)
- Only patch what the evidence supports — 0 patches is valid
- Keep new_content compact — these files are fed to agents as context tokens
- {regular_patch_note if not is_postseason else "Always update franchise_player_rules and playoff_context series_context every session"}
- Never patch commit_staking without also patching scout confidence_staking
- intelligence_gaps: run through this checklist every session:
    1. Was there a line anomaly that advanced stats would have explained?
    2. Is there a stat trend (pace, DefRtg cluster, injury pattern) my agents don't track yet?
    3. Did any section produce a bad outcome this week that evidence now contradicts?
    4. {"Are there series momentum patterns or elimination game edges worth tracking?" if is_postseason else "Are there upcoming schedule patterns (B2B clusters, playoff seeding races) worth noting?"}
    5. Is the injury feed coverage adequate, or do I need a better source for any team?
  Output [] if nothing genuinely worth flagging. Quality over quantity.
"""


# ── Standings + injuries → compact text ───────────────────────────────────────

def _franchise_status_text(statuses: dict) -> str:
    """Format verified franchise player statuses for Analyst prompt."""
    if not statuses:
        return "Franchise player verification: no notable absences confirmed from roster + injury feed."
    lines = ["VERIFIED FRANCHISE PLAYER ABSENCES (confirmed via ESPN roster + NBA injury feed):"]
    for team, players in statuses.items():
        for p in players:
            verified = "[VERIFIED]" if p["verified"] else "[roster-only]"
            r = f" — {p['reason']}" if p.get("reason") else ""
            lines.append(f"  {team}: {p['name']} ({p['position']}) {p['status']}{r} [{verified}]")
    lines.append("Use ONLY these verified names when patching franchise_player_rules.")
    lines.append("Do NOT write any player name not in this list.")
    return "\n".join(lines)


def _advanced_stats_text(stats: dict) -> str:
    """Compact advanced stats for top/bottom teams — relevant for Analyst context."""
    if not stats:
        return "Advanced stats unavailable."
    # Sort by NetRtg
    ranked = sorted(stats.items(), key=lambda x: x[1].get("net_rtg", 0), reverse=True)
    lines = ["Team: OffRtg / DefRtg / NetRtg / Pace"]
    for team, s in ranked:
        lines.append(
            f"{team}: {s['off_rtg']} / {s['def_rtg']} / {s['net_rtg']:+.1f} / {s['pace']}"
        )
    return "\n".join(lines[:20])


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
    for w, l, name, s in rows[:20]:
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
    llm     = agent_model_name("analyst")

    # ── 1. Load state ──────────────────────────────────────────────────────────
    state, history = store.read_state_and_history()

    # ── 2. Fetch NBA context ───────────────────────────────────────────────────
    log.info("Analyst: fetching standings + injuries + advanced stats…")
    standings  = fetch_standings()
    injuries   = fetch_injuries()
    adv_stats  = fetch_advanced_stats()
    netrtg_l15 = state.get("netrtg_l15") or {}
    log.info(f"NetRtg L15: {len(netrtg_l15)} teams from state")

    # ── Franchise player roster verification ──────────────────────────────────
    # Identify franchise-tier teams (top-10 by wins) + known injury-sensitive teams
    franchise_teams = []
    seen = set()
    rows = sorted(
        [(int(v.get("wins", 0)), k) for k, v in standings.items() if len(k) > 3],
        reverse=True
    )
    for _, team in rows[:12]:
        if team not in seen:
            franchise_teams.append(team)
            seen.add(team)
    # Always include known high-absence teams
    for team in ["Los Angeles Lakers", "Washington Wizards", "Detroit Pistons"]:
        if team not in seen:
            franchise_teams.append(team)

    log.info(f"Analyst: verifying rosters for {len(franchise_teams)} franchise-tier teams")
    franchise_statuses = fetch_franchise_player_statuses(franchise_teams, injuries)
    franchise_str = _franchise_status_text(franchise_statuses)

    standings_str  = _standings_text(standings)
    injuries_str   = _injuries_text(injuries)
    adv_str        = _advanced_stats_text(adv_stats)

    # ── 3. Load current skills files ──────────────────────────────────────────
    scout_content    = store.read_md("scout_skills")
    commit_content   = store.read_md("commit_skills")
    analyst_rules    = store.read_md("analyst_rules")
    if not analyst_rules:
        log.warning("Analyst: analyst_rules.md missing — using minimal system prompt")

    # ── 3b. Season phase + playoff context ────────────────────────────────────
    season_phase    = fetch_season_phase()
    playoff_context = ""
    playoff_series_str = ""
    if season_phase in ("playoffs", "playin"):
        playoff_context = store.read_md("playoff_context") or ""
        playoff_series  = fetch_playoff_series()
        playoff_series_str = format_playoff_series_for_prompt(playoff_series)
        log.info(f"Analyst: season phase={season_phase} — playoff context + {len(playoff_series)} series loaded")

    # ── 4. Parse current version numbers ──────────────────────────────────────
    scout_meta,  _ = _parse_frontmatter(scout_content)
    commit_meta, _ = _parse_frontmatter(commit_content)
    scout_ver  = int(scout_meta.get("version", 1))
    commit_ver = int(commit_meta.get("version", 1))

    # ── 4b. Milestone detection + performance stats ───────────────────────────
    milestone_type, milestone_n, total_settled = _detect_milestone(state)
    perf_stats  = _compute_performance_stats(state, history)
    stats_block = _format_stats_block(perf_stats, milestone_type, total_settled)

    if milestone_type == "milestone":
        log.info(f"Analyst: MILESTONE run at {total_settled} settled bets (milestone={milestone_n})")
        milestone_instructions = ""          # already embedded in stats_block flag line
    elif milestone_type == "checkpoint":
        log.info(f"Analyst: CHECKPOINT run at {total_settled} settled bets (25-bet zone)")
        milestone_instructions = ""
    else:
        log.info(f"Analyst: daily run — {total_settled} settled bets")
        milestone_instructions = ""

    # ── 5. Call LLM ───────────────────────────────────────────────────────────
    log.info("Analyst: calling LLM for skills review…")
    system = ANALYST_SYSTEM
    user   = _build_analyst_prompt(stats_block, milestone_instructions,
                                    standings_str, injuries_str,
                                    adv_str, franchise_str, scout_content,
                                    commit_content, analyst_rules,
                                    season_phase=season_phase,
                                    playoff_context=playoff_context,
                                    playoff_series_str=playoff_series_str)
    state["agent_models"] = state.get("agent_models", {})
    state["agent_models"]["analyst"] = llm
    llm_result = call_llm_full(system, user, max_tokens=10000, agent="analyst")
    raw = llm_result.text

    # ── 6. Parse LLM response ─────────────────────────────────────────────────
    try:
        # Strip markdown code fences if present
        clean = re.sub(r'^```(?:json)?\s*', '', raw.strip(), flags=re.MULTILINE)
        clean = re.sub(r'\s*```$', '', clean.strip(), flags=re.MULTILINE)
        # Extract only the JSON object — ignore any trailing text Claude may add
        brace_start = clean.find('{')
        if brace_start > 0:
            clean = clean[brace_start:]
        # Find the matching closing brace
        depth = 0
        end_idx = 0
        for i, c in enumerate(clean):
            if c == '{': depth += 1
            elif c == '}':
                depth -= 1
                if depth == 0:
                    end_idx = i + 1
                    break
        if end_idx > 0:
            clean = clean[:end_idx]
        result = json.loads(clean)
    except json.JSONDecodeError as e:
        log.error(f"Analyst: LLM returned invalid JSON: {e}\nRaw: {raw[:400]}")
        _append_audit(store, now_iso, llm, error=str(e),
                      scout_patches=[], commit_patches=[], notes="JSON parse error")
        store.write_data_js(state, history, config=store.read_config())
        return

    scout_patches          = result.get("scout_patches", [])
    commit_patches         = result.get("commit_patches", [])
    playoff_context_patches = result.get("playoff_context_patches", [])
    analyst_notes          = result.get("analyst_notes", "")
    no_change              = result.get("no_change_reason", "")
    intelligence_gaps      = result.get("intelligence_gaps", [])
    if intelligence_gaps:
        log.info(f"Analyst: {len(intelligence_gaps)} intelligence gap(s) identified")
        for g in intelligence_gaps:
            log.info(f"  GAP: {g.get('gap','?')[:100]}")

    log.info(f"Analyst: {len(scout_patches)} scout patches, {len(commit_patches)} commit patches, {len(playoff_context_patches)} playoff patches")

    # ── 7. Apply patches ──────────────────────────────────────────────────────
    scout_changed = commit_changed = playoff_changed = False
    scout_applied = commit_applied = playoff_applied = []

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

    if playoff_context_patches and season_phase in ("playoffs", "playin"):
        playoff_meta, _ = _parse_frontmatter(playoff_context)
        playoff_ver = int(playoff_meta.get("version", 1))
        new_playoff, playoff_applied = _apply_patches(
            playoff_context, playoff_context_patches, playoff_ver + 1, now_iso, llm)
        if playoff_applied:
            store.write_md("playoff_context", new_playoff,
                           f"analyst: patch playoff_context v{playoff_ver+1} ({today})")
            playoff_changed = True

    # ── 8. Write analyst_notes.md ─────────────────────────────────────────────
    # Persist milestone so it doesn't retrigger tomorrow
    if milestone_type == "milestone":
        state["analyst_last_milestone"] = milestone_n
        log.info(f"Analyst: milestone {milestone_n} recorded in state")
    elif milestone_type == "checkpoint":
        state["analyst_checkpoint_done"] = True
        log.info("Analyst: 25-bet checkpoint recorded in state")

    notes_content = f"""---
date: {today}
llm: {llm}
scout_patches: {len(scout_applied)}
commit_patches: {len(commit_applied)}
milestone: {milestone_type or "daily"} ({total_settled} bets)
---

## Today's Analysis — {today}

{analyst_notes}

## Performance Stats
{stats_block}

{"## No changes this run" + chr(10) + no_change if no_change and not scout_applied and not commit_applied and not playoff_applied else ""}

## Scout patches applied
{chr(10).join(f"- [{p['section']}] {p['reason']}" for p in scout_applied) or "None"}

## Commit patches applied
{chr(10).join(f"- [{p['section']}] {p['reason']}" for p in commit_applied) or "None"}

## Playoff context patches applied
{chr(10).join(f"- [{p['section']}] {p['reason']}" for p in playoff_applied) or "None (regular season or no updates needed)"}

## Intelligence gaps identified
{chr(10).join(f"- **{g.get('gap','')}** — {g.get('why','')} → {g.get('suggestion','')}" for g in intelligence_gaps) or "None"}
"""
    state["analyst_updated_at"] = now_iso
    if netrtg_l15:
        state["netrtg_l15"] = netrtg_l15
    store.write_json("state", state, f"analyst: updated_at {today}")
    store.write_md("analyst_notes", notes_content,
                   f"analyst: notes {today}")

    # ── 9. Audit log ──────────────────────────────────────────────────────────
    _append_audit(store, now_iso, llm, error="",
                  scout_patches=scout_applied,
                  commit_patches=commit_applied,
                  playoff_patches=playoff_applied,
                  notes=analyst_notes,
                  no_change=no_change,
                  intelligence_gaps=intelligence_gaps,
                  bankroll=state["bankroll"],
                  net_pnl=state.get("net_pnl", 0),
                  milestone_type=milestone_type or "daily",
                  total_settled=total_settled,
                  perf_stats=perf_stats,
                  llm_meta=llm_result.to_audit_dict())
    store.write_data_js(state, history, config=store.read_config())

    log.info(f"Analyst done — scout changed={scout_changed}, commit changed={commit_changed}")
    if analyst_notes:
        log.info(f"Notes: {analyst_notes[:120]}")


def _append_audit(store, ts: str, llm: str, error: str = "",
                  scout_patches: list = None, commit_patches: list = None,
                  playoff_patches: list = None,
                  notes: str = "", no_change: str = "",
                  intelligence_gaps: list = None,
                  bankroll: float = 0, net_pnl: float = 0,
                  milestone_type: str = "daily", total_settled: int = 0,
                  perf_stats: dict = None,
                  llm_meta: dict = None):
    entry = {
        "ts":               ts,
        "agent":            "analyst",
        "llm":              llm,
        "error":            error,
        "bankroll":         round(bankroll, 2),
        "net_pnl":          round(net_pnl, 2),
        "milestone_type":   milestone_type,
        "total_settled":    total_settled,
        "perf_stats":       perf_stats or {},
        "scout_patches":    scout_patches or [],
        "commit_patches":   commit_patches or [],
        "playoff_patches":  playoff_patches or [],
        "notes":            notes,
        "no_change_reason": no_change,
        "intelligence_gaps": intelligence_gaps or [],
        **(llm_meta or {}),
    }
    try:
        store.append_jsonl("analyst_log", entry)
    except Exception as e:
        log.warning(f"Analyst audit log failed: {e}")
