---
version: 24
updated_at: 2026-05-04T12:20:08.624588+00:00
updated_by: analyst_2026-05-04
llm: claude-sonnet-4-6
---

## SECTION:phase
NBA Playoffs — Mixed Phase: Round 1 Final Games + Round 2 Semifinals Beginning

Play-In Tournament is OVER. Round 1 is in final stages (Game 7s and one closing game). Round 2 (Semifinals) has begun for at least two series.
Apply series context, elimination urgency, and rest rules — NOT play-in rules.
playin_rules section is INACTIVE this phase — ignore it entirely.

Round 2 series active (per ESPN):
- East Semifinals: Tied 0-0 (Game 2 next) — verify exact matchup from ESPN
- West Semifinals: Tied 0-0 (Game 2 next) — verify exact matchup from ESPN

Round 1 still active (per ESPN live):
- Detroit Pistons leads 4-3 (Game 8 next — DATA ANOMALY; verify series status)
- Cleveland Cavaliers leads 4-3 (Game 8 next — DATA ANOMALY; verify series status)
- Philadelphia 76ers leads 4-3 (Game 8 next — DATA ANOMALY; verify series status)
- Los Angeles Lakers leads 4-2 (Game 7 next)
- New York Knicks leads 4-2 (Game 7 next — likely Round 1 complete; verify)
- Minnesota Timberwolves leads 4-2 (Game 7 next)
- San Antonio Spurs leads 4-1 (Game 6 next — verify if concluded)
- Oklahoma City Thunder leads 4-0 (Game 5 next — DATA ANOMALY; treat as COMPLETE)

DATA QUALITY WARNING: ESPN live feed continues to show anomalies (Game 8 listings in a best-of-7, Game 5 after 4-0). Treat any 'Game 8' listing as a feed error — maximum games in a series is 7. Scout and Commit MUST verify individual series status from ESPN before drafting any pick this session.

## SECTION:series_context
NBA PLAYOFFS — Active Series (updated from ESPN live feed)

DATA CONFLICT WARNING: ESPN live feed shows persistent anomalies (Game 8 in best-of-7, Game 5 after 4-0 sweep). Maximum series length is 7 games. Any 'Game 8' listing is a feed error. Ground truth = ESPN live, corrected for known anomalies. Verify each series before pick.

--- ROUND 2 (SEMIFINALS) ---

EAST Semifinals:
- [Team A] vs [Team B]: Tied 0-0 — GAME 2 NEXT.
  VERIFY exact matchup from ESPN — feed shows East Semifinals starting. Likely BOS/PHI winner vs NYK/ATL winner.
  Jayson Tatum (BOS) roster-only OUT — re-verify before any BOS pick if BOS is in this series.
  Home court for Game 2 follows standard format (higher seed has home court in series).
  Advanced stats context: BOS (+8.2 NetRtg), NYK (+6.5), PHI (-0.2) — verify which teams advanced.

WEST Semifinals:
- [Team A] vs [Team B]: Tied 0-0 — GAME 2 NEXT.
  VERIFY exact matchup from ESPN — feed shows West Semifinals starting. Likely OKC (4-0 vs PHX winner) vs SAS/POR winner.
  OKC (+11.1 NetRtg, 64-18 record) is the strongest statistical team remaining if they advanced.
  Re-verify SGA, Chet Holmgren, Jalen Williams for any OKC Round 2 pick.

--- ROUND 1 FINAL GAMES ---

EAST Round 1 Final:
- Detroit Pistons vs [ORL]: DET leads 4-3 per ESPN. DATA ANOMALY: ESPN shows 'Game 8 next' — impossible in best-of-7. Treat as series COMPLETE (DET wins 4-3) OR verify from ESPN if truly an active series.
  If DET won: DET advances to Round 2. ORL ELIMINATED.
  If somehow active: Re-verify DET franchise players (Cunningham, Stewart, Duren). Kevin Huerter (DET) OUT. ML only.

- Cleveland Cavaliers vs Toronto Raptors: CLE leads 4-3 per ESPN. DATA ANOMALY: 'Game 8 next' — treat as COMPLETE (CLE wins 4-3) OR verify.
  If CLE won: CLE advances to Round 2. TOR ELIMINATED.
  Quickley OUT for TOR (entire series). CLE (NetRtg +4.0) vs TOR (+2.6) — CLE edge confirmed over series.

