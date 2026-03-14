---
version: 1
updated_at: null
updated_by: bootstrap
llm: bootstrap
---

## SECTION:line_movement_rules
Line moved > 0.10 in your favour → confirm pick, note improvement.
Line moved > 0.10 against → investigate WHY before confirming (injury? sharp money?).
Line moved > 0.20 either way → treat as major signal, always re-research first.

## SECTION:injury_check_rules
Anchor player confirmed OUT → cancel pick immediately. Reason: "Anchor [name] OUT confirmed".
Anchor player upgraded (was Questionable, now Probable/Active) → re-evaluate odds; may increase confidence.
New injury discovered since scout (not in anchor_players) → re-evaluate impact before confirming.

## SECTION:late_scout_triggers
Actively hunt for new edges that emerged since 14:00 scout:
- Stars ruled out in the last 2–3 hours (books often slow to react)
- Significant line movement suggesting sharp money
- Back-to-back confirmed late
- Odds that drifted INTO the 1.70–2.50 range since scout

## SECTION:cancel_criteria
Cancel a draft pick if ANY of:
- Anchor player confirmed OUT
- Line moved > 0.20 against with no clear explanation
- New information fundamentally changes the edge (e.g. opponent's star back from injury)
- Total exposure would exceed 70% of bankroll after adding this pick

## SECTION:commit_staking
Same confidence/staking rules as scout.
Recalculate stake based on CURRENT bankroll at commit time (not scout time).
If total committed stake (draft picks + new picks) > 70% bankroll → reduce lowest-confidence picks first.
