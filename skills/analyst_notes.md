---
date: 2026-03-22
llm: claude-sonnet-4-6
scout_patches: 3
commit_patches: 1
milestone: daily (2 bets)
---

## Today's Analysis — 2026-03-22

Today's standout factual updates: the Atlanta Hawks' historic 11-game win streak has ended (now W1), validating the regression-fade thesis that was flagged last session — this is evidence the HOT STREAK FADE RULE works and should be retained. The Lakers (W9, NetRtg +1.4) are now the primary regression candidate with a similar profile: elite recent record masking a weak underlying rating. Macro trend: Pace data is 0.0 for all 30 teams in the current feed, meaning O/U pace-based signals are completely suppressed this session and any totals pick is higher risk; Scout and Commit now have an explicit gate for this. OKC's Jalen Williams absence alongside a W11 streak creates a genuine line tension — books may be pricing the streak rather than the injury, watch for value on OKC opponents at inflated odds.

## Performance Stats
ALL-TIME: 0W / 2L | Win rate: 0.0% | P&L: €-325.00 | Avg odds: 2.14 | Avg conf: 66.5/100
RECENT 2: 0W / 2L | 0.0% WR | P&L: €-325.00
By market:      ML 1bets 0W/1L 0.0% €-100.00  |  SPREAD 1bets 0W/1L 0.0% €-225.00
By confidence:  High 1bets 0W/1L 0.0% €-225.00  |  Speculative 1bets 0W/1L 0.0% €-100.00
By odds range:  1.90-2.09 1bets 0W/1L 0.0% €-225.00  |  2.10-2.50 1bets 0W/1L 0.0% €-100.00



## Scout patches applied
- [franchise_player_rules] Verified franchise player list updated to match current ESPN roster cross-reference: removed Aaron Gordon, Isaiah Hartenstein, Luguentz Dort, Jae'Sean Tate (not in verified list); added Landry Shamet (NYK) and Naz Reid (MIN); Grayson Allen (PHX) added per verified feed.
- [tanking_teams] Standings materially updated: OKC now 56-15 (W11), Spurs 53-18, Pistons 51-19, Lakers 46-25 (W9); Atlanta Hawks streak ended (now W1 after L10:9-1 run), Lakers' NetRtg +1.4 vs 46-25 record flags strong regression risk; Golden State L10:2-8 now tank-watch level.
- [data_quality_rules] Pace = 0.0 for all 30 teams in the current advanced stats feed is a confirmed data quality issue that would cause Scout to misapply pace-based O/U signals; adding an explicit gate prevents bad totals picks.

## Commit patches applied
- [data_quality_rules] Keeping commit data_quality_rules in sync with scout patch adding the Pace=0.0 quality gate to prevent confirming totals picks built on missing pace data.

## Intelligence gaps identified
- **Pace = 0.0 for all 30 teams universally — this is a data pipeline issue, not a genuine stat value.** — Scout's O/U signals (lean Over when both Pace > 100, lean Under when both < 97) and pace mismatch rules are completely inoperative when pace data is missing; any totals pick drafted today would be flying blind on pace. → Data pipeline fix needed: ensure Pace per-possession (or pace proxy from game tempo logs) is fetched and populated before Scout runs. This session's gate patch mitigates the risk but the root data fetch should be corrected upstream.
- **No L15 NetRtg data present in today's prompt despite priority_stats listing it as the primary directional signal.** — Scout is instructed to use L15 NetRtg as the PRIMARY signal ahead of season NetRtg, but the advanced stats table shows only season-level ratings — if L15 is systematically missing, Scout is always falling back to the secondary signal and applying confidence -5, which may be suppressing valid picks. → Flag to data pipeline: verify L15 NetRtg computation from ESPN game logs is running correctly and surfacing in the daily context. If consistently absent, consider promoting season NetRtg with L10 record as joint primary signal until L15 feed is restored.
- **Lakers hot streak (W9, NetRtg +1.4) mirrors the Atlanta Hawks pattern that preceded a correct regression fade, but the HOT STREAK FADE RULE only explicitly names Atlanta as an example.** — Scout may not automatically apply the fade rule to the Lakers without an explicit current example in the selectivity section, missing a high-confidence regression opportunity in upcoming Lakers games. → The tanking_teams patch already adds Lakers as a HOT STREAK FADE CANDIDATE with explicit language — this gap is addressed by today's patch. Monitor Lakers opponents' odds over the next 5-7 games for fade opportunities.
