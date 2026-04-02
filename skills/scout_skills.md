---
version: 19
updated_at: 2026-04-02T11:43:30.572422+00:00
updated_by: analyst_2026-04-02
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
- Thomas Sorber (C): OUT [roster-only]

San Antonio Spurs:
- David Jones Garcia (F): OUT [roster-only]

Detroit Pistons:
- Cade Cunningham (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet Detroit ML without re-verification.
- Isaiah Stewart (F): OUT [roster-only]

Boston Celtics:
- Nikola Vucevic (C): OUT [roster-only]

Los Angeles Lakers:
- Marcus Smart (G): OUT [roster-only]

Cleveland Cavaliers:
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
- Anthony Davis (F): OUT [roster-only] — FRANCHISE PLAYER
- Kyshawn George (F): OUT [roster-only]
- D'Angelo Russell (G): OUT [roster-only] — FRANCHISE PLAYER
- Alex Sarr (C): OUT [roster-only] — FRANCHISE PLAYER (confirmed via injury landscape)
- Cam Whitmore (F): OUT [roster-only]
- Trae Young (G): OUT [roster-only] — FRANCHISE PLAYER (confirmed via injury landscape)

Franchise players requiring mandatory NBA official PDF verification before ANY pick involving their team:
- Cade Cunningham (Detroit) — verify before ANY Detroit pick
- Immanuel Quickley (Toronto) — verify before ANY Toronto pick
- Any player flagged [roster-only] — these are NOT confirmed via official injury report

NOTE: Players removed from verified feed this session vs prior session — no longer listed as OUT:
- Landry Shamet (NYK), Spencer Jones (DEN), Zeke Nnaji (DEN), Sam Merrill (CLE).
  Do NOT list these players as OUT until re-confirmed in a future verified feed.
  Re-verify NYK, DEN, CLE rosters carefully before any pick on those teams.

CRITICAL: Alex Sarr confirmed OUT via injury landscape feed this session — Washington remains full-tank.
Washington Wizards franchise player absences now confirmed by BOTH roster-only AND injury landscape feeds.

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
- Golden State Warriors: 36-40, L10: 4-6, streak: L2 — play-in bubble fading further; NetRtg -0.2 now below breakeven; treat as confirmed tank-watch. Two-game losing streak confirms trajectory.

Hot streaks (may create line inefficiencies):
- OKC Thunder: 60-16, L10: 9-1, streak: W3 — elite team; NetRtg +10.9 best in league. Thomas Sorber (C) OUT [roster-only] — bench depth only. Star rest risk increasing with postseason clinch near; re-verify full roster before any OKC pick.
- San Antonio Spurs: 58-18, L10: 10-0, streak: W10 — elite tier; NetRtg +8.2; L10 perfect run commands premium price. David Jones Garcia OUT [roster-only]. Re-verify all SAS players before any pick. CAUTION: 10-game winning streak may produce inflated odds against opponents — do not blindly fade.
- Detroit Pistons: 55-21, L10: 7-3, streak: W1 — Cade Cunningham OUT [roster-only]; Isaiah Stewart also OUT. Do not bet Detroit ML without verification.
- Los Angeles Lakers: 50-26, L10: 9-1, streak: W4 — strong recent form; NetRtg +2.1 vs record suggests run-differential luck; regression risk elevated. Marcus Smart OUT [roster-only].
- New York Knicks: 49-28, L10: 7-3, streak: W1 — NetRtg +6.2; top-seed contender East; streak recovered after prior L3 skid.
- Boston Celtics: 51-25, L10: 8-2, streak: W1 — NetRtg +7.7; seeding race live. Nikola Vucevic OUT [roster-only].
- Denver Nuggets: 49-28, L10: 8-2, streak: W7 — NetRtg +4.8; extended resurgence; re-verify depth.
- Atlanta Hawks: 44-33, L10: 8-2, streak: W3 — NetRtg +2.2 sharply below .571 W% implied talent; hot-streak-fade rule applies.
- Charlotte Hornets: 40-36, L10: 7-3, streak: W1 — NetRtg +4.9; play-in motivation positive.
- Cleveland Cavaliers: 47-29, L10: 7-3, streak: L1 — Jaylon Tyson, Dean Wade OUT [roster-only]. CAUTION: Sam Merrill, Jarrett Allen, Max Strus no longer in verified feed — re-verify before any pick.
- Houston Rockets: 47-29, L10: 6-4, streak: W4 — Fred VanVleet, Steven Adams OUT [roster-only]; NetRtg +4.7.
- Minnesota Timberwolves: 46-29, L10: 6-4, streak: W1 — Jaden McDaniels OUT [roster-only]; Anthony Edwards NOT in current verified feed — re-verify before any MIN pick.
- Toronto Raptors: 42-34, L10: 5-5, streak: L2 — Immanuel Quickley, Jamison Battle, Chucky Hepburn OUT [roster-only]; L10 now balanced; two-game skid; verify before any Toronto pick.
- Philadelphia 76ers: 42-34, L10: 7-3, streak: W1 — NetRtg -0.1 deeply concerning for 42-34 record; significant regression risk.
- Phoenix Suns: 42-34, L10: 3-7, streak: L1 — NetRtg +1.8; L10 3-7 confirms cold stretch despite mid-table record.
- Miami Heat: 40-37, L10: 2-8, streak: L1 — NetRtg +2.0; L10 2-8 alarming; fade candidate.
- Orlando Magic: 40-36, L10: 2-8, streak: L1 — NetRtg -0.2 near breakeven; L10 2-8 confirms volatility; cautious.
- Portland Trail Blazers: 39-38, L10: 7-3, streak: W2 — play-in bubble; motivation-positive; NetRtg data unavailable in feed, use with caution.

HOT STREAK FADE CANDIDATES:
- Los Angeles Lakers (L10: 9-1, streak: W4): NetRtg +2.1 sharply below what 50-26 record implies — regression candidate. Any opponent at ≥ 1.80 warrants explicit fade evaluation.
- Atlanta Hawks (L10: 8-2, streak: W3): W% ~.571 above .550 threshold; NetRtg +2.2 divergence from record is real; opponents at ≥ 1.80 warrant fade evaluation.
- Philadelphia 76ers (42-34, L10: 7-3, streak: W1): NetRtg -0.1 deeply concerning — significant regression risk; any opponent at ≥ 1.75 warrants fade evaluation.

Schedule seeding context (early April):
- OKC (60-16), Spurs (58-18), Pistons (55-21) locked into top-3 seeds — star rest risk increasing significantly.
- Play-in bubble (seeds 7-10 East/West): Charlotte (40-36), Portland (39-38), Golden State (36-40), Clippers (39-37), Miami (40-37) — motivation-positive for play-in teams, but Miami and Golden State showing deteriorating form.
- San Antonio Spurs 10-game winning streak: fully priced in by books; do not expect underdog value against them.

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
