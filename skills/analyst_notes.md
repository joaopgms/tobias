---
date: 2026-05-23
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (41 bets)
---

## Today's Analysis — 2026-05-23

WCF has shifted decisively: OKC leads SAS 2-1 per ESPN live feed, making OKC the clear series favourite with both in-series lead and superior NetRtg (+11.1 vs +8.3). Game 4 is likely at SAS home (standard bracket Games 3-4 at higher seed's opponent for road games) — Wembanyama's health and SAS home court desperation are the key swing factors to monitor before drafting. ECF Game 3 result must be verified from ESPN before any Game 4 drafting; if NYK leads 3-0, CLE faces near-elimination at home and the historical ~3% comeback rate means NYK should be backed with confidence even on the road, while a 2-1 NYK lead would keep the series more open with CLE home motivation still meaningful. Performance data continues to show ML at 1.70-1.89 as the weakest market segment (9W/10L, -€818) — Scout should default to spread evaluation first in Conference Finals where advanced stats are fully available for both teams.

## Performance Stats
ALL-TIME: 30W / 29L | Win rate: 50.8% | P&L: €-19.85 | Avg odds: 1.94 | Avg conf: 65.6/100
RECENT 20: 11W / 9L | 55.0% WR | P&L: €+245.95
By market:      ML 24bets 11W/13L 45.8% €-524.71  |  SPREAD 28bets 15W/13L 53.6% €+350.41  |  TOTAL 7bets 4W/3L 57.1% €+154.45
By confidence:  High 18bets 7W/11L 38.9% €-894.80  |  Medium 39bets 23W/16L 59.0% €+1016.26  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 20bets 10W/10L 50.0% €-617.67  |  1.90-2.09 35bets 19W/16L 54.3% €+539.83  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Updating WCF series state to OKC leads 2-1 per ESPN live feed and ECF to reflect Game 3 has passed (NYK led 2-0 entering Game 3); all other verified absences unchanged from injury feed.

## Commit patches applied
None

## Playoff context patches applied
- [phase] Updating WCF to OKC leads 2-1 per ESPN live feed and clarifying ECF Game 3 status requires ESPN verification before Game 4 drafting.
- [series_context] Updating WCF to OKC leads 2-1 per ESPN live feed and adding conditional ECF Game 3 outcome framing since Game 3 result requires ESPN verification before any ECF Game 4 drafting.
- [elimination_flags] Updating WCF elimination flags to reflect OKC leads 2-1 (SAS under must-win pressure) and adding conditional ECF flags based on Game 3 outcome pending ESPN verification.
- [playoff_rest] Updating WCF rest context to reflect OKC leads 2-1 with Game 4 likely at SAS home, and flagging ECF rest context is contingent on Game 3 result verification from ESPN.
- [playoff_motivation] Updating WCF motivation to reflect OKC leads 2-1 (primary in-series signal now established) and restructuring ECF framing to be conditional on Game 3 result pending ESPN verification.
- [h2h_playoff] Updating WCF h2h_playoff section to reflect OKC leads 2-1 as confirmed by ESPN live feed and restructuring ECF h2h framing to be conditional on Game 3 outcome requiring ESPN verification.
- [l15_caveat] Updating WCF l15_caveat to reflect OKC leads 2-1 as confirmed by ESPN live feed, adding SAS-trailing-1-2 home game framing, and making ECF guidance conditional on Game 3 result verification.
- [no_tanking] Updating no_tanking section to reflect OKC leads WCF 2-1 (SAS near-elimination pressure added) and making ECF near-elimination flags conditional on Game 3 result pending ESPN verification.

## Intelligence gaps identified
- **WCF Game 3 specific result details (score, Wembanyama performance/minutes, SGA performance) are not in the current data feed — only the series score update is confirmed.** — Wembanyama's Game 3 performance would materially affect Game 4 confidence — if he was limited or injured in Game 3, SAS Game 4 backing becomes riskier even at home. → Fetch ESPN box score for WCF Game 3 before Scout runs; add Wembanyama minutes/performance gate to WCF game-day verification protocol.
- **LAL Round 2 opponent identity and current series score are not confirmed in the current data feed despite LAL being listed as active.** — Scout cannot draft any LAL Round 2 pick without knowing the opponent, series score, and whether Doncic-free LAL has a viable edge in context. → Add mandatory ESPN bracket lookup for LAL Round 2 opponent and series score as a hard gate in franchise_player_rules LAL note — already partially present but the opponent is still unidentified.
- **No L15 NetRtg data is available for WCF or ECF teams in the current advanced stats feed — only season NetRtg is provided.** — L15 NetRtg is the primary short-term directional signal per priority_stats; without it for Conference Finals teams, Scout is relying entirely on season NetRtg which may not reflect current form (e.g. CLE's form entering playoffs vs their season average). → Add a Conference Finals L15 flag to priority_stats: if L15 NetRtg is unavailable for either Conference Finals team, apply confidence -5 on any pick where L15 would be decisive, and escalate in-series data to full primary signal.
