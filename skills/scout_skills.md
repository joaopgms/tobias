---
version: 1
updated_at: null
updated_by: bootstrap
llm: bootstrap
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

## SECTION:tanking_teams
No teams confirmed tanking at start of season. Analyst will update based on standings.
Tanking criteria (ALL THREE must be met):
  (a) Team owns its own 2026 draft pick
  (b) Bad record confirmed by both W-L AND L10
  (c) No realistic path to playoffs or play-in

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
