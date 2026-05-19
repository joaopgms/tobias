---
date: 2026-05-19
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 1
milestone: daily (39 bets)
---

## Today's Analysis — 2026-05-19

The WCF Game 1 result (SAS wins at OKC) is the dominant signal today — OKC's extended rest rust has been confirmed empirically, and SAS now holds both the in-series lead and the match-sharpness advantage entering Game 2. The performance data (57 bets) reveals a critical structural pattern: High-confidence picks are losing at 38.9% (-€895) while Medium-confidence picks win at 56.8% (+€632), suggesting our confidence calibration is systematically overconfident in the 70-84 range — today's patches add extra scrutiny criteria before staking 20%+ on any pick. The ML market in the 1.70-1.89 odds band is our single biggest loss source (-€818 across 19 bets), and the EV floor for that specific market/odds combination has been raised to 0.08 to address this.

## Performance Stats
ALL-TIME: 28W / 29L | Win rate: 49.1% | P&L: €-404.31 | Avg odds: 1.94 | Avg conf: 65.6/100
RECENT 20: 10W / 10L | 50.0% WR | P&L: €-190.01
By market:      ML 23bets 10W/13L 43.5% €-725.09  |  SPREAD 27bets 14W/13L 51.9% €+166.33  |  TOTAL 7bets 4W/3L 57.1% €+154.45
By confidence:  High 18bets 7W/11L 38.9% €-894.80  |  Medium 37bets 21W/16L 56.8% €+631.80  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 19bets 9W/10L 47.4% €-818.05  |  1.90-2.09 34bets 18W/16L 52.9% €+355.75  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Updating franchise_player_rules to reflect current Conference Finals matchups (ECF: NYK vs CLE; WCF: OKC vs SAS) and removing stale series references; verified player statuses from ESPN roster + NBA injury feed.
- [confidence_staking] Performance data (57 bets) shows High confidence tier losing at 38.9% (-€895) while Medium tier wins at 56.8% (+€632); tightening High-conf criteria and raising ML EV floor in the worst-performing odds band.

## Commit patches applied
- [commit_staking] Syncing commit_staking with updated scout confidence_staking to reflect performance evidence from 57 settled bets showing High-conf ML picks in low-odds range are the primary loss source.

## Playoff context patches applied
- [phase] ESPN live feed shows WCF is SAS leads 1-0 (Game 2 next) and ECF is Tied 0-0 (Game 1 next); updating phase section to reflect Game 1 WCF result and its implications.
- [series_context] ESPN live feed shows WCF SAS leads 1-0 (Game 2 next); updating series_context to elevate SAS in-series lead as primary WCF signal and recalibrate OKC rust/home court narrative.
- [elimination_flags] Updating elimination flags to reflect WCF SAS leads 1-0 and OKC now trails; ECF remains Tied 0-0 with Game 1 pending.
- [playoff_rest] WCF Game 1 has been played (SAS leads 1-0), confirming OKC rust thesis; updating rest section to reflect this result and calibrate Game 2 confidence adjustments.
- [playoff_motivation] WCF Game 1 result (SAS leads 1-0) fundamentally changes the WCF motivation and statistical hierarchy; updating to elevate in-series result as primary WCF signal and recalibrate OKC expectations.
- [h2h_playoff] WCF Game 1 result (SAS leads 1-0) is now available and must be elevated as primary WCF signal per the l15_caveat hierarchy; updating h2h_playoff to reflect this in-series data.
- [l15_caveat] WCF Game 1 result (SAS leads 1-0) activates the in-series PRIMARY signal rule; updating l15_caveat to apply this hierarchy immediately to WCF Game 2 analysis.
- [no_tanking] Updating no_tanking section to reflect current playoff bracket state including WCF SAS leads 1-0.

## Intelligence gaps identified
- **WCF Game 1 score and box-score details (margin, Wembanyama stats, SGA performance) are not available in the current feed — only the series score (SAS leads 1-0) is confirmed.** — Knowing whether SAS won Game 1 by 5 or 25 points, and whether SGA was impacted by rust vs Wembanyama dominating, would materially change WCF Game 2 confidence calibration and which team to back. → Fetch ESPN box score for WCF Game 1 before drafting any WCF Game 2 pick — game margin and key player performance are decisive inputs for in-series momentum assessment.
- **LAL Round 2 opponent identity and current series score are unverified — the feed only confirms LAL is active in Round 2 without naming the opponent or score.** — Without knowing who LAL faces, their seed, home court situation, and any relevant injuries, Scout cannot responsibly draft any LAL Round 2 pick — the pick would be based on incomplete information. → Mandatory ESPN verification of LAL Round 2 opponent and series state before any LAL pick is drafted; add explicit 'verify LAL Round 2 opponent from ESPN — MANDATORY' note to franchise_player_rules LAL entry (already present, but verify it's enforced by Scout).
- **High-confidence pick losses (7W/11L, -€895) lack granular breakdown by signal type — we know the loss pattern but cannot identify whether losses came from NetRtg-based picks, B2B picks, or home court picks specifically.** — Without signal-level attribution for High-conf losses, the patch (adding NetRtg gap ≥ 5.0 AND home court/health requirement before 20%+ stake) is directionally correct but may not target the actual root cause. → Add signal_type field to bet log output so future Analyst sessions can cross-reference High-conf losses by the specific priority_stats signal that drove the pick (e.g. NetRtg gap, B2B, franchise player absence).
- **ECF regular-season H2H record (NYK vs CLE this season) is not available in the current feed, leaving only NetRtg and rest as differentiators for ECF Game 1.** — Regular season H2H is listed as a tiebreaker in priority_stats, and for a tight matchup (NYK +2.5pt NetRtg gap only), H2H results in 2025-26 could be a meaningful tiebreaker signal. → Fetch ESPN regular-season H2H for NYK vs CLE and OKC vs SAS before any Conference Finals pick is drafted; flag if either team went 0-2 or 2-0 in the regular-season matchup.
