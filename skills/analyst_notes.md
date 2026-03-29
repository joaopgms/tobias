---
date: 2026-03-29
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (8 bets)
---

## Today's Analysis — 2026-03-29

Performance remains deeply negative (2W/6L, -€564.69) with totals (0W/2L) and high-confidence bets (0W/1L) the worst performers — the data sample is still too small (8 bets) to patch strategic sections, but the pattern of losses across all markets suggests edge identification rather than execution is the core problem. Two extreme anomalies in today's standings warrant Scout attention: Philadelphia 76ers sit at 41-33 with NetRtg -0.2 (historically rare — implies extreme positive variance in close games, very high regression risk), and the Lakers at 48-26 with NetRtg +1.7 remain the clearest hot-streak-fade candidate in the league. Pace = 0.0 persists across most teams in the advanced stats feed (only a handful reporting), confirming the pace data pipeline issue flagged last session remains unresolved — O/U pace signals must remain suppressed.

## Performance Stats
ALL-TIME: 2W / 6L | Win rate: 25.0% | P&L: €-564.69 | Avg odds: 1.99 | Avg conf: 65.8/100
RECENT 8: 2W / 6L | 25.0% WR | P&L: €-564.69
By market:      ML 3bets 1W/2L 33.3% €-135.06  |  SPREAD 3bets 1W/2L 33.3% €-245.36  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 1bets 0W/1L 0.0% €-225.00  |  Medium 6bets 2W/4L 33.3% €-239.69  |  Speculative 1bets 0W/1L 0.0% €-100.00
By odds range:  1.70-1.89 1bets 0W/1L 0.0% €-115.53  |  1.90-2.09 6bets 2W/4L 33.3% €-349.16  |  2.10-2.50 1bets 0W/1L 0.0% €-100.00



## Scout patches applied
- [franchise_player_rules] Updated to reflect current verified feed: Tre Johnson and Alex Sarr confirmed via injury landscape, Jaden McDaniels removed as not in current verified feed, Washington Wizards roster updated with all confirmed absences.
- [tanking_teams] Updated standings to reflect current data (Spurs 56-18 W8 streak, Pistons 54-20, Hornets 39-35 streak broken, Nuggets 47-28 W5 added), Atlanta Hawks fade threshold now clearly triggered at W%~.560, Philadelphia flagged as extreme regression candidate with NetRtg -0.2 at 41-33.

## Commit patches applied
None

## Intelligence gaps identified
- **Philadelphia 76ers have a 41-33 record with NetRtg -0.2 — one of the most extreme record/NetRtg divergences in the league this season — but no specific fade rule exists for teams with positive records AND negative NetRtg.** — A team with negative NetRtg and a winning record is almost certainly overperforming in close games and will regress; betting against them at reasonable odds is a systematic edge that current rules only partially capture via the hot-streak-fade rule. → Add a specific flag in selectivity or market_rules: 'If team W% > .530 AND season NetRtg < 0.0, treat as regression candidate equivalent to hot-streak-fade — require opponent odds ≥ 1.75 and apply +10 confidence to fade.' Confidence in this logic: 0.75 — act on it.
- **Pace = 0.0 for the majority of teams in the advanced stats feed has persisted across multiple sessions, suggesting a data pipeline issue rather than a one-off gap.** — Without pace data, O/U signals are suppressed and confidence floors are raised, reducing pick volume and edge identification on totals — a market that could be profitable with full data. → Flag as data pipeline fix needed: fetch Pace from a secondary source (Basketball-Reference or NBA.com team stats page) to supplement the primary feed. Cannot patch rules to fix this — requires infrastructure change.
- **Current rules have no explicit handling for teams in top-3 seed positions (OKC 58-16, Spurs 56-18, Pistons 54-20) that have clinched seeding and may begin systematic rest rotation in the final 2-3 weeks of the regular season.** — A star rest game for a clinched top-3 seed dramatically changes the ML/spread calculation — without a rule flagging this risk, Scout may draft picks against rested opponents without knowing the top seed is fielding a B-squad. → Add to selectivity or tanking_teams: 'For teams that have clinched top-3 seed with 5 or fewer games remaining, treat any home/away game as high rest-risk — require NBA official lineup confirmation before any pick on that team. Apply confidence -20 if lineup not confirmed by Scout time.' Confidence: 0.8 — should be patched.
- **Totals market is 0W/2L (-€184.27) but with only 2 settled bets, it is impossible to determine whether the losses stemmed from pace data absence, incorrect confidence calibration, or genuine market difficulty.** — The 0% win rate on totals may justify raising the confidence floor further or banning totals entirely during pace-data-unavailable sessions, but 2 bets is insufficient evidence to patch strategically. → Track next 3 totals bets with explicit logging of: (a) whether pace data was available, (b) which signal triggered the pick (pace vs OffRtg/DefRtg). After 5 total settled bets, re-evaluate the totals confidence floor with actual evidence.
