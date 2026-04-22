---
date: 2026-04-22
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (20 bets)
---

## Today's Analysis — 2026-04-22

Performance data shows a stark confidence-tier inversion: High confidence bets (12 bets) are running at 33.3% WR and -€739.59, while Medium confidence (24 bets) are at 58.3% and +€397.60 — this is the most critical pattern in the dataset and suggests overconfidence calibration is miscalibrated rather than the underlying edge. The odds range 2.10-2.50 is 0W/3L (-€229.31), reinforcing that chasing longer prices has not worked; the sweet spot remains 1.90-2.09 (52% WR, +€215.95). On the playoff side, the LAL vs DEN first-round matchup (if confirmed) is the most structurally interesting series to watch: Denver on a W12 streak at +5.2 NetRtg faces a Lakers team without Doncic and Reaves, creating a potential extreme mismatch — verify rosters before any pick as LAL's situation could be resolved by the time series begins.

## Performance Stats
ALL-TIME: 18W / 20L | Win rate: 47.4% | P&L: €-483.30 | Avg odds: 1.95 | Avg conf: 65.9/100
RECENT 20: 12W / 8L | 60.0% WR | P&L: €+254.94
By market:      ML 15bets 7W/8L 46.7% €-275.39  |  SPREAD 20bets 10W/10L 50.0% €-184.64  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 12bets 4W/8L 33.3% €-739.59  |  Medium 24bets 14W/10L 58.3% €+397.60  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 10bets 5W/5L 50.0% €-469.94  |  1.90-2.09 25bets 13W/12L 52.0% €+215.95  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Updated HOU franchise player section to reflect Kevin Durant no longer appearing in the verified absence feed this session (data conflict flag added), and removed Jordan McLaughlin from SAS (not in verified list this session); all other entries preserved from verified feed.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] Updated streak data from current standings, added Kevin Durant data-conflict flag, updated session date, and clarified LAL roster-thin status in seedings context.
- [elimination_flags] Updated session date, added concrete NetRtg-based edge notes for each play-in matchup, clarified LAL roster risk vs DEN in first round, and maintained all existing elimination structure.
- [h2h_playoff] Updated session date, added specific priority flag for LAL vs DEN first-round matchup given extreme roster asymmetry, maintained all structural H2H rules.
- [playoff_rest] Updated session date and added OKC/SAS late-season streak note as potential load management signal; preserved all rest calculation rules.

## Intelligence gaps identified
- **High confidence tier (70-84, 85-100) is producing 33.3% WR vs Medium tier at 58.3% — the confidence calibration model appears systematically overconfident at the top tier** — If high-confidence picks are losing at a 66.7% rate (-€739.59), the rules governing when to assign confidence ≥ 70 are producing incorrect signals, meaning staking rules are directing larger stakes toward worse-performing picks → After 5 more high-confidence settled bets (approaching 17 total), run a formal review of what signal types drove high confidence assignments on the 8 losses — if NetRtg L15, H2H, or franchise player flags were the primary drivers of high confidence in losing picks, tighten those confidence bonuses from +10 to +5
- **Odds range 2.10-2.50 is 0W/3L (-€229.31) — the ceiling of the odds_targets range may be producing negative EV in practice despite passing the EV formula** — Three losses at the top of the odds range suggests either the EV calculation is accepting false edges at these prices (overestimating implied win probability) or the signal quality at these odds levels is insufficient → Consider tightening ML ceiling from 2.50 to 2.30 to match the spread ceiling, or adding a confidence floor of 60 for any ML pick priced 2.10-2.50 (same bar as spreads)
- **Denver is ranked as #6 West seed (54-28) behind LA Lakers at #3 (53-29) — this seeding is arithmetically anomalous given Denver's superior record and W12 streak** — If the seeding is incorrect, first-round matchup assumptions (LAL vs DEN) could be wrong, leading Scout to evaluate the wrong matchup and apply incorrect home court, H2H, and series context → Infrastructure fix needed: pull official NBA bracket from NBA.com or ESPN bracket page to confirm West seeds 1-6; update series_context and h2h_playoff immediately upon confirmation
- **Kevin Durant's absence status is contradicted between sessions — previously roster-only OUT, now absent from the verified absence feed — creating a data reliability issue for HOU picks** — If Durant is actually available, HOU becomes a significantly stronger pick candidate (52-30, +5.4 NetRtg, W1 streak); if he is still OUT but simply dropped from the feed, backing HOU is dangerous at reduced confidence → Infrastructure fix needed: cross-reference NBA official injury PDF specifically for HOU each session; add a 'feed-dropout flag' to data_quality_rules to catch players who disappear from the injury feed without a confirmed return-to-play note
