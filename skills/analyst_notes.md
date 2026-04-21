---
date: 2026-04-21
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (18 bets)
---

## Today's Analysis — 2026-04-21

Play-in matchups remain unconfirmed officially — Scout must not draft any play-in picks until the bracket is published. The most notable statistical edge in the field remains Charlotte Hornets (NetRtg +5.0) who are statistically the strongest play-in team despite being seeded 8th in the East; if priced as an underdog versus Philadelphia (NetRtg -0.2), this is a high-confidence regression-fade setup. Performance data shows High confidence bets are deeply underwater (4W/8L, -€739) while Medium confidence bets are the engine of profit (14W/8L, +€935) — no strategic rule changes are warranted without further evidence, but Scout should be aware of this tier inversion and avoid forcing High-tier confidence labels without overwhelming signal convergence.

## Performance Stats
ALL-TIME: 18W / 18L | Win rate: 50.0% | P&L: €+54.70 | Avg odds: 1.95 | Avg conf: 65.9/100
RECENT 20: 12W / 8L | 60.0% WR | P&L: €+682.94
By market:      ML 15bets 7W/8L 46.7% €-275.39  |  SPREAD 18bets 10W/8L 55.6% €+353.36  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 12bets 4W/8L 33.3% €-739.59  |  Medium 22bets 14W/8L 63.6% €+935.60  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 10bets 5W/5L 50.0% €-469.94  |  1.90-2.09 23bets 13W/10L 56.5% €+753.95  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Verified absence feed unchanged from prior session — all player statuses confirmed consistent with prior session data; no new additions or removals detected beyond what was already captured.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] Refreshing series_context timestamp and confirming no new play-in matchup announcements or roster changes have emerged in today's verified data feed.
- [elimination_flags] No new elimination events have occurred — play-in bracket not yet officially confirmed; updating timestamp and retaining all prior flags with consistent data.
- [h2h_playoff] Refreshing timestamp — no new H2H data available as official play-in matchups have not yet been announced; maintaining all prior caveats.

## Intelligence gaps identified
- **Official play-in matchup pairings and tip-off times have not been confirmed in the data feed, preventing any structured pre-game analysis for play-in games.** — Scout cannot safely draft any play-in picks without official matchup confirmation — incorrect pairing assumptions could produce picks on wrong team dynamics or wrong rest calculations. → Infrastructure fix needed: add an official NBA schedule API or confirmed bracket source to the daily data pull so play-in pairings are verified before Scout runs at 14:00 UTC.
- **High confidence tier (conf 70-84) is producing 33.3% win rate and -€739.59 P&L across 12 bets, a severe underperformance versus the Medium tier (63.6%, +€935.60).** — This tier inversion suggests the signals being used to push picks into the High confidence bracket are not adding genuine edge — a selectivity rule or confidence ceiling could prevent overconfident picks in ambiguous matchups. → After 5 more High-tier settled bets, evaluate whether to add a High-tier qualifier: High confidence (70-84) requires NetRtg L15 gap ≥ 6 AND at least one secondary signal (B2B, DefRtg gap, franchise player absence). Without two converging signals, cap at Medium (55-69).
- **Odds range 2.10-2.50 is producing 0W/3L (0.0%, -€229.31) — the upper end of the ML odds target range is systematically losing.** — Picks at 2.10-2.50 imply we are backing underdogs with ~40-48% implied probability, but we are winning 0% — suggesting our edge detection is failing at the top of the odds range, possibly because these are genuine underdogs we are over-crediting. → After 2-3 more settled bets in the 2.10-2.50 range, evaluate tightening ML ceiling to 2.10 or requiring NetRtg L15 gap ≥ 8 to justify backing any team priced above 2.10.
- **Trae Young data conflict (appearing in both ATL and WAS verified absence feeds) has persisted across multiple sessions without resolution.** — If Trae Young is actually an Atlanta Hawk and active, any ATL pick could be incorrectly penalised; if he is genuinely injured/traded to WAS, ATL picks lack the key playmaker caveat. → Infrastructure fix: cross-reference NBA official transaction wire and official roster API to resolve team affiliation definitively. This is a data integrity issue that cannot be patched via rules.
