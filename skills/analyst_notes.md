---
date: 2026-04-02
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (12 bets)
---

## Today's Analysis — 2026-04-02

Washington Wizards are confirmed full-tank with Alex Sarr now validated OUT via injury landscape alongside Trae Young, Anthony Davis, D'Angelo Russell, Kyshawn George, and Cam Whitmore — six roster-relevant absences making them the clearest no-bet in the league. San Antonio Spurs' 10-game winning streak (L10: 10-0) is a notable market signal — books will be pricing them heavily, so fade opportunities against them warrant scrutiny of the opponent's odds for value rather than backing the Spurs at compressed prices. Performance data remains deeply concerning at 33.3% win rate and -€617.86 P&L across all markets, with totals (0W/2L) and high-confidence bets (0W/2L) particularly troubling — strategic section changes are withheld pending more data, but selectivity discipline is the current priority.

## Performance Stats
ALL-TIME: 4W / 8L | Win rate: 33.3% | P&L: €-617.86 | Avg odds: 1.98 | Avg conf: 65.0/100
RECENT 12: 4W / 8L | 33.3% WR | P&L: €-617.86
By market:      ML 5bets 2W/3L 40.0% €-141.53  |  SPREAD 5bets 2W/3L 40.0% €-292.06  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 2bets 0W/2L 0.0% €-320.54  |  Medium 9bets 4W/5L 44.4% €-197.32  |  Speculative 1bets 0W/1L 0.0% €-100.00
By odds range:  1.70-1.89 2bets 1W/1L 50.0% €-66.69  |  1.90-2.09 9bets 3W/6L 33.3% €-451.17  |  2.10-2.50 1bets 0W/1L 0.0% €-100.00



## Scout patches applied
- [franchise_player_rules] Verified feed has changed: Alex Sarr confirmed OUT via injury landscape, Trae Young confirmed OUT; prior session note players (Landry Shamet, Spencer Jones, Zeke Nnaji, Sam Merrill) are no longer in the verified feed and must be removed from OUT list.
- [tanking_teams] Standings data updated reflecting current records (SAS 58-18 W10 streak, DEN W7 streak, HOU W4, PHX/MIA/ORL confirmed cold, GSW now below breakeven NetRtg); Alex Sarr confirmed OUT via injury landscape added to Washington tank confirmation.

## Commit patches applied
None

## Intelligence gaps identified
- **High-confidence picks (0W/2L, -€320.54) are dramatically underperforming relative to medium-confidence picks (4W/5L, -€197.32), suggesting the confidence calibration model is miscalibrated at the top tier.** — Elite/High confidence bets should win more than medium bets — the inverse pattern suggests overconfidence bias, potentially from stacking multiple positive signals without sufficient discount for market efficiency. → After reaching 20 settled bets (currently 12), conduct a full confidence_staking review; interim flag: require High tier picks to have NetRtg gap ≥ 6 AND injury feed = nba_official, not just ≥ 4.
- **Totals market is 0W/2L (-€184.27) with zero wins, yet the rules currently allow totals with confidence ≥ 65 when pace data is available.** — Two straight losses on totals may reflect that O/U lines in the current NBA market are extremely efficient and our pace/OffRtg signals are not providing sufficient edge. → Raise totals confidence floor to 70 (from 65) universally — not just when pace data is absent — and require BOTH pace AND a NetRtg-aligned OffRtg signal before drafting any total.
- **Portland Trail Blazers (39-38, L10: 7-3, W2 streak) appear in standings as a play-in contender but no advanced stats (NetRtg, OffRtg, DefRtg) are present in today's feed for them.** — Without NetRtg context, any Portland pick would lack the primary directional signal and could produce a miscalibrated confidence rating. → Infrastructure fix needed — ensure Portland Trail Blazers advanced stats are included in the daily feed; interim: treat Portland as NetRtg-unavailable and apply confidence -5 per existing priority_stats rule.
- **Sacramento Kings and Brooklyn Nets are listed as confirmed tanks in tanking_teams but their exact current records and advanced stats are absent from today's data feed.** — Without current NetRtg confirmation, the tank designation relies on stale approximations (~18-52, ~17-52) which may be outdated by several weeks. → Infrastructure fix — include all 30 teams' records and advanced stats in the daily standings feed, not just the top/bottom relevant teams; analyst is filling gaps from prior session memory.
