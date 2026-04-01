---
date: 2026-04-01
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (11 bets)
---

## Today's Analysis — 2026-04-01

Standings have shifted meaningfully at the top: OKC (60-16) and Spurs (57-18) are dominant with elite NetRtg differentials, while the Knicks' L3 streak and the Pistons returning to W1 suggest the East top-3 race is tightening. The TOTALS market remains the weakest performer (0W/2L, -€184.27) and high-confidence bets are 0W/1L — both reinforce the existing confidence caps and totals floor of 65+ without additional evidence to loosen them. The Philadelphia 76ers' NetRtg of -0.3 against a 41-34 record remains one of the clearest regression signals on the board and warrants active monitoring for fade opportunities.

## Performance Stats
ALL-TIME: 4W / 7L | Win rate: 36.4% | P&L: €-522.32 | Avg odds: 1.99 | Avg conf: 64.4/100
RECENT 11: 4W / 7L | 36.4% WR | P&L: €-522.32
By market:      ML 5bets 2W/3L 40.0% €-141.53  |  SPREAD 4bets 2W/2L 50.0% €-196.52  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 1bets 0W/1L 0.0% €-225.00  |  Medium 9bets 4W/5L 44.4% €-197.32  |  Speculative 1bets 0W/1L 0.0% €-100.00
By odds range:  1.70-1.89 2bets 1W/1L 50.0% €-66.69  |  1.90-2.09 8bets 3W/5L 37.5% €-355.63  |  2.10-2.50 1bets 0W/1L 0.0% €-100.00



## Scout patches applied
- [franchise_player_rules] Updated Denver Nuggets absences to add Spencer Jones and Zeke Nnaji per verified feed; all other entries confirmed unchanged against current verified list.
- [tanking_teams] Standings updated to reflect current session data; Pistons win streak corrected to W1, Lakers to W4, Knicks streak extended to L3, Charlotte corrected to W1, Houston to W3; Denver depth absences added; Suns cold streak flagged; all records synced to provided standings.

## Commit patches applied
None

## Intelligence gaps identified
- **TOTALS market is 0W/2L (-€184.27) but sample size is only 2 bets — insufficient to determine whether the losses stem from pace-signal failures, injury uncertainty, or odds targeting.** — If the 2 losses were both taken during ESPN-fallback sessions or when Pace data was unavailable, the existing data_quality_rules already address this; if they were taken under clean conditions, the totals confidence floor or EV floor may need tightening. → Track totals bets with a tag for injury-feed source (nba_official vs ESPN) and pace-data availability at draft time, so the next 3-5 totals bets can be audited for root cause.
- **High-confidence tier (85-100) is 0W/1L with a single bet at -€225.00 — the staking tier allocates up to 30% of bankroll to elite picks but there is no additional filter requiring NetRtg gap or injury certainty at the elite tier.** — A single high-confidence loss could indicate the elite-tier pick was based on soft signals (e.g. record + streak) rather than hard advanced-stat confirmation; adding a mandatory NetRtg gap minimum for elite-tier picks would reduce exposure to record-inflated confidence. → Consider adding a rule: confidence ≥ 85 requires NetRtg L15 gap ≥ 6.0 AND NBA official injury PDF available (not ESPN fallback) before the elite stake tier applies.
- **Phoenix Suns (42-34, L10: 3-7, NetRtg +1.8) show the same hot-streak-fade profile as Atlanta and the Lakers but are not currently listed in the HOT STREAK FADE CANDIDATES section.** — Suns' L10 3-7 with a positive record but near-breakeven NetRtg matches the fade criteria (W% above .550 threshold but NetRtg divergence present); opponents at ≥ 1.80 may be underpriced if books are still weighting the season record. → Phoenix Suns have been added to the tanking_teams section under cold-streak monitoring; if the Suns appear in a game as favourite at ≤ 1.85, Scout should run explicit fade evaluation — this is addressed in the tanking_teams patch above.
