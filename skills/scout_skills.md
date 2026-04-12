---
version: 29
updated_at: 2026-04-12T11:32:54.826472+00:00
updated_by: analyst_2026-04-12
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
- Shai Gilgeous-Alexander (G): OUT [roster-only] — FRANCHISE PLAYER
- Isaiah Hartenstein (C): OUT [roster-only] — key big
- Chet Holmgren (C): OUT [roster-only] — FRANCHISE PLAYER
- Isaiah Joe (G): OUT [roster-only]
- Ajay Mitchell (G): OUT [roster-only]
- Thomas Sorber (C): OUT [roster-only]
- Cason Wallace (G): OUT [roster-only]
- Jalen Williams (G): OUT [roster-only] — FRANCHISE PLAYER
- Jaylin Williams (F): OUT [roster-only]
NOTE: OKC has ALL major franchise players in roster-only OUT feed. Do NOT draft OKC picks without NBA official PDF verification. Top seed locked at 64-17 — star rest risk MAXIMUM.

San Antonio Spurs:
- David Jones Garcia (F): OUT [roster-only]
- Luke Kornet (C): OUT [roster-only]
NOTE: Victor Wembanyama NOT in current verified absence feed — re-verify before any SAS pick. Star rest risk elevated; top seed secured at 62-19.

Detroit Pistons:
- Jalen Duren (C): OUT [roster-only] — key big
NOTE: Cade Cunningham and Isaiah Stewart NOT in current verified absence feed — re-verify before any DET pick.

Boston Celtics:
- Jaylen Brown (G): OUT [roster-only] — FRANCHISE PLAYER
- Neemias Queta (C): OUT [roster-only]
- Jayson Tatum (F): OUT [roster-only] — FRANCHISE PLAYER
- Derrick White (G): OUT [roster-only] — key secondary player
NOTE: Both Tatum and Brown in roster-only OUT feed — BOS franchise player depth critically thin. Do NOT draft BOS ML without re-verification.

New York Knicks:
- OG Anunoby (F): OUT [roster-only] — key wing
- Jalen Brunson (G): OUT [roster-only] — FRANCHISE PLAYER
- Josh Hart (G): OUT [roster-only] — key secondary player
- Tyler Kolek (G): OUT [roster-only]
- Mitchell Robinson (C): OUT [roster-only]
- Karl-Anthony Towns (C): OUT [roster-only] — FRANCHISE PLAYER
NOTE: NYK has multiple franchise-level players in roster-only OUT feed. Do NOT draft NYK ML without NBA official PDF verification.

Denver Nuggets:
- Christian Braun (G): OUT [roster-only]
- Aaron Gordon (F): OUT [roster-only] — key piece
- Tim Hardaway Jr. (G): OUT [roster-only]
- Cameron Johnson (F): OUT [roster-only]
- Spencer Jones (F): OUT [roster-only]
- Jamal Murray (G): OUT [roster-only] — FRANCHISE PLAYER
- Peyton Watson (G): OUT [roster-only]
NOTE: Nikola Jokic NOT in current verified absence feed — re-verify before any DEN pick. Jamal Murray in roster-only OUT feed — DEN depth significantly altered without Murray.

