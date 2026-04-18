---
date: 2026-04-18
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (13 bets)
---

## Today's Analysis — 2026-04-18

Major roster status shift this session: numerous players previously flagged as roster-only OUT (including Sengun, Murray, Mitchell, Allen, Mobley, Harden, Brunson, Towns, Randle, Gobert, Conley) no longer appear in the verified absence feed — this does NOT confirm them available, but mandates re-verification against NBA official PDF before any pick involving those teams. Performance data continues to show the High confidence tier underperforming badly (33.3% WR, -€341.66) while Medium confidence is carrying the system (60.0% WR, +€442.43), reinforcing the case that top-of-range confidence scores may be systematically inflated — worth monitoring closely as play-in picks tend to invite higher confidence calls. Charlotte Hornets (NetRtg +5.0, W1, best stats in East play-in field) and Miami Heat (NetRtg +2.2, W2) are the most statistically credible play-in sides; Golden State (NetRtg -0.4, L3, 37-45) remains the clearest fade target if play-in games offer appropriate odds.

## Performance Stats
ALL-TIME: 15W / 16L | Win rate: 48.4% | P&L: €-40.54 | Avg odds: 1.96 | Avg conf: 65.3/100
RECENT 20: 11W / 9L | 55.0% WR | P&L: €+481.78
By market:      ML 15bets 7W/8L 46.7% €-275.39  |  SPREAD 13bets 7W/6L 53.8% €+258.12  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 9bets 3W/6L 33.3% €-341.66  |  Medium 20bets 12W/8L 60.0% €+442.43  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 9bets 5W/4L 55.6% €-86.43  |  1.90-2.09 19bets 10W/9L 52.6% €+275.20  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Verified absence feed has changed significantly since last session — several players previously flagged roster-only OUT (Sengun, Murray, Mitchell, Allen, Mobley, Harden, Brunson, Towns, Randle, Gobert, Conley, Reaves, Hayes) no longer appear in the current verified feed and must be treated as status-changed with re-verification required.
- [tanking_teams] Golden State Warriors (37-45, L3, NetRtg -0.4) are confirmed below the play-in cutoff and showing deteriorating form — moving to confirmed tank-watch; standings data also cleaned up to remove outdated record approximations.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] Roster absence feed has changed materially this session with multiple previously-OUT players no longer appearing in the verified list — series context must reflect these updates so Scout can properly assess which teams can field competitive rosters.
- [elimination_flags] Roster status changes this session mean top-seed strength assumptions need recalibration — elimination pressure flags updated to reflect this and GSW fade candidate note strengthened given confirmed 37-45 record with L3 and negative NetRtg.
- [h2h_playoff] Roster status changes this session invalidate some H2H assumptions — caveat added to ensure Scout discounts H2H records compiled under materially different roster conditions.

## Intelligence gaps identified
- **High confidence tier (70-84) is producing a 33.3% win rate and -€341.66 P&L across 9 bets — significantly worse than Medium tier which wins at 60.0%.** — If High confidence picks are systematically losing, the confidence calibration methodology is inflated at the top end — bets are being over-sized and over-trusted, leading to disproportionate losses when wrong. → After reaching 15+ High confidence settled bets, formally review whether the confidence_staking High tier (20-25% stake) should be reduced to 15-20%, and whether the confidence floor for High should be raised to 75+ to filter out borderline calls.
- **Speculative tier (50-54) shows 0% win rate across 2 bets and -€141.31 — the floor may be too low to produce positive EV at this odds range.** — Two speculative losses at high odds (likely 2.10+ range) contributed -€141.31 — if the system cannot generate genuine edge at 50-54 confidence, these bets should be eliminated entirely. → After 5+ speculative bets settled, evaluate whether the Speculative tier should be abolished (floor raised to 55 for all markets) or restricted to ML-only at odds ≥ 1.90.
- **Odds range 2.10-2.50 shows 0W/3L and -€229.31 — the system is consistently failing at the upper end of the odds target range.** — Every bet placed at 2.10+ odds has lost, suggesting either the model is over-confident in underdogs or the odds target ceiling should be tightened. → Consider tightening ML odds ceiling from 2.50 to 2.20 for non-speculative picks, or requiring NetRtg L15 gap confirmation before any pick above 2.10.
- **No confirmed play-in matchup schedule or official bracket has been provided — Scout cannot draft picks without knowing which teams are playing.** — All play-in pick analysis is blocked until official matchups are confirmed; Scout risks drafting picks for wrong matchups or non-existent games. → Infrastructure fix required: inject confirmed play-in schedule (7v8 and 9v10 matchups for both conferences, tip-off times, home court) into the daily context before Scout runs.
- **Trae Young appears simultaneously in Atlanta Hawks and Washington Wizards verified absence feeds — a clear data integrity error that has persisted across multiple sessions.** — Any ATL pick evaluation is blocked pending resolution; if the system incorrectly treats Trae Young as unavailable for ATL when he is actually available, it could miss legitimate ATL edges or incorrectly discount ATL strength. → Infrastructure fix required: cross-reference Trae Young's official ESPN roster page and NBA trade database to confirm his current team before each session; inject confirmed team affiliation into the verified player statuses feed.
