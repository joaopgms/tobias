---
version: 5
updated_at: 2026-03-18T12:00:00.000000+00:00
updated_by: manual_review
llm: claude-sonnet-4-6
---

## SECTION:odds_targets
ML target range: 1.70–2.50 (decimal). Minimum one side must fall in range.
Spread odds target: 1.80–2.30.
O/U odds target: 1.80–2.05.
Commit confirmation floor: 1.65 ML (Scout already validated edge).
All three markets are available. Use the best edge regardless of market type.

## SECTION:priority_stats
Priority order — follow exactly, stop early if game is disqualified:

0. LINE ANOMALY CHECK (always first)
   Flag as anomaly if ANY of:
   - Tank-tier team priced as favourite at ≤ 1.35
   - Home team with materially better record priced as underdog at ≥ 2.20
   - Implied probability gap > 40pts vs actual record gap
   - Line moved > 0.30 in last 2 hours with no news explanation
   If anomaly → do NOT draft. Note in scout_report. Flag for Commit to investigate.

1. NetRtg L15 — most predictive short-term signal
2. Back-to-back + schedule density (games_l7) — see b2b_rules for numeric adjustments
3. Franchise player injury status — see franchise_player_rules
4. Play-in / playoff race motivation
   LATE SEASON FLAG (March onwards): teams locked into seeding may rest stars;
   teams fighting for play-in often overperform. Check seeding context explicitly.
5. L10 record (meaningful sample)
6. Home court advantage — worth ~2-3 points (~0.10-0.15 odds). Factor into close matchups
   where NetRtg gap is < 3 points between teams.
7. Home/away splits
8. DefRtg gap — if > 8 points between teams, significant spread edge signal
9. Pace — if both teams Pace > 100, lean Over; if both < 97, lean Under
10. H2H last 3 meetings — only meaningful if games are from current or last season.
    Ignore H2H older than 12 months. Books already price H2H in — use as tiebreaker only.
11. Season NetRtg (baseline context)

## SECTION:ev_requirement
Every drafted pick MUST satisfy: EV = (confidence/100 × odds) - 1 ≥ 0.05 (5% minimum EV).
Calculate and state EV explicitly in reasoning for every pick.
EV ≥ 0.15 = strong edge. EV 0.05–0.14 = marginal, proceed with caution.
EV < 0.05 → do NOT draft regardless of confidence tier.

## SECTION:market_rules
MONEYLINE (ML):
  Confidence floor: 50 (raised from 40 — conf 40 at 1.70 odds = negative EV -0.32, no genuine edge).
  EV ≥ 0.05. Odds 1.70–2.50.

