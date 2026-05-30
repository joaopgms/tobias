---
date: 2026-05-30
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (44 bets)
---

## Today's Analysis — 2026-05-30

WCF Game 7 is the sole actionable game — OKC at home holds a compound edge via NetRtg +2.8pt, historical ~60-65% home win rate in Conference Finals Game 7s, and Jalen Williams OUT (now confirmed in verified feed) which reduces SAS's primary matchup threat and may shift the spread from -5 toward -6/-7. The primary risk variable remains Wembanyama's health: if he is limited or scratched, SAS's path to a road Game 7 win collapses entirely and OKC spread value increases further. NYK's rest advantage for Finals Game 1 is now locked in at approximately 7-10 days — this is the single strongest structural edge on the board heading into the Finals and should be flagged prominently for Scout when Games 1-2 odds are posted.

## Performance Stats
ALL-TIME: 32W / 30L | Win rate: 51.6% | P&L: €+238.12 | Avg odds: 1.94 | Avg conf: 65.4/100
RECENT 20: 12W / 8L | 60.0% WR | P&L: €+730.62
By market:      ML 25bets 12W/13L 48.0% €-289.43  |  SPREAD 29bets 16W/13L 55.2% €+592.70  |  TOTAL 8bets 4W/4L 50.0% €-65.15
By confidence:  High 19bets 8W/11L 42.1% €-659.52  |  Medium 40bets 24W/16L 60.0% €+1258.55  |  Speculative 3bets 0W/3L 0.0% €-360.91
By odds range:  1.70-1.89 21bets 11W/10L 52.4% €-382.39  |  1.90-2.09 36bets 20W/16L 55.6% €+782.12  |  2.10-2.50 5bets 1W/4L 20.0% €-161.61



## Scout patches applied
- [franchise_player_rules] Jalen Williams (G/OKC) is present in the current verified feed as OUT [roster-only] — restoring the entry that was incorrectly flagged for removal in the prior version.

## Commit patches applied
None

## Playoff context patches applied
- [phase] Jalen Williams OUT status is now confirmed in the current verified feed; correcting the prior ambiguity and noting NBA Finals is the next phase to prepare for.
- [series_context] Jalen Williams OUT confirmed in current verified feed — updating from ambiguous prior language to confirmed status, and noting Finals rest advantage is now the next critical analytical frame.
- [elimination_flags] Routine session update confirming elimination flags are current; Jalen Williams OUT status now confirmed in verified feed so noted explicitly.
- [playoff_motivation] Jalen Williams OUT now confirmed in current verified feed — updating all references from ambiguous prior language and noting depth implications for OKC Game 7 spread analysis.
- [h2h_playoff] Jalen Williams OUT confirmed in current verified feed — updating all prior ambiguous notes and clarifying implications for Game 7 spread analysis.
- [l15_caveat] Jalen Williams OUT confirmed in current verified feed — correcting prior ambiguity across all playoff context sections and updating spread range estimate accordingly.
- [playoff_rest] Routine session update noting Jalen Williams OUT confirmation and its fatigue/depth implications for OKC in Game 7 and potential Finals run.
- [no_tanking] Session refresh confirming elimination flags and adding Jalen Williams OUT confirmation to OKC Game 7 entry.

## Intelligence gaps identified
- **No rule exists to quantify the depth-reduction impact on spread when a team's starting-caliber guard (Jalen Williams) is confirmed OUT in a winner-take-all game with a thin roster.** — Williams OUT likely widens OKC's effective spread vs SAS by 1-2 points beyond the season NetRtg gap, but current rules have no mechanism to translate a depth-reduction absence (non-franchise player) into a spread adjustment — only franchise player absences trigger explicit confidence changes. → Add a sub-rule under franchise_player_rules (or market_rules spread section) for 'starter-level guard/forward OUT in playoff context': apply confidence +5 to the opponent's spread if the absent player averaged 15+ PPG and the team's NetRtg gap is already ≥ 2.0 in your favour.
- **LAL Round 2 series status and opponent identity are unverified — the current feed shows LAL as 'still active' but provides no series score, opponent, or game number.** — If LAL is facing elimination or has already been eliminated, any LAL pick would be catastrophically wrong; conversely if LAL leads the series, the Luka Doncic OUT impact assessment changes materially. → Fetch ESPN bracket data for LAL Round 2 series before each session and patch elimination_flags and series_context with opponent name, current score, and next game date.
- **No tracking of cumulative playoff minutes load for franchise players (SGA, Holmgren, Wembanyama) across a 7-game series to quantify fatigue-driven performance degradation risk in Finals Game 1.** — NYK's rest advantage for Finals Game 1 is the strongest structural edge on the board, but its magnitude depends on how taxed OKC or SAS franchise players are — a fatigued SGA in Games 1-2 of the Finals would meaningfully shift ML and spread value toward NYK. → Add a playoff_rest sub-rule: 'After a 7-game series, apply confidence -5 to the advancing team's spread picks for Finals Games 1-2, stacking with any existing rest asymmetry adjustment, when the opponent had 7+ days rest.'
