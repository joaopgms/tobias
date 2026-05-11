---
date: 2026-05-11
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (38 bets)
---

## Today's Analysis — 2026-05-11

Major bracket update: NYK swept PHI 4-0 (series complete, PHI eliminated) and LAL won Game 7 vs HOU (HOU eliminated — Durant OUT was decisive). Three active Round 2 series remain: OKC leads 3-0 (potential sweep Game 4), SAS leads MIN 2-1 (Edwards status is the series variable), and DET leads CLE 2-1 (CLE must-win pressure building). Performance data shows a clear ML underperformance pattern (43.5% WR, -€725) versus spread outperformance (53.8% WR, +€274) — Scout should continue to prioritise spread evaluation over ML-default picks, particularly in series where NetRtg gaps are established and home court is clear. LAL entering Round 2 after a Game 7 carries a meaningful short-rest flag that should suppress spread confidence in their Round 2 Game 1.

## Performance Stats
ALL-TIME: 28W / 28L | Win rate: 50.0% | P&L: €-296.31 | Avg odds: 1.94 | Avg conf: 65.7/100
RECENT 20: 10W / 10L | 50.0% WR | P&L: €-351.01
By market:      ML 23bets 10W/13L 43.5% €-725.09  |  SPREAD 26bets 14W/12L 53.8% €+274.33  |  TOTAL 7bets 4W/3L 57.1% €+154.45
By confidence:  High 18bets 7W/11L 38.9% €-894.80  |  Medium 36bets 21W/15L 58.3% €+739.80  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 19bets 9W/10L 47.4% €-818.05  |  1.90-2.09 33bets 18W/15L 54.5% €+463.75  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Updating franchise_player_rules to reflect ESPN live feed: NYK leads PHI 4-0 (COMPLETE), LAL leads HOU 4-2 (COMPLETE — HOU eliminated), DET leads East Semifinals now showing Game 5 per ESPN; removing stale Game 7 LAL/HOU context.

## Commit patches applied
None

## Playoff context patches applied
- [phase] ESPN live feed confirms NYK-PHI is COMPLETE at 4-0 (not 3-0), and LAL-HOU Round 1 is COMPLETE (LAL leads 4-2 marked COMPLETE); phase section must reflect accurate current state.
- [series_context] ESPN live feed confirms NYK-PHI COMPLETE at 4-0 and LAL-HOU COMPLETE (LAL wins); series_context must remove active Game 7 narrative and update NYK-PHI to swept/eliminated status.
- [elimination_flags] ESPN confirms PHI eliminated (NYK swept 4-0) and HOU eliminated (LAL won Game 7 / series 4-2 COMPLETE); elimination_flags must reflect both new eliminations.
- [h2h_playoff] ESPN confirms NYK swept PHI 4-0 (series complete) and LAL won Game 7 over HOU (series complete at 4-2); h2h_playoff must close out those series and update lesson set.
- [playoff_rest] ESPN confirms series updates require playoff_rest to reflect LAL just finished Game 7 (short rest entering Round 2) and NYK now in ECF with potential extended rest; inter-game context updated to Game 4/5 stage.
- [playoff_motivation] ESPN confirms PHI eliminated (NYK advances to ECF), HOU eliminated (LAL advances); motivation hierarchy must reflect these state changes and LAL short-rest flag entering Round 2.
- [l15_caveat] ESPN confirms NYK swept PHI (4-0 COMPLETE) and LAL eliminated HOU (Game 7 win); l15_caveat lessons and effective NetRtg table must reflect current bracket reality and updated series results.
- [no_tanking] ESPN live feed confirms PHI and HOU eliminated; no_tanking section must list all confirmed-eliminated teams including the two new additions.

## Intelligence gaps identified
- **OKC's Round 2 opponent identity is unverified in the current data — ESPN feed shows 'Tied 2-2 (Game 5 next) [West Semifinals]' which conflicts with the OKC leads 3-0 entry and suggests a possible bracket mismatch in the live feed.** — Without confirmed opponent identity, any OKC pick cannot be properly evaluated for franchise player absences, NetRtg gaps, or home court assignment — a mismatch in the feed could cause Scout to draft a pick with wrong matchup assumptions. → Fetch ESPN bracket page directly before any OKC Round 2 pick — confirm opponent name, current series score, and next game venue. Do not draft OKC picks until opponent is confirmed by name.
- **ML market is underperforming significantly (43.5% WR, -€725 across 23 bets) while spread bets are profitable (53.8% WR, +€274 across 26 bets) — the current market_rules confidence floor for ML (50) may be too low relative to spread floor (60), allowing too many marginal ML picks through.** — If ML picks at confidence 50-59 are driving the ML losses, raising the ML floor would filter out the worst-performing tier and redirect picks toward the more profitable spread market. → Analyse ML bets by confidence tier — if ML losses cluster at confidence 50-64 (medium-low tier), raise ML confidence floor from 50 to 60 to match spread floor. Confidence 0.72 that this is directionally correct based on market performance split.
- **High-confidence bets (85-100 tier) are severely underperforming: 7W/11L (38.9% WR, -€894.80) versus medium confidence bets at 58.3% WR (+€739.80) — the elite/high staking tiers may be over-sizing on picks that don't warrant it.** — This is the most important performance signal in the dataset: high-confidence picks are losing at a rate that destroys bankroll, while medium picks are profitable. If high-confidence sizing (20-30% bankroll) is applied to picks that prove wrong at 61% rate, the staking structure amplifies losses. → At 28 total bets, this pattern is emerging but not yet at the 20-bet-per-tier threshold for strategic patching. Flag for review at 35+ total bets. If pattern persists, reduce High tier staking from 20-25% to 15-20% and cap Elite at 20%.
