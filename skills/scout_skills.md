---
version: 27
updated_at: 2026-04-10T11:46:18.591072+00:00
updated_by: analyst_2026-04-10
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
- Alex Caruso (G): OUT [roster-only]
- Shai Gilgeous-Alexander (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet OKC ML without re-verification.
- Isaiah Hartenstein (C): OUT [roster-only]
- Chet Holmgren (C): OUT [roster-only] — key big; OKC depth altered.
- Isaiah Joe (G): OUT [roster-only]
- Ajay Mitchell (G): OUT [roster-only]
- Thomas Sorber (C): OUT [roster-only]
- Cason Wallace (G): OUT [roster-only]
- Jalen Williams (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet OKC ML without re-verification.
- Jaylin Williams (F): OUT [roster-only]

NOTE: OKC has 10 players flagged OUT [roster-only] — this is an extraordinary number and likely reflects end-of-season rest/load management. Re-verify ALL OKC absences via NBA official PDF before any OKC pick. Do NOT draft OKC picks without verification.

San Antonio Spurs:
- David Jones Garcia (F): OUT [roster-only]

Denver Nuggets:
- Spencer Jones (F): OUT [roster-only]
- Peyton Watson (G): OUT [roster-only]

Los Angeles Lakers:
- Luka Doncic (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet LAL ML without re-verification.
- Austin Reaves (G): OUT [roster-only] — key secondary player; LAL depth critically thin.
- Marcus Smart (G): OUT [roster-only]

Houston Rockets:
- Steven Adams (C): OUT [roster-only]
- Fred VanVleet (G): OUT [roster-only]

Cleveland Cavaliers:
- Jarrett Allen (C): OUT [roster-only] — key big; affects CLE frontcourt depth.
- Thomas Bryant (C): OUT [roster-only]
- Sam Merrill (G): OUT [roster-only]
- Donovan Mitchell (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet CLE ML without re-verification.
- Jaylon Tyson (G): OUT [roster-only]

Minnesota Timberwolves:
- Anthony Edwards (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet MIN ML without re-verification.
- Rudy Gobert (C): OUT [roster-only] — FRANCHISE PLAYER (anchor big). Do NOT bet MIN ML without re-verification.
- Joe Ingles (F): OUT [roster-only]

Toronto Raptors:
- Chucky Hepburn (G): OUT [roster-only]

Atlanta Hawks:
- Jock Landale (C): OUT [roster-only]

Washington Wizards:
- Anthony Davis (F): OUT [roster-only + injury landscape confirmed] — FRANCHISE PLAYER
- Kyshawn George (F): OUT [roster-only]
- Tre Johnson (G): OUT [roster-only + injury landscape confirmed]
- D'Angelo Russell (G): OUT [roster-only] — FRANCHISE PLAYER
- Alex Sarr (C): OUT [roster-only + injury landscape confirmed] — FRANCHISE PLAYER
- Tristan Vukcevic (F): OUT [roster-only + injury landscape confirmed]
- Cam Whitmore (F): OUT [roster-only]
- Trae Young (G): OUT [roster-only] — FRANCHISE PLAYER

NOTE: Victor Wembanyama (SAS), Cade Cunningham (DET), Isaiah Stewart (DET), Immanuel Quickley (TOR), Jaden McDaniels (MIN) — NOT in current verified absence feed. Do NOT list as OUT. Re-verify via NBA official PDF before any pick involving their teams.

Franchise players requiring mandatory NBA official PDF verification before ANY pick involving their team:
- Shai Gilgeous-Alexander (OKC) — OUT [roster-only]; removes primary offensive engine. Verify before ANY OKC pick.
- Jalen Williams (OKC) — OUT [roster-only]; removes secondary star. Verify before ANY OKC pick.
- Luka Doncic (Los Angeles Lakers) — OUT [roster-only]; removes primary offensive engine. Verify before ANY LAL pick.
- Donovan Mitchell (Cleveland Cavaliers) — OUT [roster-only]; removes primary offensive engine. Verify before ANY CLE pick.
- Anthony Edwards (Minnesota Timberwolves) — OUT [roster-only]; removes primary offensive engine. Verify before ANY MIN pick.
- Rudy Gobert (Minnesota Timberwolves) — OUT [roster-only]; removes anchor defender. Verify before ANY MIN pick.
- Any player flagged [roster-only] — NOT confirmed via official injury report.

CRITICAL: Alex Sarr, Tristan Vukcevic, and Tre Johnson confirmed OUT via injury landscape feed this session.
Washington Wizards: Anthony Davis also confirmed via injury landscape. Full tank confirmed — Do NOT bet Washington to win.

OKC THUNDER ALERT: Shai Gilgeous-Alexander AND Jalen Williams AND Chet Holmgren AND Isaiah Hartenstein all OUT [roster-only] — effectively the entire starting lineup flagged. OKC picks require mandatory re-verification; treat as severely depleted until confirmed.

CLEVELAND CAVALIERS ALERT: Donovan Mitchell AND Jarrett Allen both OUT [roster-only] — franchise player and anchor big absent simultaneously. CLE ML bets require extreme caution; do NOT draft without verification.

LOS ANGELES LAKERS ALERT: Luka Doncic AND Austin Reaves both OUT [roster-only] — two of top-3 offensive players absent. LAL ML bets require extreme caution.

MINNESOTA TIMBERWOLVES ALERT: Anthony Edwards AND Rudy Gobert both OUT [roster-only] — franchise player and anchor big absent. Do NOT bet MIN ML without re-verification of both statuses.

## SECTION:tanking_teams
Confirmed tanking-tier teams (all three criteria met):
- Washington Wizards: bottom of standings; Trae Young, Anthony Davis, D'Angelo Russell, Alex Sarr, Tre Johnson, Kyshawn George, Cam Whitmore, Tristan Vukcevic all OUT — clearest tank in league. Do not bet Washington to win.
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
- Golden State Warriors: 37-43, L10: 4-6, streak: L1 — NetRtg -0.4 at breakeven; confirmed tank-watch. Play-in path eliminated or near-eliminated.

Current standings and form (updated this session):
- OKC Thunder: 64-16, L10: 9-1, streak: W7 — elite; NetRtg +12.0 best in league. CRITICAL: SGA, Jalen Williams, Chet Holmgren, Isaiah Hartenstein, Alex Caruso, Cason Wallace, Isaiah Joe, Ajay Mitchell, Thomas Sorber, Jaylin Williams all OUT [roster-only] — extraordinary end-of-season rest scenario; OKC effectively fielding a depleted roster. Do NOT draft OKC picks without full re-verification via NBA official PDF.
- San Antonio Spurs: 61-19, L10: 9-1, streak: W2 — elite tier; NetRtg +8.3. David Jones Garcia OUT [roster-only]. Victor Wembanyama NOT in current verified absence feed — re-verify before any SAS pick. Star rest risk elevated; top seed locked.
- Detroit Pistons: 58-22, L10: 7-3, streak: W1 — NetRtg +8.1; Cade Cunningham and Isaiah Stewart NOT in current verified absence feed — re-verify before any DET pick.
- Boston Celtics: 54-26, L10: 7-3, streak: L1 — NetRtg +8.0; seeding race active; streak snapped — monitor.
- Denver Nuggets: 52-28, L10: 10-0, streak: W10 — NetRtg +4.9; historic 10-game winning streak; Spencer Jones, Peyton Watson OUT [roster-only] (role players). HOT STREAK FLAG: Overall W% .650 above .550 threshold — do NOT auto-fade per rule, but monitor opponent stats carefully.
- New York Knicks: 52-28, L10: 7-3, streak: W4 — NetRtg +6.6; top-seed contender East; strong.
- Cleveland Cavaliers: 51-29, L10: 8-2, streak: W4 — NetRtg +4.3; CRITICAL: Donovan Mitchell AND Jarrett Allen both OUT [roster-only] — franchise player + anchor big absent. CLE record and streak may be misleading without star. Re-verify all CLE absences before any pick.
- Los Angeles Lakers: 51-29, L10: 6-4, streak: W1 — NetRtg +1.1; Luka Doncic, Austin Reaves, Marcus Smart all OUT [roster-only]. LAL record disguises severely depleted roster. Do NOT bet LAL without re-verification.
- Houston Rockets: 51-29, L10: 8-2, streak: W8 — Fred VanVleet, Steven Adams OUT [roster-only]; NetRtg +5.2; eight-game streak; play-in secured, seeding race live.
- Minnesota Timberwolves: 47-33, L10: 4-6, streak: L1 — Anthony Edwards AND Rudy Gobert both OUT [roster-only]; NetRtg +3.0; L10 4-6 with two stars missing. Do NOT bet MIN without verification.
- Toronto Raptors: 45-35, L10: 6-4, streak: W2 — NetRtg +2.4; Chucky Hepburn OUT [roster-only]; Immanuel Quickley NOT in current verified absence feed — re-verify before any TOR pick.
- Atlanta Hawks: 45-35, L10: 7-3, streak: L2 — NetRtg +2.5; Jock Landale OUT [roster-only]; two-game losing streak after hot spell; hot-streak-fade risk elevated.
- Orlando Magic: 44-36, L10: 6-4, streak: W4 — NetRtg +0.3; play-in motivated; verify roster before bets.
- Phoenix Suns: 44-36, L10: 5-5, streak: W1 — NetRtg +1.4; L10 5-5; single-game bounce; cautious.
- Charlotte Hornets: 43-37, L10: 7-3, streak: L1 — NetRtg +5.2; play-in motivation positive; streak snapped — monitor fade risk.
- Philadelphia 76ers: 43-37, L10: 5-5, streak: L3 — NetRtg -0.4 deeply concerning for record; fade candidate with three-game losing streak.
- Miami Heat: 41-39, L10: 3-7, streak: L2 — NetRtg +1.6; L10 3-7 alarming; confirmed cold fade candidate.
- LA Clippers: 41-39, L10: 7-3, streak: L1 — NetRtg +1.3; play-in bubble; streak snapped; neutral.
- Portland Trail Blazers: 40-40, L10: 6-4, streak: L2 — play-in bubble; motivation-positive but L2 losing streak; verify NetRtg before bets.
- Golden State Warriors: 37-43, L10: 4-6, streak: L1 — NetRtg -0.4; confirmed tank-watch; do not back GS without significant situational reason.

HOT STREAK FADE CANDIDATES:
- Philadelphia 76ers (43-37, L10: 5-5, streak: L3): NetRtg -0.4 — negative with three-game losing streak; fade signal strong.
- Miami Heat (41-39, L10: 3-7): confirmed cold fade candidate — do not back Miami without strong situational reason.
- Los Angeles Lakers (51-29, streak: W1): Luka Doncic + Austin Reaves + Marcus Smart OUT fundamentally changes LAL ceiling; treat record as inflated.
- Atlanta Hawks (45-35, streak: L2): NetRtg +2.5; second consecutive loss after hot period; fade risk elevated.
- Denver Nuggets (52-28, L10: 10-0): W% .650 above .550 threshold so hot-streak-fade rule does NOT auto-apply per selectivity rule; but 10-game streak warrants monitoring for regression — require NetRtg gap > 4.0 before backing opponent.

SCHEDULE SEEDING CONTEXT (mid-April — final regular season stretch):
- OKC (64-16), Spurs (61-19), Pistons (58-22) locked into top seeds — star rest risk MAXIMUM; top roster players being rested en masse. Treat OKC and SAS as severely depleted until verified.
- Denver (52-28, W10 streak) surging into top-3 West conversation — monitor rest patterns as seeding locks in.
- Play-in bubble (seeds 7-10 East/West): Charlotte (43-37), Portland (40-40), Clippers (41-39), Miami (41-39) — motivation-positive for play-in teams, but Miami showing deteriorating form.
- Houston (51-29, W8) strong seeding push in West — motivated.
- Cleveland (51-29, W4 streak) strong but Mitchell + Allen both missing — record may not reflect current capability.
- MIN without Edwards + Gobert is fundamentally altered — treat as bottom-tier team until verified.
- GS Warriors (37-43) tank-watch confirmed; Portland at .500 is play-in motivated.

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
