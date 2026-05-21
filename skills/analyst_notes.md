---
date: 2026-05-21
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (40 bets)
---

## Today's Analysis — 2026-05-21

The WCF is now a legitimately open series at 1-1 after OKC won Game 2 at home to answer SAS's stunning Game 1 road win — the key analytical shift is applying the TIED SERIES RULE where season NetRtg (+2.8pt OKC edge) and home court are co-primary signals for Game 3 at SAS. The ECF structure is clearer: NYK leads 1-0 but must now win a road Game 3 at CLE, where home court (+3-4pts) and must-win motivation for CLE partially offset NYK's in-series lead — expect CLE to open as modest home favourites and NYK road odds to be in the 1.90-2.10 range. Performance-wise, medium confidence (55-69) continues to outperform at 57.9% with +€815.88 while high confidence remains badly underwater at 38.9% (-€894.80); Scout should remain in the medium-confidence band and scrutinise any high-confidence ECF or WCF picks with extraordinary care, particularly on the ML market at 1.70-1.89 odds which has produced the worst losses.

## Performance Stats
ALL-TIME: 29W / 29L | Win rate: 50.0% | P&L: €-220.23 | Avg odds: 1.94 | Avg conf: 65.6/100
RECENT 20: 11W / 9L | 55.0% WR | P&L: €+263.07
By market:      ML 23bets 10W/13L 43.5% €-725.09  |  SPREAD 28bets 15W/13L 53.6% €+350.41  |  TOTAL 7bets 4W/3L 57.1% €+154.45
By confidence:  High 18bets 7W/11L 38.9% €-894.80  |  Medium 38bets 22W/16L 57.9% €+815.88  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 19bets 9W/10L 47.4% €-818.05  |  1.90-2.09 35bets 19W/16L 54.3% €+539.83  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Routine mandatory session update to franchise_player_rules reflecting current playoff phase (Conference Finals active, Game 3 next for both series) with verified player statuses from the ESPN/NBA injury feed cross-reference.

## Commit patches applied
None

## Playoff context patches applied
- [phase] ESPN live feed shows WCF is now Tied 1-1 (Game 3 next) and ECF NYK leads 1-0 (Game 3 next), requiring phase and series state to be updated from the previous Game 2 framing.
- [series_context] ESPN live feed shows WCF is now Tied 1-1 with Game 3 next, requiring full series context recalibration — OKC won Game 2 at home to split the series, and Game 3 framing shifts to SAS home court advantage.
- [elimination_flags] WCF is now Tied 1-1 per ESPN live feed, eliminating the SAS in-series lead framing and replacing it with an open competitive series context; CLE trails 0-1 with must-win urgency for Game 3.
- [playoff_rest] WCF tied 1-1 with Game 3 next at SAS home; rest context must reflect OKC now as road team at SAS and the shift from SAS in-series lead to tied-series framing with SAS home court as primary advantage.
- [playoff_motivation] WCF tied 1-1 fundamentally changes the motivation hierarchy — OKC partially cleared rust by winning Game 2, series signals are now split, and Game 3 at SAS home requires recalibrating both the OKC rust thesis and the SAS in-series lead framing.
- [h2h_playoff] WCF tied 1-1 requires fundamentally updating the h2h_playoff section to reflect a split series where season NetRtg and home court re-take primary status, and to update ECF Game 3 framing with CLE returning home with must-win urgency.
- [l15_caveat] WCF tied 1-1 requires the L15 caveat section to implement the new TIED SERIES RULE where season NetRtg and home court re-take primary status, and ECF Game 3 at CLE home requires updating home court framing for that series.
- [no_tanking] WCF series status updated from SAS leads 1-0 to TIED 1-1 per ESPN live feed; no_tanking section must reflect accurate current standings for all active teams.

## Intelligence gaps identified
- **WCF Game 3 exact location and date not confirmed — listed as 'likely at SAS' but requires ESPN schedule verification before any WCF Game 3 pick is drafted.** — If home court is misidentified (e.g. neutral site or scheduling anomaly), the entire Game 3 edge framework collapses — the SAS home court premium is the central signal for Game 3 betting. → Scout must pull ESPN schedule at 14:00 draft time and confirm WCF Game 3 location before drafting any WCF pick; add explicit instruction to verify game location as Step 0 for any Conference Finals pick.
- **LAL Round 2 opponent and current series score are unconfirmed — the verified injury feed shows no LAL Round 2 opponent data and the standings/series section does not list LAL's Round 2 matchup.** — LAL with Doncic OUT is a significant franchise-player-absence scenario; without knowing their opponent and series score, Scout cannot correctly evaluate motivation, rest, or in-series signals for any LAL Round 2 pick. → Fetch LAL Round 2 opponent and series score from ESPN bracket before next session; update series_context and elimination_flags with confirmed LAL Round 2 data.
- **No Wembanyama (SAS) minute-load or physical health data available beyond roster-only status — given he is the decisive WCF variable, game-by-game load tracking would materially improve WCF Game 3 confidence calibration.** — SAS's entire WCF edge thesis depends on Wembanyama being healthy and dominant; a high-minute Game 1 followed by an OKC defensive adjustment in Game 2 could signal fatigue entering Game 3 at home — this would shift the WCF Game 3 edge significantly. → Add a Wembanyama minutes-per-game tracker and points/efficiency split to playoff_context WCF section; flag if minutes > 38 in any single game as a health-watch trigger requiring confidence -5 on next SAS pick.
