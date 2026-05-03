---
version: 23
updated_at: 2026-05-03T11:40:18.924657+00:00
updated_by: analyst_2026-05-03
llm: claude-sonnet-4-6
---

## SECTION:phase
First Round Playoffs — Game 7 Stage (and Game 6 closing games)

Play-In Tournament is OVER. First Round Playoffs (best-of-7) are active.
Apply series context, elimination urgency, and Round 1 rest rules — NOT play-in rules.
playin_rules section is INACTIVE this phase — ignore it entirely.

Active series this session:
- BOS vs PHI: Tied 3-3 — GAME 7 NEXT
- ORL vs DET: ORL leads 3-2 — GAME 7 NEXT (ESPN feed previously showed 'Tied 3-3 Game 8' — treat ORL leads 3-2 as ground truth)
- CLE vs TOR: CLE leads 3-2 — GAME 7 NEXT
- LAL vs HOU: LAL leads 4-2 — GAME 7 NEXT
- NYK vs ATL: DATA CONFLICT — ESPN shows NYK leads 4-2 Game 7 next vs prior context complete. VERIFY before any pick.
- MIN vs DEN: DATA CONFLICT — ESPN shows MIN leads 4-2 Game 7 next vs prior context complete. VERIFY before any pick.
- SAS vs POR: SAS leads 4-1 — Game 6 next (verify if concluded; SAS can close).
- OKC vs PHX: OKC leads 4-0 — ESPN shows 'Game 5' which is DATA ANOMALY. Treat as SERIES COMPLETE unless ESPN explicitly confirms Game 5 is live.

DATA QUALITY WARNING: ESPN live feed has shown persistent anomalies (Game 8 listings, Game 5 after 4-0, completion status conflicts). Scout and Commit MUST verify individual series status from ESPN before drafting any pick this session.

## SECTION:series_context
FIRST ROUND PLAYOFFS — Active (updated 2026-05-03)

DATA CONFLICT WARNING: ESPN live feed diverges from prior context on several series. Ground truth = ESPN live feed. Verify each series before pick.

EAST Round 1:
- Boston Celtics vs Philadelphia 76ers: Tied 3-3 — GAME 7 NEXT.
  CRITICAL: Jayson Tatum is roster-only OUT — re-verify via NBA official PDF before ANY BOS pick. If Tatum confirmed OUT, BOS loses primary scorer — PHI upset risk increases substantially.
  Verify Game 7 home court from ESPN — decisive.
  BOS (+8.2 NetRtg) vs PHI (-0.2 NetRtg) — massive statistical gap. PHI won Games 5 AND 6 (survival momentum +5 confidence).
  PHI roster is depleted but has demonstrated genuine playoff resilience. Home court is primary tiebreaker.
  In-series: tied 3-3. ML only — do NOT bet spread in Game 7.
  Bet thesis: BOS ML if Tatum confirmed active + BOS home + standard NetRtg edge. PHI ML only if PHI home + odds ≥ 1.90 + Tatum confirmed OUT.

- Orlando Magic vs Detroit Pistons: ORL leads 3-2 — GAME 7 NEXT.
  ESPN feed previously showed 'Tied 3-3 Game 8' — data anomaly; treat ORL leads 3-2 Game 7 as ground truth.
  Verify home court from ESPN — critical.
  ORL (NetRtg +0.6) vs DET (NetRtg +8.2) — DET 7.6pt statistical edge has NOT translated. ORL scheme/execution override confirmed over 5 games.
  Do NOT use DET NetRtg as primary signal. ORL in-series lead is the primary input.
  Re-verify DET franchise players (Cunningham, Stewart, Duren). ML only in Game 7.

- New York Knicks vs Atlanta Hawks: DATA CONFLICT.
  Prior context = series COMPLETE (NYK won 4-2). ESPN live = NYK leads 4-2, Game 7 next.
  VERIFY from ESPN before any NYK pick. If complete: NYK to Round 2, no further picks. If Game 7: NYK (NetRtg +6.5) vs ATL (+2.4), NYK favoured at home, ML only.

- Cleveland Cavaliers vs Toronto Raptors: CLE leads 3-2 — GAME 7 NEXT.
  Verify home court from ESPN — critical.
  CLE (NetRtg +4.0) vs TOR (NetRtg +2.6). Quickley OUT for TOR reduces offensive ceiling significantly.
  CLE should be favoured in Game 7. TOR fighting for survival with depleted rotation.
  Re-verify CLE and TOR rosters before any pick. ML only in Game 7.

