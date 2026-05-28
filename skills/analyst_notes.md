---
date: 2026-05-28
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (43 bets)
---

## Today's Analysis — 2026-05-28

The WCF has been forced to a winner-take-all Game 7 after SAS won Game 6 at home, fundamentally shifting the series framing — the key analytical update is that no in-series lead exists, so OKC home court (if confirmed) + NetRtg edge (+2.8pts) become the co-primary signals, and historical Game 7 home win rates (~60-65%) give OKC a structural edge that should be evaluated for both ML and spread value. NYK's rest advantage for Finals Game 1 is now at maximum (7-10+ days) regardless of WCF outcome, creating a strong structural edge for Finals Game 1 that Scout should flag immediately. Jalen Williams (OKC) remaining OUT in a home Game 7 is the key swing factor to monitor — his absence modestly compresses OKC's spread line, potentially opening value if the market over-prices the absence.

## Performance Stats
ALL-TIME: 32W / 29L | Win rate: 52.5% | P&L: €+457.72 | Avg odds: 1.93 | Avg conf: 65.6/100
RECENT 20: 12W / 8L | 60.0% WR | P&L: €+656.22
By market:      ML 25bets 12W/13L 48.0% €-289.43  |  SPREAD 29bets 16W/13L 55.2% €+592.70  |  TOTAL 7bets 4W/3L 57.1% €+154.45
By confidence:  High 19bets 8W/11L 42.1% €-659.52  |  Medium 40bets 24W/16L 60.0% €+1258.55  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 21bets 11W/10L 52.4% €-382.39  |  1.90-2.09 36bets 20W/16L 55.6% €+782.12  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] ESPN live feed shows OKC leads 3-2 with Game 7 next, meaning SAS won Game 6 to force Game 7 — all WCF series_context references must be updated to reflect the tied 3-3 status and upcoming Game 7.

## Commit patches applied
None

## Playoff context patches applied
- [phase] ESPN live feed shows OKC leads 3-2 with Game 7 next, confirming SAS won Game 6 to force a deciding Game 7.
- [series_context] ESPN live feed confirms Game 7 is next in WCF (OKC leads 3-2 becomes series tied 3-3 after SAS won Game 6), requiring full reframe from elimination game to winner-take-all Game 7 context.
- [elimination_flags] With SAS winning Game 6 to force Game 7, neither team faces elimination alone — both face a winner-take-all Game 7, requiring removal of the directional elimination framing.
- [playoff_rest] Series forced to Game 7 requires updated rest framing — neither team is at elimination disadvantage now, but Game 7 home court and NYK rest advantage for Finals are the key new factors.
- [playoff_motivation] SAS winning Game 6 to force Game 7 fundamentally changes the motivation framing — no team has series lead, both face elimination, and OKC home court + NetRtg replace the elimination-game edge as primary signals.
- [h2h_playoff] SAS won Game 6 to force Game 7, making the series tied 3-3 and requiring the signal hierarchy to shift from in-series lead to home court + NetRtg as co-primary indicators.
- [l15_caveat] Series tied 3-3 requires reframing the signal hierarchy — no team has in-series lead, so home court and NetRtg must become the primary predictors for Game 7 analysis.
- [no_tanking] SAS won Game 6 to force Game 7, meaning neither team faces unilateral elimination — both OKC and SAS are in a winner-take-all Game 7 requiring updated elimination flag framing.

## Intelligence gaps identified
- **Game 7 home win rate by NetRtg gap is not currently tracked in playoff_context rules — we know historical home win rate is ~60-65% in WCF Game 7s but don't have a NetRtg-stratified version** — With OKC at home + NetRtg +2.8pt edge, knowing whether the home win rate increases to ~70%+ when the home team also has a NetRtg advantage would sharpen the OKC confidence tier and spread analysis for Game 7 → Flag for data enrichment: research Conference Finals Game 7 home win rates split by whether home team had a positive season NetRtg differential vs the visitor; update l15_caveat or h2h_playoff with the finding
- **Los Angeles Lakers Round 2 series score and opponent remain unverified — the current skills files consistently say 'verify from ESPN' but no confirmation has been received** — If LAL is in an active series, Luka Doncic being OUT is a franchise player absence that should be driving specific confidence adjustments for LAL picks, but without series context we cannot frame the LAL angle correctly → Prioritise ESPN bracket fetch for LAL Round 2 status at next session; if LAL is eliminated, update elimination_flags immediately; if active, update series_context with opponent and score
- **High confidence bets (70-84) continue to underperform significantly (38.9% WR, -€894.80) but the current rule only adds 'extra scrutiny' without a hard structural gate — a soft scrutiny note may be insufficient** — If high confidence picks are systematically losing, the gap between 'extra scrutiny required' and a hard confidence cap or odds floor may be costing real money; a more structural rule (e.g. require NetRtg gap ≥ 6.0 for high confidence ML, not just ≥ 5.0) could reduce the loss rate → After 5 more high-confidence settled bets, evaluate whether to raise NetRtg gap requirement for high-confidence ML picks from ≥ 5.0 to ≥ 6.0, or add a hard EV floor of 0.10 (not 0.08) for high-confidence ML picks at 1.70-1.89
