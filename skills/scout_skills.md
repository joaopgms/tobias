---
version: 23
updated_at: 2026-04-06T11:47:45.935284+00:00
updated_by: analyst_2026-04-06
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

Detroit Pistons:
- Cade Cunningham (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet Detroit ML without re-verification.
- Isaiah Stewart (F): OUT [roster-only]

Los Angeles Lakers:
- Luka Doncic (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet LAL ML without re-verification.
- Austin Reaves (G): OUT [roster-only] — key secondary player; LAL depth critically thin.
- Marcus Smart (G): OUT [roster-only]

Denver Nuggets:
- Spencer Jones (F): OUT [roster-only]
- Zeke Nnaji (F): OUT [roster-only]
- Peyton Watson (G): OUT [roster-only]

Cleveland Cavaliers:
- Jarrett Allen (C): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet CLE ML without re-verification.
- Evan Mobley (C): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet CLE ML without re-verification.
- Sam Merrill (G): OUT [roster-only]
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
- Immanuel Quickley (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet Toronto ML without re-verification.

Washington Wizards:
- Anthony Davis (F): OUT [roster-only] — FRANCHISE PLAYER
- Kyshawn George (F): OUT [roster-only + injury landscape confirmed]
- D'Angelo Russell (G): OUT [roster-only] — FRANCHISE PLAYER
- Alex Sarr (C): OUT [roster-only + injury landscape confirmed] — FRANCHISE PLAYER
- Cam Whitmore (F): OUT [roster-only]
- Trae Young (G): OUT [roster-only + injury landscape confirmed] — FRANCHISE PLAYER

NOTE: Tristan Vukcevic removed from verified feed this session — NOT in current verified list. Do NOT list as OUT.
NOTE: Nikola Vucevic (Boston) removed from verified feed this session — NOT in current verified list. Do NOT list as OUT.

Franchise players requiring mandatory NBA official PDF verification before ANY pick involving their team:
- Cade Cunningham (Detroit) — verify before ANY Detroit pick
- Luka Doncic (Los Angeles Lakers) — verify before ANY LAL pick
- Jarrett Allen + Evan Mobley (Cleveland) — BOTH out; verify before ANY CLE pick
- Immanuel Quickley (Toronto) — verify before ANY Toronto pick
- Any player flagged [roster-only] — these are NOT confirmed via official injury report

CRITICAL: Trae Young, Alex Sarr, Kyshawn George confirmed OUT via injury landscape feed this session.
Washington Wizards franchise player absences confirmed by BOTH roster-only AND injury landscape feeds — full tank confirmed.

CLEVELAND ALERT: Jarrett Allen AND Evan Mobley both OUT [roster-only] — dual franchise-level big man absence. CLE NetRtg +4.0 at severe risk. Do NOT bet CLE ML without NBA official PDF re-verification.
LOS ANGELES LAKERS ALERT: Luka Doncic AND Austin Reaves both OUT [roster-only] — two of top-3 offensive players absent. LAL ML bets require extreme caution; NetRtg +1.5 already tepid.

## SECTION:tanking_teams
Confirmed tanking-tier teams (all three criteria met):
- Washington Wizards: bottom of standings; Trae Young, Anthony Davis, D'Angelo Russell, Alex Sarr, Kyshawn George, Cam Whitmore all OUT — clearest tank in league. Do not bet Washington to win.
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
- Golden State Warriors: 36-42, L10: 3-7, streak: L4 — NetRtg -0.3 below breakeven; confirmed tank-watch. Play-in path fading rapidly.

Hot streaks and current form:
- OKC Thunder: 62-16, L10: 9-1, streak: W5 — elite; NetRtg +11.3 best in league. Thomas Sorber (C) OUT [roster-only]. Star rest risk high with postseason clinch near — re-verify full roster before any OKC pick.
- San Antonio Spurs: 59-19, L10: 9-1, streak: L1 — elite tier; NetRtg +8.2. Streak snapped; monitor for fatigue. David Jones Garcia OUT [roster-only]. Victor Wembanyama NOT in current verified absence feed — treat as potentially full-strength BUT re-verify via NBA official PDF before any pick.
- Detroit Pistons: 57-21, L10: 8-2, streak: W3 — Cade Cunningham OUT [roster-only]; Isaiah Stewart also OUT. Do not bet Detroit ML without verification. Strong record despite absences — depth-driven.
- Boston Celtics: 53-25, L10: 8-2, streak: W3 — NetRtg +8.1; seeding race live.
- New York Knicks: 50-28, L10: 7-3, streak: W2 — NetRtg +6.6; top-seed contender East.
- Los Angeles Lakers: 50-28, L10: 7-3, streak: L2 — NetRtg +1.5 sharply below .641 W% implied talent; Luka Doncic AND Austin Reaves OUT [roster-only] — CRITICAL dual absence; Marcus Smart also OUT. Do NOT bet LAL without re-verification; treat as severely depleted.
- Denver Nuggets: 50-28, L10: 9-1, streak: W8 — NetRtg +4.8; extended resurgence. Spencer Jones, Zeke Nnaji, Peyton Watson OUT [roster-only].
- Cleveland Cavaliers: 49-29, L10: 8-2, streak: W2 — Jarrett Allen AND Evan Mobley both OUT [roster-only] — CRITICAL dual big man absence; NetRtg +4.0 at risk. Do NOT bet CLE without NBA PDF re-verification.
- Houston Rockets: 49-29, L10: 8-2, streak: W6 — Fred VanVleet, Steven Adams OUT [roster-only]; NetRtg +5.1; six-game streak notable.
- Minnesota Timberwolves: 46-32, L10: 5-5, streak: L3 — Jaden McDaniels OUT [roster-only]; three-game losing streak; NetRtg +3.2. Re-verify before any MIN pick.
- Atlanta Hawks: 45-33, L10: 8-2, streak: W4 — NetRtg +2.6 divergence from .577 W% implied talent; hot-streak-fade rule applies. Jock Landale OUT [roster-only].
- Charlotte Hornets: 43-36, L10: 8-2, streak: W4 — NetRtg +5.3; play-in motivation positive; strong recent form.
- Philadelphia 76ers: 43-35, L10: 6-4, streak: L1 — NetRtg -0.2 deeply concerning for 43-35 record; significant regression risk.
- Toronto Raptors: 43-35, L10: 4-6, streak: L1 — Immanuel Quickley, Chucky Hepburn OUT [roster-only]; L10 4-6 and losing streak confirm cold patch; verify before any Toronto pick.
- Phoenix Suns: 43-35, L10: 4-6, streak: W1 — NetRtg +1.5; L10 4-6 and prior skid confirm cold stretch; single-game bounce insufficient to reverse fade status.
- Orlando Magic: 42-36, L10: 4-6, streak: W2 — NetRtg -0.1 near breakeven; L10 4-6 confirms volatility; cautious.
- Miami Heat: 41-37, L10: 3-7, streak: W1 — NetRtg +2.2; L10 3-7 alarming; confirmed cold fade candidate.
- LA Clippers: 40-38, L10: 6-4, streak: W1 — NetRtg +1.1; play-in bubble; one-game bounce after losing streak; neutral.
- Portland Trail Blazers: 40-38, L10: 8-2, streak: W3 — play-in bubble; motivation-positive; verify NetRtg before bets.
- Golden State Warriors: 36-42, L10: 3-7, streak: L4 — NetRtg -0.3; confirmed tank-watch; do not back GS without significant situational reason.

HOT STREAK FADE CANDIDATES:
- Atlanta Hawks (L10: 8-2, streak: W4): NetRtg +2.6 vs .577 W% — divergence real; opponents at ≥ 1.80 warrant fade evaluation.
- Philadelphia 76ers (43-35, L10: 6-4, streak: L1): NetRtg -0.2 — now negative; fade signal strengthening; any opponent at ≥ 1.70 warrants fade evaluation.
- Miami Heat (41-37, L10: 3-7): confirmed cold fade candidate — do not back Miami without strong situational reason.
- Los Angeles Lakers (50-28, streak: L2): Luka Doncic + Austin Reaves OUT fundamentally changes LAL ceiling; treat as significantly weakened.
- Toronto Raptors (43-35, L10: 4-6, streak: L1): losing streak + key absences + below-.600 L10 confirms fade candidate.

Schedule seeding context (mid-April):
- OKC (62-16), Spurs (59-19), Pistons (57-21) locked into top-3 seeds — star rest risk very high; postseason clinch imminent for OKC.
- Denver (50-28, W8 streak) surging into top-4 West conversation — monitor rest patterns.
- Play-in bubble (seeds 7-10 East/West): Charlotte (43-36, hot), Portland (40-38), Clippers (40-38), Miami (41-37) — motivation-positive for play-in teams, but Miami showing deteriorating form.
- CLE (49-29) with Allen + Mobley both out is a major line distortion risk — books may not have fully priced dual absence.
- Lakers effectively a different team without Doncic + Reaves — any LAL line requires fresh pricing context.
- GS Warriors (36-42, L4) and Toronto (43-35, L1, L10: 4-6) both trending downward into end-of-season; fade-eligible.

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