WEST Round 1:
- Oklahoma City Thunder vs Phoenix Suns: OKC leads 4-0 — SERIES COMPLETE (treat as such).
  ESPN shows 'Game 5 next' — confirmed DATA ANOMALY. No further picks on OKC-PHX.
  OKC advances to Round 2. Re-verify SGA, Chet Holmgren, Jalen Williams for Round 2 matchup.

- Los Angeles Lakers vs Houston Rockets: LAL leads 4-2 — GAME 7 NEXT.
  ESPN live feed is ground truth (prior session context showed 3-2 — ESPN 4-2 overrides).
  Verify home court from ESPN — critical.
  LAL (+1.7 NetRtg) vs HOU (+5.4 NetRtg) — HOU has better season stats but LAL has dominated series 4-2.
  Luka Doncic (LAL): roster-only OUT — confirmed absent; LAL still winning without him.
  Kevin Durant (HOU): roster-only OUT — CRITICAL. Do NOT draft HOU ML without Durant confirmed active via NBA official PDF.
  Game 7: ML only. Do NOT bet LAL spread — garbage time / blowout risk.
  HOU valid pick only if: Durant confirmed active + HOU home court + odds ≥ 2.00.

- San Antonio Spurs vs Portland Trail Blazers: SAS leads 4-1 — Game 6 next.
  Verify from ESPN if Game 6 has been played and series concluded.
  SAS (NetRtg +8.3) vs POR (-0.2 NetRtg) — 8.5pt gap reflected in dominant series performance.
  Re-verify Victor Wembanyama active before any SAS pick. SAS ML valid at ≥ 1.70 if Wembanyama active.
  Do NOT bet SAS spread at < 1.75 — closing looseness risk.

- Minnesota Timberwolves vs Denver Nuggets: DATA CONFLICT.
  Prior context = series COMPLETE (MIN won 4-2). ESPN live = MIN leads 4-2, Game 7 next.
  VERIFY from ESPN before any MIN/DEN pick.
  If complete: MIN to Round 2. Anthony Edwards re-verify for Round 2.
  If Game 7: Aaron Gordon OUT for DEN. Edwards status critical — re-verify. MIN (NetRtg +3.1) vs DEN (+5.2). Verify home court.

## SECTION:elimination_flags
ROUND 1 ELIMINATION FLAGS (as of 2026-05-03):

DATA CONFLICT ALERT: ESPN live feed diverges from prior session context on several series. Treat ESPN live feed as ground truth. Verify each series before pick.

Series confirmed complete:
- Oklahoma City Thunder vs Phoenix Suns: OKC wins 4-0. ESPN 'Game 5' is a feed anomaly. PHX ELIMINATED. No further picks. OKC advances to Round 2.

Series with DATA CONFLICTS (must verify from ESPN before ANY pick):
- New York Knicks vs Atlanta Hawks: Prior context = COMPLETE (NYK won 4-2). ESPN live = NYK leads 4-2, Game 7 next. VERIFY BEFORE ANY PICK. If complete: ATL eliminated, NYK to Round 2. If Game 7: NYK favoured.
- Minnesota Timberwolves vs Denver Nuggets: Prior context = COMPLETE (MIN won 4-2). ESPN live = MIN leads 4-2, Game 7 next. VERIFY BEFORE ANY PICK. If complete: DEN eliminated, MIN to Round 2. If Game 7: Aaron Gordon OUT for DEN; verify Edwards.

Teams facing elimination (Game 7 — one loss = out):
- Philadelphia 76ers: Tied 3-3 vs BOS. Game 7 must-win. Jayson Tatum roster-only OUT for BOS — if confirmed, PHI's elimination odds improve significantly. Re-verify Tatum before any pick.
- Detroit Pistons: ORL leads 3-2 vs DET. Game 7 must-win. ORL has tactically dominated despite inferior NetRtg. Verify home court.
- Toronto Raptors: CLE leads 3-2 vs TOR. Game 7 must-win. Quickley OUT reduces TOR ceiling. TOR survival odds limited.
- Houston Rockets: LAL leads 4-2 vs HOU. Game 7 must-win. Durant status unresolved — CRITICAL. Do NOT draft HOU ML without Durant confirmed active.
- Portland Trail Blazers: SAS leads 4-1 vs POR. Game 6 may already be final — verify if concluded.

