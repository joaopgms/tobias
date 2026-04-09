---
date: 2026-04-09
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (5 bets)
---

## Today's Analysis — 2026-04-09

Key factual updates this session: Anthony Edwards joins the verified OUT list for Minnesota (roster-only), fundamentally altering their outlook at 47-33 with an already mixed L10 4-6 — any MIN line must be treated with extreme caution until NBA official PDF confirms. Denver's 10-game winning streak (L10: 10-0) is the macro story of the week; at NetRtg +4.9 and W% .650 their streak is performance-backed rather than pure regression bait, so the hot-streak-fade rule does not auto-apply, but the streak length warrants monitoring for rest management with postseason positioning secured. Performance data continues to show the system losing value in the 1.90–2.09 odds band (6W/9L, -€484.98) and at high confidence (2W/5L, 28.6%), suggesting overconfidence in medium-odds picks remains the primary structural leak requiring future evidence-based tightening.

## Performance Stats
ALL-TIME: 9W / 14L | Win rate: 39.1% | P&L: €-599.24 | Avg odds: 1.99 | Avg conf: 65.3/100
RECENT 20: 8W / 12L | 40.0% WR | P&L: €-369.41
By market:      ML 12bets 5W/7L 41.7% €-256.91  |  SPREAD 8bets 3W/5L 37.5% €-319.06  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 7bets 2W/5L 28.6% €-190.54  |  Medium 14bets 7W/7L 50.0% €-267.39  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 5bets 3W/2L 60.0% €+115.05  |  1.90-2.09 15bets 6W/9L 40.0% €-484.98  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Verified absence feed updated: Anthony Edwards now appears as OUT [roster-only] for MIN (new this session); Jaxson Hayes added for LAL; several prior entries (Emanuel Miller, Cade Cunningham, Isaiah Stewart, Thomas Bryant, Dean Wade, Jaden McDaniels) removed as they are NOT in the current verified list and must not be listed as OUT per rules.
- [tanking_teams] Standings updated to current session data (OKC 64-16, SAS 61-19, DET 58-22, DEN 52-28 W10, MIN 47-33 L1); Anthony Edwards now flagged OUT [roster-only] for MIN requiring franchise-player-level alert; Jaxson Hayes added to LAL absences; Detroit alert revised per verified feed (Cunningham/Stewart not in verified list this session); Denver 10-game streak noted with correct hot-streak-fade rule application.

## Commit patches applied
None

## Intelligence gaps identified
- **High-confidence bets (conf 70-84) are performing at only 28.6% win rate (2W/5L, -€190.54) — significantly below the implied ~55-60% expected win rate at those confidence levels.** — This is the single largest P&L leak in the system; if high-confidence picks are losing at this rate, either the confidence calibration is too aggressive or specific signal types are generating false confidence. → After 10 more settled high-confidence bets, audit which specific signals (NetRtg gap, B2B, franchise player absence) were present in each losing high-conf pick and tighten the confidence floor or add a 'high-confidence gate' requiring two independent signals to justify conf ≥ 70.
- **Spread bets showing 37.5% win rate (3W/5L, -€319.06) with negative P&L despite being the most EV-sensitive market type — possible that spread confidence floor of 60 is too low.** — Spread losses are disproportionate to bet count; the half-point margin sensitivity means spread picks at confidence 60-64 may be systematically mispriced when injury data is partial. → Consider raising spread confidence floor from 60 to 65 after 10+ settled spread bets confirm the pattern; in the interim flag any spread pick at confidence 60-64 as requiring an additional confirming signal (e.g. B2B or DefRtg gap > 8).
- **Anthony Edwards' (MIN) absence status changed from 'not in verified feed' to OUT [roster-only] this session, but no rule currently governs how quickly to re-integrate a returning franchise player if their status reverses at commit time.** — A player moving from OUT [roster-only] to Active between Scout (14:00) and Commit (tip-off) would require confidence +10 per injury_check_rules, but the current rules don't specify how to re-price the team's NetRtg expectation when a franchise player returns — Scout may have already discounted the team heavily. → Add a clause to injury_check_rules: 'If franchise player upgraded from OUT to Active at commit time, re-evaluate team's effective NetRtg as season baseline (not absence-adjusted) and recalculate EV before confirming any pick on or against that team.'
- **Denver's 10-game winning streak (L10: 10-0) is exceptional but their NetRtg +4.9 is only 5th in the league — streak may be partly schedule-driven (soft opponents) rather than pure performance improvement.** — If Denver faces an elite opponent (OKC, Boston, SAN) during the streak, books may not fully price regression risk; knowing opponent quality during the streak would help calibrate whether to back or fade Denver. → Add opponent quality context to tanking_teams hot streak notes — flag when a streak was built against sub-.500 opponents vs. elite opponents, as this changes regression probability; requires schedule data pipeline addition.