Los Angeles Lakers:
- Luka Doncic (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet LAL ML without re-verification.
- Jaxson Hayes (C): OUT [roster-only] — key big
- Austin Reaves (G): OUT [roster-only] — key secondary player; LAL depth critically thin.

Houston Rockets:
- Steven Adams (C): OUT [roster-only]
- Kevin Durant (F): OUT [roster-only] — FRANCHISE PLAYER
- Alperen Sengun (C): OUT [roster-only] — FRANCHISE PLAYER
- Jabari Smith Jr. (F): OUT [roster-only]
- Amen Thompson (G): OUT [roster-only]
- Fred VanVleet (G): OUT [roster-only]
NOTE: Houston has Durant AND Sengun in roster-only OUT feed. Do NOT draft HOU ML without NBA official PDF verification.

Cleveland Cavaliers:
- Jarrett Allen (C): OUT [roster-only] — FRANCHISE PLAYER
- Thomas Bryant (C): OUT [roster-only]
- Keon Ellis (G): OUT [roster-only]
- James Harden (G): OUT [roster-only] — FRANCHISE PLAYER
- Sam Merrill (G): OUT [roster-only]
- Donovan Mitchell (G): OUT [roster-only] — FRANCHISE PLAYER
- Evan Mobley (C): OUT [roster-only] — FRANCHISE PLAYER
- Dennis Schroder (G): OUT [roster-only]
- Dean Wade (F): OUT [roster-only]
NOTE: CLE has Mitchell, Allen, Mobley, Harden all in roster-only OUT feed — virtually entire core absent. Do NOT draft CLE without NBA official PDF verification.

Minnesota Timberwolves:
- Kyle Anderson (F): OUT [roster-only]
- Mike Conley (G): OUT [roster-only]
- Ayo Dosunmu (G): OUT [roster-only]
- Anthony Edwards (G): OUT [roster-only] — FRANCHISE PLAYER
- Rudy Gobert (C): OUT [roster-only] — FRANCHISE PLAYER
- Bones Hyland (G): OUT [roster-only]
- Jaden McDaniels (F): OUT [roster-only] — key wing
- Julius Randle (F): OUT [roster-only] — FRANCHISE PLAYER
- Naz Reid (C): OUT [roster-only] — key big
NOTE: MIN has Edwards, Gobert, Randle all in roster-only OUT feed — virtually entire core absent. Do NOT draft MIN without NBA official PDF verification.

Atlanta Hawks:
- Jock Landale (C): OUT [roster-only]

Toronto Raptors:
- Chucky Hepburn (G): OUT [roster-only]
NOTE: Immanuel Quickley NOT in current verified absence feed — re-verify before any TOR pick.

Washington Wizards:
- Bilal Coulibaly (G): OUT [roster-only + injury landscape confirmed]
- Anthony Davis (F): OUT [roster-only] — FRANCHISE PLAYER
- Kyshawn George (F): OUT [roster-only]
- Tre Johnson (G): OUT [roster-only + injury landscape confirmed]
- D'Angelo Russell (G): OUT [roster-only] — FRANCHISE PLAYER
- Alex Sarr (C): OUT [roster-only + injury landscape confirmed] — FRANCHISE PLAYER
- Tristan Vukcevic (F): OUT [roster-only + injury landscape confirmed]
- Cam Whitmore (F): OUT [roster-only]
- Trae Young (G): OUT [roster-only] — FRANCHISE PLAYER
NOTE: Washington full tank confirmed. Do NOT bet Washington to win under any circumstances.

Franchise players requiring mandatory NBA official PDF verification before ANY pick involving their team:
- Shai Gilgeous-Alexander, Jalen Williams, Chet Holmgren (OKC) — roster-only OUT; top-seed rest risk maximum
- Jayson Tatum, Jaylen Brown (BOS) — roster-only OUT; franchise core absent
- Jalen Brunson, Karl-Anthony Towns (NYK) — roster-only OUT; franchise core absent
- Jamal Murray (DEN) — roster-only OUT; Jokic status requires verification
- Kevin Durant, Alperen Sengun (HOU) — roster-only OUT; franchise duo absent
- Donovan Mitchell, Jarrett Allen, Evan Mobley, James Harden (CLE) — roster-only OUT; entire core absent
- Anthony Edwards, Rudy Gobert, Julius Randle (MIN) — roster-only OUT; entire core absent
- Luka Doncic (LAL) — roster-only OUT; removes primary offensive engine
- Luka Doncic (Los Angeles Lakers) — OUT [roster-only]; removes primary offensive engine.

## SECTION:tanking_teams
Confirmed tanking-tier teams (all three criteria met):
- Washington Wizards: bottom of standings; Trae Young, Anthony Davis, D'Angelo Russell, Alex Sarr, Tre Johnson, Kyshawn George, Cam Whitmore, Tristan Vukcevic, Bilal Coulibaly all OUT — clearest tank in league. Do not bet Washington to win.
- Sacramento Kings: ~18-52 region, L10: 5-5 — worst record in West; NetRtg worst in league.
- Brooklyn Nets: ~17-52 region, L10: 2-8 — bottom East; extreme negative NetRtg.
- Utah Jazz: ~20-49 region, L10: 2-8 — confirmed tank.
- Dallas Mavericks: ~23-47 region, L10: 2-8 — confirmed tank.
- Memphis Grizzlies: ~24-44 region — NetRtg negative; verify pick ownership before bets.
- Milwaukee Bucks: ~28-40 region, L10: 2-8 — verify pick ownership before each bet.

Tanking criteria (ALL THREE must be met):
(a) Team owns its own 2026 draft pick
(b) Bad record confirmed by both W-L AND L10
(c) No realistic path to playoffs or play-in

When betting AGAINST tanking teams: edge-positive.
When betting ON tanking teams: require odds ≥ 2.20 and strong situational reason.

Emerging tank-watch:
- Chicago Bulls (~28-41 region, L10: 4-6) — borderline play-in; monitor.
- New Orleans Pelicans (~24-46 region, L10: 6-4) — record tank-tier but L10 shows fight; treat as volatile, not confirmed tank.
- Golden State Warriors: 37-44, L10: 4-6, streak: L2 — NetRtg -0.4; confirmed tank-watch. Play-in path eliminated or near-eliminated.

Current standings and form (updated this session — 2026-04-19):
- OKC Thunder: 64-17, L10: 8-2, streak: L1 — elite; NetRtg +11.6 best in league. Top seed locked; Shai Gilgeous-Alexander, Jalen Williams, Chet Holmgren, Isaiah Hartenstein all roster-only OUT — star rest risk MAXIMUM. Do NOT draft OKC picks without NBA official PDF verification.
- San Antonio Spurs: 62-19, L10: 9-1, streak: W3 — elite tier; NetRtg +8.5. David Jones Garcia, Luke Kornet OUT [roster-only]. Victor Wembanyama NOT in current verified absence feed — re-verify before any SAS pick. Star rest risk elevated.
- Detroit Pistons: 59-22, L10: 7-3, streak: W2 — NetRtg +8.2; Jalen Duren OUT [roster-only]. Cade Cunningham and Isaiah Stewart NOT in current verified absence feed — re-verify before any DET pick.
- Boston Celtics: 55-26, L10: 8-2, streak: W1 — NetRtg +8.2; Jayson Tatum AND Jaylen Brown AND Derrick White all roster-only OUT. BOS franchise core critically depleted — Do NOT draft BOS without re-verification.
- New York Knicks: 53-28, L10: 7-3, streak: W5 — NetRtg +6.7; Jalen Brunson AND Karl-Anthony Towns AND OG Anunoby AND Josh Hart all roster-only OUT. NYK franchise core critically depleted — Do NOT draft NYK without re-verification.
- Denver Nuggets: 53-28, L10: 10-0, streak: W11 — NetRtg +5.1; Jamal Murray, Aaron Gordon, Christian Braun, Cameron Johnson, Tim Hardaway Jr. all roster-only OUT. HOT STREAK FLAG: 11-game winning streak; Nikola Jokic status requires re-verification. Require NetRtg gap > 4.0 before backing opponent fade.
- Los Angeles Lakers: 52-29, L10: 6-4, streak: W2 — NetRtg +1.5; Luka Doncic, Austin Reaves, Jaxson Hayes all OUT [roster-only]. LAL record disguises severely depleted roster. Do NOT bet LAL without re-verification.
- Cleveland Cavaliers: 51-30, L10: 7-3, streak: L1 — NetRtg +3.9; Donovan Mitchell, Jarrett Allen, Evan Mobley, James Harden, Dennis Schroder all roster-only OUT — virtually entire competitive core absent. Do NOT draft CLE without NBA official PDF verification.
- Houston Rockets: 51-30, L10: 8-2, streak: L1 — Kevin Durant AND Alperen Sengun AND Fred VanVleet all roster-only OUT; NetRtg +5.1; seeding race live but franchise core depleted. Do NOT draft HOU without re-verification.
- Minnesota Timberwolves: 48-33, L10: 5-5, streak: W1 — NetRtg +3.0; Anthony Edwards, Rudy Gobert, Julius Randle, Jaden McDaniels all roster-only OUT — entire core absent. Do NOT draft MIN without NBA official PDF verification.
- Atlanta Hawks: 46-35, L10: 7-3, streak: W1 — NetRtg +2.7; Jock Landale OUT [roster-only]. Play-in secured; monitoring streak sustainability.
- Toronto Raptors: 45-36, L10: 5-5, streak: L1 — NetRtg +2.2; Chucky Hepburn OUT [roster-only]; Immanuel Quickley NOT in current verified absence feed — re-verify before any TOR pick.
- Orlando Magic: 45-36, L10: 7-3, streak: W5 — NetRtg +0.6; play-in motivated; verify roster before bets.
- Philadelphia 76ers: 44-37, L10: 5-5, streak: W1 — NetRtg -0.4; negative rating with volatile L10; cautious.
- Phoenix Suns: 44-37, L10: 5-5, streak: L1 — NetRtg +1.0; L10 5-5; neutral.
- Charlotte Hornets: 43-38, L10: 6-4, streak: L2 — NetRtg +4.9; play-in motivation positive but two-game losing streak; fade risk elevated.
- Miami Heat: 42-39, L10: 4-6, streak: W1 — NetRtg +1.9; L10 4-6; single-game bounce; confirmed cold team — cautious.
- Portland Trail Blazers: 41-40, L10: 6-4, streak: W1 — play-in bubble; motivation-positive; verify NetRtg before bets.
- LA Clippers: 41-40, L10: 6-4, streak: L2 — NetRtg +1.1; play-in bubble; two-game losing streak; neutral-cautious.
- Golden State Warriors: 37-44, L10: 4-6, streak: L2 — NetRtg -0.4; confirmed tank-watch; do not back GS without significant situational reason.

HOT STREAK FADE CANDIDATES:
- Denver Nuggets (53-28, L10: 10-0, W11): Requires Jokic presence verification before any directional bet; opposing-team fade requires NetRtg gap > 4.0 AND verification of DEN roster state.
- Charlotte Hornets (43-38, streak: L2): NetRtg +4.9 but two-game losing streak after strong L10; fade risk elevated.
- Miami Heat (42-39, L10: 4-6): confirmed cold fade candidate — do not back Miami without strong situational reason.
- Los Angeles Lakers (52-29, streak: W2): Luka Doncic + Austin Reaves + Jaxson Hayes OUT fundamentally changes LAL ceiling; treat record as inflated.

SCHEDULE SEEDING CONTEXT (mid-to-late April — final regular season stretch):
- OKC (64-17), Spurs (62-19), Pistons (59-22) locked into top seeds — star rest risk MAXIMUM. Treat as severely depleted until verified each session.
- BOS, NYK, CLE, HOU all have multiple franchise-level players in roster-only OUT feed — NONE of these teams are safe to pick without NBA official PDF verification this session.
- Denver (53-28, W11 streak) surging; Jokic status must be verified before any DEN directional bet.
- Play-in bubble (seeds 7-10 East/West): Charlotte (43-38), Portland (41-40), Clippers (41-40), Miami (42-39) — motivation-positive for play-in teams.
- MIN without verified Edwards + Gobert + Randle status is fundamentally altered — treat as volatile until confirmed.
- GS Warriors (37-44) tank-watch confirmed; Portland at .506 is play-in motivated.

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
