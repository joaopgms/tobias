---
version: 25
updated_at: 2026-04-08T11:53:45.985891+00:00
updated_by: analyst_2026-04-08
llm: claude-sonnet-4-6
---

## SECTION:odds_targets
ML target range: 1.60–2.50 (decimal). Minimum one side must fall in range.
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
EV ≥ 0.05. Odds 1.60–2.50.

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
- Thomas Sorber (C): OUT [roster-only]

San Antonio Spurs:
- David Jones Garcia (F): OUT [roster-only]
- Emanuel Miller (F): OUT [roster-only]

Detroit Pistons:
- Cade Cunningham (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet Detroit ML without re-verification.
- Isaiah Stewart (F): OUT [roster-only]

Los Angeles Lakers:
- Luka Doncic (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet LAL ML without re-verification.
- Austin Reaves (G): OUT [roster-only] — key secondary player; LAL depth critically thin.
- Marcus Smart (G): OUT [roster-only]

Denver Nuggets:
- Spencer Jones (F): OUT [roster-only]
- Peyton Watson (G): OUT [roster-only]

Cleveland Cavaliers:
- Thomas Bryant (C): OUT [roster-only]
- Jaylon Tyson (G): OUT [roster-only]
- Dean Wade (F): OUT [roster-only]

Houston Rockets:
- Steven Adams (C): OUT [roster-only]
- Fred VanVleet (G): OUT [roster-only]

Minnesota Timberwolves:
- Jaden McDaniels (F): OUT [roster-only]

Atlanta Hawks:
- Jock Landale (C): OUT [roster-only]

Toronto Raptors:
- Chucky Hepburn (G): OUT [roster-only]

Washington Wizards:
- Anthony Davis (F): OUT [roster-only + injury landscape confirmed] — FRANCHISE PLAYER
- Kyshawn George (F): OUT [roster-only]
- D'Angelo Russell (G): OUT [roster-only] — FRANCHISE PLAYER
- Alex Sarr (C): OUT [roster-only] — FRANCHISE PLAYER
- Tristan Vukcevic (F): OUT [roster-only + injury landscape confirmed]
- Cam Whitmore (F): OUT [roster-only]
- Trae Young (G): OUT [roster-only + injury landscape confirmed] — FRANCHISE PLAYER

NOTE: Jalen Williams (OKC) NOT in current verified absence feed — removed from franchise_player_rules absent list. Re-verify via NBA official PDF before any OKC pick.
NOTE: Anthony Edwards (Minnesota) NOT in current verified absence feed — removed from franchise_player_rules absent list. Re-verify via NBA official PDF before any MIN pick.
NOTE: Immanuel Quickley (Toronto) NOT in current verified absence feed — removed. Re-verify before any Toronto pick.
NOTE: Jarrett Allen, Evan Mobley, Sam Merrill, Zeke Nnaji — NOT in current verified list. Do NOT list as OUT.

Franchise players requiring mandatory NBA official PDF verification before ANY pick involving their team:
- Cade Cunningham (Detroit) — verify before ANY Detroit pick
- Luka Doncic (Los Angeles Lakers) — verify before ANY LAL pick; OUT [roster-only] removes primary offensive engine
- Any player flagged [roster-only] — these are NOT confirmed via official injury report

CRITICAL: Trae Young, Alex Sarr confirmed OUT via injury landscape feed this session.
Washington Wizards: Anthony Davis also confirmed via injury landscape. Full tank confirmed — Do NOT bet Washington to win.

LOS ANGELES LAKERS ALERT: Luka Doncic AND Austin Reaves both OUT [roster-only] — two of top-3 offensive players absent. LAL ML bets require extreme caution; NetRtg +0.9 already tepid with these absences baked in.

DETROIT ALERT: Cade Cunningham OUT [roster-only]; Isaiah Stewart also OUT. Both OUT [roster-only] — do NOT bet Detroit ML without re-verification.

## SECTION:tanking_teams
Confirmed tanking-tier teams (all three criteria met):
- Washington Wizards: bottom of standings; Trae Young, Anthony Davis, D'Angelo Russell, Alex Sarr, Kyshawn George, Cam Whitmore, Tristan Vukcevic all OUT — clearest tank in league. Do not bet Washington to win.
- Sacramento Kings: ~18-52, L10: 5-5 — worst record in West; NetRtg worst in league.
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
- Golden State Warriors: 37-42, L10: 4-6, streak: W1 — NetRtg -0.2 at breakeven; confirmed tank-watch. Play-in path eliminated or near-eliminated.

Hot streaks and current form:
- OKC Thunder: 63-16, L10: 9-1, streak: W6 — elite; NetRtg +11.9 best in league. Thomas Sorber (C) OUT [roster-only]. Jalen Williams NOT in current verified absence feed — re-verify via NBA official PDF before ANY OKC pick. Star rest risk elevated with postseason clinch imminent.
- San Antonio Spurs: 60-19, L10: 9-1, streak: W1 — elite tier; NetRtg +8.3. David Jones Garcia, Emanuel Miller OUT [roster-only]. Victor Wembanyama NOT in current verified absence feed — re-verify via NBA official PDF before any pick.
- Detroit Pistons: 57-22, L10: 7-3, streak: L1 — Cade Cunningham AND Isaiah Stewart OUT [roster-only]; do not bet Detroit ML without verification. Strong record implies depth; still cautious with franchise player absent.
- Boston Celtics: 54-25, L10: 8-2, streak: W4 — NetRtg +8.2; seeding race active; one of league's most complete rosters.
- New York Knicks: 51-28, L10: 7-3, streak: W3 — NetRtg +6.6; top-seed contender East.
- Denver Nuggets: 51-28, L10: 9-1, streak: W9 — NetRtg +4.8; extended resurgence. Spencer Jones, Peyton Watson OUT [roster-only] (role players).
- Cleveland Cavaliers: 50-29, L10: 8-2, streak: W3 — NetRtg +4.2; Thomas Bryant, Jaylon Tyson, Dean Wade OUT [roster-only] (role players per current verified feed). Re-verify Allen/Mobley status before any CLE pick.
- Los Angeles Lakers: 50-29, L10: 6-4, streak: L3 — NetRtg +0.9 well below record-implied talent; Luka Doncic AND Austin Reaves OUT [roster-only] — CRITICAL dual absence; Marcus Smart also OUT. Three-game losing streak. Do NOT bet LAL without re-verification; treat as severely depleted.
- Houston Rockets: 50-29, L10: 8-2, streak: W7 — Fred VanVleet, Steven Adams OUT [roster-only]; NetRtg +5.1; seven-game streak notable; play-in secured, seeding race live.
- Minnesota Timberwolves: 47-32, L10: 5-5, streak: W1 — Jaden McDaniels OUT [roster-only]; Anthony Edwards NOT in current verified absence feed — re-verify before any MIN pick. Streak bounced to W1 but L10 mixed.
- Atlanta Hawks: 45-34, L10: 7-3, streak: L1 — NetRtg +2.6; Jock Landale OUT [roster-only]; streak snapped; hot-streak-fade risk elevated.
- Charlotte Hornets: 43-37, L10: 7-3, streak: L1 — NetRtg +5.2; play-in motivation positive; streak snapped — monitor fade risk.
- Philadelphia 76ers: 43-36, L10: 6-4, streak: L2 — NetRtg -0.4 deeply concerning for .544 W% record; fade candidate strengthening.
- Toronto Raptors: 44-35, L10: 5-5, streak: W1 — Chucky Hepburn OUT [roster-only]; Immanuel Quickley NOT in current verified absence feed — re-verify before any Toronto pick. L10 5-5 mixed.
- Phoenix Suns: 43-36, L10: 4-6, streak: L1 — NetRtg +1.4; L10 4-6 cold stretch; single-game bounce insufficient.
- Orlando Magic: 43-36, L10: 5-5, streak: W3 — NetRtg +0.2 near breakeven; cautious despite win streak.
- Miami Heat: 41-38, L10: 3-7, streak: L1 — NetRtg +1.8; L10 3-7 alarming; confirmed cold fade candidate.
- LA Clippers: 41-38, L10: 7-3, streak: W2 — NetRtg +1.6; play-in bubble; two-game bounce; neutral.
- Portland Trail Blazers: 40-39, L10: 7-3, streak: L1 — play-in bubble; motivation-positive but streak snapped; verify NetRtg before bets.
- Golden State Warriors: 37-42, L10: 4-6, streak: W1 — NetRtg -0.2; confirmed tank-watch; do not back GS without significant situational reason.

HOT STREAK FADE CANDIDATES:
- Philadelphia 76ers (43-36, L10: 6-4, streak: L2): NetRtg -0.4 — negative with losing streak; fade signal strong; any opponent at ≥ 1.70 warrants fade evaluation.
- Miami Heat (41-38, L10: 3-7): confirmed cold fade candidate — do not back Miami without strong situational reason.
- Los Angeles Lakers (50-29, streak: L3): Luka Doncic + Austin Reaves OUT fundamentally changes LAL ceiling; three-game losing streak confirms fade.
- Charlotte Hornets (43-37, streak: L1): NetRtg +5.2 solid but streak snapped; monitor if opponent has neutral/positive stats.
- Phoenix Suns (43-36, L10: 4-6): cold stretch confirmed; NetRtg only +1.4; fade-eligible vs motivated opponents.

Schedule seeding context (mid-April):
- OKC (63-16), Spurs (60-19), Pistons (57-22) locked into top-3 seeds — star rest risk very high; postseason clinch imminent for OKC.
- Denver (51-28, W9 streak) surging into top-3 West conversation — monitor rest patterns.
- Play-in bubble (seeds 7-10 East/West): Charlotte (43-37), Portland (40-39), Clippers (41-38), Miami (41-38) — motivation-positive for play-in teams, but Miami showing deteriorating form.
- Houston (50-29, W7) strong seeding push in West — motivated.
- Lakers effectively a different team without Doncic + Reaves — any LAL line requires fresh pricing context.
- GS Warriors (37-42, W1) and Toronto (44-35, W1) both borderline; Warriors tank-watch confirmed.

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