- Philadelphia 76ers vs Boston Celtics: PHI leads 4-3 per ESPN. DATA ANOMALY: 'Game 8 next' — treat as COMPLETE (PHI wins 4-3) OR verify.
  If PHI won: MASSIVE UPSET. PHI (-0.2 NetRtg) beat BOS (+8.2 NetRtg). Jayson Tatum confirmed OUT was decisive. PHI advances to Round 2.
  If somehow active: CRITICAL — verify Tatum status. PHI survival momentum + Tatum OUT = PHI favoured.

WEST Round 1 Final:
- Los Angeles Lakers vs Houston Rockets: LAL leads 4-2 — GAME 7 NEXT (ESPN live, confirmed).
  Luka Doncic (LAL): roster-only OUT — LAL winning without him across series.
  Kevin Durant (HOU): roster-only OUT — CRITICAL. Do NOT draft HOU ML without Durant confirmed active via NBA official PDF.
  LAL (+1.7 NetRtg) vs HOU (+5.4 NetRtg) — LAL tactical dominance confirmed across 5 games.
  Game 7: ML only. Do NOT bet LAL spread. HOU valid only if Durant confirmed active + home court + odds ≥ 2.00.
  Verify home court from ESPN. Alperen Sengun re-verify.

- Minnesota Timberwolves vs Denver Nuggets: MIN leads 4-2 — GAME 7 NEXT (ESPN live).
  Aaron Gordon (DEN): OUT [roster-only] — significant loss for DEN.
  Anthony Edwards (MIN): OUT [roster-only] — FRANCHISE PLAYER. CRITICAL: re-verify via NBA official PDF before any MIN pick.
  MIN (NetRtg +3.1) vs DEN (+5.2) — DEN has better season NetRtg but MIN leads series 4-2.
  If Edwards confirmed OUT: MIN without primary scorer — evaluate DEN ML if odds ≥ 1.90.
  Game 7: verify home court from ESPN. ML only.

- San Antonio Spurs vs Portland Trail Blazers: SAS leads 4-1 — Game 6 next.
  Verify from ESPN if Game 6 has been played and series concluded.
  SAS (NetRtg +8.3) vs POR (-0.2) — dominant series performance, gap reflected.
  Re-verify Victor Wembanyama active before any SAS pick. SAS ML valid at ≥ 1.70 if Wembanyama active.
  Do NOT bet SAS spread at < 1.75 — closing looseness risk.

- Oklahoma City Thunder vs Phoenix Suns: OKC leads 4-0 — SERIES COMPLETE.
  ESPN shows 'Game 5 next' — confirmed DATA ANOMALY. OKC advances to Round 2. PHX ELIMINATED.
  No further OKC-PHX picks. Re-verify SGA, Chet Holmgren for Round 2.

## SECTION:elimination_flags
PLAYOFFS ELIMINATION FLAGS (updated from ESPN live feed)

DATA ANOMALY ALERT: ESPN shows 'Game 8 next' for DET-ORL, CLE-TOR, PHI-BOS — impossible in best-of-7. These are feed errors. Treat 4-3 series as COMPLETE unless ESPN explicitly confirms a live Game 7 is scheduled. Verify before any pick.

Teams CONFIRMED ELIMINATED:
- Phoenix Suns: OKC won 4-0. ESPN 'Game 5' anomaly confirmed. PHX OUT. No further picks.
- Atlanta Hawks: NYK won 4-2 (Round 1). ATL ELIMINATED. ESPN shows East Semifinals active — ATL not a participant. No further ATL picks.
- Portland Trail Blazers: SAS leads 4-1 — verify if Game 6 concluded. If SAS won: POR ELIMINATED.

Teams LIKELY ELIMINATED (ESPN 4-3 series with 'Game 8' anomaly — verify):
- Orlando Magic: DET leads 4-3 per ESPN feed. If series complete: ORL ELIMINATED. Verify from ESPN.
- Toronto Raptors: CLE leads 4-3 per ESPN feed. If series complete: TOR ELIMINATED. Verify from ESPN.
- Boston Celtics: PHI leads 4-3 per ESPN feed. If series complete: BOS ELIMINATED (Tatum OUT was decisive). Verify from ESPN. MAJOR UPSET if confirmed.

Teams facing elimination (active Game 7 — confirmed):
- Houston Rockets: LAL leads 4-2, Game 7 next. Durant OUT makes HOU survival dependent on his return.
- Denver Nuggets: MIN leads 4-2, Game 7 next. Aaron Gordon OUT, Edwards status critical for MIN.

Teams that can close in next game:
- Los Angeles Lakers: leads 4-2, Game 7. LAL win = series close.
- Minnesota Timberwolves: leads 4-2, Game 7. MIN win = series close.
- San Antonio Spurs: leads 4-1, Game 6 (verify if concluded).

