---
date: 2026-05-29
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (44 bets)
---

## Today's Analysis — 2026-05-29

WCF Game 7 at OKC is the sole active game — OKC holds compound edge via home court (+3-4pts), superior season NetRtg (+2.8pts over SAS), and historical Conference Finals home win rate (~60-65%); the primary structural bet remains OKC ML at odds ≥ 1.55 or spread if accessible near -5/-6. Key integrity flag this session: Jalen Williams does NOT appear in the current verified injury feed, meaning his OUT status must be re-confirmed from the NBA official PDF before Scout drafts — if he is now active, OKC's ceiling rises and the spread line will likely tighten. NYK's extended rest advantage (6-10 days before Finals Game 1) is building into the strongest structural edge on the horizon, and should be front-loaded into Finals Game 1 analysis regardless of which WCF team advances.

## Performance Stats
ALL-TIME: 32W / 30L | Win rate: 51.6% | P&L: €+238.12 | Avg odds: 1.94 | Avg conf: 65.4/100
RECENT 20: 12W / 8L | 60.0% WR | P&L: €+730.62
By market:      ML 25bets 12W/13L 48.0% €-289.43  |  SPREAD 29bets 16W/13L 55.2% €+592.70  |  TOTAL 8bets 4W/4L 50.0% €-65.15
By confidence:  High 19bets 8W/11L 42.1% €-659.52  |  Medium 40bets 24W/16L 60.0% €+1258.55  |  Speculative 3bets 0W/3L 0.0% €-360.91
By odds range:  1.70-1.89 21bets 11W/10L 52.4% €-382.39  |  1.90-2.09 36bets 20W/16L 55.6% €+782.12  |  2.10-2.50 5bets 1W/4L 20.0% €-161.61



## Scout patches applied
- [franchise_player_rules] Current verified list does NOT include Jalen Williams — removing him from OKC entry to comply with HARD CONSTRAINT; all other player entries remain consistent with verified feed, and playoff phase notes updated to reflect Game 7 winner-take-all status.

## Commit patches applied
None

## Playoff context patches applied
- [phase] Removing Jalen Williams reference from phase section as he is not in the current verified injury feed — agents must not carry forward unverified absences.
- [series_context] Removing unverified Jalen Williams OUT reference from authoritative series_context and flagging need for re-verification per current session's verified injury feed.
- [elimination_flags] No structural changes to elimination flags required; kept current and consistent with verified feed data.
- [playoff_rest] No changes to rest logic required this session; content remains accurate for Game 7 context.
- [h2h_playoff] Updating h2h_playoff to flag Jalen Williams OUT status as needing re-verification since he is absent from current verified feed, while preserving all other accurate series intelligence.
- [l15_caveat] Correcting all Jalen Williams references to flag re-verification requirement since he does not appear in current verified injury feed, preserving all other accurate playoff framing.
- [playoff_motivation] Updating all Jalen Williams references to require re-verification rather than stating confirmed OUT status, as he is not present in the current session's verified injury feed.

## Intelligence gaps identified
- **Jalen Williams (OKC) was listed as OUT [roster-only] in prior sessions but does NOT appear in today's verified injury feed — his current status is unconfirmed** — If Williams is now active, OKC's execution ceiling rises meaningfully for Game 7, the spread line tightens, and any spread pick drafted at current prices could be at stale odds; if still OUT, the existing framing holds → Scout MUST query NBA official PDF immediately before drafting any WCF Game 7 pick and explicitly confirm Williams status — if active, adjust OKC spread confidence upward by +5 and note in pick reasoning
- **Los Angeles Lakers Round 2 series status, opponent, and current score are unverified in today's data feed** — Without knowing LAL's series score and opponent, Scout cannot evaluate rest days, elimination urgency, or home court advantage for any potential LAL pick → Add explicit LAL Round 2 series data to the ESPN live feed input — or instruct Scout to skip LAL picks entirely until series_context is confirmed from ESPN bracket
- **No performance data exists yet for Game 7 playoff picks specifically — the system has never bet a Conference Finals Game 7** — Game 7s have unique dynamics (maximum motivation both sides, home court amplified, elimination stress) that may not be fully captured by regular-season or earlier-round patterns in current rules → After Game 7 settles, tag the pick with a 'game7_conf_finals' label and track separately — if 3+ Game 7 bets settle, analyse whether home-court edge is being correctly priced relative to current 1.55 OKC floor
