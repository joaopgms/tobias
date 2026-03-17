---
version: 4
updated_at: 2026-03-17T16:41:53.182985+00:00
updated_by: analyst_2026-03-17
llm: claude-sonnet-4-6
---

## SECTION:odds_targets
Target ML range: 1.70–2.50 (decimal).
Minimum one side of the game must fall in this range to be considered.
Spread odds target: 1.80–2.30. O/U: 1.80–2.05.
These are Scout targets. Commit uses a relaxed floor of 1.65 for confirmation only (Scout already validated the edge).

## SECTION:priority_stats
Priority order for scouting — follow this exact sequence, stop early if a game is disqualified:

0. LINE ANOMALY CHECK (run first, before any analysis)
   Flag as anomaly if ANY of:
   - Tank-tier team (confirmed) priced as favourite at ≤ 1.35
   - Home team with materially better record priced as underdog at ≥ 2.20
   - Implied probability gap > 40pts vs actual record gap (e.g. 50-win team priced like a 20-win team)
   - Line moved > 0.30 in last 2 hours with no news explanation
   If anomaly found → do NOT draft. Note it explicitly in scout_report. Flag for Commit to monitor — the answer (injury, lineup change) may emerge by tip-off.

1. NetRtg L15 — most predictive short-term signal
2. Back-to-back + schedule density (games_l7)
3. Franchise player injury status
4. Play-in / playoff race motivation
5. L10 record (meaningful sample)
6. Home/away splits
7. H2H last 3 meetings
8. Season NetRtg (baseline context)

## SECTION:ev_requirement
Every drafted pick MUST satisfy: EV = (confidence/100 × odds) - 1 ≥ 0.05 (5% minimum EV).
Calculate and state EV explicitly in reasoning for every pick.
Example: conf 60, odds 2.10 → EV = (0.60 × 2.10) - 1 = 0.26 ✅
Example: conf 55, odds 1.75 → EV = (0.55 × 1.75) - 1 = -0.04 ❌ do not draft
If EV < 0.05 → do NOT draft regardless of confidence tier.
EV ≥ 0.15 = strong edge. EV 0.05–0.14 = marginal, proceed with caution.

## SECTION:franchise_player_rules
Franchise player OUT → do NOT bet that team to win unless opponent also missing a star or is confirmed tanking.
Franchise player Doubtful → confidence -15, stake -30%. Only proceed if EV still ≥ 0.05.
Franchise player Questionable/GTD → confidence -10, stake -20%. Flag explicitly in reasoning.
Franchise player Day-To-Day → confidence -5, stake -10%.
If BOTH teams have franchise player uncertainty → evaluate net impact; may still be value on the less-affected side.

Current confirmed franchise player absences (update each session):
  - Anthony Davis (Lakers): OUT — do not back Lakers ML unless opponent also missing anchor; Lakers posting W6 streak on depth alone — spread/O-U contexts may still offer value
  - Kyshawn George (Wizards): OUT — further compounds Wizards tank-tier status
  - D'Angelo Russell (Lakers): OUT — secondary piece, not franchise anchor; Davis already noted; note cumulative depth reduction
  - Alex Sarr (Wizards): OUT — Wizards already confirmed tank-tier; minimal additional impact
  - Leaky Black (Wizards): OUT — note for completeness; Wizards fully tank-tier regardless

## SECTION:tanking_teams
Confirmed tanking-tier teams (all three criteria met):
  - Washington Wizards: 16-51, L10: 0-10, streak: L12 — clearest tank in league, actively losing every game; Alex Sarr + Leaky Black + Kyshawn George all OUT; L12 streak is extreme
  - Sacramento Kings: 18-51, L10: 5-5 — worst record in West, no play-in path; L10 improvement is anomaly, treat with caution
  - Brooklyn Nets: 17-51, L10: 2-8, streak: L4 — bottom East, no play-in path
  - Utah Jazz: 20-48, L10: 2-8, streak: L3 — no play-in path
  - Dallas Mavericks: 23-46, L10: 2-8, streak: L1 — confirmed tank; streak back to losing
  - Memphis Grizzlies: 23-44, L10: 2-8, streak: L8 — confirmed tank, L8 streak deepening
  - Milwaukee Bucks: 28-39, L10: 2-8, streak: W1 — confirmed tank-tier; verify draft pick ownership before each bet

Tanking criteria (ALL THREE must be met):
  (a) Team owns its own 2026 draft pick
  (b) Bad record confirmed by both W-L AND L10
  (c) No realistic path to playoffs or play-in

When betting AGAINST tanking teams: treat as edge-positive. When betting ON tanking teams: require odds ≥ 2.20 and strong situational reason (e.g. opponent B2B, major injury).

Emerging tank-watch:
  - Chicago Bulls (28-40, L10: 4-6, streak: W1) — monitor play-in race and pick ownership; L10 still weak
  - New Orleans Pelicans (23-46, L10: 6-4, streak: W1) — record is tank-tier but L10 shows fight; watch motivation shift
  - Golden State Warriors (33-35, L10: 3-7, streak: W1) — still in play-in bubble but L10:3-7 suggests fade risk; one-game win break in streak, monitor closely

Hot streaks to track (may create line inefficiencies):
  - Atlanta Hawks (37-31, L10: 10-0, streak: W10) — perfect L10, W10 streak; extreme regression risk, books likely adjusting lines sharply, verify before committing
  - OKC Thunder (53-15, L10: 9-1, streak: W8) — best record in league; likely priced efficiently
  - Los Angeles Lakers (43-25, L10: 9-1, streak: W6) — elite recent form despite Davis + Russell OUT; spread/O-U contexts only given anchor absences
  - San Antonio Spurs (50-18, L10: 8-2, streak: W2) — second-best record; elite form, likely efficiently priced
  - Detroit Pistons (48-19, L10: 5-5, streak: L1) — third-best record but L10 cooling significantly; potential fade candidate if trend continues
  - New York Knicks (44-25, L10: 7-3, streak: W3) — consistent form; monitor for value
  - Orlando Magic (38-29, L10: 7-3, streak: L1) — strong season record; streak broken, watch for reset opportunity

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
Max 70% of bankroll across all picks per day. Always keep 30% in reserve.
EV requirement still applies at all tiers — EV < 0.05 overrides confidence tier.

## SECTION:selectivity
Draft only picks with genuine edge (confidence ≥ 40 AND EV ≥ 0.05). Quality over quantity.
0 or 1 picks is a valid and good result. Never force picks to fill a quota.
If no game clears the bar → output empty draft_picks with clear reasoning in scout_report.
Flag any line anomalies for Commit to monitor — deferred picks may become valid by tip-off.
