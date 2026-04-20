---
version: 37
updated_at: 2026-04-20T12:02:13.352242+00:00
updated_by: analyst_2026-04-20
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

NOTE — PLAY-IN / PLAYOFF PHASE: All remaining teams are fully motivated. Roster-only flags MUST be re-verified against NBA official PDF each session before any pick.

Oklahoma City Thunder:
- Thomas Sorber (C): OUT [roster-only]
NOTE: Shai Gilgeous-Alexander, Jalen Williams, Chet Holmgren NOT in current verified absence feed — re-verify before any OKC pick. Previously in roster-only OUT — status may have changed. Top seed at 64-18.

San Antonio Spurs:
- David Jones Garcia (F): OUT [roster-only]
- Jordan McLaughlin (G): OUT [roster-only]
NOTE: Victor Wembanyama NOT in current verified absence feed — re-verify before any SAS pick. Previously in OUT feed; status may have changed. #2 seed at 62-20.

Detroit Pistons:
NOTE: No players in current verified absence feed. Re-verify Cade Cunningham, Isaiah Stewart, Jalen Duren before any DET pick.

Boston Celtics:
NOTE: No players in current verified absence feed. Jayson Tatum previously in roster-only OUT — status may have changed. Re-verify Jayson Tatum and Jaylen Brown before any BOS pick.

New York Knicks:
NOTE: No players in current verified absence feed. Jalen Brunson, Karl-Anthony Towns require re-verification before any NYK pick.

Denver Nuggets:
- Peyton Watson (G): OUT [roster-only]
NOTE: Nikola Jokic and Jamal Murray NOT in current verified absence feed — re-verify before any DEN pick. Denver on W12 streak; #6 seed in West bracket.

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
NOTE: Donovan Mitchell, Jarrett Allen, Evan Mobley NOT in current verified absence feed — re-verify before any CLE pick. Previously entire core was absent; status changed significantly.

Minnesota Timberwolves:
NOTE: No players in current verified absence feed. Anthony Edwards previously OUT [roster-only] — status may have changed. Re-verify Edwards, Rudy Gobert, Mike Conley, Julius Randle before any MIN pick.

Atlanta Hawks:
- Jock Landale (C): OUT [roster-only]
NOTE: Trae Young NOT in current verified absence feed for ATL — DATA CONFLICT: Trae Young appears in WAS feed. Verify official team affiliation via NBA official PDF before any ATL pick.

Toronto Raptors:
- Chucky Hepburn (G): OUT [roster-only]
- Immanuel Quickley (G): OUT [roster-only]

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
NOTE: Washington eliminated. Do NOT bet Washington to win under any circumstances.

Franchise players requiring mandatory NBA official PDF verification before ANY pick involving their team:
- Shai Gilgeous-Alexander, Jalen Williams, Chet Holmgren (OKC) — previously roster-only OUT; re-verify status this session
- Victor Wembanyama (SAS) — previously in OUT feed; re-verify status this session
- Jayson Tatum (BOS) — previously roster-only OUT; re-verify status this session
- Kevin Durant (HOU) — roster-only OUT; Sengun status changed — re-verify
- Luka Doncic (LAL) — roster-only OUT; removes primary offensive engine
- Anthony Davis, D'Angelo Russell, Alex Sarr (WAS) — confirmed OUT; team eliminated

## SECTION:tanking_teams
NOTE — PLAYOFF PHASE ACTIVE: See playoff_context.md no_tanking section. Tanking logic does NOT apply to any remaining play-in or playoff team. All remaining teams are motivated. Only apply tank logic to fully eliminated non-playoff teams.

Eliminated / no-motivation teams (not in play-in or playoffs):
- Washington Wizards: fully eliminated; Trae Young, Anthony Davis, D'Angelo Russell, Alex Sarr all OUT — clearest tank in league. Do not bet Washington to win.
- Sacramento Kings: eliminated from playoff/play-in contention.
- Brooklyn Nets: eliminated from playoff/play-in contention.
- Utah Jazz: eliminated from playoff/play-in contention.
- Dallas Mavericks: eliminated from playoff/play-in contention.
- Memphis Grizzlies: eliminated from playoff/play-in contention.
- Milwaukee Bucks: verify pick ownership before each bet; eliminated from play-in contention.
- Golden State Warriors (37-45, L3): NetRtg -0.4 — SEE playoff_context.md; verified 9-seed in West play-in. Under play-in phase, treat as motivated (win-or-go-home). Do NOT apply tank logic. After elimination, revert to fade candidate.

When betting AGAINST eliminated teams: edge-positive.
When betting ON eliminated teams: require odds ≥ 2.20 and strong situational reason.

Play-in and playoff teams (NOT tanking — all fully motivated):
- See playoff_context.md series_context for current bracket and seeding.
- Do NOT apply tanking penalties to any team listed in play-in participants or playoff bracket.

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
