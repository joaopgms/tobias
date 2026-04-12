---
date: 2026-04-12
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (8 bets)
---

## Today's Analysis — 2026-04-12

This session's roster-only OUT feed reveals an extraordinary number of franchise-level players absent across elite teams: OKC, BOS, NYK, CLE, MIN, and HOU all have their primary stars flagged — this is almost certainly a data artifact from end-of-regular-season roster management rather than confirmed injuries, but cannot be assumed without NBA official PDF verification. The practical consequence is that today's slate carries extreme uncertainty: nearly every top-10 team cannot be picked without PDF verification, severely narrowing the safe betting universe to mid-tier teams (ATL, TOR, ORL, CHH, POR, LAC) where rosters are more stable and the injury feed is cleaner. Denver's 11-game winning streak with Jokic's status unconfirmed adds a further complication — the streak is real but the personnel state is uncertain.

## Performance Stats
ALL-TIME: 11W / 15L | Win rate: 42.3% | P&L: €-394.64 | Avg odds: 1.98 | Avg conf: 65.5/100
RECENT 20: 10W / 10L | 50.0% WR | P&L: €+147.12
By market:      ML 12bets 5W/7L 41.7% €-256.91  |  SPREAD 11bets 5W/6L 45.5% €-114.46  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 8bets 3W/5L 37.5% €+32.90  |  Medium 16bets 8W/8L 50.0% €-286.23  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 6bets 3W/3L 50.0% €-67.95  |  1.90-2.09 17bets 8W/9L 47.1% €-97.38  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Verified absence feed expanded significantly this session — OKC, BOS, NYK, HOU, CLE, MIN, DEN all show multiple franchise-level players in roster-only OUT feed requiring mandatory re-verification before any picks on those teams.
- [tanking_teams] Standings and verified absence feed updated this session — BOS, NYK, CLE, HOU, MIN, DEN, OKC all show multiple franchise-level players in roster-only OUT feed, requiring tanking_teams to flag these teams explicitly as requiring mandatory re-verification before any picks.

## Commit patches applied
None

## Intelligence gaps identified
- **The roster-only OUT feed is flagging nearly all franchise players across top-10 teams simultaneously, which is statistically implausible and likely reflects end-of-season roster filing rather than true absences.** — If Scout treats all roster-only OUTs as true absences, it will incorrectly disqualify games involving OKC, BOS, NYK, CLE, MIN, HOU, DEN — eliminating most high-quality matchups and leaving only mid-tier games to bet. → Add a rule to data_quality_rules: when > 50% of top-10 teams have 3+ franchise-level players in roster-only OUT status simultaneously, flag as 'mass roster-only anomaly' and require NBA official PDF for all picks that session rather than treating roster-only as a confidence cap signal.
- **No rule exists to handle the scenario where an entire team's top-4 players are all in roster-only OUT status simultaneously (e.g. CLE: Mitchell, Allen, Mobley, Harden all OUT roster-only) — current rules only address individual franchise player absences.** — A team missing its entire competitive core at once is a qualitatively different situation from one missing a single star — the team becomes effectively a G-League squad, and any odds offered on them are mispriced relative to their actual roster. → Add a rule to franchise_player_rules: if 3+ franchise-level players on the same team are in roster-only OUT status, apply a 'depleted roster flag' — confidence CAP 45 on that team's ML/spread regardless of NBA PDF status until at least one franchise player is confirmed active.
- **No B2B data is available in today's feed — cannot assess which teams are playing second nights of back-to-backs on this slate.** — B2B rest disadvantage is one of Scout's most reliable spread signals; without knowing which games have B2B teams, the b2b_rules section cannot be applied and confident spread picks cannot be made. → Ensure schedule data (games_l7, B2B flag per team) is included in the daily analyst prompt — this is a data pipeline fix, not a rules patch.
- **The 2.10–2.50 odds range is 0W/3L (0.0% win rate, €-229.31 loss) across all-time bets — a stark underperformance suggesting the agents are systematically mispricing longer-odds picks.** — At 0-for-3 in this odds band, the implied confidence required to generate EV (>47% at 2.10, >40% at 2.50) is not being achieved — Scout may be overconfident when selecting underdogs. → Consider raising the ML odds ceiling from 2.50 to 2.30 (matching the spread ceiling) to exclude the highest-variance range where performance is worst; alternatively, raise the EV floor to 0.08 for picks with odds > 2.10.