Teams that can close in next game:
- Los Angeles Lakers: leads 4-2, Game 7. LAL win = series close. No LAL spread in Game 7.
- Boston Celtics: Tied 3-3, Game 7. Must verify Tatum status FIRST — series edge depends on it.
- Orlando Magic: leads 3-2, Game 7. Can close despite inferior NetRtg.
- Cleveland Cavaliers: leads 3-2, Game 7. CLE favoured; verify home court.
- San Antonio Spurs: leads 4-1, Game 6. Likely to close — verify if already concluded.

## SECTION:playoff_rest
ROUND 1 REST RULES (active):
- True B2B does NOT exist in playoffs — NBA mandates minimum 1 day off between games.
- 1 rest day (minimum): short rest — confidence -10 on spread picks for the road team.
- 2 rest days: standard rest — no adjustment.
- 3+ rest days: extended rest — slight rust risk for hot teams; confidence -5.
- Home court advantage in playoffs worth ~3-4 points (stronger than regular season ~2-3pts).

Verify actual rest days from ESPN scoreboard — do not assume.

## SECTION:playoff_motivation
Playoff motivation hierarchy (Round 1 — Game 7/closing stage, updated 2026-05-03):

1. GAME 7 (maximum desperation — both teams fully committed; season on the line):
   Active Game 7s: BOS vs PHI, ORL vs DET, CLE vs TOR, LAL vs HOU.
   VERIFY: NYK vs ATL and MIN vs DEN — ESPN feed shows Game 7 next despite prior context showing complete; confirm from ESPN.
   → Home team in Game 7: add confidence +8 (home floor historically +60% win rate in G7).
   → Road team in Game 7: add confidence +5 (nothing-to-lose factor). Require odds ≥ 1.90.
   → Do NOT bet spread in Game 7 — blowout or wire-to-wire grind equally possible. ML only.
   → In Game 7, in-series result is primary context; NetRtg and home court are the main inputs.

2. TATUM OUT WILDCARD — BOS vs PHI Game 7 (NEW — highest priority flag this session):
   → Jayson Tatum is roster-only OUT for BOS. If confirmed OUT via NBA official PDF:
     - PHI upset probability increases substantially. Do NOT bet BOS ML without Tatum confirmation.
     - If Tatum confirmed OUT: PHI ML with home court becomes legitimate pick (odds likely ≥ 1.90).
     - If Tatum confirmed ACTIVE: BOS standard Game 7 analysis applies (home court + NetRtg + +8 home).
   → This is the most consequential franchise player flag for this session.

3. PHI SURVIVAL MOMENTUM (compound factor — earned across Games 5 AND 6):
   → PHI won two consecutive elimination games: apply confidence +5 for PHI in Game 7.
   → PHI depleted roster limits ceiling — BOS NetRtg (+8.2pt gap) is primary lean IF Tatum active.
   → PHI at home in Game 7 (if verified): +8 home + +5 survival = meaningful confidence boost. Respect.
   → PHI on road in Game 7: +5 road G7 + +5 survival = moderate factor. Require odds ≥ 2.00.

4. ORL TACTICAL DOMINANCE FACTOR:
   → ORL leads DET 3-2 despite 7.6pt NetRtg disadvantage — scheme has overridden stats all series.
   → In Game 7, respect ORL's in-series edge over DET. Do NOT over-weight DET NetRtg.
   → Home court is the primary tiebreaker. Verify Game 7 location before any pick.

5. HOU DURANT WILDCARD (Game 7 vs LAL — LAL leads 4-2):
   → Durant status unresolved — do NOT draft HOU ML unless Durant confirmed active.
   → If Durant confirmed active + HOU has home court: legitimate Game 7 upset risk.
   → LAL tactical dominance across 5+ games (Doncic absent) is the baseline.
   → Require HOU odds ≥ 2.00 even with Durant active.

6. SERIES MOMENTUM (SAS closing — leads 4-1):
   → SAS can close in Game 6. Verify game has not already concluded.
   → SAS ML at ≥ 1.70 valid if Wembanyama confirmed active. NetRtg gap (+8.5pts) consistently reflected.
   → Do NOT bet SAS spread at < 1.75 — closing looseness risk.

