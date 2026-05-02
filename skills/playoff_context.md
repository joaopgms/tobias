---
version: 22
updated_at: 2026-05-02T11:42:54.039271+00:00
updated_by: analyst_2026-05-02
llm: claude-sonnet-4-6
---

## SECTION:phase
First Round Playoffs — Game 7 Stage (and Game 6 closing games)

Play-In Tournament is OVER. First Round Playoffs (best-of-7) are active.
Apply series context, elimination urgency, and Round 1 rest rules — NOT play-in rules.
playin_rules section is INACTIVE this phase — ignore it entirely.

Four series remain active; three at Game 7 or Game 6 closing stage:
- Three series tied 3-3 (Game 7 next): BOS vs PHI, CLE vs TOR — and one series label reads 'Tied 3-3 Game 8 next' (DATA ANOMALY — verify from ESPN; likely a feed error, treat as Game 7 context).
- One series with LAL leads 4-2 (Game 7 next per ESPN live feed — NOTE: scout_skills previously stated 3-2; ESPN live data shows 4-2; treat 4-2 as ground truth).
- One series NYK leads 4-2 (Game 7 next per ESPN live feed — NOTE: prior context stated series COMPLETE at 4-2; ESPN live feed shows Game 7 next — DATA CONFLICT. Verify from ESPN before any NYK pick).
- One series MIN leads 4-2 (Game 7 next per ESPN live feed — same conflict as NYK; prior context stated COMPLETE; verify).
- SAS leads POR 4-1 (Game 6 next — SAS can close).
- OKC leads PHX 4-0 (Game 5 listed — DATA ANOMALY: 4-0 series should be complete; likely feed error. Treat OKC as having eliminated PHX unless ESPN confirms otherwise).

DATA QUALITY WARNING: ESPN live series feed contains apparent anomalies (Game 8, Game 5 after 4-0). Scout and Commit MUST verify individual series status from ESPN before drafting any pick this session.

## SECTION:series_context
FIRST ROUND PLAYOFFS — Active (updated 2026-05-02)

DATA CONFLICT WARNING: ESPN live feed shows series statuses that diverge from prior context entries. Ground truth = ESPN live feed. Verify each series before pick.

EAST Round 1:
- Boston Celtics vs Philadelphia 76ers: Tied 3-3 — GAME 7 NEXT (confirmed in ESPN live feed).
  Verify home court for Game 7 from ESPN — CRITICAL for home court adjustment.
  BOS (+8.2 NetRtg) vs PHI (-0.2 NetRtg) — BOS statistical edge massive but PHI consecutive survival wins create genuine uncertainty.
  Re-verify Tatum, Brown active. PHI has demonstrated playoff resilience (survived Games 5 AND 6).
  In-series: BOS won 3, PHI won 3. Home court is now THE decisive factor. ML only — do NOT bet spread in Game 7.

- Orlando Magic vs Detroit Pistons: ORL leads 3-2 — GAME 7 NEXT (confirmed ESPN live feed — previously listed as 'Tied 3-3 Game 8 next' which is a feed anomaly; treat as ORL leads 3-2 Game 7).
  Verify home court from ESPN — critical.
  ORL (NetRtg +0.6) vs DET (NetRtg +8.2) — DET statistical edge has NOT translated (ORL leads despite 7.6pt deficit).
  In-series: ORL scheme continues to override DET stats. ORL in-series lead is primary signal.
  Re-verify DET franchise players (Cunningham, Stewart, Duren). Do NOT use DET NetRtg as primary signal.
  Game 7: ML only. Home court decisive.

- New York Knicks vs Atlanta Hawks: ESPN live feed shows NYK leads 4-2 (Game 7 next). DATA CONFLICT with prior context (previously listed as SERIES COMPLETE). VERIFY from ESPN before any NYK pick.
  If series is indeed complete: NYK advances to Round 2. No further picks on NYK-ATL. ATL eliminated.
  If Game 7 is live: verify home court, apply standard Game 7 rules. NYK (NetRtg +6.5) vs ATL (NetRtg +2.4). NYK favoured.

