---
date: 2026-05-24
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (41 bets)
---

## Today's Analysis — 2026-05-24

NYK leads ECF 3-0 with CLE facing near-elimination at home for Game 4 — the 0-3 historical comeback rate (~3%) makes NYK the dominant series favourite, but CLE's home court + maximum desperation creates real single-game value at 2.10+. OKC leads WCF 2-1 with Game 5 likely at OKC home, giving OKC a three-way compound advantage (in-series lead, superior NetRtg +11.1, home court) — SAS must win on the road to avoid a near-fatal 1-3 deficit, making Wembanyama's health the swing variable. Performance data continues to show Medium confidence (55-69) outperforming at 59.0% WR +€1016, while High confidence (70-84) remains a loss leader at 38.9% -€894 — Conference Finals picks should stay in the Medium tier unless multiple confirming signals converge. Ajay Mitchell (OKC, G) is newly confirmed OUT per verified feed and has been added to franchise_player_rules.

## Performance Stats
ALL-TIME: 30W / 29L | Win rate: 50.8% | P&L: €-19.85 | Avg odds: 1.94 | Avg conf: 65.6/100
RECENT 20: 11W / 9L | 55.0% WR | P&L: €+245.95
By market:      ML 24bets 11W/13L 45.8% €-524.71  |  SPREAD 28bets 15W/13L 53.6% €+350.41  |  TOTAL 7bets 4W/3L 57.1% €+154.45
By confidence:  High 18bets 7W/11L 38.9% €-894.80  |  Medium 39bets 23W/16L 59.0% €+1016.26  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 20bets 10W/10L 50.0% €-617.67  |  1.90-2.09 35bets 19W/16L 54.3% €+539.83  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] ESPN live feed confirms OKC leads WCF 2-1 with Game 5 next (series now at Game 5, not Game 4), NYK leads ECF 3-0 with CLE facing near-elimination; also adding Ajay Mitchell (OKC) now confirmed OUT per verified feed.

## Commit patches applied
None

## Playoff context patches applied
- [phase] ESPN live feed confirms NYK leads ECF 3-0 and OKC leads WCF 2-1 with Game 5 (not Game 4) now next for WCF; ECF framing must reflect confirmed 3-0 series state with near-elimination context for CLE.
- [series_context] ESPN live feed confirms NYK leads ECF 3-0 (Game 4 at CLE next) and OKC leads WCF 2-1 with Game 5 next; series framing must reflect confirmed 3-0 state for ECF and advance WCF from Game 4 to Game 5 context.
- [elimination_flags] ESPN live feed confirms NYK leads ECF 3-0 placing CLE in near-elimination at home for Game 4, and WCF advances to Game 5 (not Game 4) context with SAS facing must-win on road at OKC.
- [playoff_rest] Series has advanced — ECF is now Game 4 (NYK leads 3-0) and WCF is now Game 5 (OKC leads 2-1); rest context must reflect confirmed series scores and correct game number framing.
- [playoff_motivation] ECF confirmed at 3-0 NYK lead and WCF at Game 5 (not Game 4) context; motivation framing must be updated to reflect correct series scores, near-elimination status for CLE, and WCF Game 5 location shift to OKC home.
- [h2h_playoff] ECF confirmed 3-0 NYK lead and WCF shifts to Game 5 context at OKC home; H2H and in-series signals must reflect updated series scores and correct game location framing.
- [l15_caveat] ECF confirmed 3-0 NYK lead and WCF advances to Game 5 context (likely at OKC home); L15 caveat hierarchy must reflect updated in-series data and correct near-elimination framing for CLE.
- [no_tanking] ESPN live feed confirms NYK leads ECF 3-0 (CLE in near-elimination) and WCF Game 5 is next (likely at OKC home after SAS hosted Games 3-4); elimination flags and active team status must reflect confirmed series scores.

## Intelligence gaps identified
- **WCF Game 5 location (OKC vs SAS) is inferred from standard bracket but not explicitly confirmed from ESPN — it is listed as 'verify from ESPN' throughout the context.** — If Game 5 is at SAS (due to a schedule anomaly or make-up game), the home court framing entirely flips — backing OKC at shorter odds on the road would be a significant error. → Add a hard gate in series_context: 'MANDATORY: Verify WCF Game 5 location from ESPN bracket before any pick is drafted — do NOT assume OKC home.' This is already present but should be elevated to a blocking gate similar to franchise player checks.
- **LAL Round 2 opponent and current series score remain unconfirmed — the context consistently says 'verify from ESPN' but the opponent identity and series state are never populated.** — If LAL is in a close series (e.g. trailing or facing elimination), the staking and confidence framing changes materially — a LAL team without Doncic in a must-win game is a very different risk profile than a comfortable series lead. → Fetch LAL Round 2 opponent and current series score from ESPN bracket and populate it explicitly in series_context and franchise_player_rules at next session — this is a data pipeline fetch, not a rule change.
- **No in-series performance tracking for how well our confidence calibration performs specifically in elimination games (0-3 trailing, 1-3 trailing contexts).** — Elimination games historically skew toward the trailing team winning at home (~55-65% for 0-3 teams winning Game 4) — if we are consistently backing the series leader in elimination contexts, we may be leaving value on the trailing team. → After Conference Finals conclude, audit settled bets tagged as 'elimination game' context and measure win rate vs our confidence vs actual outcome — flag in next session if 3+ elimination game bets exist.
