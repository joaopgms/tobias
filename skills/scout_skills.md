---
version: 16
updated_at: 2026-03-31T11:47:18.290426+00:00
updated_by: analyst_2026-03-31
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

1. NetRtg L15 — most predictive short-term signal (now available in prompt above season stats)
   Source: computed from ESPN game logs (last 15 completed games, point differential scaled to NetRtg)
   This is an approximation — treat as directionally accurate, not exact.
   Use L15 as the PRIMARY directional signal. Season NetRtg as secondary context.
   If NetRtg L15 is missing for a team: apply confidence -5 on any pick where L15 would be decisive.
   NetRtg L15 gap threshold: >= 4.0 points = meaningful edge signal (lower than season threshold due to approximation).
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
CRITICAL RULE: Only apply injury information to the TWO TEAMS in the specific game being evaluated.
NEVER mention or apply injuries from teams not playing in that game.
Example: If evaluating Rockets vs Lakers, ONLY consider Rockets and Lakers injuries.
Wizards/Pistons/any other team injuries are IRRELEVANT and must NOT be mentioned.

Franchise player OUT → do NOT bet that team to win unless opponent also missing a star or confirmed tanking.
Franchise player Doubtful → confidence -15, stake -30%. Only proceed if EV still ≥ 0.05.
Franchise player Questionable/GTD → confidence -10, stake -20%. Flag explicitly in reasoning.
WARNING: If your edge DEPENDS on them being OUT, apply confidence -25 (not -10).
A Questionable player has ~50% chance of playing — never build a bet thesis on their absence.
Franchise player Day-To-Day → confidence -5, stake -10%.
If BOTH teams have franchise player uncertainty → evaluate net impact.

Known absences (roster-only flags — confirmed via ESPN roster cross-reference, NOT official injury report):
These are flagged as likely OUT but must be re-verified against NBA official PDF each session.

