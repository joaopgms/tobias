---
date: 2026-05-09
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (36 bets)
---

## Today's Analysis — 2026-05-09

ESPN live feed confirms four Round 2 series with updated scores: NYK leads PHI 3-0 (PHI facing elimination), DET leads 2-0 (opponent likely CLE — verify), OKC leads 2-0 (opponent verify), and SAS leads MIN 2-1 — the only truly competitive series with a clear variable (Edwards status). The LAL-HOU Game 7 remains the most analytically interesting pick, where Durant's confirmed absence/presence is the sole determinant of whether HOU has a legitimate case. Performance data shows ML bets are deeply negative (9W/13L, €-930) while spreads are profitable (14W/12L, €+274) and Medium confidence is significantly outperforming High confidence — this pattern suggests Scout should continue favouring spread markets and avoid high-stakes ML plays, particularly at the 1.70-1.89 odds range which shows the worst ROI (8W/10L, €-1023).

## Performance Stats
ALL-TIME: 27W / 27L | Win rate: 50.0% | P&L: €-283.04 | Avg odds: 1.94 | Avg conf: 65.7/100
RECENT 20: 10W / 10L | 50.0% WR | P&L: €-462.37
By market:      ML 22bets 9W/13L 40.9% €-930.10  |  SPREAD 26bets 14W/12L 53.8% €+274.33  |  TOTAL 6bets 4W/2L 66.7% €+372.73
By confidence:  High 17bets 6W/11L 35.3% €-1099.81  |  Medium 35bets 21W/14L 60.0% €+958.08  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 18bets 8W/10L 44.4% €-1023.06  |  1.90-2.09 32bets 18W/14L 56.2% €+682.03  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Updated series scores from ESPN live feed (DET 2-0, OKC 2-0, NYK 3-0, SAS 2-1 in Round 2), confirmed BOS and TOR eliminations, and aligned all franchise player notes with current verified absence list.

## Commit patches applied
None

## Playoff context patches applied
- [phase] Updated to reflect current ESPN series scores: NYK 3-0, DET 2-0, OKC 2-0, SAS 2-1; LAL-HOU Game 7 remains the only active Round 1 game.
- [series_context] Updated series scores to ESPN live ground truth: NYK 3-0, DET 2-0, OKC 2-0, SAS 2-1; confirmed all Round 1 series complete; identified NYK vs PHI and SAS vs MIN as the active Round 2 matchups.
- [elimination_flags] All Round 1 series now confirmed complete per ESPN; updated Round 2 elimination pressure (PHI faces 0-3 deficit; HOU in Game 7) and series leaders.
- [h2h_playoff] Updated all in-series records to current ESPN scores; added PHI vs NYK as confirmed East Semifinals matchup; incorporated SAS vs MIN West Semifinals data and relevant in-series lessons.
- [playoff_rest] Updated to reflect Round 2 is now at Game 3/4 stage — rust from Round 1 transition is fully dissipated; added elimination game rest override rule.
- [playoff_motivation] Updated motivation hierarchy to reflect current series scores (PHI facing 0-3 elimination, Game 7 LAL-HOU, SAS 2-1 vs MIN) and added elimination game confidence rules.
- [l15_caveat] Updated hierarchy to reflect Game 3/4 stage where in-series data (2-3 games) now outweighs season NetRtg; incorporated confirmed Round 1 lessons including PHI over BOS.
- [no_tanking] Updated with all confirmed Round 1 eliminations (BOS, TOR, DEN, ORL, POR confirmed) and current active teams in Round 2.

## Intelligence gaps identified
- **High confidence bets (17 bets, 35.3% WR, €-1099) are massively underperforming medium confidence (60% WR, €+958) — the confidence calibration appears systematically off, over-rating certainty.** — High confidence picks are losing at a rate suggesting the model is over-confident on its strongest signals; the EV calculation uses confidence as a key input and inflated confidence produces inflated EV on losing picks. → Consider tightening high-confidence threshold from 70-84 to 75-84 range, or adding a 'high confidence handicap' of -5 confidence for playoff picks where franchise player verification is roster-only rather than NBA official PDF confirmed.
- **ML bets at 1.70-1.89 odds range are the worst performing segment (8W/10L, €-1023) — this is the range where most strong-favourite playoff picks cluster.** — At these odds, books already heavily price in the favourite — the market is efficient and our edge is thinnest, yet Scout may be drafting these based on NetRtg gaps that books have already incorporated. → Add a rule in market_rules: for ML picks in the 1.70-1.89 range, require NetRtg gap > 8pts OR in-series lead of 2+ games, not just the standard EV threshold; this would filter out marginal favourites where our edge is already priced out.
- **OKC opponent in Round 2 West Semifinals is unclear — the four confirmed Round 2 participants are NYK, DET, MIN, OKC, but OKC's opponent is not explicitly identified in ESPN feed while SAS is separately listed in West Semifinals.** — If SAS is in West Semifinals vs OKC (Series B) and MIN is in West Semifinals vs [someone], there may be a bracket discrepancy — picking OKC or SAS without confirmed opponent creates an analytical blind spot for home court and in-series context. → ESPN bracket data needs explicit opponent mapping for each Round 2 series slot — the live feed should be queried with 'West Semifinals Series B: OKC vs [verify opponent]' before any OKC or remaining West team picks are drafted.
