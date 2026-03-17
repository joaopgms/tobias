---
version: 1
updated_at: null
updated_by: bootstrap
llm: claude-sonnet-4-6
---

## SECTION:odds_targets
Target Betano ML range: 1.70–2.50 (decimal).
Minimum one side of the game must fall in this range to be considered.
Spread odds target: 1.75–2.10. O/U: 1.80–2.05.

## SECTION:priority_stats
Priority order for scouting:
1. NetRtg L15 — most predictive short-term signal
2. Back-to-back + schedule density (games_l7)
3. Franchise player injury status
4. Play-in / playoff race motivation
5. L10 record (meaningful sample)
6. Home/away splits
7. H2H last 3 meetings
8. Season NetRtg (baseline context)

## SECTION:franchise_player_rules
Franchise player OUT → do NOT bet that team to win unless opponent also missing a star or is confirmed tanking.
Franchise player Doubtful → confidence -15, stake -30%. Only proceed if EV still ≥ 8%.
Franchise player Questionable/GTD → confidence -10, stake -20%. Flag explicitly in reasoning.
Franchise player Day-To-Day → confidence -5, stake -10%.
If BOTH teams have franchise player uncertainty → evaluate net impact; may still be value on the less-affected side.

Current confirmed franchise player absences (update each session):
  - Anthony Davis (Lakers): OUT — do not back Lakers ML unless opponent also missing anchor; Lakers still posting W8 in L10/W5 streak on depth alone — spread/O-U contexts may still offer value
  - Alex Sarr (Wizards): OUT — Wizards already confirmed tank-tier; minimal additional impact on assessment
  - Leaky Black (Wizards): OUT — note for completeness; Wizards fully tank-tier regardless

## SECTION:tanking_teams
Confirmed tanking-tier teams (all three criteria met):
  - Washington Wizards: 16-50, L10: 0-10, streak: L11 — clearest tank in league, actively losing every game; Alex Sarr OUT compounds; L11 streak is extreme
  - Sacramento Kings: 18-51, L10: 5-5 — worst record in West, no play-in path; L10 improvement is anomaly, treat with caution
  - Brooklyn Nets: 17-50, L10: 2-8, streak: L3 — bottom East, no play-in path
  - Utah Jazz: 20-48, L10: 2-8, streak: L3 — no play-in path
  - Dallas Mavericks: 23-45, L10: 2-8, streak: W1 — confirmed tank; one-game win irrelevant to trend
  - Memphis Grizzlies: 23-43, L10: 2-8, streak: L7 — confirmed tank
  - Milwaukee Bucks: 28-39, L10: 2-8, streak: W1 — confirmed tank-tier; verify draft pick ownership before each bet

Tanking criteria (ALL THREE must be met):
  (a) Team owns its own 2026 draft pick
  (b) Bad record confirmed by both W-L AND L10
  (c) No realistic path to playoffs or play-in

When betting AGAINST tanking teams: treat as edge-positive. When betting ON tanking teams: require odds ≥ 2.20 and strong situational reason (e.g. opponent B2B, major injury).

Emerging tank-watch:
  - Chicago Bulls (27-40, L10: 3-7, streak: L2) — monitor play-in race and pick ownership; trending toward tank
  - New Orleans Pelicans (22-46, L10: 6-4, streak: L1) — record is tank-tier but L10 shows fight; watch motivation shift
  - Golden State Warriors (32-35, L10: 2-8, streak: L5) — play-in bubble but L10:2-8 and L5 streak suggest significant fade; monitor if they fall out of play-in contention

Hot streaks to track (may create line inefficiencies):
  - Atlanta Hawks (36-31, L10: 9-1, streak: W9) — elite recent form; W9 streak risks sharp regression, verify line before committing
  - Orlando Magic (38-28, L10: 8-2, streak: W7) — strong run; monitor for inflated lines
  - OKC Thunder (53-15, L10: 9-1, streak: W8) — best record in league; likely priced efficiently
  - Los Angeles Lakers (42-25, L10: 8-2, streak: W5) — strong depth despite Davis OUT; spread/O-U contexts only given anchor absence
  - San Antonio Spurs (49-18, L10: 8-2, streak: W1) — second-best record; elite form, likely efficiently priced
  - Detroit Pistons (48-19, L10: 5-5, streak: L1) — third-best record but L10 cooling significantly; potential fade candidate if trend continues

## SECTION:b2b_rules
B2B teams cover the spread less than 45% of the time historically.
B2B vs rested = clear edge especially for spreads.
Heavy load (4+ games in 7 days) amplifies B2B impact — note as HIGH FATIGUE.
5+ games in 7 days = EXTREME FATIGUE regardless of today's rest days.

## SECTION:confidence_staking
85–100 Elite: up to 30% of bankroll
70–84 High: 20–25%
55–69 Medium: 15–20%
40–54 Speculative: 10%
0–39: Do not draft
Max 70% of bankroll across all picks per day.
Always keep 30% in reserve.

## SECTION:selectivity
Draft only picks with genuine edge (confidence ≥ 40). Quality over quantity.
0 or 1 picks is a valid result. Never force picks to fill a quota.
If no game clears the bar → output empty draft_picks with reasoning.
