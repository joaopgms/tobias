---
date: 2026-03-30
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (9 bets)
---

## Today's Analysis — 2026-03-30

Today's key structural update: Cleveland's injury situation is materially worse than previously captured — 5 confirmed roster-only absences including Jarrett Allen and Max Strus reduce their effective rotation depth significantly, warranting downgraded confidence on any CLE pick. The Philadelphia 76ers remain the most alarming fade candidate in the league with a -0.2 NetRtg on a 41-33 record — their L10 7-3 streak is almost certainly luck-driven and any opponent priced ≥ 1.75 deserves fade evaluation. Macro trend: the top-3 seeds (OKC, SAS, DET) are increasingly likely to rest starters with 5-6 games remaining, creating significant trap-game risk if those absences aren't captured in the injury feed before Scout drafts.

## Performance Stats
ALL-TIME: 2W / 7L | Win rate: 22.2% | P&L: €-629.99 | Avg odds: 1.99 | Avg conf: 65.1/100
RECENT 9: 2W / 7L | 22.2% WR | P&L: €-629.99
By market:      ML 4bets 1W/3L 25.0% €-200.36  |  SPREAD 3bets 1W/2L 33.3% €-245.36  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 1bets 0W/1L 0.0% €-225.00  |  Medium 7bets 2W/5L 28.6% €-304.99  |  Speculative 1bets 0W/1L 0.0% €-100.00
By odds range:  1.70-1.89 1bets 0W/1L 0.0% €-115.53  |  1.90-2.09 7bets 2W/5L 28.6% €-414.46  |  2.10-2.50 1bets 0W/1L 0.0% €-100.00



## Scout patches applied
- [franchise_player_rules] Updated to sync exactly with today's verified feed: Adou Thiero and Jaden McDaniels re-added (present in today's verified list), Jarrett Allen/Max Strus/Dean Wade restored for CLE (present in today's verified list), Tre Johnson and Alex Sarr removed from WAS (absent from today's verified feed), no other structural changes.
- [tanking_teams] Updated all standings, records, streaks, NetRtg values, and injury counts to match today's verified data feed; corrected NYK streak to L2, CLE injury count to 5, GSW NetRtg to 0.0, and removed stale Tre Johnson/Alex Sarr WAS references not in today's verified feed.

## Commit patches applied
None

## Intelligence gaps identified
- **The standings data shows Philadelphia 76ers at 41-33 with NetRtg -0.2, but the advanced stats section does not include bottom-tier teams like Sacramento, Brooklyn, Utah, Dallas, Memphis — making it impossible to confirm their NetRtg for betting-against purposes.** — When evaluating bets against confirmed tanking teams, Scout has no NetRtg data to quantify the actual edge magnitude, which could lead to over- or under-sizing confidence adjustments. → Expand the advanced stats feed to include all 30 teams ranked bottom-to-top so tanking team NetRtg gaps are quantifiable at pick time.
- **The current hot-streak fade rule triggers on W% < .550 overall, but does not account for teams whose recent schedule strength (SOS) was significantly below average, which could explain inflated L10 records without representing genuine regression risk.** — A team with L10 9-1 against weak opponents is a different fade candidate than one with L10 9-1 against playoff-level competition — the rule currently treats them identically, potentially producing false fade signals. → Add a SOS qualifier to the hot-streak fade rule: require that the L10 opponents have a combined W% ≥ .470 before applying the fade signal; if SOS data unavailable, note it as a confidence limiter.
- **The injury landscape section shows only three players explicitly (Trae Young, Kyshawn George, Anthony Davis) but the verified franchise player feed contains 30+ absences — the two sources are not reconciled in a way that flags when the official injury PDF is confirming fewer players than the roster-only feed expects.** — If the official PDF is routinely confirming far fewer absences than the roster-only feed, Scout may be applying conservative confidence penalties to players who are actually active, reducing pick volume unnecessarily. → Add a reconciliation note to data_quality_rules: if official PDF confirms < 50% of roster-only flagged absences, treat remaining roster-only flags as GTD rather than OUT and apply the Questionable/GTD confidence penalty (-10) rather than the OUT rule.
