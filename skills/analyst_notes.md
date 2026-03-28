---
date: 2026-03-28
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (7 bets)
---

## Today's Analysis — 2026-03-28

Standings update confirms OKC (58-16), Spurs (55-18), and Pistons (53-20) are in full rest-management territory — any of these teams' star players could be rested on short notice, creating late line-movement risk. The Lakers regression thesis remains active: NetRtg +1.7 is dramatically below their 48-26 record, and their L10 9-1 run at low efficiency suggests luck regression is overdue. Minnesota's Anthony Edwards absence combined with a +3.6 NetRtg team suggests they are genuinely vulnerable as favourites right now — verify before any pick. ML market is 0-for-2 lifetime and spread 1W/2L; the sample (7 bets total) is too small to make strategic rule changes, but the pattern of backing higher-confidence picks at medium odds not converting warrants continued monitoring.

## Performance Stats
ALL-TIME: 1W / 6L | Win rate: 14.3% | P&L: €-610.50 | Avg odds: 1.99 | Avg conf: 65.9/100
RECENT 7: 1W / 6L | 14.3% WR | P&L: €-610.50
By market:      ML 2bets 0W/2L 0.0% €-180.87  |  SPREAD 3bets 1W/2L 33.3% €-245.36  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 1bets 0W/1L 0.0% €-225.00  |  Medium 5bets 1W/4L 20.0% €-285.50  |  Speculative 1bets 0W/1L 0.0% €-100.00
By odds range:  1.70-1.89 1bets 0W/1L 0.0% €-115.53  |  1.90-2.09 5bets 1W/4L 20.0% €-394.97  |  2.10-2.50 1bets 0W/1L 0.0% €-100.00



## Scout patches applied
- [franchise_player_rules] Updated to reflect current verified feed: Jaden McDaniels added to Timberwolves, Cam Whitmore confirmed on Wizards, Adou Thiero/Jarrett Allen/Dean Wade/Tre Johnson removed as they do not appear in today's verified roster cross-reference.
- [tanking_teams] Updated all standings/records/streaks/L10s to match current data feed; corrected Lakers record to 48-26, GSW to 36-38, Cavaliers to 46-28 with revised injury picture; updated Atlanta Hawks streak to L1 with fade candidate note.

## Commit patches applied
None

## Intelligence gaps identified
- **Pace data is showing 0.0 for the majority of teams in the advanced stats feed (OKC, Detroit, Spurs all show 0.0), while only some teams have valid Pace readings** — The data_quality_rules Pace flag triggers only when ALL teams show 0.0, but a partial 0.0 situation (top teams missing Pace) still corrupts O/U pace-mismatch analysis for those specific matchups → Add a per-matchup Pace data check: if EITHER team in a matchup has Pace = 0.0, suppress pace-based O/U signals for that specific game rather than requiring all 30 teams to show 0.0 before triggering the flag
- **No tracking of home/away NetRtg splits — season NetRtg is used but teams like Lakers (+1.7 overall) may have dramatically different home vs away profiles** — A team with +1.7 season NetRtg could be +5.0 at home and -1.5 away, which would change spread and ML confidence materially — current rules use blended NetRtg and may misprice home/away matchups → Add home_netrtg and away_netrtg to priority_stats context when available; flag in intelligence gap until data pipeline can supply home/away splits separately
- **ML market is 0W/2L (0%) with €-180 loss but no rule currently distinguishes between ML picks where the edge was stat-driven vs seeding/motivation-driven** — If ML losses are concentrated in motivation or seeding picks (harder to quantify) vs pure NetRtg picks, the confidence floor for ML could be raised selectively for motivation-only theses → Tag each ML pick at draft time with primary_edge_type (netrtg / b2b / motivation / injury / streak_fade) so future analysis can identify which ML signal types are underperforming; flag for 10-bet threshold review
- **Toronto Raptors (41-32, L10: 5-5) have Immanuel Quickley OUT [roster-only] but their NetRtg +1.5 and play-in position makes them a potential fade target — no current rule explicitly flags teams in the play-in bubble who are also missing a franchise player as double-fade candidates** — A play-in team missing a franchise player faces compounded pressure — the motivation boost may not offset the talent deficit, and books may be slow to price both factors together → Add to selectivity or market_rules: when a play-in bubble team (seeds 7-10) is missing their franchise player [roster-only or confirmed OUT], treat opponent ML as a candidate edge even at sub-2.00 odds, provided NetRtg gap favours opponent by ≥ 3.0
