---
date: 2026-04-17
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (11 bets)
---

## Today's Analysis — 2026-04-17

Play-in tournament has not yet officially begun and matchups remain unannounced — Scout must verify the official schedule before drafting any picks today. The most notable roster data change this session is that Mike Conley and Rudy Gobert no longer appear in Minnesota's verified absence feed, which may slightly improve MIN's play-in outlook, but their statuses still require NBA official PDF confirmation before any pick. Performance-wise, the recent 20-bet sample is encouraging (60% WR, +€764.56) with spreads (+€258.12, 53.8%) outperforming ML (46.2%, -€100.28), reinforcing the existing spread-first evaluation instruction — the 2.10–2.50 odds range remains a hard avoid at 0W/3L.

## Performance Stats
ALL-TIME: 14W / 15L | Win rate: 48.3% | P&L: €+134.57 | Avg odds: 1.97 | Avg conf: 64.8/100
RECENT 20: 12W / 8L | 60.0% WR | P&L: €+764.56
By market:      ML 13bets 6W/7L 46.2% €-100.28  |  SPREAD 13bets 7W/6L 53.8% €+258.12  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 8bets 3W/5L 37.5% €+32.90  |  Medium 19bets 11W/8L 57.9% €+242.98  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 7bets 4W/3L 57.1% €+88.68  |  1.90-2.09 19bets 10W/9L 52.6% €+275.20  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Updated MIN section to reflect that Mike Conley and Rudy Gobert no longer appear in the current verified absence feed, removing them from the OUT list while flagging they require re-verification; all other entries synced to current verified feed.
- [tanking_teams] Updated session date reference and synced MIN entry to reflect Gobert/Conley status change in verified absence feed.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] Updated session date, added MIN Gobert/Conley status change note, and flagged Denver seeding anomaly for Scout awareness.
- [elimination_flags] Updated session date; content unchanged as no play-in games have been played yet and no new elimination results exist.
- [h2h_playoff] Updated session date; no play-in games have concluded so H2H records remain unpopulated pending official matchup announcement.

## Intelligence gaps identified
- **Odds range 2.10–2.50 has produced 0W/3L (-€229.31) with zero recovery — the current rules only apply a general EV floor but do not restrict this range specifically.** — Three bets at this range have all lost; at these odds the implied probability is ~40–48%, and our models may be systematically overconfident on longer-priced underdogs during the play-in phase. → Consider adding a soft ceiling of 2.09 on ML picks during play-in/playoff phase, or raising the confidence floor to 68+ for any ML bet in the 2.10–2.50 range. Confidence in this patch is 0.65 — just below the 0.70 threshold given only 3 bets.
- **High confidence bets (85–100, 70–84) are underperforming at 37.5% WR vs medium confidence at 57.9% — staking structure rewards high-confidence with larger stakes but the win rate does not support it.** — The 8 high-confidence bets have produced only 3W/5L at +€32.90, barely breaking even on larger stakes — medium confidence at 19 bets is generating significantly better returns per bet. → After reaching 20+ bets in the high-confidence tier (currently 8), consider compressing the staking gap between high and medium tiers. Not patching now — sample is only 8 bets and the 20-bet minimum for staking changes has not been met.
- **West play-in 10-seed is listed as TBD — if it is a team with franchise players in the roster-only OUT feed, GSW matchup pricing may be significantly mispriced.** — GSW is already the strongest fade candidate at 37-45 with L3 and negative NetRtg; if they face a deeply depleted 10-seed, the fade signal inverts entirely and backing GSW at play-in odds could offer value. → Infrastructure fix required — Scout needs official West 10-seed confirmation from NBA.com before any GSW play-in pick can be drafted. No rule patch needed; flagging for Scout awareness.
