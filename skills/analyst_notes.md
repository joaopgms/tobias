---
date: 2026-04-16
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (11 bets)
---

## Today's Analysis — 2026-04-16

Primary data integrity concern this session: Trae Young appears in both the Atlanta Hawks and Washington Wizards verified absence feeds — this is a data pipeline conflict that must be resolved via NBA official PDF before any ATL pick is considered. The play-in field has a clear statistical outlier in Charlotte Hornets (NetRtg +5.0), who are notably stronger on advanced metrics than their #8 seeding suggests — if priced as underdog against Philadelphia (#7, NetRtg -0.2), the regression-fade opportunity is significant. Performance trends continue to favour spread picks (53.8% WR, +€258) over ML (46.2%, -€100) and totals (33.3%, -€23), with the odds band 2.10-2.50 producing 0W/3L — Scout should remain disciplined in avoiding that range.

## Performance Stats
ALL-TIME: 14W / 15L | Win rate: 48.3% | P&L: €+134.57 | Avg odds: 1.97 | Avg conf: 64.8/100
RECENT 20: 12W / 8L | 60.0% WR | P&L: €+764.56
By market:      ML 13bets 6W/7L 46.2% €-100.28  |  SPREAD 13bets 7W/6L 53.8% €+258.12  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 8bets 3W/5L 37.5% €+32.90  |  Medium 19bets 11W/8L 57.9% €+242.98  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 7bets 4W/3L 57.1% €+88.68  |  1.90-2.09 19bets 10W/9L 52.6% €+275.20  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Full sync with verified franchise player absence feed; added Trae Young data conflict flag (appears in both ATL and WAS feeds — data integrity issue requiring PDF verification); adjusted play-in rest risk note since win-or-go-home teams have no star rest incentive.
- [tanking_teams] Minor factual update to reflect current session date and added Trae Young data conflict flag in ATL entry since he appears in the WAS verified absence feed — data integrity risk for any ATL picks.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] Added Trae Young data conflict flag (appears in both ATL and WAS verified absence feeds) as a data integrity issue that must be resolved via NBA official PDF before any ATL pick; updated session date.
- [elimination_flags] Added Trae Young data conflict flag as an active decision risk for any ATL-involved play-in scenario; updated session date.
- [h2h_playoff] Updated session date; no new H2H data available as official play-in matchups not yet confirmed — placeholder structure maintained.

## Intelligence gaps identified
- **Trae Young appears in both Atlanta Hawks and Washington Wizards verified absence feeds — a clear data pipeline conflict with no resolution available from current inputs.** — Any Atlanta Hawks play-in pick that implicitly assumes Trae Young is available (or absent) could be built on wrong data; this corrupts both ML confidence and the franchise_player_rules adjustment for ATL. → Add a cross-team duplicate player check to the injury feed ingestion pipeline; flag any player appearing under two teams simultaneously and require NBA official PDF resolution before allowing picks on either team.
- **West play-in 10-seed is listed as TBD — no team has been confirmed, and the bracket cannot be fully constructed without it.** — Scout cannot evaluate West 9v10 matchup odds or apply H2H/form context without knowing both participants, creating a dead zone in the West play-in betting slate. → Verify final West standings tiebreaker resolution via NBA.com official bracket page at each session until 10-seed is confirmed; populate playoff_context h2h_playoff and elimination_flags immediately upon confirmation.
- **Odds band 2.10-2.50 has produced 0W/3L (-€229) but selectivity and odds_targets sections do not flag this range as elevated-risk.** — Three losses in this exact odds band may indicate Scout is systematically overestimating confidence on longer-priced picks, or that books are well-calibrated in this range and Tobias has no edge there. → Consider adding a soft flag in selectivity: 'Odds 2.10-2.50 — requires EV ≥ 0.12 (elevated from standard 0.05) given historical 0W/3L on this range; treat with extra caution until 5+ more bets provide a larger sample.'
- **High-confidence picks (85-100 tier) are performing at only 37.5% WR (3W/5L, +€32) while medium-confidence (55-69) is 57.9% WR (11W/8L, +€242) — the staking structure rewards high-confidence picks with larger stakes despite worse outcomes.** — If this pattern holds, the staking tiers are misaligned with actual win-rate distribution — over-staking on high-confidence picks and under-staking on medium picks destroys expected value compared to a flatter structure. → After 10+ more high-confidence bets are settled, evaluate whether high-confidence tier staking (20-25%) should be reduced to match medium-tier levels (15-20%) given current inverted performance.