7. HOME COURT ADVANTAGE (Game 7s):
   → Playoff home court worth 3-4 points — decisive in close matchups.
   → Game 7 home court win rate historically ~60-65% in NBA.
   → Verify home court for EVERY pick from ESPN before drafting.

8. CLOSING TEAM CAUTION:
   → SAS closing (4-1): avoid spread at < 1.75. ML only if value.
   → LAL (4-2): Do NOT bet LAL spread in Game 7 — garbage time / blowout risk.

9. NORMAL PLAYOFF GAME: standard NetRtg + home court + rest adjustments.

SERIES STATUS (verify from ESPN before any pick):
- OKC eliminated PHX 4-0 (ESPN anomaly shows Game 5 — verify but treat as complete).
- NYK vs ATL: DATA CONFLICT — verify if complete or Game 7 active.
- MIN vs DEN: DATA CONFLICT — verify if complete or Game 7 active.

## SECTION:playin_rules
INACTIVE — Play-In Tournament is over. Do NOT apply any play-in rules.
All series are now best-of-7 Round 1. Use playoff_motivation and playoff_rest sections only.

## SECTION:h2h_playoff
Regular season H2H as a Round 1 signal — Game 7/closing stage (updated 2026-05-03):

CRITICAL CAVEAT: At Game 7, in-series results are THE primary signal.
Regular season H2H is near-irrelevant. Coaching adjustments have fully operated.
Use regular season H2H only as last-resort tiebreaker, heavily discounted.

Active series in-series signals (primary — Game 7/closing stage):

- BOS vs PHI (G7 — TIED 3-3): PHI won Games 5 AND 6 consecutively (survival momentum — 2 straight elimination wins).
  TATUM FLAG: Jayson Tatum roster-only OUT for BOS — re-verify before any pick. If OUT, BOS edge shrinks dramatically.
  BOS NetRtg advantage (+8.4pt gap) is primary signal IF Tatum active. PHI resilience statistically significant.
  Home court is decisive tiebreaker. H2H irrelevant.

- ORL vs DET (G7 — ORL leads 3-2): ORL scheme has definitively overridden DET's superior NetRtg (+8.2 vs +0.6) across 5 games.
  In-series is the ONLY valid metric — do NOT use DET NetRtg as primary signal.
  Home court is tiebreaker in Game 7. Re-verify DET franchise players before pick.

- CLE vs TOR (G7 — CLE leads 3-2): CLE NetRtg edge (+1.4pts) + Quickley OUT for TOR.
  CLE should be favoured in Game 7. TOR must fight with depleted roster.
  Home court largely determines outcome in close Game 7 scenario. H2H irrelevant.

- LAL vs HOU (G7 — LAL leads 4-2 per ESPN live): LAL tactical dominance has overridden HOU's better season NetRtg across 5+ games. In-series confirms LAL as tactical operator.
  Durant status is sole wildcard for HOU — verify before any HOU pick. H2H fully irrelevant.

- SAS vs POR (G6 — SAS leads 4-1): SAS dominance reflected in series (NetRtg gap +8.5pts). Near-complete.
  Verify if Game 6 has already concluded. SAS ML valid if Wembanyama active.

- OKC vs PHX: SERIES COMPLETE (4-0). ESPN shows Game 5 — DATA ANOMALY. Verify but treat as complete. No further analysis.
- NYK vs ATL: DATA CONFLICT — prior context says complete (NYK 4-2), ESPN live shows Game 7. Verify before any pick. If complete: ATL eliminated, no analysis. If Game 7: NYK (NetRtg +6.5) vs ATL (+2.4), NYK favoured, home court decisive.
- MIN vs DEN: DATA CONFLICT — prior context says complete (MIN 4-2), ESPN live shows Game 7. Verify before any pick. If Game 7: Aaron Gordon OUT for DEN, Edwards status critical for MIN, verify home court.

KEY LESSONS FROM THIS ROUND (updated 2026-05-03):
- ORL vs DET: clearest example of in-series overriding NetRtg (leads 3-2 despite 7.6pt deficit into Game 7).
- PHI vs BOS: PHI won 2 consecutive elimination games — survival momentum is a real signal (+5 confidence in Game 7).
- LAL vs HOU: HOU had better season NetRtg (+5.4 vs +1.7) but LAL leads 4-2 — tactical execution > season ratings.
- BOS Tatum OUT (NEW): roster-only flag creates massive pick uncertainty — ALWAYS verify franchise player status before Game 7.
- ESPN feed anomalies persistent this session: ALWAYS verify series status from ESPN before drafting.