- Cleveland Cavaliers vs Toronto Raptors: CLE leads 3-2 — GAME 7 NEXT (confirmed ESPN live feed).
  Verify home court from ESPN — critical.
  CLE (NetRtg +4.0) vs TOR (NetRtg +2.6). TOR Quickley OUT reduces offensive options significantly.
  CLE should be favoured; TOR fighting for survival in Game 7.
  Re-verify CLE and TOR rosters before any pick.

WEST Round 1:
- Oklahoma City Thunder vs Phoenix Suns: OKC leads 4-0. ESPN live feed shows 'Game 5 next' — DATA ANOMALY (4-0 series is complete; no Game 5 needed). Treat as SERIES COMPLETE unless ESPN confirms otherwise. OKC advances to Round 2. Re-verify SGA, Holmgren for Round 2.

- Los Angeles Lakers vs Houston Rockets: LAL leads 4-2 — GAME 7 NEXT (ESPN live feed; prior context stated 3-2 — ESPN live data is ground truth).
  Verify home court from ESPN — critical.
  LAL dominating despite Doncic OUT. Durant status unresolved — do not draft HOU without Durant confirmed active.
  Game 7 is maximum intensity. Both teams fully committed.
  WARNING: Do NOT bet LAL spread in Game 7 — garbage time / blowout risk.
  HOU: Require Durant confirmed active + odds ≥ 2.00 for Game 7 pick.

- San Antonio Spurs vs Portland Trail Blazers: SAS leads 4-1 — GAME 6 NEXT (SAS can close).
  Verify if Game 6 has been played or series concluded. SAS likely closes.
  SAS (NetRtg +8.3) vs POR (-0.2 NetRtg) — 8.5pt gap reflected in series dominance.
  Re-verify Victor Wembanyama active before any SAS pick.

- Minnesota Timberwolves vs Denver Nuggets: ESPN live feed shows MIN leads 4-2 (Game 7 next). DATA CONFLICT with prior context (previously listed as SERIES COMPLETE). VERIFY from ESPN before any MIN/DEN pick.
  If series is complete: MIN advances to Round 2. No further picks on MIN-DEN. DEN eliminated.
  If Game 7 is live: Aaron Gordon OUT for DEN. Anthony Edwards status critical — re-verify. MIN (NetRtg +3.1) vs DEN (NetRtg +5.2). Verify home court.

## SECTION:elimination_flags
ROUND 1 ELIMINATION FLAGS (as of 2026-05-02):

DATA CONFLICT ALERT: ESPN live feed diverges from prior session context on several series completion statuses. Treat ESPN live feed as ground truth. Verify each series before pick.

Series confirmed complete (treat as closed unless ESPN contradicts):
- Oklahoma City Thunder vs Phoenix Suns: OKC leads 4-0. ESPN shows 'Game 5' — anomaly. Treat as OKC wins 4-0 unless confirmed otherwise. No further picks.

Series with DATA CONFLICTS (must verify from ESPN before ANY pick):
- New York Knicks vs Atlanta Hawks: Prior context = COMPLETE (NYK won 4-2). ESPN live feed = NYK leads 4-2, Game 7 next. VERIFY BEFORE PICK. If complete: ATL eliminated, NYK to Round 2. If Game 7: NYK favoured.
- Minnesota Timberwolves vs Denver Nuggets: Prior context = COMPLETE (MIN won 4-2). ESPN live feed = MIN leads 4-2, Game 7 next. VERIFY BEFORE PICK. If complete: DEN eliminated, MIN to Round 2. If Game 7: Aaron Gordon OUT for DEN.

Teams confirmed facing elimination (Game 7 — one loss = out):
- Philadelphia 76ers: Tied 3-3 vs BOS. Game 7 must-win. PHI won two consecutive elimination games — genuine resilience. PHI depleted roster limits ceiling but BOS closing looseness possible.
  Do NOT bet PHI ML unless odds ≥ 1.90. BOS NetRtg edge (+8.4pt gap) remains primary lean.
