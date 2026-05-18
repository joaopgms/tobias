---
date: 2026-05-18
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (39 bets)
---

## Today's Analysis — 2026-05-18

Round 2 is fully complete with Conference Finals matchups set: NYK vs CLE (ECF) and OKC vs SAS (WCF) with LAL still active in Round 2. The WCF is the marquee statistical matchup — OKC (+11.1 NetRtg, 8-0 playoff record) vs SAS (+8.3, Wembanyama dominant) is the tightest top-line comparison of any series this postseason, and SAS enters with match-sharpness advantage after 6 games vs MIN. Performance data continues to confirm SPREAD and TOTALS are the profitable markets (€+166, €+154) while ML bets are deeply underwater (€-725), and critically, High-confidence bets are performing below Medium-confidence (38.9% vs 56.8% win rate) — the evidence for maintaining the current medium-confidence staking discipline is strong. WCF Game 2 is next per ESPN live feed, suggesting Game 1 may have already occurred; Scout must verify that result before drafting any OKC or SAS pick.

## Performance Stats
ALL-TIME: 28W / 29L | Win rate: 49.1% | P&L: €-404.31 | Avg odds: 1.94 | Avg conf: 65.6/100
RECENT 20: 10W / 10L | 50.0% WR | P&L: €-190.01
By market:      ML 23bets 10W/13L 43.5% €-725.09  |  SPREAD 27bets 14W/13L 51.9% €+166.33  |  TOTAL 7bets 4W/3L 57.1% €+154.45
By confidence:  High 18bets 7W/11L 38.9% €-894.80  |  Medium 37bets 21W/16L 56.8% €+631.80  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 19bets 9W/10L 47.4% €-818.05  |  1.90-2.09 34bets 18W/16L 52.9% €+355.75  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] ESPN live feed confirms SAS leads 4-2 COMPLETE (series over) and CLE leads DET 4-3 COMPLETE — DET and MIN both eliminated; franchise_player_rules must reflect current playoff bracket with no further picks on eliminated teams.

## Commit patches applied
None

## Playoff context patches applied
- [phase] ESPN live feed confirms Round 2 fully complete with SAS defeating MIN 4-2 and CLE defeating DET 4-3; Conference Finals matchups are now the active stage with WCF listed as Tied 0-0 Game 2 next.
- [series_context] Round 2 fully complete per ESPN live feed; Conference Finals matchups (NYK vs CLE, OKC vs SAS) are the active stage requiring updated series context, rest gap analysis, and mandatory verification requirements.
- [elimination_flags] SAS defeated MIN 4-2 and CLE defeated DET 4-3 per ESPN live feed, eliminating MIN and DET and advancing both SAS and CLE to Conference Finals stage.
- [playoff_rest] Round 2 complete; rest context must shift to Conference Finals stage with OKC and NYK having extended rest (sweep finishers) vs SAS and CLE having less rest (longer series), creating early-series sharpness edges.
- [playoff_motivation] Conference Finals stage requires motivation hierarchy update — all teams maximally motivated, key differentiators shift to rest/sharpness gaps and franchise player health rather than elimination urgency.
- [h2h_playoff] Conference Finals stage with new matchups (NYK vs CLE, OKC vs SAS) requires complete h2h_playoff reset with Round 2 lessons integrated and no in-series data yet for new series.
- [no_tanking] MIN and DET confirmed eliminated per ESPN live feed (SAS 4-2, CLE 4-3); no_tanking elimination list must be updated to reflect current Conference Finals bracket.
- [l15_caveat] Conference Finals requires updated l15_caveat with new series context, no in-series data available, and rest/sharpness gap as the key early-series differentiator replacing elimination urgency rules from Round 2.

## Intelligence gaps identified
- **WCF Game 1 result is unknown — ESPN live feed shows Game 2 is next, implying Game 1 has been played, but no score or in-series data was provided in this session's feed** — In-series results are the PRIMARY signal for Conference Finals from Game 2 onwards per the l15_caveat hierarchy; drafting any OKC or SAS WCF pick without knowing the Game 1 result would force reliance on season NetRtg alone, which is materially weaker than having even one game of in-series data → Fetch live ESPN scoreboard/series scores for WCF Game 1 before Scout drafts any WCF pick; add a mandatory gate in scout_skills franchise_player_rules SAS/OKC notes: 'If Game 2 next — verify Game 1 result from ESPN BEFORE drafting'
- **LAL Round 2 opponent identity is still unconfirmed in the ESPN live feed — listed as 'verify from ESPN bracket' across multiple sections without resolution** — Without knowing LAL's Round 2 opponent, Scout cannot assess the matchup NetRtg gap, home court, or franchise player health for either team — making any LAL Round 2 pick essentially a blind bet → Fetch ESPN bracket to confirm LAL Round 2 opponent; update series_context, elimination_flags, and franchise_player_rules with confirmed opponent name and current series score before any LAL pick is drafted
- **High-confidence bets (conf 70-84+) are performing significantly worse than Medium-confidence bets (38.9% WR / €-894 vs 56.8% WR / €+631) over the full 57-bet sample — suggesting the current High tier staking (20-25% bankroll) may be overcapitalising on overcalibrated picks** — If High-confidence picks are win-rate negative (38.9%) over 18 bets, the staking allocation of 20-25% bankroll to these picks is the primary driver of total P&L loss (€-894 from 18 bets); reducing staking or tightening the confidence gate for High tier could improve overall P&L materially → After 5 more High-tier settled bets (reaching ~23), if WR remains below 45%, replace confidence_staking High tier to 15-20% (from 20-25%) and raise the effective High tier floor from 70 to 73 confidence; flag for next milestone review
