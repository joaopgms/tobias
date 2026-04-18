---
version: 35
updated_at: 2026-04-18T11:33:06.380400+00:00
updated_by: analyst_2026-04-18
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

NOTE — PLAY-IN PHASE: All play-in teams are fully motivated. Star rest risk is low for play-in participants (win-or-go-home). Roster-only flags must be re-verified against NBA official PDF each session before any pick.

Oklahoma City Thunder:
- Shai Gilgeous-Alexander (G): OUT [roster-only] — FRANCHISE PLAYER
- Isaiah Hartenstein (C): OUT [roster-only] — key big
- Chet Holmgren (C): OUT [roster-only] — FRANCHISE PLAYER
- Isaiah Joe (G): OUT [roster-only]
- Ajay Mitchell (G): OUT [roster-only]
- Thomas Sorber (C): OUT [roster-only]
- Cason Wallace (G): OUT [roster-only]
- Jalen Williams (G): OUT [roster-only] — FRANCHISE PLAYER
- Jaylin Williams (F): OUT [roster-only]
NOTE: OKC has ALL major franchise players in roster-only OUT feed. Do NOT draft OKC picks without NBA official PDF verification. Top seed locked at 64-18 — star rest risk MAXIMUM.

San Antonio Spurs:
- David Jones Garcia (F): OUT [roster-only]
- Luke Kornet (C): OUT [roster-only]
- Victor Wembanyama (F): OUT [roster-only] — FRANCHISE PLAYER
NOTE: Victor Wembanyama in verified absence feed. Do NOT draft SAS picks without NBA official PDF verification. Star rest risk elevated; top-2 seed locked at 62-20.

Detroit Pistons:
- Jalen Duren (C): OUT [roster-only] — key big
NOTE: Cade Cunningham and Isaiah Stewart NOT in current verified absence feed — re-verify before any DET pick.

Boston Celtics:
- Jayson Tatum (F): OUT [roster-only] — FRANCHISE PLAYER
NOTE: Jaylen Brown NOT in current verified absence feed. Jayson Tatum in roster-only OUT feed — BOS franchise core critically thin. Do NOT draft BOS ML without re-verification.

New York Knicks:
- No players in current verified absence feed.
NOTE: Jalen Brunson, Karl-Anthony Towns — NOT in current verified absence feed. Re-verify before any NYK pick. Previous session had multiple roster-only OUT flags — status changed; treat as active until re-verified.

Denver Nuggets:
- Spencer Jones (F): OUT [roster-only]
- Peyton Watson (G): OUT [roster-only]
NOTE: Nikola Jokic and Jamal Murray NOT in current verified absence feed — re-verify before any DEN pick. Denver on W12 streak; seeding battle live. Murray previously flagged roster-only OUT — status may have changed.

