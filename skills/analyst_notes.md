---
date: 2026-05-06
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (35 bets)
---

## Today's Analysis — 2026-05-06

The playoff picture has clarified significantly: four Round 2 series are confirmed active (NYK/DET/MIN/OKC each leading 1-0), and LAL-HOU Game 7 is the sole remaining Round 1 game. The most critical intelligence item today is re-verifying Anthony Edwards' status for MIN's Round 2 — he was roster-only OUT in Round 1 but MIN led DEN 4-2, and if he's active for Round 2, MIN's effective NetRtg is materially higher than the +3.1 season figure. Performance data continues to show ML is a loss market (-€930 on 22 bets, 40.9% win rate) while SPREAD (+€102.94) and TOTAL (+€372.73) are profitable — Scout should prioritise spread evaluation in Round 2 Game 2/3 matchups where NetRtg gaps exist, and avoid high-confidence ML bets given the clear pattern of over-confidence in that market (High confidence tier: 35.3% win rate, -€1,099).

## Performance Stats
ALL-TIME: 26W / 27L | Win rate: 49.1% | P&L: €-454.43 | Avg odds: 1.94 | Avg conf: 65.7/100
RECENT 20: 10W / 10L | 50.0% WR | P&L: €-376.55
By market:      ML 22bets 9W/13L 40.9% €-930.10  |  SPREAD 25bets 13W/12L 52.0% €+102.94  |  TOTAL 6bets 4W/2L 66.7% €+372.73
By confidence:  High 17bets 6W/11L 35.3% €-1099.81  |  Medium 34bets 20W/14L 58.8% €+786.69  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 17bets 7W/10L 41.2% €-1194.45  |  1.90-2.09 32bets 18W/14L 56.2% €+682.03  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Updated to reflect current ESPN live feed: NYK/MIN/DET/OKC all leading Round 2 1-0; LAL-HOU Game 7 and MIN-DEN Game 7 still active; series status for DET-ORL/CLE-TOR/PHI-BOS requires verification; Edwards status particularly important as MIN advanced to Round 2.

## Commit patches applied
None

## Playoff context patches applied
- [phase] ESPN live feed now shows four active Round 2 series with NYK/DET/MIN/OKC each leading 1-0, confirming their Round 1 series are complete; LAL-HOU Game 7 remains the only confirmed active Round 1 game.
- [series_context] ESPN live feed confirms four active Round 2 series with NYK/DET/MIN/OKC each leading 1-0; this allows inference that their Round 1 opponents are eliminated and permits bracket reconstruction with the LAL-HOU Game 7 as the only remaining Round 1 game.
- [elimination_flags] ESPN live feed confirming four Round 2 series allows inference of which Round 1 teams are eliminated; updated to reflect confirmed eliminations vs verified ones pending ESPN confirmation.
- [playoff_motivation] Updated to reflect four active Round 2 series (NYK/DET/MIN/OKC each leading 1-0), LAL-HOU Game 7 as the only active Round 1 game, and added Edwards re-verification note given MIN's Round 2 advancement.
- [h2h_playoff] Updated to reflect all four confirmed Round 2 series (NYK/DET/MIN/OKC leading 1-0), inferred Round 1 completions from bracket position, and carried forward key lesson about Edwards status re-verification for Round 2.
- [no_tanking] Updated elimination flags to reflect Round 2 bracket confirming which Round 1 teams are eliminated, with appropriate verification flags for ESPN anomaly series.
- [playoff_rest] Updated to reflect four active Round 2 series in early stages and the LAL-HOU Game 7 rest context; added note about teams closing Round 1 early having rest advantage over Game 7 survivors entering Round 2.

## Intelligence gaps identified
- **ML market is deeply unprofitable (9W/13L, 40.9%, -€930) while Spread (52%, +€103) and Total (66.7%, +€373) are profitable — but Scout may still be defaulting to ML picks when spread or total offers better edge** — The ML loss pattern is systematic, not noise — 13 losses on 22 bets with negative P&L despite reasonable odds. Spread and Total bets are both profitable. If Scout continues weighting ML as the default market, this structural loss will continue. → Add a 'market preference hierarchy' to selectivity or market_rules: when a spread edge exists (NetRtg gap > 6pts or B2B situation), EVALUATE spread first and only default to ML if spread confidence is below floor. This formalises what the data already shows.
- **High confidence tier (70-84, 17 bets) has 35.3% win rate and -€1,099 — worse than Medium confidence (58.8%, +€787), suggesting the confidence scoring model is systematically over-confident** — This is the largest single P&L driver in the data. Bets placed with High confidence are losing at a rate that implies the true confidence should be 15-20 points lower on average. This could be causing over-staking on losing picks. → Consider adding a 'playoff confidence deflator' rule: in Round 2+ playoffs, apply confidence -10 to all High-tier picks before staking, since series-level variance and franchise player uncertainty make 75+ confidence picks less reliable. This would naturally push more picks into Medium staking range.
- **Edwards re-verification: Anthony Edwards was roster-only OUT for all of Round 1, yet MIN led DEN 4-2 and advanced — his actual play status in Round 2 is unknown and could be the biggest single swing factor in West Semifinals picks** — If Edwards is active in Round 2, MIN's effective NetRtg is significantly higher than the +3.1 season figure, making MIN competitive even against DEN (+5.2) or another strong West team. Current franchise_player_rules still lists him as OUT from roster-only data. → Priority re-verification task for Scout before any MIN pick: cross-reference Edwards against NBA official PDF. If confirmed active, update franchise_player_rules to remove the OUT flag and recalibrate MIN confidence upward.
- **Odds range 1.70-1.89 is significantly unprofitable (7W/10L, 41.2%, -€1,194) — the worst performing range — suggesting Scout is taking too many short-priced favourites that are correctly priced or slightly overpriced by books** — At 1.70-1.89 odds, a 41% win rate produces heavy negative EV. These are picks where Scout believes edge exists but the market is offering tight odds, leaving no margin for error. In Round 2 playoffs, short-priced favourites (e.g. OKC at home) will frequently fall in this range. → Add to selectivity: 'Avoid ML picks where odds fall in 1.70-1.89 range unless NetRtg gap ≥ 8pts AND home court confirmed AND no franchise player uncertainty. Prefer spread bet on same game instead.' This formalises the evidence showing this odds range consistently underperforms.