Teams advancing to Round 2 (confirmed or near-confirmed):
- Oklahoma City Thunder: CONFIRMED advanced (4-0 vs PHX).
- New York Knicks: CONFIRMED advanced (4-2 vs ATL) — now in East Semifinals.
- Detroit Pistons: LIKELY advanced (leads 4-3, verify).
- Cleveland Cavaliers: LIKELY advanced (leads 4-3, verify).
- Philadelphia 76ers: LIKELY advanced (leads 4-3, verify — massive upset if BOS eliminated).
- San Antonio Spurs: NEAR-CERTAIN to advance (leads 4-1, one game from closing).

## SECTION:playoff_rest
PLAYOFF REST RULES (active — mixed Round 1 final / Round 2 start):
- True B2B does NOT exist in playoffs — NBA mandates minimum 1 day off between games.
- 1 rest day (minimum): short rest — confidence -10 on spread picks for road team.
- 2 rest days: standard rest — no adjustment.
- 3+ rest days: extended rest — slight rust risk for hot teams; confidence -5.
- Home court advantage in playoffs worth ~3-4 points (stronger than regular season ~2-3pts).
- Round 2 rest note: teams advancing from Round 1 may have 2-5 days rest before Round 2 Game 1. Extended rest rust applies if gap ≥ 5 days — flag in scout_report.
- Game 7 rest: both teams had identical rest by definition (simultaneous schedule). Home court is the primary differentiator.

Verify actual rest days from ESPN scoreboard — do not assume.

## SECTION:playoff_motivation
PLAYOFF MOTIVATION HIERARCHY (Mixed Round 1 Final / Round 2 Start — updated from ESPN live feed)

1. ROUND 2 GAME 1/2 (Series momentum building):
   East Semifinals: Tied 0-0, Game 2 next — verify matchup (likely PHI/BOS winner vs NYK).
   West Semifinals: Tied 0-0, Game 2 next — verify matchup (likely OKC vs SAS/winner).
   → Early series: home court advantage is primary input (higher seed has home court).
   → In-series signals not yet established — season NetRtg and rest are primary inputs.
   → Do NOT over-weight Round 1 momentum — teams reset tactically between rounds.
   → Verify full roster availability — new injuries may have emerged.

2. GAME 7 (maximum desperation — season on the line):
   Active confirmed Game 7s: LAL vs HOU, MIN vs DEN.
   VERIFY: DET-ORL, CLE-TOR, PHI-BOS show 4-3 in ESPN with 'Game 8 next' — if those series have a Game 7, apply same rules.
   → Home team in Game 7: add confidence +8 (historically ~60-65% win rate).
   → Road team in Game 7: add confidence +5 (nothing-to-lose). Require odds ≥ 1.90.
   → Do NOT bet spread in Game 7 — blowout or wire-to-wire equally possible. ML only.
   → In Game 7, in-series result + home court are primary inputs.

3. DURANT WILDCARD — LAL vs HOU Game 7:
   → Kevin Durant (HOU): roster-only OUT — CRITICAL. Do NOT draft HOU ML without Durant confirmed active.
   → If Durant confirmed active + HOU home court: legitimate Game 7 upset risk vs LAL (leads 4-2).
   → LAL tactical dominance across 5 games without Doncic is the baseline.
   → Require HOU odds ≥ 2.00 even with Durant active.
   → Do NOT bet LAL spread in Game 7 — blowout/garbage-time risk.

4. EDWARDS WILDCARD — MIN vs DEN Game 7:
   → Anthony Edwards (MIN): roster-only OUT — FRANCHISE PLAYER. Re-verify before any MIN pick.
   → Aaron Gordon (DEN): OUT — significant DEN loss.
   → MIN leads 4-2 but Edwards absence fundamentally changes MIN's offensive ceiling.
   → If Edwards confirmed OUT: evaluate DEN ML (NetRtg +5.2 DEN vs +3.1 MIN) + home court.
   → Game 7 home court is decisive — verify from ESPN.

5. TATUM FACTOR (BOS/PHI — if still active):
   → PHI shows 4-3 lead per ESPN (with 'Game 8' anomaly). If series active: Tatum OUT for BOS is CRITICAL.
   → PHI won survival games with Tatum out — PHI playoff resilience is real.
   → If confirmed: BOS elimination risk. PHI ML if BOS home and odds ≥ 1.80.

