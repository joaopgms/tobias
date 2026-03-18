---
date: 2026-03-18
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
---

## Today's Analysis — 2026-03-18

This is session 1 with zero settled bets, so no strategic patches are warranted — factual updates only. Two standout injury flags: Jalen Williams (OKC) and Anthony Edwards (Minnesota) are both listed OUT via roster-only sources, which would materially shift lines for the NBA's #1 seed and a playoff contender respectively — Scout must verify these via the NBA official PDF before drafting any picks involving those teams. The Atlanta Hawks' L10 10-0 streak is the most exploitable pattern in the current market: their .544 overall W% implies regression is overdue, and any opponent priced at ≥ 1.80 against Atlanta warrants explicit fade evaluation under the HOT STREAK FADE RULE.



## Scout patches applied
- [franchise_player_rules] Verified franchise player absence list updated from ESPN roster + NBA injury feed cross-reference; prior session had stale/incomplete player list and did not reflect Jalen Williams, Anthony Edwards, or multiple secondary absences now confirmed on rosters.
- [tanking_teams] Standings updated to reflect current W-L records, streaks, and L10 data from feed; Wizards streak extended to L13 and multiple player absences confirmed; OKC record corrected to 54-15; Lakers hot streak now W6 noted.

## Commit patches applied
None

## Intelligence gaps identified
- **Advanced stats (OffRtg, DefRtg, NetRtg, Pace) are unavailable this session for all 30 teams.** — Without these, Scout cannot bet spreads or totals per data_quality_rules, and NetRtg L15 — the #1 priority stat — cannot be calculated, significantly reducing pick volume and edge detection. → Ensure the advanced stats pipeline fetches from NBA.com/stats or Basketball-Reference before Scout runs at 14:00; if unavailable again, log 'ML-only session — advanced stats missing' explicitly in scout_report and enforce the spreads/totals ban.
- **The NBA official injury PDF produced zero corroborated entries this session — all absences are roster-only flags with no PDF confirmation.** — Roster-only statuses are lower confidence than PDF-confirmed; franchise player rules instruct Scout to verify via PDF, but if the feed consistently returns empty, Scout may be operating blind on true injury status for high-impact players like Jalen Williams and Anthony Edwards. → Add a data_quality_rules gate: if nba_official PDF returns 0 confirmed entries AND espn roster-only list has > 5 players flagged, treat session as ESPN-fallback quality (confidence CAP 50, spreads/totals banned) until at least one source corroborates a status.
- **No home/away split data is available for any team this session, despite it being listed as priority_stats item #7.** — Home court advantage is worth ~2-3 points in close matchups (NetRtg gap < 3), and without split data Scout cannot distinguish teams that dramatically over/underperform at home vs on the road. → Add home/away W% splits to the daily data fetch; flag in scout_report when this stat is absent and require NetRtg L15 gap > 5 (instead of the usual < 3 tiebreaker threshold) before factoring home court into confidence.
- **No schedule density data (games_l7, B2B flags) is present in today's context for upcoming games.** — B2B rules apply a -20 confidence adjustment for true back-to-backs, which is the largest single adjustment in the system — missing this data means Scout could draft a pick on a B2B road team without the penalty applied. → Ensure the daily data fetch includes each team's next-3-days schedule with rest day counts before Scout runs; if unavailable, add a scout_report flag: 'B2B status unverified — apply conservative confidence on all road teams in tight windows.'
