---
date: 2026-04-29
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (32 bets)
---

## Today's Analysis — 2026-04-29

The most striking pattern this round is the ORL vs DET series where Orlando (NetRtg +0.6) leads Detroit (NetRtg +8.2) 3-1 — the largest NetRtg-vs-outcome divergence in the bracket, confirming that playoff scheme execution can completely override season efficiency metrics, especially by Games 5-6. Multiple series are now at 3-2 (BOS/PHI, NYK/ATL, MIN/DEN) creating simultaneous must-win scenarios with maximum motivation on both sides — home court advantage (~3-4 pts playoff) becomes the primary tiebreaker in these games. Performance data continues to show High confidence bets underperforming (35.3% WR, -€1,099) while Medium confidence is profitable (58.1% WR, +€620) — Scout should continue targeting 55-69 confidence range and treating over-confidence as a direct P&L risk.

## Performance Stats
ALL-TIME: 24W / 26L | Win rate: 48.0% | P&L: €-620.43 | Avg odds: 1.94 | Avg conf: 65.9/100
RECENT 20: 9W / 11L | 45.0% WR | P&L: €-954.45
By market:      ML 22bets 9W/13L 40.9% €-930.10  |  SPREAD 24bets 13W/11L 54.2% €+236.94  |  TOTAL 4bets 2W/2L 50.0% €+72.73
By confidence:  High 17bets 6W/11L 35.3% €-1099.81  |  Medium 31bets 18W/13L 58.1% €+620.69  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 17bets 7W/10L 41.2% €-1194.45  |  1.90-2.09 29bets 16W/13L 55.2% €+516.03  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Updated series scores from ESPN live data: SAS now leads 4-1, ORL leads 3-1, NYK leads 3-2, BOS leads 3-2; all series context refreshed with current standings and verification flags maintained.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] Updated all series scores to match ESPN live data: ORL leads 3-1, BOS leads 3-2, NYK leads 3-2, SAS leads 4-1; added play-in entries that appear in ESPN feed for verification; corrected series states throughout.
- [elimination_flags] Updated elimination flags to reflect corrected series scores: SAS now leads 4-1, ORL leads 3-1, NYK leads 3-2, BOS leads 3-2; DET now facing elimination down 3-1, ATL facing elimination down 2-3, PHI facing elimination down 3-2.
- [h2h_playoff] Updated in-series records to reflect ESPN data: ORL leads 3-1, NYK leads 3-2, BOS leads 3-2, SAS leads 4-1; revised H2H notes to match current series states and flag ATL data conflict.
- [playoff_motivation] Updated motivation hierarchy to reflect current series states with multiple 3-2 series now active, adding a specific 3-2 dynamic rule and refining the DEN Jokic factor for road elimination context.
- [l15_caveat] Updated to reflect corrected series scores (ORL leads 3-1, BOS leads 3-2, NYK leads 3-2, SAS leads 4-1) and added the ORL vs DET NetRtg divergence as the most significant analytical lesson of the round.

## Intelligence gaps identified
- **ORL vs DET series shows NetRtg +8.2 team losing 3-1 — we have no rule weighting in-series offensive/defensive efficiency data from playoff games already played.** — If we had tracked ORL's actual playoff defensive rating in-series vs DET (vs their regular season rating), we would have flagged much earlier that DET's offensive advantage was being neutralised; this would have avoided any bet on DET at short odds. → Add a rule to l15_caveat and priority_stats: when in-series stats are available (points per game allowed, in-series pace), weight these OVER regular season NetRtg from Game 3 onwards in a series.
- **CLE vs TOR series score appears as 0-0 in ESPN data feed rather than reflecting Round 1 progress, suggesting a data pipeline gap for this specific series.** — Without accurate series score, Scout cannot apply elimination flags, home court context, or desperation adjustments for any CLE or TOR game — a pick on either team could be made without correct series context. → Flag CLE vs TOR as a DATA VERIFICATION REQUIRED series before any pick; Scout must confirm series score via NBA official PDF before drafting any CLE/TOR pick.
- **High confidence tier (70-84) is producing 35.3% WR and -€1,099 P&L across 17 bets — the confidence calibration appears systematically overconfident relative to actual win probability.** — If the High tier is actually producing ~35% outcomes, staking 20-25% of bankroll at this tier is destroying value; reducing the staking for 70-84 confidence or raising the EV floor for High tier picks would protect capital. → Consider raising EV floor for High confidence picks from 0.05 to 0.10 (requiring stronger edge to justify 20-25% stake), or capping High tier stake at 15% pending further data.
