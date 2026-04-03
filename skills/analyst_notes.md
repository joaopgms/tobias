---
date: 2026-04-03
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (13 bets)
---

## Today's Analysis — 2026-04-03

The most significant development this session is Victor Wembanyama appearing in the verified OUT list for San Antonio — this is a franchise-level absence that directly contradicts the Spurs' 11-game winning streak narrative and could create major line mispricing if books haven't fully adjusted. San Antonio picks must be treated with extreme caution until NBA official PDF confirms status. Performance data shows totals (0W/2L, -€184.27) and high-confidence picks (0W/2L, -€320.54) are the worst-performing segments — the data reinforces the existing high confidence floor and totals confidence floor rules, though sample sizes (2 bets each) remain too small for strategic patches. Spread underperformance (2W/3L, -€292.06) at the -€292 level versus ML's near-breakeven (-€81) continues to suggest spreads carry higher variance risk, worth monitoring as volume grows.

## Performance Stats
ALL-TIME: 5W / 8L | Win rate: 38.5% | P&L: €-557.67 | Avg odds: 1.99 | Avg conf: 64.6/100
RECENT 13: 5W / 8L | 38.5% WR | P&L: €-557.67
By market:      ML 6bets 3W/3L 50.0% €-81.34  |  SPREAD 5bets 2W/3L 40.0% €-292.06  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 2bets 0W/2L 0.0% €-320.54  |  Medium 10bets 5W/5L 50.0% €-137.13  |  Speculative 1bets 0W/1L 0.0% €-100.00
By odds range:  1.70-1.89 2bets 1W/1L 50.0% €-66.69  |  1.90-2.09 10bets 4W/6L 40.0% €-390.98  |  2.10-2.50 1bets 0W/1L 0.0% €-100.00



## Scout patches applied
- [franchise_player_rules] Verified feed adds Alex Caruso (OKC), Emanuel Miller (SAS), Victor Wembanyama (SAS) and Jock Landale (ATL) as OUT — Wembanyama is a franchise player absence requiring mandatory alert; injury landscape confirms Kyshawn George, Anthony Davis, Alex Sarr for Washington.
- [tanking_teams] Updated all standings to current session data, added Victor Wembanyama OUT alert for SAS (franchise player newly confirmed in verified feed), updated Warriors to streak L3 and NetRtg -0.3, updated all streak/record data from current standings input.

## Commit patches applied
None

## Intelligence gaps identified
- **Victor Wembanyama's absence from San Antonio creates a scenario where the Spurs' 11-game streak odds are priced on full-strength roster — no rule currently flags franchise player absences on historically hot-streak teams as a special verification priority** — Books may still be pricing SAS as full-strength, creating false favourite situations; betting against SAS at wrong odds or betting on them without Wembanyama would both be errors → The franchise_player_rules patch already adds the mandatory alert; Scout should also check SAS line movement specifically when Wembanyama status is unconfirmed — any SAS line that hasn't moved despite his roster-only OUT flag is a potential anomaly worth flagging
- **Portland Trail Blazers (40-38, L10: 8-2, streak: W3) appear in standings but have no NetRtg/OffRtg/DefRtg entry in the advanced stats feed** — Without NetRtg, Scout cannot apply the primary directional signal (step 1 of priority_stats) for any Portland game, forcing a -5 confidence penalty and degrading pick quality on a play-in bubble team with genuine motivation edge → Flag Portland as a 'NetRtg-unavailable team' in data_quality_rules or priority_stats so Scout explicitly applies the missing-L15 penalty and avoids spread bets involving Portland until advanced stats are available
- **Totals market has 0W/2L record (-€184.27, 0% WR) but sample size of only 2 bets is insufficient to determine whether the confidence floor (65, raised to 70 when Pace unavailable) needs further tightening** — At 0% win rate the totals market is the single worst-performing segment, but 2 bets could easily be explained by variance — premature tightening risks eliminating a valid market entirely → Continue tracking totals separately; if totals reach 5+ bets with WR < 35% revisit raising confidence floor to 70 permanently or adding a stronger pace/DefRtg gate
- **High-confidence picks (85–100 tier) are 0W/2L (-€320.54) — the highest-staked picks are performing worst, suggesting the confidence calibration for elite picks may be inflated** — If picks rated 85+ are losing at 0%, the staking model amplifies losses precisely when the model is most wrong — a calibration issue that compounds financial damage → When high-confidence pick sample reaches 5+, audit which specific signals (NetRtg gap, streak length, injury combination) produced those 2 losses and check if a systematic bias exists in confidence inflation
