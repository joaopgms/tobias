---
date: 2026-04-11
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (8 bets)
---

## Today's Analysis — 2026-04-11

Denver Nuggets have now extended their winning streak to 11 games (L10: 10-0, NetRtg +5.1) — the hot-streak auto-fade rule correctly does not apply at .654 W%, but any opponent bet requires NetRtg gap > 4.0 to justify fading Denver. The Washington Wizards remain the clearest fade in the league with multiple franchise players confirmed OUT via injury landscape cross-reference. Charlotte Hornets (streak: L2) and Miami Heat (L10: 4-6) are the primary cold-team fade candidates this session; the late-season rest dynamic at OKC, SAS, and DET means those franchises must be treated as unverified until NBA official PDF confirmation on any given day.

## Performance Stats
ALL-TIME: 11W / 15L | Win rate: 42.3% | P&L: €-394.64 | Avg odds: 1.98 | Avg conf: 65.5/100
RECENT 20: 10W / 10L | 50.0% WR | P&L: €+147.12
By market:      ML 12bets 5W/7L 41.7% €-256.91  |  SPREAD 11bets 5W/6L 45.5% €-114.46  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 8bets 3W/5L 37.5% €+32.90  |  Medium 16bets 8W/8L 50.0% €-286.23  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 6bets 3W/3L 50.0% €-67.95  |  1.90-2.09 17bets 8W/9L 47.1% €-97.38  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Updated franchise_player_rules to match ONLY verified names from the current ESPN+NBA injury feed cross-reference, removing players no longer in the verified absence list (SGA, Jalen Williams, Chet Holmgren, Isaiah Hartenstein, Marcus Smart, Jarrett Allen, Sam Merrill, Donovan Mitchell, Jaylon Tyson, Anthony Edwards, Rudy Gobert, Joe Ingles, Alex Caruso, Isaiah Joe, Ajay Mitchell, Cason Wallace, Jaylin Williams) and adding newly confirmed Jaxson Hayes for LAL.
- [tanking_teams] Updated all standings, streaks, and NetRtg figures to current session data; corrected LAL absences to verified list only (added Jaxson Hayes, removed Marcus Smart who is not in verified feed); removed stale OKC mass-absence note since those players are not in current verified feed.

## Commit patches applied
None

## Intelligence gaps identified
- **The current verified absence feed shows significantly fewer players than the prior session's franchise_player_rules — multiple high-profile names (SGA, Jalen Williams, Chet Holmgren, Donovan Mitchell, Jarrett Allen, Anthony Edwards, Rudy Gobert) have dropped out of the verified list entirely, creating uncertainty about whether they are now active or simply not captured by today's feed.** — If these players are genuinely active, prior picks that avoided their teams due to absence flags may have missed value; conversely if they are still resting, Scout could incorrectly back those teams. → Prioritise NBA official PDF pull at Scout time specifically for OKC, CLE, MIN, and LAL — these four teams have the highest franchise-player uncertainty this session and the most material impact on pick selection.
- **Odds range 2.10–2.50 shows 0W/3L (0%) across all-time bets, accounting for the largest P&L loss segment at €-229.31 despite only 3 bets.** — If picks in the 2.10–2.50 range systematically underperform, the current odds_targets ceiling of 2.50 may be too permissive and is concentrating outsized losses in a thin sample. → Monitor this range closely — with only 3 bets the sample is insufficient to patch (threshold requires confidence ≥ 0.70 which is not met at n=3), but flag Scout to apply extra EV scrutiny for any pick above 2.10 until sample reaches 8-10 bets.
- **Speculative tier (conf 50-54) shows 0W/2L at €-141.31, suggesting speculative picks are generating outsized losses relative to the stated 10% stake tier.** — Two speculative losses already exceed the expected loss magnitude for a 10% stake tier, indicating either the EV calculation is optimistic for low-confidence picks or the odds accessed were consistently at the ceiling of the valid range. → Review whether speculative picks have been taken at odds near 2.10-2.50 (the underperforming range) — if so, add a rule that speculative-tier picks require odds ≤ 2.00 to limit downside, since low confidence + high odds = compounded variance.
- **No L15 NetRtg data appears in today's prompt despite priority_stats listing it as the primary directional signal — the advanced stats feed shows only season-level OffRtg/DefRtg/NetRtg/Pace.** — Without L15 NetRtg, Scout must fall back to season NetRtg as primary signal, which is less predictive for late-season games where form has diverged from season average (e.g. Denver at W11 streak, Miami at L10 4-6). → Confirm whether the L15 NetRtg computation from ESPN game logs is being passed to Scout's prompt; if not, the priority_stats section directing Scout to use L15 as PRIMARY is creating false confidence in a signal that isn't actually available.
