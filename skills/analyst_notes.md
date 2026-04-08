---
date: 2026-04-08
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (4 bets)
---

## Today's Analysis — 2026-04-08

Standings have tightened significantly at the top — OKC (63-16) and Spurs (60-19) are postseason-clinched with star rest risk elevated; Denver's 9-game win streak (51-28) is the most significant momentum story and warrants respect for spread picks. The high-confidence tier (7 bets, 28.6% win rate, -€190.54) is the clearest performance problem: backing heavily on picks with conf 70+ is losing badly, suggesting over-confidence in apparently strong signals; the medium tier (53.8%) is outperforming. Spread market (3W/5L, -€319.06) continues to underperform ML significantly — the -€319 figure on 8 bets represents an average loss of ~€40/bet on spreads vs ~€5/bet on ML, reinforcing caution on spread picks.

## Performance Stats
ALL-TIME: 9W / 13L | Win rate: 40.9% | P&L: €-399.24 | Avg odds: 1.99 | Avg conf: 65.5/100
RECENT 20: 9W / 11L | 45.0% WR | P&L: €-74.24
By market:      ML 11bets 5W/6L 45.5% €-56.91  |  SPREAD 8bets 3W/5L 37.5% €-319.06  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 7bets 2W/5L 28.6% €-190.54  |  Medium 13bets 7W/6L 53.8% €-67.39  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 5bets 3W/2L 60.0% €+115.05  |  1.90-2.09 14bets 6W/8L 42.9% €-284.98  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Verified feed this session removes Jalen Williams, Anthony Edwards, Immanuel Quickley, and Emanuel Miller from prior session's absence list; adds Emanuel Miller (SAS), Thomas Bryant (CLE), Tristan Vukcevic (WAS) as newly verified; updates Washington confirmed injury landscape absences.
- [tanking_teams] Updated to reflect current standings (OKC 63-16, SAS 60-19, DET 57-22, BOS 54-25, LAL 50-29 streak L3, HOU 50-29 streak W7, MIN 47-32 streak W1, etc.), removed Jalen Williams/Anthony Edwards from confirmed-absent lists per verified feed, added Emanuel Miller/Thomas Bryant/Tristan Vukcevic per new verified feed, and refreshed form/streak data throughout.

## Commit patches applied
None

## Intelligence gaps identified
- **High-confidence tier (conf 70-84) is producing 28.6% win rate across 7 bets — worse than medium confidence — suggesting the confidence calibration model is systematically overconfident on certain signal combinations.** — If high-confidence picks are winning at 28.6% vs 53.8% for medium, the confidence scoring is inversely correlated with outcomes at the top tier, which means staking more on 'high' picks is destroying value faster than medium picks. → After 10+ more settled high-confidence bets, consider whether the high-confidence threshold should require BOTH NetRtg gap AND injury confirmation (not just one), essentially requiring two independent positive signals before assigning conf ≥ 70.
- **Spread market is -€319.06 on 8 bets (3W/5L, 37.5%) — far underperforming ML (45.5%) — but the current rules don't distinguish which spread signal types are failing (B2B, NetRtg gap, tanking opponent, or DefRtg gap).** — Without knowing which spread signal drove the 5 losses, the market_rules spread section cannot be selectively tightened — we risk either over-restricting valid signals or leaving the bad ones untouched. → Tag each settled spread bet with its primary signal type (B2B, NetRtg gap, tank-opponent, DefRtg) in the bet log so Analyst can identify which sub-signal has the worst record and tighten that specific rule.
- **Odds range 2.10-2.50 is 0W/3L (0%, -€229.31) — every bet placed at these odds has lost — but the current odds_targets ceiling of 2.50 does not penalise or restrict picks in this range.** — Three losses from three bets at 2.10-2.50 suggests either the picks in this range are being selected with insufficient edge, or the market is efficient at these odds and the system's confidence estimates are uncalibrated at higher odds. → Consider temporarily lowering the ML ceiling to 2.10 until the 2.10-2.50 range accumulates a sample of 8+ bets, OR add a rule requiring EV ≥ 0.10 (instead of 0.05) for picks with odds ≥ 2.10 as a higher evidence bar.
- **Several top-seeded teams (OKC 63-16, Spurs 60-19, Pistons 57-22) are in postseason-clinch territory where star rest is not tracked or flagged systematically beyond manual notes.** — A clinched team resting stars for the playoffs could see their roster fundamentally change with no injury feed signal — Scout could draft a pick on OKC or Spurs based on season NetRtg with the actual starting lineup being rested reserves. → Add a 'postseason clinch rest risk' flag to priority_stats: when a team's clinch number is ≤ 0 AND their seed is locked, apply confidence -10 automatically and require NBA official lineup confirmation before any pick on that team.