6. SAS CLOSING (leads 4-1):
   → Verify if Game 6 has concluded. SAS ML valid if Wembanyama active at ≥ 1.70.
   → Do NOT bet SAS spread at < 1.75 — closing looseness risk.

7. HOME COURT (all games):
   → Playoff home court worth 3-4 points — decisive in close matchups.
   → Game 7 home court historically ~60-65% win rate.
   → Round 2 Game 1/2: higher seed has home court — verify from ESPN.
   → Verify home court for EVERY pick before drafting.

8. ROUND 2 RUST FACTOR:
   → Teams with 4+ days rest between rounds may show early rust.
   → Apply confidence -5 if rest gap ≥ 5 days for the team with longer rest in Round 2.
   → Do NOT over-extend this — by Game 2 or 3 of Round 2, rust fully dissipated.

## SECTION:playin_rules
INACTIVE — Play-In Tournament is over. Do NOT apply any play-in rules.
All series are now best-of-7 Round 1. Use playoff_motivation and playoff_rest sections only.

## SECTION:h2h_playoff
PLAYOFF H2H AND IN-SERIES SIGNALS (updated from ESPN live feed)

CRITICAL CAVEAT: In-series results are the PRIMARY signal in playoff analysis.
Regular season H2H is a last-resort tiebreaker only — heavily discounted.
Round 2 Game 1/2: in-series signal not yet established. Use season NetRtg + home court + rest.

--- ROUND 2 IN-SERIES STATUS ---

East Semifinals: Tied 0-0 (Game 2 next)
- VERIFY exact matchup from ESPN. No in-series signal yet — season context is primary.
- If PHI vs NYK (likely if PHI upset BOS): PHI (NetRtg -0.2) vs NYK (+6.5) — NYK statistical favourite. PHI survival momentum is real but NYK has home court as higher seed.
- If BOS vs NYK: BOS (NetRtg +8.2) vs NYK (+6.5) — close statistical matchup; home court decisive.
- Tatum OUT (BOS) remains critical franchise player flag regardless of opponent.

West Semifinals: Tied 0-0 (Game 2 next)
- VERIFY exact matchup from ESPN. No in-series signal yet.
- If OKC vs SAS: OKC (NetRtg +11.1) vs SAS (+8.3) — OKC statistical edge. OKC has better record (64-18 vs 62-20); home court likely OKC.
- If OKC vs MIN: OKC (+11.1) vs MIN (+3.1) — large NetRtg gap. Edwards OUT for MIN is critical.
- Wembanyama (SAS) and SGA/Chet (OKC) require re-verification each session.

--- ROUND 1 FINAL IN-SERIES STATUS ---

LAL vs HOU (Game 7 — LAL leads 4-2):
- LAL tactical dominance across 5 games with Doncic OUT is definitive in-series signal.
- HOU had better season NetRtg (+5.4 vs +1.7) but in-series result overrides.
- Durant (HOU) OUT is the sole wildcard. Verify before any HOU pick.

MIN vs DEN (Game 7 — MIN leads 4-2):
- MIN leads despite Edwards roster-only OUT. DEN Aaron Gordon OUT.
- MIN in-series dominance (4-2) overrides DEN's better season NetRtg (+5.2 vs +3.1).
- Verify Edwards and Gordon actual status before any pick.

DET leads ORL 4-3 / CLE leads TOR 4-3 / PHI leads BOS 4-3 (ESPN anomaly — verify):
- If these series are complete: series signals fully established. Key learnings logged below.
- ORL overperformed vs DET (leads 4-3 despite 7.6pt NetRtg deficit) — scheme matter confirmed.
- PHI potentially won 4-3 vs BOS despite -8.4pt NetRtg deficit — Tatum OUT decisive factor.
- CLE won 4-3 vs TOR — small NetRtg edge confirmed; Quickley OUT for TOR amplified CLE edge.

KEY LESSONS THIS ROUND (updated):
1. Scheme/execution > NetRtg: ORL over DET, LAL over HOU, potentially PHI over BOS all confirmed.
2. Franchise player absences override NetRtg: Tatum OUT (BOS) likely decisive if PHI won 4-3 despite -8.4pt deficit.
3. Edwards OUT for MIN has not prevented MIN from leading 4-2 — team depth can compensate in-series.
4. ESPN feed anomalies persist (Game 8, Game 5 after sweep): ALWAYS verify series status before drafting.
5. Round 2 resets: Do not carry Round 1 momentum blindly into Round 2 — teams adjust tactically between rounds.
6. Early series (Round 2 0-0): Season NetRtg + home court are primary inputs with no in-series data.

