---
date: 2026-03-19
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
---

## Today's Analysis — 2026-03-19

The Atlanta Hawks 11-game win streak (L10: 10-0) is the most actionable market signal today — their NetRtg of only +1.5 versus a .551 season W% strongly implies regression is overdue, and any opponent priced ≥ 1.80 should trigger the hot streak fade evaluation. The Washington Wizards (L13, 0-10 L10, all three franchise players OUT) remain the clearest fade target in the league and are approaching historically bad territory. OKC's perfect L10 (10-0) with a +10.9 NetRtg is the strongest team profile in the league but Jalen Williams' unverified absence remains a hard block on their picks until the official PDF confirms.



## Scout patches applied
- [franchise_player_rules] Updated Detroit Pistons roster to add Wendell Moore Jr. (F) OUT per verified feed; removed stale Naz Reid (Minnesota) entry not present in current verified list; all other absences reconciled against today's verified franchise player statuses.
- [tanking_teams] Updated all records, streaks, and L10 figures to match current standings; Atlanta Hawks streak extended to W11 (L10: 10-0) requiring stronger regression-fade flag; Lakers updated to 44-25 W7 streak; OKC updated to 55-15 W10; Brooklyn and Utah streaks updated; Memphis single win noted but tank status maintained given L10 2-8.

## Commit patches applied
None

## Intelligence gaps identified
- **Pace data is universally 0.0 across all 30 teams in the advanced stats feed this session.** — Pace is required for totals betting decisions — both the O/U confidence floor rule and the pace-cluster signals in market_rules depend on it. Without pace data, totals bets cannot be properly evaluated, yet Scout has no automated gate that detects a missing-pace condition and bans totals accordingly. → Add a data quality check in priority_stats step 0 or data_quality_rules: if Pace = 0.0 for all teams (feed failure), treat as 'Pace unavailable' and apply the same ban on totals bets as the ESPN fallback rule does for spreads. Flag in scout_report: 'Pace data missing — totals bets banned this session.'
- **Los Angeles Lakers' NetRtg (+1.4) is dramatically inconsistent with their 44-25 record and 9-1 L10 — suggesting significant luck or strength-of-schedule inflation not currently tracked.** — Scout uses NetRtg as the primary predictive signal (priority_stats step 1) but does not cross-check for record-vs-NetRtg divergence. A team with a top-5 record but a bottom-10 NetRtg is a regression trap that could produce bad ML picks at compressed odds. → Add a record-vs-NetRtg divergence flag to priority_stats or selectivity: if a team's win rate implies top-10 but NetRtg is below +3.0, apply a caution flag (confidence -5) and note potential regression risk in scout reasoning.
- **No rule currently governs when two confirmed tanking teams face each other, which creates a genuinely edgeless matchup.** — If Washington (16-52) plays Brooklyn (17-52) or Utah faces Dallas, tanking rules create contradictory signals — both teams qualify as 'bet against' targets but only one can win. Scout could draft a pick against the worse team without recognising the mutual-tank dynamic. → Add to tanking_teams or market_rules: 'If BOTH teams are confirmed tanking-tier, do NOT draft any pick — no reliable edge exists. Log as no-bet: mutual tank matchup.'