SPREAD (ATS):
  Confidence floor: 60 (higher bar — half-point margins matter).
  EV ≥ 0.05. Odds 1.80–2.30.
  Strong spread signals:
    - B2B road team vs rested home (cover rate < 45% historically)
    - DefRtg gap > 8 points (elite defence vs poor offence)
    - Tank team as large underdog (tankers don't cover spreads)
    - NetRtg L15 gap > 6 points
  Avoid spreads when:
    - Injury feed coverage low (< 10 teams reporting) — undisclosed absences corrupt lines
    - Line anomaly present (flag instead)
    - Game-time decisions unresolved for either team

TOTALS (O/U):
  Confidence floor: 65 (highest bar — requires both teams' pace/style data).
  EV ≥ 0.05. Odds 1.80–2.05.
  Strong O/U signals:
    - Both teams Pace > 100 AND both OffRtg > 114 → lean Over
    - Both teams Pace < 97 AND both DefRtg < 112 → lean Under
    - Pace mismatch > 5 → unpredictable, require confidence ≥ 70 minimum
  Only bet totals when advanced stats (Pace, OffRtg, DefRtg) are available.

## SECTION:franchise_player_rules
Franchise player OUT → do NOT bet that team to win unless opponent also missing a star or confirmed tanking.
Franchise player Doubtful → confidence -15, stake -30%. Only proceed if EV still ≥ 0.05.
Franchise player Questionable/GTD → confidence -10, stake -20%. Flag explicitly in reasoning.
Franchise player Day-To-Day → confidence -5, stake -10%.
If BOTH teams have franchise player uncertainty → evaluate net impact.

Current confirmed absences (update each session):
  - Anthony Davis (Lakers): OUT — do not back Lakers ML; spread/O-U may still offer value
  - Alex Sarr (Wizards): OUT — Wizards fully tank-tier regardless
  - Leaky Black (Wizards): OUT
  - Kyshawn George (Wizards): OUT
  - D'Angelo Russell (Lakers): OUT — further weakens Lakers ML case

## SECTION:tanking_teams
Confirmed tanking-tier teams (all three criteria met):
  - Washington Wizards: 16-51, L10: 0-10, streak: L12 — clearest tank; multiple stars OUT
  - Sacramento Kings: 18-51, L10: 5-5 — worst record in West; L10 improvement is anomaly
  - Brooklyn Nets: 17-51, L10: 2-8, streak: L4 — bottom East
  - Utah Jazz: 20-48, L10: 2-8, streak: L3
  - Dallas Mavericks: 23-46, L10: 2-8, streak: L1 — confirmed tank
  - Memphis Grizzlies: 23-44, L10: 2-8, streak: L8 — deepening
  - Milwaukee Bucks: 28-39, L10: 2-8, streak: W1 — verify pick ownership before each bet

Tanking criteria (ALL THREE must be met):
  (a) Team owns its own 2026 draft pick
  (b) Bad record confirmed by both W-L AND L10
  (c) No realistic path to playoffs or play-in

When betting AGAINST tanking teams: edge-positive.
When betting ON tanking teams: require odds ≥ 2.20 and strong situational reason.

Emerging tank-watch:
  - Chicago Bulls (28-40, L10: 4-6) — monitor play-in race
  - New Orleans Pelicans (23-46, L10: 6-4) — record tank-tier but L10 shows fight
  - Golden State Warriors (33-35, L10: 3-7) — play-in bubble but fading

Hot streaks (may create line inefficiencies):
  - Atlanta Hawks (37-31, L10: 10-0, W10) — extreme regression risk; verify odds before committing
  - OKC Thunder (53-15, L10: 9-1) — efficiently priced
  - San Antonio Spurs (50-18, L10: 8-2) — efficiently priced
  - Los Angeles Lakers (43-25, L10: 9-1) — Davis+Russell OUT; spreads/totals only

## SECTION:b2b_rules
B2B and rest day rules — apply numeric confidence adjustments:

Rest days impact (apply to the team with fewer rest days):
  0 rest days (true B2B):        confidence -20, spread cover rate < 45%
  1 rest day (short turnaround): confidence -10
  2+ rest days:                  no adjustment — fully recovered

Amplifiers (stack with rest day penalty):
  Away game:                     additional -5
  4+ games in 7 days (heavy):   additional -10
  5+ games in 7 days (extreme): additional -15 (regardless of rest days)
  Facing top-10 DefRtg team:     additional -10

Examples:
  B2B road team vs rested home = -20 (B2B) -5 (away) = -25 total confidence adjustment
  B2B road, heavy schedule, elite defence = -20 -5 -10 -10 = -45 → likely below threshold

These adjustments are applied to the favoured team's base confidence.
B2B edge is most reliable for spread bets (cover rate impact is measurable).

## SECTION:confidence_staking
85–100 Elite: up to 30% of bankroll
70–84 High: 20–25%
55–69 Medium: 15–20%
50–54 Speculative: 10%
0–49: Do not draft
Max 70% of bankroll across all picks per day. Always keep 30% in reserve.
EV requirement overrides confidence tier — EV < 0.05 means no bet regardless.

## SECTION:selectivity
Draft only picks with genuine edge (confidence ≥ floor for market type AND EV ≥ 0.05).
0 or 1 picks is a valid and good result. Never force picks.
Flag line anomalies for Commit — deferred picks may become valid by tip-off.
When advanced stats unavailable, do not bet spreads or totals.

## SECTION:data_quality_rules
INJURY FEED QUALITY GATES — apply before any pick is drafted:

Source: nba_official (PDF)
  → Full 30-team coverage. Normal confidence rules apply.

Source: espn (fallback)
  → Partial coverage. Unknown injury status for most teams.
  → Confidence CAP: 50 on ALL picks regardless of tier.
  → Spreads and totals BANNED — injury uncertainty corrupts line analysis.
  → ML only. Flag in scout_report: "ESPN fallback — confidence capped at 50."

Source: espn + coverage < 5 teams reporting
  → Critically incomplete feed.
  → Confidence CAP: 40. Only speculative ML picks allowed.
  → Require odds ≥ 2.00 (wider margin needed to justify uncertainty).
  → Flag in scout_report: "Critically low injury coverage — high uncertainty."

Source: none / unavailable
  → 0 picks. Note in scout_report: "No injury data — cannot assess franchise player risk."

These gates override confidence tier and EV calculation.
Even a conf 80 pick becomes conf 50 if the injury feed is ESPN fallback.
