---
date: 2026-04-20
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (18 bets)
---

## Today's Analysis — 2026-04-20

Play-in tournament is imminent but official matchup schedule remains unconfirmed — Scout must verify before drafting any picks. The Charlotte Hornets (NetRtg +5.0, best of all play-in teams) represent the most statistically compelling play-in angle if priced as an underdog against Philadelphia (NetRtg -0.2), which has the weakest advanced stats of any 7-seed. Performance data shows a strong ML underperformance (-€275 on 15 bets, 46.7%) versus spread outperformance (+€353 on 18 bets, 55.6%) — Scout should continue prioritising spread markets in play-in games where NetRtg gaps and home court advantages are most measurable. High-confidence bets (conf 70-84 mapped to High tier) have dramatically underperformed (4W/8L, -€739) versus Medium confidence (14W/8L, +€935), suggesting over-confidence inflation at the High tier warrants monitoring after 20+ more bets.

## Performance Stats
ALL-TIME: 18W / 18L | Win rate: 50.0% | P&L: €+54.70 | Avg odds: 1.95 | Avg conf: 65.9/100
RECENT 20: 12W / 8L | 60.0% WR | P&L: €+682.94
By market:      ML 15bets 7W/8L 46.7% €-275.39  |  SPREAD 18bets 10W/8L 55.6% €+353.36  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 12bets 4W/8L 33.3% €-739.59  |  Medium 22bets 14W/8L 63.6% €+935.60  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 10bets 5W/5L 50.0% €-469.94  |  1.90-2.09 23bets 13W/10L 56.5% €+753.95  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Current session verified absence feed confirms Immanuel Quickley (TOR) is now in the roster-only OUT list, correcting prior session's re-verify note; all other statuses carry forward from verified feed with no new changes beyond this correction.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] Session date advanced to 2026-04-24 and Immanuel Quickley (TOR) now confirmed in current verified absence feed as roster-only OUT, requiring series_context roster update log to reflect this change.
- [elimination_flags] Session date updated to 2026-04-24; content unchanged as no new eliminations or bracket results have occurred since last session.
- [h2h_playoff] Session date updated to 2026-04-24; no new H2H records available as play-in matchups remain unconfirmed and no games have been played yet.

## Intelligence gaps identified
- **High-confidence picks (12 bets, 4W/8L, 33.3%, -€739) are dramatically underperforming Medium-confidence picks (22 bets, 14W/8L, 63.6%, +€935), suggesting confidence calibration at the 70-84 tier is systematically too high.** — Bets staked at the High tier (20-25% bankroll) are losing at a rate that erases gains from other tiers; if High-conf picks actually have ~50% true win rate, the EV calculation is inflated and the staking tier amplifies losses. → After 5 more High-confidence settled bets, review whether the High tier (70-84) should require additional confirmation criteria (e.g. NetRtg gap > 5 AND spread signal AND no roster uncertainty) before allowing full 20-25% stake — consider splitting into 70-76 'Low-High' at 15% and 77-84 'True High' at 20-25%.
- **Odds range 2.10-2.50 has produced 0W/3L (-€229) — the entire upper range of the ML target is loss-generating with zero wins.** — If bets at odds 2.10-2.50 have a 0% win rate across 3 bets, the EV floor of 0.05 may not be sufficient to justify picks in this range, particularly in play-in/playoff settings where lines are sharper and books are more efficient. → Monitor for 5 more settled bets in the 2.10-2.50 range; if losses continue, consider raising ML ceiling to 2.10 (excluding the upper range) or requiring confidence ≥ 70 minimum for any pick at odds ≥ 2.10.
- **Official play-in matchup schedule and rest day data for each play-in team are not yet confirmed in the context, leaving Scout unable to apply b2b_rules or home court advantage reliably.** — Home court in play-in is worth +3 points per playoff_rest rules, and 1 rest day triggers confidence -8 on spread picks — without confirmed matchups and schedule, these adjustments cannot be applied, increasing the risk of a structurally incorrect pick. → Require Scout to explicitly verify and log the official play-in schedule (matchup pairs, dates, venues, rest days since last game) via NBA official source before drafting any play-in pick — this is an infrastructure/data-fetch requirement, not a rule gap.
