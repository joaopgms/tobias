---
version: 3
updated_at: 2026-03-14T18:46:12.101354+00:00
updated_by: analyst_2026-03-14
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
  - Anthony Davis (Lakers): OUT — do not back Lakers ML unless opponent also missing anchor
  - D'Angelo Russell (Lakers): OUT — compounds Lakers roster concerns; Lakers still 41-25 with W4 streak, suggesting depth is covering adequately — monitor but do not discount Lakers entirely in spread/O-U contexts
  - Kyshawn George (Wizards): OUT — note: Wizards already tank-tier, minimal additional impact on assessment

## SECTION:tanking_teams
Confirmed tanking-tier teams (all three criteria met):
  - Washington Wizards: 16-49, L10: 0-10, streak: L10 — clearest tank in league, actively losing every game
  - Sacramento Kings: 16-51, L10: 4-6 — worst record in West, no play-in path
  - Brooklyn Nets: 17-49, L10: 2-8 — bottom East, no play-in path
  - Utah Jazz: 20-47, L10: 2-8 — no play-in path
  - Dallas Mavericks: 22-45, L10: 1-9 — now meets all three tanking criteria; treat as confirmed tank

Tanking criteria (ALL THREE must be met):
  (a) Team owns its own 2026 draft pick
  (b) Bad record confirmed by both W-L AND L10
  (c) No realistic path to playoffs or play-in

When betting AGAINST tanking teams: treat as edge-positive. When betting ON tanking teams: require odds ≥ 2.20 and strong situational reason (e.g. opponent B2B, major injury).

Emerging tank-watch: Memphis Grizzlies (23-43, L10: 2-8, streak: L7) — trending toward tank criteria, monitor draft pick ownership.

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
