---
date: 2026-05-10
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (37 bets)
---

## Today's Analysis — 2026-05-10

Primary update today is factual: OKC has advanced to 3-0 in their West Semifinals series (opponent identity needs ESPN verification — likely Memphis or another West seed; DEN confirmed eliminated), and DET-CLE is confirmed at 2-1 making that series competitive again with CLE facing must-win urgency. Performance data shows a clear and actionable pattern: Medium confidence (55-69) is profitable at 58.3% WR / +€739.80 while High confidence (70-84) is deeply underwater at 35.3% / -€1,099.81 — this is now 17 bets of evidence and the most important signal in the dataset. The ML market continues to underperform (40.9%, -€930.10) versus spreads (53.8%, +€274.33), reinforcing that Scout should prioritise spread evaluation in every session where advanced stats and injury data are available.

## Performance Stats
ALL-TIME: 27W / 28L | Win rate: 49.1% | P&L: €-501.32 | Avg odds: 1.94 | Avg conf: 65.6/100
RECENT 20: 9W / 11L | 45.0% WR | P&L: €-939.53
By market:      ML 22bets 9W/13L 40.9% €-930.10  |  SPREAD 26bets 14W/12L 53.8% €+274.33  |  TOTAL 7bets 4W/3L 57.1% €+154.45
By confidence:  High 17bets 6W/11L 35.3% €-1099.81  |  Medium 36bets 21W/15L 58.3% €+739.80  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 18bets 8W/10L 44.4% €-1023.06  |  1.90-2.09 33bets 18W/15L 54.5% €+463.75  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Updated OKC series lead to 3-0 (from 2-0) per ESPN live feed; all other statuses aligned to current verified injury list with no new additions.

## Commit patches applied
None

## Playoff context patches applied
- [phase] Updated OKC series lead to 3-0 per ESPN live feed; DET confirmed opponent is CLE per series_context data.
- [series_context] Updated OKC series to 3-0, DET series to 2-1, confirmed DET opponent as CLE per ESPN live bracket feed.
- [elimination_flags] Updated OKC to 3-0 lead, DET to 2-1 lead, CLE confirmed as DET opponent; added OKC opponent elimination flag.
- [playoff_rest] Updated to reflect OKC 3-0 lead (opponent now also facing elimination), DET 2-1 series with CLE confirmed.
- [playoff_motivation] Updated to reflect OKC 3-0 lead, DET 2-1 with CLE confirmed, added nuance on PHI 0-3 desperation vs statistical reality.
- [h2h_playoff] Updated OKC to 3-0, DET to 2-1 with CLE confirmed as opponent, refreshed all in-series lesson tags.
- [l15_caveat] Updated OKC series to 3-0, DET-CLE to 2-1 with 3 games of in-series data; added CLE desperation context and strengthened OKC lesson with cumulative 7-game evidence.
- [no_tanking] Updated eliminated teams list to reflect all confirmed Round 1 completions; aligned active teams list with current ESPN bracket.

## Intelligence gaps identified
- **High-confidence picks (70-84 tier) are losing at 35.3% across 17 bets — far worse than Medium-confidence picks at 58.3%, suggesting the confidence calibration is systematically over-confident in that tier** — The staking rules assign 20-25% of bankroll to High confidence picks; if these are losing at 35.3%, the system is betting largest on its worst-performing tier, which explains the -€1,099.81 loss concentration → After 20 bets at High confidence, this warrants a strategic review of what signals are driving High confidence inflation — likely NetRtg-heavy analysis without sufficient in-series or injury weighting in playoff context; consider raising the High tier floor to 75 or adding a playoff-specific confidence cap
- **ML market is 40.9% win rate over 22 bets (-€930.10) while spreads are 53.8% over 26 bets (+€274.33) — a consistent and large divergence across the full sample** — Scout currently treats ML and spread as equal alternatives; if spreads are systematically outperforming ML by ~13 percentage points across a significant sample, the market_rules selectivity for ML should be raised or spreads should be default-preferred when both markets are available → Add a preference rule to market_rules: when both ML and spread show EV ≥ 0.05 on the same game, default to the spread market unless ML odds are ≥ 2.10 (where ML-specific value exists); also consider raising ML confidence floor from 50 to 55
- **OKC's Round 2 opponent identity is unconfirmed in current data — the skills file references an unknown opponent at 0-3 down** — Scout cannot evaluate OKC games without knowing the opponent's NetRtg, injury status, home court, and series context; a pick drafted with 'unknown opponent' risks using wrong franchise player rules or rest data → Mandatory ESPN bracket verification before any OKC pick is already flagged; no patch needed — infrastructure/data fetch issue, not a rules gap
- **Anthony Edwards (MIN) status is unknown for Round 2 — he was roster-only OUT in Round 1 but MIN advanced to Round 2, suggesting possible return, and this is the decisive variable in SAS vs MIN series odds** — If Edwards is active, MIN's effective NetRtg rises significantly (from ~+1.5 to closer to +3.1 or higher), which would change any SAS vs MIN pick thesis materially; current rules flag re-verification but don't provide a fallback confidence adjustment if Edwards status cannot be confirmed → Add to franchise_player_rules a specific note: if Edwards status cannot be confirmed via NBA official PDF, apply confidence -20 to ALL MIN picks (not just -10) given he is the franchise player and was recently OUT; this is stronger than the standard GTD adjustment given the recent injury history
