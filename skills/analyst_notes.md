---
date: 2026-04-24
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (24 bets)
---

## Today's Analysis — 2026-04-24

Key update this session: Jalen Williams (OKC) has entered the verified absence feed as OUT [roster-only], which is significant for the #1 West seed entering the play-in/playoffs — re-verification via NBA official PDF is mandatory before any OKC pick, and the absence materially affects OKC's ceiling despite their +11.1 NetRtg. Performance data shows a sharp High-confidence bet problem: the system is 5W/9L (35.7%) at High confidence tier, producing -€816 — this is the primary drag on overall P&L and warrants close monitoring, though the 20-bet minimum for strategic patches has not been crossed for a clean pattern. The 1.70-1.89 odds range is also -€766 on 13 bets (46.2%), suggesting the system may be slightly over-confident on chalk picks; ML market is underperforming spreads significantly (ML 44.4% vs SPREAD 52.4%), which supports the existing guidance to prioritise spread evaluation.

## Performance Stats
ALL-TIME: 20W / 22L | Win rate: 47.6% | P&L: €-492.50 | Avg odds: 1.95 | Avg conf: 65.8/100
RECENT 20: 11W / 9L | 55.0% WR | P&L: €-93.26
By market:      ML 18bets 8W/10L 44.4% €-502.09  |  SPREAD 21bets 11W/10L 52.4% €+32.86  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 14bets 5W/9L 35.7% €-816.09  |  Medium 26bets 15W/11L 57.7% €+464.90  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 13bets 6W/7L 46.2% €-766.44  |  1.90-2.09 25bets 13W/12L 52.0% €+215.95  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Updated OKC section to reflect Jalen Williams now appearing as OUT [roster-only] in the verified absence feed; added Jordan McLaughlin (SAS) and Keshon Gilbert (ATL) who were in the verified feed but missing from prior rules; removed Thomas Bryant (CLE) who does not appear in current verified feed.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] Updated to reflect new session date (2026-04-30), Jalen Williams now appearing as OUT [roster-only] in OKC's verified absence feed, Jordan McLaughlin (SAS) and Keshon Gilbert (ATL) additions to verified absence feed.
- [elimination_flags] Added OKC roster alert (Jalen Williams now OUT [roster-only]) and updated playoff first-round risk flags for LAL and HOU; kept play-in flags consistent with prior session.
- [h2h_playoff] Updated caveat date and OKC roster alert (Williams now OUT [roster-only]); all H2H records remain unpopulated pending official matchup announcements.

## Intelligence gaps identified
- **High-confidence bets (70-84) are 5W/9L (35.7%, -€816) — the worst-performing confidence tier by far — but the sample is 14 bets, just below the 20-bet threshold for strategic patching.** — If the pattern holds, the High confidence tier is generating negative EV in practice despite passing the 5% EV floor; the system is likely over-confident on short-priced chalk picks in the 1.70-1.89 range where 46.2% win rate produces -€766. → At 20 bets in the High tier, evaluate whether to raise the confidence floor to 75 for High-tier classification or require EV ≥ 0.08 at odds < 1.90 to compensate for variance. Flag in next milestone review.
- **ML market is 8W/10L (44.4%, -€502) vs SPREAD 11W/10L (52.4%, +€33) — a material divergence suggesting ML picks are being taken at insufficient edge while spread picks are performing above expectation.** — If this pattern reflects a systematic over-reliance on ML for games where spread is the better market, tightening ML confidence floors (or requiring EV ≥ 0.08 specifically for ML in the 1.70-1.89 range) could shift selection toward better-performing markets. → At 25 settled ML bets, consider raising ML confidence floor from 50 to 55 and requiring EV ≥ 0.08 for ML picks at odds < 1.90. Monitor 5 more ML bets before patching.
- **West 10-seed for play-in is listed as TBD — this creates a gap in GSW's elimination_flags and h2h_playoff sections where the opponent is unknown.** — Without knowing the West 10-seed, Scout cannot properly evaluate GSW's play-in game — H2H record, roster status, and NetRtg gap are all unknown, making any GSW play-in pick potentially uninformed. → Require infrastructure/data pipeline to confirm West 10-seed via official NBA standings feed before any GSW play-in pick is drafted. This is a data fetch requirement, not a rule patch.
- **Keshon Gilbert (ATL) was in the verified absence feed this session but was missing from the prior franchise_player_rules entry for Atlanta — suggesting the absence feed may add players between sessions without Analyst catching them.** — If Scout evaluates an ATL game without knowing Gilbert is OUT, it may overestimate ATL's depth and confidence on ATL-related picks. → Already patched this session (Gilbert added to ATL franchise_player_rules). Going forward, perform a diff between the current and prior verified absence lists at the start of each session to catch newly added names.