- Detroit Pistons: ORL leads 3-2 vs DET. Game 7 must-win. Verify home court. ORL has solved DET tactically over 5 games — caution on DET despite superior NetRtg.
- Toronto Raptors: CLE leads 3-2 vs TOR. Game 7 must-win. Quickley OUT. TOR survival mode — limited offensive ceiling.
- Houston Rockets: LAL leads 4-2 vs HOU. Game 7 must-win. Durant status UNRESOLVED — do NOT draft HOU ML unless Durant confirmed active. If at HOU: home desperation +5. Require odds ≥ 2.00.
- Portland Trail Blazers: SAS leads 4-1 vs POR. Game 6 may be final — verify if concluded.

Teams that can close in next game:
- San Antonio Spurs: leads 4-1, Game 6 (verify location). SAS likely closes. ML valid if Wembanyama active.
- Los Angeles Lakers: leads 4-2, Game 7 next. LAL close if they win. Do NOT bet LAL spread in Game 7.

## SECTION:playoff_rest
ROUND 1 REST RULES (active):
- True B2B does NOT exist in playoffs — NBA mandates minimum 1 day off between games.
- 1 rest day (minimum): short rest — confidence -10 on spread picks for the road team.
- 2 rest days: standard rest — no adjustment.
- 3+ rest days: extended rest — slight rust risk for hot teams; confidence -5.
- Home court advantage in playoffs worth ~3-4 points (stronger than regular season ~2-3pts).

Verify actual rest days from ESPN scoreboard — do not assume.

## SECTION:playoff_motivation
Playoff motivation hierarchy (Round 1 — Game 7/closing stage):

1. GAME 7 (maximum desperation — both teams fully committed; season on the line):
   Active Game 7s: BOS vs PHI, ORL vs DET, CLE vs TOR, LAL vs HOU.
   VERIFY: NYK vs ATL and MIN vs DEN — ESPN feed shows Game 7 next despite prior context showing complete; confirm from ESPN.
   → Home team in Game 7: add confidence +8 (home floor historically +60% win rate in G7).
   → Road team in Game 7: add confidence +5 (nothing-to-lose factor). Require odds ≥ 1.90.
   → Do NOT bet spread in Game 7 — blowout or wire-to-wire grind equally possible. ML only.
   → In Game 7, in-series result is primary context; NetRtg and home court are the main inputs.

2. PHI SURVIVAL MOMENTUM (compound factor — earned across Games 5 AND 6):
   → PHI won two consecutive elimination games: apply confidence +5 for PHI in Game 7.
   → BUT PHI depleted roster limits ceiling — BOS NetRtg (+8.4pt gap) remains primary lean.
   → PHI at home in Game 7 (if verified): +8 home + +5 survival = meaningful confidence boost. Respect.
   → PHI on road in Game 7: +5 road Game 7 + +5 survival = moderate factor. Require odds ≥ 2.00.

3. ORL TACTICAL DOMINANCE FACTOR:
   → ORL leads DET 3-2 despite 7.6pt NetRtg disadvantage — scheme has overridden stats all series.
   → In Game 7, respect ORL's in-series edge over DET. Do NOT over-weight DET NetRtg.
   → Home court is the primary tiebreaker. Verify Game 7 location before any pick.

4. HOU DURANT WILDCARD (Game 7 vs LAL — LAL leads 4-2):
   → Durant status unresolved — do NOT draft HOU ML unless Durant confirmed active.
   → If Durant confirmed active + HOU has home court: legitimate Game 7 upset risk exists.
   → LAL tactical dominance across 5+ games is the baseline — HOU must demonstrate Durant is active.
   → Require HOU odds ≥ 2.00 even with Durant active.

5. SERIES MOMENTUM (SAS closing — leads 4-1):
   → SAS can close in Game 6. Verify game has not already concluded.
   → SAS ML at ≥ 1.70 valid if Wembanyama confirmed active. NetRtg gap (+8.5pts) consistently reflected.
   → Do NOT bet SAS spread at < 1.75 — closing looseness risk.

