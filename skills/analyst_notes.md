---
date: 2026-04-28
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (32 bets)
---

## Today's Analysis — 2026-04-28

Key series updates: OKC has swept PHX 4-0 (verify if series is officially complete), MIN leads DEN 3-2 meaning DEN survived Game 5 — Jokic's elimination-game elevation is the critical signal for Game 6 at MIN. The most urgent data conflict remains Trae Young's team affiliation — he appears in the WAS verified absence feed yet ATL is active in the playoffs; this MUST be resolved via NBA official PDF before any ATL pick can be safely drafted. Performance data continues to show High confidence picks (31.2% WR) significantly underperforming Medium confidence picks (59.4% WR), suggesting the system should lean into medium-confidence edges rather than forcing high-confidence thesis plays — no strategic patch is warranted yet at 16 High bets, but this pattern warrants close monitoring as we approach 20.

## Performance Stats
ALL-TIME: 24W / 26L | Win rate: 48.0% | P&L: €-620.50 | Avg odds: 1.94 | Avg conf: 65.7/100
RECENT 20: 9W / 11L | 45.0% WR | P&L: €-954.52
By market:      ML 22bets 9W/13L 40.9% €-930.10  |  SPREAD 23bets 12W/11L 52.2% €+96.23  |  TOTAL 5bets 3W/2L 60.0% €+213.37
By confidence:  High 16bets 5W/11L 31.2% €-1240.52  |  Medium 32bets 19W/13L 59.4% €+761.33  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 17bets 7W/10L 41.2% €-1194.45  |  1.90-2.09 29bets 16W/13L 55.2% €+515.96  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Updating franchise player statuses to reflect live ESPN series data showing MIN leads DEN 3-2 (not 3-1) and OKC leads PHX 4-0, and aligning all series-specific notes with current verified absence feed.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] Updating series scores to reflect ESPN live data: OKC leads PHX 4-0 (series may be complete), MIN leads DEN 3-2 (DEN survived Game 5), and clarifying home court and elimination contexts for all active series.
- [elimination_flags] Updating elimination flags to reflect MIN leading DEN 3-2 (DEN survived elimination), OKC potentially completing sweep of PHX, and adding ATL data conflict flag as a high-risk warning.
- [h2h_playoff] Updating H2H section to reflect MIN leading DEN 3-2 (adding MIN/Edwards roster caveat for H2H), OKC 4-0 series context, and reinforcing that Game 5/6 series are now fully decided by in-series performance.
- [playoff_motivation] Adding a 'survived elimination momentum' rule to capture the DEN Game 5 survival scenario (and future similar situations) where a team's escape from elimination can create positive psychological momentum for the next game.
- [l15_caveat] Updating L15 caveat to reflect current series outcomes (SAS 3-1, BOS 3-1, MIN 3-2, LAL 3-1) validating or contradicting NetRtg predictions, providing Scout with calibrated guidance on when to trust vs discount L15 at this late series stage.

## Intelligence gaps identified
- **Trae Young appears in the Washington Wizards verified absence feed despite ATL being active in the playoffs vs NYK — team affiliation cannot be determined from current data.** — Any ATL pick drafted without resolving this could be built on fundamentally incorrect roster assumptions; if Young is not on ATL, their offensive ceiling is severely reduced and the series edge vs NYK changes materially. → Require NBA official PDF verification of Young's team affiliation before ANY ATL pick is drafted; Scout should treat ATL picks as BANNED until this is resolved each session.
- **High confidence bets (16 bets, 31.2% WR, -€1240.52) are massively underperforming medium confidence bets (32 bets, 59.4% WR, +€761.33) — the confidence-to-outcome relationship is inverted.** — If high-confidence picks are systematically losing while medium-confidence picks win, the system is overconfident on certain signal types; this could indicate that the signals used to push confidence into the 70-84 range are noisy or that those games attract sharper market pricing that eliminates edge. → After reaching 20 High confidence bets (currently 16), conduct a full audit of which specific signals (NetRtg gap, franchise player absence, series momentum) were present on the losing High confidence picks vs winning Medium ones; consider raising the High confidence threshold or adding an 'over-confidence suppressor' rule.
- **ML market is significantly underperforming SPREAD market (ML 40.9% WR -€930 vs SPREAD 52.2% WR +€96) with roughly equal bet counts — suggesting ML odds are overpriced for the edges being identified.** — If the same edge expressed as a spread beats the same edge expressed as ML, Scout should be defaulting to spread bets more aggressively rather than ML bets, particularly on games with clear NetRtg gaps. → Add a rule to market_rules that when a game has NetRtg gap > 4 AND spread is available with odds 1.80-2.10, evaluate spread BEFORE ML as the primary market; current rules say evaluate both but don't prioritise spread in these scenarios.
- **Denver Nuggets' W12 regular season streak did not predict playoff performance (down 3-2 to MIN) — the Hot Streak Fade Rule in selectivity may need a playoff-specific override.** — The current Hot Streak Fade Rule is written for regular season hot streaks from non-elite teams; DEN is a legitimate elite team whose regular season W12 streak was rendered irrelevant by playoff-specific matchup factors (MIN defensive scheme, Edwards presence), suggesting the rule needs a 'playoff games override — weight in-series results only' clause. → Add a note to the Hot Streak Fade Rule in selectivity: 'In playoff phase, regular season streaks are NOT predictive — use in-series record exclusively; do not apply hot streak fade logic to playoff teams regardless of regular season L10.'
