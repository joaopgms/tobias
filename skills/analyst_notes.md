---
date: 2026-06-07
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (47 bets)
---

## Today's Analysis — 2026-06-07

NBA Finals stands at NYK 2-0 SAS with Game 3 at San Antonio next — the structural calculus shifts materially as SAS activates home court (+3-4pts) stacked with their +1.8pt NetRtg edge, creating a genuine ~+5pt situational SAS advantage. The critical swing variables entering Game 3 are (1) Wembanyama's efficiency and fatigue profile from Games 1-2 and the 7-game WCF grind, and (2) whether Brunson/KAT are fully healthy for NYK on the road. No settled bets from today's session exist to trigger strategic section patches; franchise_player_rules confirmed clean against the verified feed with no new statuses. Intelligence gap to monitor: we lack game-specific in-series box score data (Wembanyama minutes, efficiency splits, NYK road performance metrics from this series) which would sharpen Game 3 confidence calibration — Scout must pull this from ESPN before drafting.

## Performance Stats
ALL-TIME: 32W / 33L | Win rate: 49.2% | P&L: €-477.38 | Avg odds: 1.94 | Avg conf: 65.4/100
RECENT 20: 11W / 9L | 55.0% WR | P&L: €+150.12
By market:      ML 25bets 12W/13L 48.0% €-289.43  |  SPREAD 30bets 16W/14L 53.3% €+370.20  |  TOTAL 10bets 4W/6L 40.0% €-558.15
By confidence:  High 20bets 8W/12L 40.0% €-955.52  |  Medium 42bets 24W/18L 57.1% €+839.05  |  Speculative 3bets 0W/3L 0.0% €-360.91
By odds range:  1.70-1.89 22bets 11W/11L 50.0% €-678.39  |  1.90-2.09 38bets 20W/18L 52.6% €+362.62  |  2.10-2.50 5bets 1W/4L 20.0% €-161.61



## Scout patches applied
- [franchise_player_rules] Mandatory session update to franchise_player_rules confirming all verified absences match the current ESPN + NBA injury feed cross-reference; no changes to player statuses from prior session.

## Commit patches applied
None

## Playoff context patches applied
- [phase] No change to series scores from prior session — NYK still leads 2-0 with Game 3 at SAS next; confirming phase section is current.
- [series_context] Series score unchanged at NYK 2-0 SAS with Game 3 at SAS next; confirming series_context is current and accurate.
- [elimination_flags] No new eliminations this session; confirming elimination flags are current with all previously confirmed eliminations intact.
- [playoff_rest] Rest context unchanged from prior session; confirming playoff_rest accurately reflects Game 3 at SAS with standard rest for both teams.
- [h2h_playoff] No change to series result since last session; confirming h2h_playoff is current and accurate for Game 3 at SAS context.
- [playoff_motivation] No series result changes since prior session; confirming playoff_motivation accurately reflects Game 3 at SAS context.
- [l15_caveat] No series result changes; confirming l15_caveat is current and accurately reflects Game 3 at SAS as the first SAS home game of the Finals.
- [no_tanking] No eliminations this session; confirming no_tanking section is current with all active and eliminated teams correctly flagged.

## Intelligence gaps identified
- **No in-series box score data available (Wembanyama minutes per game in Finals Games 1-2, NYK road performance splits this postseason) to calibrate fatigue and road-readiness confidence adjustments** — Wembanyama fatigue is explicitly flagged as the #1 SAS swing factor in multiple sections, but without actual minutes/efficiency data from Games 1-2 the confidence adjustment is qualitative rather than data-driven; similarly NYK's road performance in this postseason would sharpen the NYK-on-road odds floor rule → Scout should pull Wembanyama game log (minutes, OffRtg, DefRtg, +/-) for Finals Games 1-2 and WCF Game 7 from ESPN before drafting any Game 3 pick; flag if minutes exceed 38 per game as high-fatigue threshold
- **LAL Round 2 series score and opponent are unverified — only 'Round 2 active' noted in elimination_flags with no confirmed result or current status** — If LAL has been eliminated or advanced to Round 3, the franchise_player_rules and elimination_flags entries for LAL become stale, potentially causing Scout to evaluate a non-active team → Verify LAL Round 2 series status from ESPN live bracket each session and update elimination_flags accordingly; if LAL is eliminated, add to confirmed eliminated list and remove from active teams
- **Total bets performance (40.0% win rate, -€558.15) suggests the totals confidence floor and pace-signal requirements may not be tight enough to generate positive EV in playoff conditions** — Only 10 total bets but uniformly negative P&L; playoff totals are harder to price due to defensive intensity escalation game-to-game, and our pace/OffRtg signals are calibrated for regular season patterns → Consider raising the totals confidence floor to 70 during playoffs (from 65) when Pace data is available, and requiring BOTH Pace > 100 AND OffRtg > 116 (tighter than current 114) for Over leans in playoff context