6. HOME COURT ADVANTAGE (Game 7s):
   → Playoff home court worth 3-4 points — decisive in close matchups.
   → Game 7 home court win rate historically ~60-65% in NBA.
   → Verify home court for EVERY pick from ESPN before drafting.

7. CLOSING TEAM CAUTION (leads 4-1 or 4-2):
   → SAS closing (4-1): avoid spread at < 1.75. ML only if value.
   → LAL (4-2): Do NOT bet LAL spread in Game 7 — garbage time / blowout risk.

8. NORMAL PLAYOFF GAME: standard NetRtg + home court + rest adjustments.

SERIES STATUS (verify from ESPN before any pick):
- OKC eliminated PHX 4-0 (ESPN anomaly shows Game 5 — verify).
- NYK vs ATL: DATA CONFLICT — verify if complete or Game 7 active.
- MIN vs DEN: DATA CONFLICT — verify if complete or Game 7 active.

## SECTION:playin_rules
INACTIVE — Play-In Tournament is over. Do NOT apply any play-in rules.
All series are now best-of-7 Round 1. Use playoff_motivation and playoff_rest sections only.

## SECTION:h2h_playoff
Regular season H2H as a Round 1 signal — Game 7/closing stage:

CRITICAL CAVEAT: At Game 7, in-series results are THE primary signal.
Regular season H2H is near-irrelevant. Coaching adjustments have fully operated.
Use regular season H2H only as last-resort tiebreaker, heavily discounted.

Active series in-series signals (primary — Game 7/closing stage):

- BOS vs PHI (G7 — TIED 3-3): PHI won Games 5 AND 6 consecutively (survival momentum — 2 straight elimination wins). BOS NetRtg advantage (+8.4pt gap) is primary signal. PHI resilience statistically significant. Home court is decisive tiebreaker. H2H irrelevant.

- ORL vs DET (G7): ORL leads 3-2 in series. ORL scheme has definitively overridden DET's superior NetRtg (+8.2 vs +0.6) across 5 games. In-series is the ONLY valid metric — do NOT use DET NetRtg as primary signal. Home court is tiebreaker in Game 7.

- CLE vs TOR (G7): CLE leads 3-2. CLE NetRtg edge (+1.4pts) + Quickley OUT for TOR. CLE should be favoured. TOR must fight with depleted roster. H2H largely irrelevant.

- LAL vs HOU (G7 — LAL leads 4-2 per ESPN): LAL tactical dominance has overridden HOU's better season NetRtg across 5+ games. In-series confirms LAL as tactical operator. HOU's season stats (+5.4 NetRtg vs LAL +1.7) definitively irrelevant. Durant status is sole wildcard — verify before any HOU pick. H2H fully irrelevant.

- SAS vs POR (G6 — SAS leads 4-1): SAS dominance reflected in series (NetRtg gap +8.5pts). Near-complete. Verify if concluded.

- OKC vs PHX: Likely SERIES COMPLETE (4-0). ESPN shows Game 5 — DATA ANOMALY. Verify. No further analysis if complete.
- NYK vs ATL: DATA CONFLICT — prior context says complete (NYK 4-2), ESPN live shows Game 7. Verify before any pick. If complete: ATL eliminated, no analysis. If Game 7: NYK (NetRtg +6.5) vs ATL (+2.4), NYK favoured, home court decisive.
- MIN vs DEN: DATA CONFLICT — prior context says complete (MIN 4-2), ESPN live shows Game 7. Verify before any pick. If Game 7: Aaron Gordon OUT for DEN, Edwards status critical for MIN, verify home court.

KEY LESSONS FROM THIS ROUND (updated):
- ORL vs DET: clearest example of in-series overriding NetRtg (leads 3-2 despite 7.6pt deficit heading into Game 7).
- PHI vs BOS: PHI won 2 consecutive elimination games — survival momentum is a real signal (+5 confidence in Game 7).
- LAL vs HOU: HOU had better season NetRtg (+5.4 vs +1.7) but LAL leads 4-2 — tactical execution matters more than season ratings.
- MIN vs DEN (if complete): MIN won series 4-2 despite DEN having Jokic. Scheme overrode statistics definitively.