## SECTION:l15_caveat
L15 NetRtg CAVEAT FOR PLAYOFFS (Mixed Round 1 Final / Round 2 Start — updated from ESPN live feed)

CRITICAL HIERARCHY:
1. In-series result (Game 5+ stage): PRIMARY signal — overrides season NetRtg.
2. Franchise player availability: SECONDARY — a key absence can negate any NetRtg gap.
3. Home court: TERTIARY — worth 3-4pts in playoffs; decisive in close Game 7s.
4. Season NetRtg: CONTEXT ONLY at Game 7 stage; PRIMARY for Round 2 Game 1/2.
5. L15 NetRtg: directional only — weight less than in-series or home court.

ROUND 2 SPECIAL RULE:
→ For Game 1/2 of Round 2: in-series signal does not yet exist.
→ Season NetRtg and current franchise player status are the primary inputs.
→ Use L15 as directional secondary. Home court (higher seed) is decisive tiebreaker.
→ Do NOT over-weight Round 1 momentum across rounds — teams reset tactically.

Key NetRtg vs series result divergences (Round 1 — confirmed as of current ESPN feed):

- LAL (+1.7) vs HOU (+5.4): LAL leads 4-2 despite inferior NetRtg — tactical execution definitively overrides.
  Durant (HOU) OUT amplified LAL advantage. In-series is the only valid metric for Game 7.

- MIN (+3.1) vs DEN (+5.2): MIN leads 4-2 despite inferior NetRtg — Edwards OUT yet MIN wins.
  Aaron Gordon OUT for DEN also a factor. Game 7: verify both key player statuses.

- PHI (-0.2) vs BOS (+8.2): PHI shows 4-3 lead per ESPN (verify). Tatum OUT for BOS is the primary explanation for 8.4pt NetRtg being meaningless.
  KEY LESSON: Franchise player absence can completely negate a large NetRtg gap.

- DET (+8.2) vs ORL (+0.6): ORL potentially leads or tied (verify) — scheme overrode 7.6pt NetRtg deficit.
  In-series confirmed that scheme execution matters more than season ratings in Round 1.

- SAS (+8.3) vs POR (-0.2): SAS leads 4-1 — gap reflected in dominant series performance. Consistent case where NetRtg predicted outcome.

- OKC (+11.1) vs PHX (+1.4): SERIES COMPLETE (4-0). NetRtg gap (9.7pts) fully validated — strongest predictor this round.

Round 2 NetRtg baseline (as of current data):
- OKC: +11.1 (best in league)
- SAS: +8.3
- BOS: +8.2 (Tatum OUT — effective rating lower)
- DET: +8.2
- NYK: +6.5
- HOU: +5.4 (Durant OUT — effective rating lower)
- DEN: +5.2 (Gordon OUT)
- MIN: +3.1 (Edwards OUT — effective rating lower)
- PHI: -0.2 (playoff resilience has overcome this all round)
- CLE: +4.0

KEY LESSONS UPDATED:
1. Franchise player absence > NetRtg gap: Tatum OUT negated 8.4pt BOS advantage (if PHI won 4-3).
2. Scheme execution overrides season stats by Game 7: ORL, LAL, PHI all confirmed.
3. OKC +11.1 is the most reliable NetRtg signal this postseason — gap too large for scheme to override.
4. Round 2 Game 1/2: season NetRtg is primary input (no in-series data yet) — weight it more heavily than in late Round 1.
5. Edwards/Durant OUT statuses: despite being roster-only, in-series results confirm their teams are competing — verify actual play status before any pick.

## SECTION:no_tanking
Tanking does not exist in playoffs. All remaining teams are fully motivated.
Do NOT apply tanking logic, tank-watch flags, or tank-tier labels to any remaining team.
Ignore the regular-season tanking_teams section entirely.

Eliminated teams (no further picks):
- Phoenix Suns: eliminated (OKC won 4-0).
- Atlanta Hawks: eliminated (NYK won 4-2).
- Portland Trail Blazers: near-elimination (SAS leads 4-1); verify if Game 6 concluded.
- Washington Wizards: did not qualify for playoffs.

Additional teams likely eliminated (verify from ESPN — ESPN shows 4-3 series leads with 'Game 8' anomalies):
- Orlando Magic: if DET won 4-3 — ORL eliminated. Verify.
- Toronto Raptors: if CLE won 4-3 — TOR eliminated. Verify.
- Boston Celtics: if PHI won 4-3 — BOS eliminated. Verify. (Tatum OUT was likely decisive.)