## SECTION:l15_caveat
L15 NetRtg caveat for Round 1 playoffs (Game 7/closing stage, updated 2026-05-03):

CRITICAL: At Game 7, in-series results are THE primary signal.
Regular season L15 is directional context only — weight in-series playoff performance most heavily.

Key NetRtg vs series result divergences (confirmed as of 2026-05-03):

- ORL (+0.6 NetRtg) vs DET (+8.2 NetRtg): ORL leads 3-2 heading into Game 7 despite 7.6pt NetRtg disadvantage.
  Largest NetRtg-vs-series-result divergence in Round 1. ORL scheme completely overriding DET season rating.
  Do NOT use DET NetRtg as primary signal in Game 7 — in-series performance is the ONLY valid metric.
  Home court is the primary tiebreaker.

- LAL (+1.7 NetRtg) vs HOU (+5.4 NetRtg): HOU had better NetRtg yet LAL leads 4-2 (ESPN live ground truth; prior 3-2 overridden).
  LAL tactical dominance has overridden HOU's statistics across 5+ games. In-series is definitive.
  Durant status is the sole wildcard — verify before any HOU pick.

- BOS (+8.2 NetRtg) vs PHI (-0.2 NetRtg): Tied 3-3 heading into Game 7. PHI won Games 5 AND 6 consecutively.
  TATUM FLAG (NEW): Tatum roster-only OUT for BOS. If confirmed OUT, BOS statistical edge shrinks substantially — do NOT rely on NetRtg gap without first verifying Tatum active.
  BOS NetRtg remains primary lean IF Tatum active. PHI resilience commands +5 confidence. Home court decisive.

- SAS (+8.3 NetRtg) vs POR (-0.2 NetRtg): SAS leads 4-1 — NetRtg gap reflected. Consistent case.
  Verify Game 6 completion status.

- CLE (+4.0 NetRtg) vs TOR (+2.6 NetRtg): CLE leads 3-2 heading into Game 7.
  NetRtg gap partially reflected. Quickley OUT for TOR amplifies CLE's edge beyond raw NetRtg.

- OKC (+11.1 NetRtg) vs PHX (+1.4 NetRtg): SERIES COMPLETE (OKC won 4-0). ESPN Game 5 listing is anomaly — verify.
- NYK (+6.5 NetRtg) vs ATL (+2.4 NetRtg): DATA CONFLICT — verify series status. If complete: NYK won 4-2, NetRtg advantage validated. If Game 7: standard analysis applies.
- MIN (+3.1 NetRtg) vs DEN (+5.2 NetRtg): DATA CONFLICT — verify series status. If complete: MIN won 4-2 despite DEN's superior NetRtg — confirms scheme-over-stats thesis. If Game 7: Aaron Gordon OUT for DEN is significant.

KEY LESSONS THIS ROUND (updated 2026-05-03):
1. Scheme/execution divergence: ORL, MIN (if complete), and LAL all overperformed their NetRtg. Playoff schemes matter more than season ratings — especially reaching Game 7.
2. PHI survival pattern: winning two consecutive elimination games is a genuine signal of playoff resilience (+5 confidence in Game 7).
3. LAL leads 4-2 despite inferior NetRtg to HOU — in-series dominance definitively overrides season metrics.
4. FRANCHISE PLAYER VERIFICATION OVERRIDES NETRG (NEW): Tatum roster-only OUT for BOS is more impactful than BOS's +8.2 NetRtg. Always verify franchise player status before applying statistical edges.
5. Game 7s: Home court (~60-65% win rate) is the most reliable single input when teams are evenly matched or in-series signals are mixed.
6. ESPN live feed anomalies persist (Game 8, Game 5 after 4-0, series completion conflicts): ALWAYS verify series status from ESPN before drafting.

## SECTION:no_tanking
Tanking does not exist in playoffs. All remaining teams are fully motivated.
Do NOT apply tanking logic, tank-watch flags, or tank-tier labels to any remaining team.
Ignore the regular-season tanking_teams section entirely.