## SECTION:l15_caveat
L15 NetRtg caveat for Round 1 playoffs (Game 7/closing stage):

CRITICAL: At Game 7, in-series results are THE primary signal.
Regular season L15 is directional context only — weight in-series playoff performance most heavily.

Key NetRtg vs series result divergences (confirmed as of 2026-05-02):

- ORL (+0.6 NetRtg) vs DET (+8.2 NetRtg): ORL leads 3-2 heading into Game 7 despite 7.6pt NetRtg disadvantage.
  Largest NetRtg-vs-series-result divergence in Round 1. ORL scheme completely overriding DET season rating.
  Do NOT use DET NetRtg as primary signal in Game 7 — in-series performance is the ONLY valid metric.
  Home court is the primary tiebreaker.

- LAL (+1.7 NetRtg) vs HOU (+5.4 NetRtg): HOU had better NetRtg yet LAL leads 4-2 heading into Game 7 (ESPN ground truth; prior context said 3-2).
  LAL tactical dominance has overridden HOU's statistics across 5+ games. In-series is definitive.
  Durant status is the sole wildcard — verify before any HOU pick.

- BOS (+8.2 NetRtg) vs PHI (-0.2 NetRtg): Tied 3-3 heading into Game 7. PHI won Games 5 AND 6 consecutively.
  NetRtg gap partially reflected (BOS leads in overall record) but PHI survival across two elimination games is statistically meaningful.
  BOS NetRtg remains primary lean but PHI resilience pattern commands +5 confidence consideration.
  Home court decisive in Game 7.

- SAS (+8.3 NetRtg) vs POR (-0.2 NetRtg): SAS leads 4-1 — NetRtg gap reflected. Consistent case.
  Verify Game 6 completion status.

- CLE (+4.0 NetRtg) vs TOR (+2.6 NetRtg): CLE leads 3-2 heading into Game 7.
  NetRtg gap partially reflected. Quickley OUT for TOR amplifies CLE's edge beyond raw NetRtg.

- OKC (+11.1 NetRtg) vs PHX (+1.4 NetRtg): Likely SERIES COMPLETE (OKC won 4-0). ESPN Game 5 listing is anomaly — verify.
- NYK (+6.5 NetRtg) vs ATL (+2.4 NetRtg): DATA CONFLICT — verify series status. If complete: NYK won 4-2, NetRtg advantage validated. If Game 7: standard analysis applies.
- MIN (+3.1 NetRtg) vs DEN (+5.2 NetRtg): DATA CONFLICT — verify series status. If complete: MIN won 4-2 despite DEN's superior NetRtg — confirms scheme-over-stats thesis. If Game 7: Aaron Gordon OUT for DEN is significant.

KEY LESSONS THIS ROUND (updated 2026-05-02):
1. Scheme/execution divergence: ORL, MIN (if complete), and LAL all overperformed their NetRtg. Playoff schemes matter more than season ratings — especially in series that reach Game 7.
2. PHI survival pattern: winning two consecutive elimination games is a genuine signal of playoff resilience — treat as +5 confidence in Game 7.
3. LAL leads 4-2 despite inferior NetRtg to HOU — in-series dominance confirmation definitively overrides season metrics.
4. Game 7s: Home court (~60-65% win rate) is the most reliable single input when teams are evenly matched or in-series signals are mixed.
5. ESPN live feed anomalies this session (Game 8 listing, Game 5 after 4-0, series completion conflicts): ALWAYS verify series status from ESPN before drafting. Feed errors are real.

## SECTION:no_tanking
Tanking does not exist in playoffs. All remaining teams are fully motivated.
Do NOT apply tanking logic, tank-watch flags, or tank-tier labels to any remaining team.
Ignore the regular-season tanking_teams section entirely.
