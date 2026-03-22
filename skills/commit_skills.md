---
version: 5
updated_at: 2026-03-22T14:14:46.407021+00:00
updated_by: analyst_2026-03-22
llm: claude-sonnet-4-6
---

## SECTION:odds_validation
Commit MUST re-validate odds before confirming any pick:
- ML floor: 1.65 (Scout floor is 1.70 — Commit allows 0.05 drift as Scout already validated the edge)
- ML ceiling: 2.50 (same as Scout — do not confirm if odds drifted above 2.50, re-evaluate)
- Spread target: 1.80–2.30 (floor 1.75 at commit — same 0.05 drift allowance)
- O/U target: 1.80–2.05 (floor 1.75 at commit — same 0.05 drift allowance)
- EV requirement: EV = (confidence/100 × odds) - 1 ≥ 0.05. Recalculate EV at commit-time odds.
If current odds fall outside valid range → do NOT confirm. Cancel with reason "odds out of valid range at commit time".

## SECTION:line_movement_rules
Compare current odds to Scout's drafted odds (stored in draft pick).
Movement in your favour (odds improved, e.g. 2.38 → 2.55):
→ Confirm at ORIGINAL stake. Do not increase stake. Note improvement in report.
→ Rationale: Scout set confidence based on analysis, not on odds alone.
Movement against (odds worsened, e.g. 2.38 → 2.15):
→ Still above floor: re-evaluate with confidence -10. Recalculate EV at new odds. Confirm only if EV ≥ 0.05.
→ Below floor: cancel. Reason: "Odds fell below confirmation floor".
Movement > 0.20 in either direction: treat as major signal. Always check for undisclosed injuries or lineup changes.
Movement > 0.30: cancel unless you can explicitly explain the cause.

## SECTION:injury_check_rules
Anchor player confirmed OUT → cancel immediately. Reason: "Anchor [name] OUT confirmed at commit time".
Anchor player upgraded (was OUT/Doubtful, now Active) → re-evaluate with confidence +10. May increase EV.
New injury discovered since Scout (not in anchor_players) → re-evaluate full pick. Apply franchise_player_rules from scout_skills.
No injury update available → proceed with Scout's original assessment.

CRITICAL — QUESTIONABLE/GTD RULE:
If your bet thesis DEPENDS on a key player being OUT (i.e. their absence is why you have the edge):
- Player listed Questionable or GTD → DO NOT confirm. Cancel: "Pick depends on unconfirmed absence."
- Player listed Doubtful → proceed with confidence -15, stake -20% ONLY if EV still ≥ 0.05 without them.
- Only confirm injury-dependent picks when player is listed OUT or officially scratched (DNP).
If your bet thesis does NOT depend on their absence (edge exists regardless):
- Questionable → apply standard confidence -10, stake -20% per franchise_player_rules.
- Proceed if EV ≥ 0.05 after adjustment.

## SECTION:line_anomaly_check
Run the same anomaly check as Scout before confirming ANY pick AND before adding any late picks:
- Tank-tier team priced as favourite at ≤ 1.35 → do not confirm/add
- Home team with materially better record priced as underdog at ≥ 2.20 → investigate before confirming
- Implied probability gap > 40pts vs actual record gap → flag and investigate
- Line moved > 0.30 in last 2 hours with no news → cancel/defer
If an anomaly Scout flagged at 14:00 now has an explanation (e.g. star confirmed OUT) → anomaly resolved. Re-evaluate at current odds.

## SECTION:late_scout_triggers
Hunt for new edges that emerged since 14:00 Scout:
- Time gate: only add new picks if first_game_time - now > 20 minutes.
- Quantity gate: max 1 new pick added at Commit phase per day.
- Confidence gate: new picks require confidence ≥ 60.
- EV gate: EV ≥ 0.05 required.
- Odds gate: same odds_validation rules apply.
Triggers worth acting on:
- Star ruled out in last 2-3 hours and books haven't fully adjusted
- Odds drifted INTO valid range since Scout
- B2B confirmed late that Scout didn't have
- Line anomaly from Scout now has confirmed explanation creating value on the other side

## SECTION:cancel_criteria
Cancel a draft pick if ANY of:
- Anchor player confirmed OUT at commit time
- Odds fell outside valid range for market type
- Line moved > 0.20 against with no clear explanation
- Line moved > 0.30 for any reason without explicit justification
- New information fundamentally changes the edge
- Total exposure would exceed 70% of bankroll after all picks
- EV recalculated at current odds falls below 0.05

## SECTION:data_quality_rules
INJURY FEED QUALITY GATES — same as Scout, applied at commit time:

Source: nba_official → normal rules apply.
Source: espn fallback → confidence CAP 50, spreads/totals BANNED.
If a draft pick has confidence > 50 and injury source is ESPN → reduce to 50 before confirming.
If a draft pick is a spread or total and injury source is ESPN → CANCEL: "ESPN fallback — spread/total too risky."
Source: espn + < 5 teams → cancel ALL picks: "Critically incomplete injury data at commit time."
Source: none → cancel ALL picks.

PACE DATA QUALITY FLAG:
→ If Pace = 0.0 universally in the advanced stats feed, treat Pace as unavailable at commit time.
→ Cancel any totals pick whose thesis relied on pace signals if pace was flagged as unavailable at Scout.
→ Log: "Pace data unavailable at Scout — totals pick thesis compromised, cancelling."

## SECTION:commit_staking
Apply exact same confidence/staking tiers as scout_skills confidence_staking section.
Recalculate stake based on CURRENT bankroll at commit time (not scout time).
Do NOT increase stake even if odds improved since Scout — original stake stands.
If total committed stake > 70% bankroll → reduce lowest-confidence picks first.
If a pick's confidence was adjusted (injury news, line movement) → recalculate stake at new confidence level.

85–100 Elite: up to 30% of bankroll
70–84 High: 20–25%
55–69 Medium: 15–20%
50–54 Speculative: 10%
0–49: Do not confirm
