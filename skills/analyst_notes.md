---
date: 2026-04-14
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (9 bets)
---

## Today's Analysis — 2026-04-14

The verified absence feed has thinned significantly from prior sessions — multiple players previously listed as OUT for BOS (Jaylen Brown, Hugo Gonzalez, Sam Hauser, Payton Pritchard, Neemias Queta, Nikola Vucevic, Derrick White) and ATL (CJ McCollum) are no longer in today's confirmed list, suggesting either recovery, roster moves, or feed gaps; Scout MUST re-verify against NBA official PDF before any BOS pick. The Play-In Tournament is now the active phase with Charlotte Hornets holding the strongest NetRtg (+5.0) of any bubble team, making them a statistically credible underdog-fade target if priced wrong as 8-seed vs PHI. Denver's W12 streak (L10: 10-0, NetRtg +5.2) is the dominant hot-streak signal in the league, but Jamal Murray's roster-only OUT status and the need to verify Jokic's availability means DEN picks carry maximum uncertainty — do not draft without PDF confirmation.

## Performance Stats
ALL-TIME: 12W / 15L | Win rate: 44.4% | P&L: €-202.64 | Avg odds: 1.98 | Avg conf: 65.4/100
RECENT 20: 11W / 9L | 55.0% WR | P&L: €+407.86
By market:      ML 12bets 5W/7L 41.7% €-256.91  |  SPREAD 12bets 6W/6L 50.0% €+77.54  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 8bets 3W/5L 37.5% €+32.90  |  Medium 17bets 9W/8L 52.9% €-94.23  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 6bets 3W/3L 50.0% €-67.95  |  1.90-2.09 18bets 9W/9L 50.0% €+94.62  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Updated to reflect current verified absence feed: previous BOS entries (Jaylen Brown, Hugo Gonzalez, Sam Hauser, Payton Pritchard, Neemias Queta, Nikola Vucevic, Derrick White) and ATL entry (CJ McCollum) are NOT in today's verified list and must be removed per MANDATORY rule; Jayson Tatum remains verified OUT.
- [tanking_teams] Refreshed ATL injury note to remove CJ McCollum (not in current verified absence feed) and corrected BOS note to reflect only Tatum as verified OUT with Brown requiring re-verification.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] Updated to reflect current final regular-season standings and current team streaks; corrected conference seeding brackets; flagged depleted top-seed rosters as play-in context.
- [elimination_flags] Updated elimination flags with current NetRtg data, current streaks, and specific risk notes for each play-in participant to help Scout prioritise edges.
- [h2h_playoff] Updated with current seedings and specific notes on roster-uncertainty caveats for play-in H2H; placeholder entries maintained pending official matchup confirmation.
- [playoff_rest] Added play-in rest context note for 2026-04-19 session to flag that rest days are not yet confirmed and Scout must verify at draft time.

## Intelligence gaps identified
- **Play-in matchup schedules (dates, venues, rest days) are not yet confirmed in the context data, preventing accurate rest-day and home-court adjustments.** — Rest-day confidence adjustments (-8 for road team on 1-day rest) and home-court value (+3 pts) are material to spread and ML picks in single-elimination games — without confirmed schedules these adjustments cannot be applied accurately. → Fetch official NBA play-in schedule (dates, times, venues) and populate playoff_context.md series_context and playoff_rest sections with confirmed matchup data before Scout runs.
- **Multiple players previously listed as OUT for Boston Celtics (Jaylen Brown, Sam Hauser, Payton Pritchard, Nikola Vucevic, Derrick White) are absent from today's verified feed, but it is unclear whether this reflects recovery, rest, or feed incompleteness.** — If Jaylen Brown and others have returned to active status, the BOS franchise player rules and tanking_teams note overstated BOS roster depletion — potentially suppressing valid BOS picks in the play-in bracket. → Prioritise NBA official PDF cross-reference for BOS roster before each session; add explicit session note that BOS roster status is highly volatile and requires daily re-verification rather than carry-forward.
- **Odds at 2.10–2.50 range have a 0W/3L record (0.0% win rate, €-229.31) — the worst performing odds band by a significant margin.** — This pattern suggests Scout is over-confident on longer-priced picks; the EV calculation may be producing false positives at the high end of the odds range where variance is highest and edges are hardest to identify. → Consider adding a selectivity rule capping picks at odds ≤ 2.10 unless NetRtg gap > 8pts or elimination-game desperation factor applies; requires 5+ more bets in this range to reach 0.70 confidence for a formal patch.
- **ML market is 5W/7L (41.7%, €-256.91) all-time while Spread is 6W/6L (50.0%, €+77.54) — ML is meaningfully underperforming Spread despite being the more commonly drafted market.** — If ML selection criteria are producing worse outcomes than spread, Scout may be defaulting to ML when spread offers better risk-adjusted edge — the rules encourage spread evaluation but ML may still be the default in practice. → Review whether ML picks are being taken on games where a spread pick would have been better (e.g. large NetRtg gaps that make covering more predictable than outright winning); current evidence leans toward tightening ML confidence floor to 55 but sample is 12 bets — monitor for 5 more before patching.
