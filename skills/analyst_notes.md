---
date: 2026-05-22
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (41 bets)
---

## Today's Analysis — 2026-05-22

ECF has shifted decisively — NYK leads 2-0 and CLE now faces near-elimination entering Game 3 at home; CLE's desperation at home (historically ~60-65% win rate when down 0-2 in a series) makes them a credible live underdog worth evaluating at appropriate odds, but NYK's dominant in-series lead remains the primary signal. WCF remains live at 1-1 but Game 3 result (SAS hosting) is critical context that must be verified from ESPN before any Game 4 pick is drafted — whoever leads 2-1 will carry a strong series advantage. The ML market continues to underperform (-€524.71, 45.8%) while spreads (+€350.41, 53.6%) and medium confidence picks (+€1,016.26, 59.0%) are the profit drivers; Scout should continue prioritising spread evaluation in Conference Finals and maintain the EV ≥ 0.08 filter for ML picks in the 1.70-1.89 odds range.

## Performance Stats
ALL-TIME: 30W / 29L | Win rate: 50.8% | P&L: €-19.85 | Avg odds: 1.94 | Avg conf: 65.6/100
RECENT 20: 11W / 9L | 55.0% WR | P&L: €+245.95
By market:      ML 24bets 11W/13L 45.8% €-524.71  |  SPREAD 28bets 15W/13L 53.6% €+350.41  |  TOTAL 7bets 4W/3L 57.1% €+154.45
By confidence:  High 18bets 7W/11L 38.9% €-894.80  |  Medium 39bets 23W/16L 59.0% €+1016.26  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 20bets 10W/10L 50.0% €-617.67  |  1.90-2.09 35bets 19W/16L 54.3% €+539.83  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Updating WCF series state to TIED 1-1 with Game 4 next (from Game 3), and ECF to NYK leads 2-0 with Game 3 at CLE next, based on live ESPN playoff feed.

## Commit patches applied
None

## Playoff context patches applied
- [phase] Updating ECF to NYK leads 2-0 (Game 3 next at CLE) and WCF to TIED 1-1 (Game 4 next) per ESPN live playoff feed.
- [series_context] Updating ECF to NYK leads 2-0 with Game 3 at CLE (elimination pressure on CLE), and flagging WCF Game 4 contingency on Game 3 result which must be verified from ESPN.
- [elimination_flags] CLE now trails ECF 0-2 and faces near-elimination pressure entering Game 3 at home; WCF Game 4 location depends on Game 3 outcome which must be verified.
- [playoff_rest] Updating ECF rest context to reflect NYK 2-0 lead and CLE maximum desperation at home in Game 3; flagging WCF Game 4 rest assessment contingent on Game 3 result.
- [playoff_motivation] Updating ECF to NYK 2-0 with CLE facing near-elimination at home Game 3, and flagging WCF Game 4 as contingent on Game 3 verification from ESPN.
- [h2h_playoff] Updating ECF in-series data to NYK 2-0 with CLE facing near-elimination, and flagging WCF Game 4 as fully contingent on Game 3 result verification from ESPN.
- [l15_caveat] Updating ECF to NYK 2-0 dominant lead with CLE near-elimination context for Game 3, and establishing hard gate on WCF Game 4 requiring Game 3 result verification from ESPN.
- [no_tanking] Updating CLE near-elimination status (trails 0-2, must win Game 3) and WCF Game 4 contingency status requiring ESPN verification of Game 3 result.

## Intelligence gaps identified
- **ECF Game 3 odds for CLE at home (trailing 0-2) are unknown — historical 0-2 series desperation data suggests CLE ~60-65% to win Game 3 at home, but no rule currently encodes this pattern.** — If CLE opens at 1.70-1.85 as home underdog trailing 0-2, the desperation + home court edge may represent genuine value that Scout would currently underprice without a specific near-elimination home game rule. → Add a playoff_motivation sub-rule: 'Team trailing 0-2 in Conference Finals hosting Game 3 → apply +8 confidence bonus (desperation + home court compound effect, historical ~62% win rate). Only override if franchise player confirmed absent or opponent NetRtg gap > 5pts.'
- **WCF Game 4 pick cannot be drafted this session without Game 3 result — the system has no hard gate preventing Scout from drafting a WCF pick based on stale 1-1 series data.** — If Scout drafts a WCF Game 4 pick using the pre-Game 3 tied-series framing but Game 3 has already been played, the pick thesis would be built on incorrect series state — a systematic error. → Add a data_quality_rules entry: 'When drafting any playoff pick for Game N+1, verify the Game N result from ESPN as a mandatory pre-draft gate. If Game N result is unavailable, do NOT draft Game N+1 pick.' This is already partially in playoff_context notes but should be a hard rule in data_quality_rules.
- **No tracking of NYK road performance metrics in ECF — NYK has played both ECF games at home (Games 1 and 2) and Game 3 at CLE is their first road game; Scout lacks a framework for evaluating a team's first road game in a series.** — First road game in a playoff series carries a specific psychological and tactical adjustment cost — teams that dominated at home sometimes struggle in their first road environment. Without this signal, Scout may over-weight NYK's in-series lead for a road game. → Add to h2h_playoff or selectivity: 'First road game in a series for the leading team → apply confidence -5 (road environment adjustment, especially if all prior series wins were at home). Offset if NetRtg gap > 5pts or opponent franchise player absent.'
