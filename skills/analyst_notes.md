---
date: 2026-03-31
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (11 bets)
---

## Today's Analysis — 2026-03-31

The verified injury feed shows a significant reset this session — 10 players previously listed as [roster-only] OUT (including Hartenstein, J.Williams, Jalen Duren, Jarrett Allen, Max Strus, Alex Sarr, Bilal Coulibaly) are no longer in the cross-reference, which materially changes confidence assessments for OKC, Detroit, Cleveland, and Washington picks; Scout must re-verify all four rosters before drafting. Performance remains deeply negative (36.4% WR, -€522 P&L across 11 bets) with totals the worst market (0-2, -€184) — the O/U confidence floor of 65 and pace data gate remain appropriate defences but Scout should treat totals as last-resort only until the sample improves. The Lakers (NetRtg +1.9 behind a 49-26 record) and Philadelphia (NetRtg -0.3 at 41-34) remain the strongest regression-fade candidates heading into the final weeks of the regular season.

## Performance Stats
ALL-TIME: 4W / 7L | Win rate: 36.4% | P&L: €-522.32 | Avg odds: 1.99 | Avg conf: 64.4/100
RECENT 11: 4W / 7L | 36.4% WR | P&L: €-522.32
By market:      ML 5bets 2W/3L 40.0% €-141.53  |  SPREAD 4bets 2W/2L 50.0% €-196.52  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 1bets 0W/1L 0.0% €-225.00  |  Medium 9bets 4W/5L 44.4% €-197.32  |  Speculative 1bets 0W/1L 0.0% €-100.00
By odds range:  1.70-1.89 2bets 1W/1L 50.0% €-66.69  |  1.90-2.09 8bets 3W/5L 37.5% €-355.63  |  2.10-2.50 1bets 0W/1L 0.0% €-100.00



## Scout patches applied
- [franchise_player_rules] Verified franchise player feed has changed materially — multiple prior [roster-only] absences (Hartenstein, J.Williams, Duren, T.Harris, D.Robinson, Thiero, J.Allen, Strus, Coulibaly, Sarr) are no longer in the current cross-reference and must be removed; updated list reflects only names in today's verified feed.
- [tanking_teams] Verified injury feed changed materially — multiple prior absences dropped from confirmed list requiring updated roster flags, seeding positions updated, and tanking/hot-streak assessments refreshed to match current standings and streaks.

## Commit patches applied
None

## Intelligence gaps identified
- **Totals market is 0-2 (-€184, 100% loss rate) but the sample is too small to distinguish bad signals from variance — no granular data on whether losses came from Over or Under bets, or which pace/OffRtg conditions were present.** — If both losses were Overs in slow-pace games or Unders in fast-pace games, a directional tightening of the O/U signal criteria would be warranted; without this breakdown, any patch risks overcorrecting. → Log each settled total bet with market direction (Over/Under), both teams' Pace at draft time, and final score vs line — after 5 settled totals, run a directional audit.
- **Multiple high-profile players (Jalen Williams OKC, Jarrett Allen CLE, Alex Sarr WAS, Isaiah Hartenstein OKC) dropped out of the verified injury feed this session with no explanation — it is unclear whether they have returned to active status or the feed simply lost coverage.** — If Jalen Williams is now active for OKC, the franchise player gate currently blocking OKC ML bets should be lifted; if Allen returned for Cleveland, the depth-concern flag overstates the risk. → Add an explicit rule to data_quality_rules: when a previously [roster-only] OUT player disappears from the verified feed, treat their status as UNKNOWN (not Active) and require NBA official PDF confirmation before removing the absence flag — do not silently assume return to play.
- **The spread market is 2W-2L (50% WR, -€196) with no breakdown by which spread signal type drove each pick — NetRtg gap, B2B, or DefRtg gap — making it impossible to identify if any specific spread signal is underperforming.** — A 50% win rate on spreads at roughly -0.10 vig odds is a losing proposition long-term; if one signal type (e.g. DefRtg gap > 8) is responsible for both losses, it should be tightened. → Tag each settled spread bet with the primary signal that justified it (NetRtg gap / B2B / DefRtg / tank-fade) so future Analyst sessions can audit by signal type after 8-10 spread bets.
- **The high-confidence tier (85-100) is 0W-1L (0%, -€225) on a single bet — the staking rules allow up to 30% of bankroll at this tier, which represents maximum risk exposure, yet the only high-conf bet lost.** — One loss is not a pattern, but at 30% bankroll exposure a single failure at this tier costs disproportionately; the question is whether Scout is calibrating 85+ confidence correctly given the overall 36.4% WR. → After 5 elite-tier bets are settled, audit calibration: if win rate is below 60% at the 85-100 tier, reduce the max stake to 20% and raise the EV floor for that tier to 0.10.