Oklahoma City Thunder:
- Isaiah Hartenstein (C): OUT [roster-only]
- Thomas Sorber (C): OUT [roster-only]
- Jalen Williams (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet OKC ML without re-verification.

San Antonio Spurs:
- David Jones Garcia (F): OUT [roster-only]

Detroit Pistons:
- Cade Cunningham (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet Detroit ML without re-verification.
- Jalen Duren (C): OUT [roster-only]
- Tobias Harris (F): OUT [roster-only]
- Duncan Robinson (F): OUT [roster-only]
- Isaiah Stewart (F): OUT [roster-only]

Boston Celtics:
- Nikola Vucevic (C): OUT [roster-only]

Los Angeles Lakers:
- Marcus Smart (G): OUT [roster-only]
- Adou Thiero (F): OUT [roster-only]

New York Knicks:
- Landry Shamet (G): OUT [roster-only]

Cleveland Cavaliers:
- Jarrett Allen (C): OUT [roster-only]
- Max Strus (G): OUT [roster-only]
- Jaylon Tyson (G): OUT [roster-only]
- Dean Wade (F): OUT [roster-only]

Minnesota Timberwolves:
- Jaden McDaniels (F): OUT [roster-only]

Houston Rockets:
- Steven Adams (C): OUT [roster-only]
- Fred VanVleet (G): OUT [roster-only]

Toronto Raptors:
- Jamison Battle (F): OUT [roster-only]
- Chucky Hepburn (G): OUT [roster-only]
- Immanuel Quickley (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet Toronto ML without re-verification.

Washington Wizards:
- Bilal Coulibaly (G): OUT [roster-only] (confirmed via injury landscape)
- Anthony Davis (F): OUT [roster-only] — FRANCHISE PLAYER
- Kyshawn George (F): OUT [roster-only]
- D'Angelo Russell (G): OUT [roster-only] — FRANCHISE PLAYER
- Alex Sarr (C): OUT [roster-only] (confirmed via injury landscape) — FRANCHISE PLAYER
- Cam Whitmore (F): OUT [roster-only]
- Trae Young (G): OUT [roster-only] — FRANCHISE PLAYER (confirmed via injury landscape)

Franchise players requiring mandatory NBA official PDF verification before ANY pick involving their team:
- Jalen Williams (OKC) — verify before ANY OKC pick
- Cade Cunningham (Detroit) — verify before ANY Detroit pick
- Immanuel Quickley (Toronto) — verify before ANY Toronto pick
- Alex Sarr (Washington) — verify before ANY Washington pick
- Any player flagged [roster-only] — these are NOT confirmed via official injury report

NOTE: Anthony Edwards (Minnesota) removed from verified absences this session — not in current verified feed. Do not list as OUT until re-confirmed. Craig Porter Jr. (Cleveland), Miles McBride (NY), Kevin McCullar Jr. (NY) removed — not in current verified feed. Do not include until re-confirmed.

## SECTION:tanking_teams
Confirmed tanking-tier teams (all three criteria met):
- Washington Wizards: bottom of standings; Bilal Coulibaly, Alex Sarr, Trae Young confirmed OUT via injury landscape + multiple additional roster-only absences (Davis, Russell, George, Whitmore) — clearest tank in league. Do not bet Washington to win.
- Sacramento Kings: ~18-52, L10: 5-5 — worst record in West; L10 improvement unreliable, NetRtg worst in league.
- Brooklyn Nets: ~17-52, L10: 2-8 — bottom East; extreme negative NetRtg.
- Utah Jazz: ~20-49, L10: 2-8 — confirmed tank.
- Dallas Mavericks: ~23-47, L10: 2-8 — confirmed tank.
- Memphis Grizzlies: ~24-44 — NetRtg negative; verify pick ownership before bets.
- Milwaukee Bucks: ~28-40, L10: 2-8 — verify pick ownership before each bet.

Tanking criteria (ALL THREE must be met):
(a) Team owns its own 2026 draft pick
(b) Bad record confirmed by both W-L AND L10
(c) No realistic path to playoffs or play-in

When betting AGAINST tanking teams: edge-positive.
When betting ON tanking teams: require odds ≥ 2.20 and strong situational reason.

Emerging tank-watch:
- Chicago Bulls (~28-41, L10: 4-6) — borderline play-in; monitor.
- New Orleans Pelicans (~24-46, L10: 6-4) — record tank-tier but L10 shows fight; treat as volatile, not confirmed tank.
- Golden State Warriors: 36-39, L10: 4-6, streak: L1 — play-in bubble fading; NetRtg +0.0 at breakeven; treat as tank-watch.

Hot streaks (may create line inefficiencies):
- OKC Thunder: 60-16, L10: 9-1, streak: W3 — elite team; NetRtg +10.9 best in league. Jalen Williams OUT [roster-only] — CRITICAL: star absence must be verified before any OKC pick. Star rest risk increasing with postseason clinch near.
- San Antonio Spurs: 57-18, L10: 9-1, streak: W9 — elite tier; NetRtg +8.2; efficiently priced. Re-verify all SAS players before any pick.
- Detroit Pistons: 54-21, L10: 7-3, streak: L1 — Cade Cunningham OUT [roster-only]; Jalen Duren, Tobias Harris, Duncan Robinson, Isaiah Stewart also OUT. Do not bet Detroit ML without verification. Streak cooling — L1.
- Los Angeles Lakers: 49-26, L10: 9-1, streak: W3 — strong recent form; NetRtg +1.9 vs record suggests run-differential luck; regression risk elevated.
- New York Knicks: 48-27, L10: 7-3, streak: L2 — NetRtg +6.5; top-seed contender East; two straight losses flag short-term fade risk.
- Boston Celtics: 50-25, L10: 7-3, streak: L1 — NetRtg +7.6; seeding race with Knicks/Detroit live; streak cooled.
- Denver Nuggets: 48-28, L10: 8-2, streak: W6 — NetRtg +4.7; resurgent. Re-verify full roster before picks.
- Atlanta Hawks: 43-33, L10: 8-2, streak: W2 — NetRtg +1.9 sharply below .565 W% implied talent; hot-streak-fade rule applies.
- Charlotte Hornets: 39-36, L10: 7-3, streak: L2 — NetRtg +4.5; play-in motivation positive but streak cooling.
- Cleveland Cavaliers: 47-28, L10: 7-3, streak: W2 — 4 confirmed OUT [roster-only] including Jarrett Allen and Max Strus; depth depleted; treat with caution despite streak.
- Houston Rockets: 45-29, L10: 5-5, streak: W2 — Fred VanVleet OUT [roster-only]; NetRtg +4.5; momentum stabilising.

HOT STREAK FADE CANDIDATES:
- Los Angeles Lakers (L10: 9-1, streak: W3): NetRtg +1.9 sharply below what 49-26 record implies — regression candidate. Any opponent at ≥ 1.80 warrants explicit fade evaluation.
- Atlanta Hawks (L10: 8-2, streak: W2): W% ~.565 above .550 threshold triggers fade rule; NetRtg +1.9 divergence from record is real; opponents at ≥ 1.80 warrant fade evaluation.
- Philadelphia 76ers (41-34, L10: 6-4, streak: L1): NetRtg -0.3 deeply concerning for 41-34 record — significant regression risk; hot streak fading; any opponent at ≥ 1.75 warrants fade evaluation.

Schedule seeding context (late March/early April):
- OKC (60-16), Spurs (57-18), Pistons (54-21) locked into top-3 seeds — star rest risk increasing significantly. OKC: Jalen Williams already OUT adds depth concern.
- Play-in bubble (seeds 7-10 East/West): Charlotte (39-36), Portland (38-38), Golden State (36-39), Clippers (39-36), Miami (40-36) — motivation-positive.
- Miami Heat (40-36, L10: 3-7, streak: W1): NetRtg +2.3; L10 3-7 alarming despite single-game win; fade candidate on multi-game bets.
- Orlando Magic (39-35, L10: 3-7, streak: L1): NetRtg +0.1 near breakeven; L10 3-7 confirms fade; cautious.
- Minnesota Timberwolves (46-29, L10: 6-4, streak: W1): Jaden McDaniels OUT [roster-only]; Anthony Edwards absence NOT confirmed in current feed — re-verify before any pick.
- Toronto Raptors (42-32, L10: 6-4, streak: W2): Immanuel Quickley OUT [roster-only]; verify before any Toronto pick.

## SECTION:b2b_rules
B2B and rest day rules — apply numeric confidence adjustments:

Rest days impact (apply to the team with fewer rest days):
0 rest days (true B2B): confidence -20, spread cover rate < 45%
1 rest day (short turnaround): confidence -10
2+ rest days: no adjustment — fully recovered

Amplifiers (stack with rest day penalty):
Away game: additional -5
4+ games in 7 days (heavy): additional -10
5+ games in 7 days (extreme): additional -15 (regardless of rest days)
Facing top-10 DefRtg team: additional -10

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
Draft picks with genuine edge (confidence ≥ floor for market type AND EV ≥ 0.05).

TARGET: Aim for 2-4 picks per session when the slate supports it.
- 1 pick is acceptable on difficult nights (extreme mismatches, low odds range).
- 0 picks is valid when no game meets quality thresholds — do NOT force picks.
- 5+ picks in a single session requires exceptional justification.

SPREAD AND TOTAL BETS:
- Actively look for spread edges in EVERY session — do not default to ML only.
- Spreads are valid whenever: advanced stats available AND NBA official injury PDF available.
- When a game has a clear NetRtg gap (> 6pts) or B2B situation, EVALUATE the spread first.
- ML and spread can coexist on the same game if both markets offer independent edges.

Flag line anomalies for Commit — deferred picks may become valid by tip-off.
When advanced stats unavailable, do not bet spreads or totals (ML-only session — log explicitly).

HOT STREAK FADE RULE:
When a non-elite team (outside top-8 record) shows L10 ≥ 9-1 AND season record implies
sub-.550 true talent (i.e. their overall W% is below .550 despite the hot streak):
→ Flag opponent as having regression-based edge
→ Check current ML odds on the opponent explicitly
→ If opponent odds are ≥ 1.80 (books haven't fully priced regression risk), add confidence +10
→ Do NOT fade the hot team blindly — require opponent to also have neutral or positive stats
→ This rule applies regardless of market (ML, spread, total)
Current example: Atlanta Hawks (37-31, W10) — overall .544 W% implies ~.500 true talent.
Any opponent at ≥ 1.80 against Atlanta warrants explicit regression-fade evaluation.

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

PACE DATA QUALITY FLAG:
→ If Pace = 0.0 for ALL teams in the advanced stats feed (as seen in current session), treat Pace as unavailable.
→ Do NOT use Pace-based signals (O/U lean, pace mismatch rules) when Pace = 0.0 universally.
→ Flag in scout_report: "Pace data unavailable — O/U pace signals suppressed this session."
→ Totals confidence floor raises to 70 (from 65) when Pace data is absent.

These gates override confidence tier and EV calculation.
Even a conf 80 pick becomes conf 50 if the injury feed is ESPN fallback.
