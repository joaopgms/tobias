---
version: 12
updated_at: 2026-03-28T11:26:41.553824+00:00
updated_by: analyst_2026-03-28
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

New York Knicks:
- Miles McBride (G): OUT [roster-only]
- Kevin McCullar Jr. (G): OUT [roster-only]
- Landry Shamet (G): OUT [roster-only]

Boston Celtics:
- Nikola Vucevic (C): OUT [roster-only]

Los Angeles Lakers:
- Marcus Smart (G): OUT [roster-only]
NOTE: Anthony Davis and D'Angelo Russell were traded to Wizards. Do NOT apply their absences to Lakers games.

Minnesota Timberwolves:
- Anthony Edwards (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet Minnesota ML without re-verification.
- Jaden McDaniels (F): OUT [roster-only]

Cleveland Cavaliers:
- Craig Porter Jr. (G): OUT [roster-only]
- Jaylon Tyson (G): OUT [roster-only]
NOTE: Jarrett Allen, Dean Wade not in current verified feed — removed pending re-verification.

Houston Rockets:
- Steven Adams (C): OUT [roster-only]
- Fred VanVleet (G): OUT [roster-only]

Toronto Raptors:
- Chucky Hepburn (G): OUT [roster-only]
- Immanuel Quickley (G): OUT [roster-only] — FRANCHISE PLAYER. Do NOT bet Toronto ML without re-verification.

Washington Wizards:
- Anthony Davis (F): OUT [roster-only] — FRANCHISE PLAYER
- D'Angelo Russell (G): OUT [roster-only] — FRANCHISE PLAYER
- Trae Young (G): OUT [roster-only] — FRANCHISE PLAYER
- Kyshawn George (F): OUT [roster-only]
- Cam Whitmore (F): OUT [roster-only]
NOTE: Tre Young listed in injury landscape as Out (confirmed). Tre Johnson not in current verified feed — removed pending re-verification.

Franchise players requiring mandatory NBA official PDF verification before ANY pick involving their team:
- Cade Cunningham (Detroit) — verify before ANY Detroit pick
- Anthony Edwards (Minnesota) — verify before ANY Minnesota pick
- Immanuel Quickley (Toronto) — verify before ANY Toronto pick
- Any player flagged [roster-only] — these are NOT confirmed via official injury report

NOTE: Players removed from prior version not confirmed in current verified feed:
Adou Thiero (LAL), Jarrett Allen (CLE), Dean Wade (CLE), Tre Johnson (WAS), Alex Sarr (WAS),
Tristan Vukcevic (WAS), De'Aaron Fox (SAS), Luke Kornet (SAS), Marcus Sasser (DET),
Deandre Ayton (LAL), Rui Hachimura (LAL), Nick Smith Jr. (LAL), Aaron Gordon (DEN),
Max Strus (CLE) — removed pending re-verification as they do not appear in today's verified feed.

## SECTION:tanking_teams
Confirmed tanking-tier teams (all three criteria met):
- Washington Wizards: bottom of standings; 5 players OUT [roster-only] including franchise players (Davis, Russell, Young all OUT) — clearest tank in league
- Sacramento Kings: ~18-52, L10: 5-5 — worst record in West; L10 improvement unreliable, NetRtg worst in league
- Brooklyn Nets: ~17-52, L10: 2-8 — bottom East; extreme negative NetRtg
- Utah Jazz: ~20-49, L10: 2-8 — confirmed tank
- Dallas Mavericks: ~23-47, L10: 2-8 — confirmed tank
- Memphis Grizzlies: ~24-44 — NetRtg negative; verify pick ownership before bets
- Milwaukee Bucks: ~28-40, L10: 2-8 — verify pick ownership before each bet

Tanking criteria (ALL THREE must be met):
(a) Team owns its own 2026 draft pick
(b) Bad record confirmed by both W-L AND L10
(c) No realistic path to playoffs or play-in

When betting AGAINST tanking teams: edge-positive.
When betting ON tanking teams: require odds ≥ 2.20 and strong situational reason.

Emerging tank-watch:
- Chicago Bulls (~28-41, L10: 4-6) — borderline play-in; monitor
- New Orleans Pelicans (~24-46, L10: 6-4) — record tank-tier but L10 shows fight; treat as volatile, not confirmed tank
- Golden State Warriors: 36-38, L10: 4-6, streak: W3 — play-in bubble fading; NetRtg +0.3 barely above water; W3 streak is noise vs broader L10 4-6 pattern; treat as tank-watch

Hot streaks (may create line inefficiencies):
- OKC Thunder: 58-16, L10: 9-1, streak: W1 — elite team; NetRtg +10.9 best in league. Star rest risk increasing with postseason clinch near. Re-verify Thomas Sorber status before any OKC pick.
- San Antonio Spurs: 55-18, L10: 9-1, streak: W7 — efficiently priced; NetRtg +7.7; David Jones Garcia (F) OUT [roster-only]. Re-verify De'Aaron Fox status before any SAS pick (not in current verified feed).
- Detroit Pistons: 53-20, L10: 8-2, streak: W1 — Cade Cunningham OUT [roster-only]; do not bet Detroit ML without verification.
- Los Angeles Lakers: 48-26, L10: 9-1, streak: W2 — strong record; NetRtg only +1.7 vs record suggests positive run-differential luck; regression risk remains elevated.
- New York Knicks: 48-26, L10: 7-3, streak: L1 — NetRtg +6.7; top-seed contender East; streak cooling.
- Boston Celtics: 49-24, L10: 7-3, streak: W2 — NetRtg +7.7; seeding race with Knicks/Detroit live.
- Atlanta Hawks: 41-33, L10: 8-2, streak: L1 — re-emergence fading slightly; NetRtg +1.7 is low for 41-33 record; hot-streak-fade rule: W% ~.554 is marginally above .550 threshold — fade rule does NOT strictly apply, but NetRtg divergence from record is a regression signal.
- Charlotte Hornets: 39-34, L10: 7-3, streak: W5 — unexpected mid-table performer; NetRtg +4.9; play-in motivation positive.

HOT STREAK FADE CANDIDATES:
- Los Angeles Lakers (L10: 9-1, streak: W2): NetRtg +1.7 sharply below what 48-26 record implies — regression candidate. Any opponent at ≥ 1.80 warrants explicit fade evaluation.
- Atlanta Hawks (L10: 8-2, streak: L1): W% ~.554 at boundary of fade threshold; NetRtg +1.7 divergence is real; streak now broken — monitor if L1 extends.

Schedule seeding context (late March):
- OKC (58-16), Spurs (55-18), Pistons (53-20) locked into top-3 seeds — star rest risk increasing significantly
- Play-in bubble (seeds 7-10 East/West): Charlotte (39-34), Portland (37-38), Golden State (36-38), Clippers (38-36), Philadelphia (40-33) — motivation-positive for these teams
- Cleveland Cavaliers (46-28, L10: 7-3, streak: W1): 2 confirmed OUT [roster-only]; depth slightly depleted; treat with moderate caution.
- Minnesota Timberwolves (45-28, L10: 5-5, streak: W2): Anthony Edwards OUT [roster-only] — do not bet Minnesota ML without verification. Jaden McDaniels also OUT.
- Houston Rockets (44-29, L10: 5-5, streak: W1): Fred VanVleet OUT [roster-only]; momentum stabilising after prior skid.
- Miami Heat (39-35, L10: 4-6, streak: L1) — fading; NetRtg +2.4 mildly positive but L10 soft.
- Orlando Magic (39-34, L10: 4-6, streak: W1) — NetRtg +0.8 near breakeven; cautious.

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