Los Angeles Lakers:
- Luka Doncic (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet LAL ML without re-verification.
- Austin Reaves (G): OUT [roster-only] — key secondary player; LAL depth critically thin.

Houston Rockets:
- Steven Adams (C): OUT [roster-only]
- Kevin Durant (F): OUT [roster-only] — FRANCHISE PLAYER
- Fred VanVleet (G): OUT [roster-only]
NOTE: Alperen Sengun NOT in current verified absence feed — re-verify before any HOU pick. Durant remains in roster-only OUT feed. Do NOT draft HOU ML without NBA official PDF verification.

Cleveland Cavaliers:
- Thomas Bryant (C): OUT [roster-only]
NOTE: Donovan Mitchell, Jarrett Allen, Evan Mobley NOT in current verified absence feed — re-verify before any CLE pick. Previously entire core was absent; status may have changed significantly.

Minnesota Timberwolves:
- Anthony Edwards (G): OUT [roster-only] — FRANCHISE PLAYER
NOTE: Mike Conley, Rudy Gobert, Julius Randle NOT in current verified absence feed — re-verify status before any MIN pick. Edwards remains OUT.

Atlanta Hawks:
- Jock Landale (C): OUT [roster-only]
NOTE: Trae Young NOT in current verified absence feed — re-verify before any ATL pick. DATA CONFLICT: Trae Young appears in WAS feed — confirm official team affiliation via NBA official PDF.

Toronto Raptors:
- Chucky Hepburn (G): OUT [roster-only]
NOTE: Immanuel Quickley NOT in current verified absence feed — re-verify before any TOR pick.

Washington Wizards:
- Bilal Coulibaly (G): OUT [roster-only + injury landscape confirmed]
- Anthony Davis (F): OUT [roster-only] — FRANCHISE PLAYER
- Kyshawn George (F): OUT [roster-only]
- Tre Johnson (G): OUT [roster-only]
- D'Angelo Russell (G): OUT [roster-only] — FRANCHISE PLAYER
- Alex Sarr (C): OUT [roster-only + injury landscape confirmed] — FRANCHISE PLAYER
- Tristan Vukcevic (F): OUT [roster-only + injury landscape confirmed]
- Cam Whitmore (F): OUT [roster-only]
- Trae Young (G): OUT [roster-only] — FRANCHISE PLAYER (DATA CONFLICT: also appears in ATL feed — verify)
NOTE: Washington full tank confirmed. Do NOT bet Washington to win under any circumstances.

Franchise players requiring mandatory NBA official PDF verification before ANY pick involving their team:
- Shai Gilgeous-Alexander, Jalen Williams, Chet Holmgren (OKC) — roster-only OUT; top-seed rest risk maximum
- Victor Wembanyama (SAS) — verified absence feed; re-verify each session
- Jayson Tatum (BOS) — roster-only OUT; Jaylen Brown requires verification
- Kevin Durant (HOU) — roster-only OUT; Sengun status changed — re-verify
- Anthony Edwards (MIN) — roster-only OUT; Gobert/Conley/Randle status changed — re-verify
- Luka Doncic (LAL) — roster-only OUT; removes primary offensive engine

## SECTION:tanking_teams
NOTE — PLAY-IN PHASE ACTIVE: Tanking logic applies only to teams eliminated from play-in contention.
All play-in bubble teams (seeds 7-10) are fully motivated — do NOT apply tanking penalties to them.
See playoff_context.md no_tanking section for play-in rules.

Confirmed tanking-tier teams (eliminated from play-in, no motivation to win):
- Washington Wizards: bottom of standings; Trae Young, Anthony Davis, D'Angelo Russell, Alex Sarr all OUT — clearest tank in league. Do not bet Washington to win.
- Sacramento Kings: bottom West; worst record in West; NetRtg worst in league.
- Brooklyn Nets: bottom East; extreme negative NetRtg.
- Utah Jazz: confirmed tank.
- Dallas Mavericks: confirmed tank.
- Memphis Grizzlies: NetRtg negative; verify pick ownership before bets.
- Milwaukee Bucks: verify pick ownership before each bet.
- Golden State Warriors (37-45, L10: 3-7, streak: L3): NetRtg -0.4; eliminated from play-in contention — CONFIRMED TANK-WATCH. Do not back without significant situational edge.

Tanking criteria (ALL THREE must be met):
(a) Team owns its own 2026 draft pick
(b) Bad record confirmed by both W-L AND L10
(c) No realistic path to playoffs or play-in

When betting AGAINST tanking teams: edge-positive.
When betting ON tanking teams: require odds ≥ 2.20 and strong situational reason.

Play-in and seeding-contention teams (updated 2026-04-22 — NOT tanking):
- OKC Thunder: 64-18, L10: 7-3, streak: L2 — top seed locked; star rest risk MAXIMUM.
- San Antonio Spurs: 62-20, L10: 8-2, streak: L1 — #2 seed locked; Victor Wembanyama in OUT feed; rest risk elevated.
- Detroit Pistons: 60-22, L10: 8-2, streak: W3 — NetRtg +8.2; elite form.
- Boston Celtics: 56-26, L10: 8-2, streak: W2 — NetRtg +8.2; Jayson Tatum OUT [roster-only]; Jaylen Brown status requires verification.
- Denver Nuggets: 54-28, L10: 10-0, streak: W12 — HOT STREAK; NetRtg +5.2; Jokic/Murray status requires verification.
- New York Knicks: 53-29, L10: 6-4, streak: L1 — franchise core status changed from previous session; re-verify.
- Los Angeles Lakers: 53-29, L10: 7-3, streak: W3 — Luka Doncic + Reaves OUT [roster-only]; record inflated.
- Cleveland Cavaliers: 52-30, L10: 7-3, streak: W1 — previously entire core OUT; status changed — re-verify.
- Houston Rockets: 52-30, L10: 9-1, streak: W1 — Durant OUT [roster-only]; Sengun status changed — re-verify.
- Minnesota Timberwolves: 49-33, L10: 5-5, streak: W2 — Edwards OUT; Gobert/Conley/Randle status changed — re-verify.
- Atlanta Hawks: 46-36, L10: 6-4, streak: L1 — play-in secured; Trae Young requires verification (data conflict).
- Toronto Raptors: 46-36, L10: 6-4, streak: W1 — NetRtg +2.6; play-in race.
- Philadelphia 76ers: 45-37, L10: 6-4, streak: W2 — NetRtg -0.2; volatile; cautious.
- Orlando Magic: 45-37, L10: 7-3, streak: L1 — NetRtg +0.6; play-in motivated.
- Phoenix Suns: 45-37, L10: 5-5, streak: W1 — NetRtg +1.4; neutral.
- Charlotte Hornets: 44-38, L10: 6-4, streak: W1 — NetRtg +5.0; play-in bubble.
- Miami Heat: 43-39, L10: 5-5, streak: W2 — NetRtg +2.2; play-in bubble.
- Portland Trail Blazers: 42-40, L10: 7-3, streak: W2 — play-in bubble; motivation-positive.
- LA Clippers: 42-40, L10: 6-4, streak: W1 — NetRtg +1.1; play-in bubble.

HOT STREAK FLAGS:
- Denver Nuggets (W12, L10: 10-0): NetRtg +5.2; Jokic presence verification required before any directional bet.
- Los Angeles Lakers (W3): record disguises critically depleted roster — Doncic + Reaves OUT [roster-only].

EMERGING FADE CANDIDATES:
- Golden State Warriors (37-45, L3): NetRtg negative; confirmed tank-watch — eliminated from play-in.
- Orlando Magic (streak: L1): motivation positive but recent form dipping; neutral-cautious.
- Atlanta Hawks (streak: L1): verify Trae Young before any ATL pick (data conflict with WAS feed).

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
