---
version: 25
updated_at: 2026-05-06T12:26:21.749533+00:00
updated_by: analyst_2026-05-06
llm: claude-sonnet-4-6
---

## SECTION:phase
NBA Playoffs — Mixed Phase: Round 1 Final Games + Round 2 (Semifinals) Underway

Play-In Tournament is OVER. Round 1 is in final stages (Game 7s remaining). Round 2 (Semifinals) has begun — at least four series are active with Game 2 or Game 3 next.
Apply series context, elimination urgency, and rest rules — NOT play-in rules.
playin_rules section is INACTIVE this phase — ignore it entirely.

Round 2 series active (per ESPN live feed):
- East Semifinals: New York Knicks leads 1-0 (Game 3 next)
- East Semifinals: Detroit Pistons leads 1-0 (Game 2 next)
- West Semifinals: Minnesota Timberwolves leads 1-0 (Game 3 next)
- West Semifinals: Oklahoma City Thunder leads 1-0 (Game 2 next)

Round 1 still active (confirmed by ESPN — Game 7 or closing games):
- Los Angeles Lakers leads Houston Rockets 4-2 (Game 7 next)
- VERIFY: DET leads ORL 4-3 (Game 8 anomaly — ESPN live shows DET in Semifinals, so Round 1 likely complete)
- VERIFY: CLE leads TOR 4-3 (Game 8 anomaly — verify if series concluded)
- VERIFY: PHI leads BOS 4-3 (Game 8 anomaly — ESPN live shows East Semifinals active; verify which teams)
- VERIFY: NYK leads 4-2 (Game 7 — ESPN shows NYK in Semifinals, so likely complete)
- VERIFY: MIN leads DEN 4-2 (Game 7 — ESPN shows MIN in Semifinals, so likely complete; but LAL-HOU still active)
- SAS leads POR 4-1 (Game 6 — verify if concluded; ESPN shows SAS in West Semifinals)
- OKC leads PHX 4-0 (COMPLETE — OKC in West Semifinals confirmed)

DATA QUALITY WARNING: ESPN live feed shows persistent anomalies. Most informative ground truth: ESPN Semifinals active series showing four teams (NYK, DET, MIN, OKC) each leading Round 2 1-0 — this implies their Round 1 opponents are eliminated. LAL-HOU Game 7 is the one confirmed active Round 1 game.

## SECTION:series_context
NBA PLAYOFFS — Active Series (updated from ESPN live feed)

DATA CONFLICT WARNING: ESPN live feed shows persistent anomalies. Four Round 2 series are confirmed active. LAL-HOU Game 7 is the last active Round 1 game. All 'Game 8' Round 1 listings are feed errors — series are complete.

--- ROUND 2 (SEMIFINALS) ---

EAST Semifinals — Series A:
- New York Knicks leads 1-0 (Game 3 next)
  NYK (NetRtg +6.5, 53-29) advanced from Round 1 (beat ATL 4-2).
  VERIFY opponent from ESPN — likely DET or PHI or CLE based on bracket.
  NYK home court advantage as higher seed (verify for this series).
  Re-verify Jalen Brunson, Karl-Anthony Towns before any pick. MANDATORY.
  No current franchise player absences confirmed for NYK.

EAST Semifinals — Series B:
- Detroit Pistons leads 1-0 (Game 2 next)
  DET (NetRtg +8.2, 60-22) — VERIFY opponent from ESPN.
  Kevin Huerter (DET): OUT [roster-only]. Re-verify Cade Cunningham, Isaiah Stewart, Jalen Duren. MANDATORY.
  Possible opponents: CLE, PHI, BOS — verify bracket.

WEST Semifinals — Series A:
- Minnesota Timberwolves leads 1-0 (Game 3 next)
  MIN (NetRtg +3.1, 49-33) advanced from Round 1 (led DEN 4-2 in Game 7 — verify if concluded).
  CRITICAL: Anthony Edwards (MIN) was roster-only OUT in Round 1 — re-verify status for Round 2 via NBA official PDF. If Edwards active, MIN outlook significantly stronger.
  Donte DiVincenzo (G): OUT [roster-only].
  VERIFY opponent from ESPN — likely DEN (if MIN won Game 7) or another West team.
  If opponent is DEN: DEN (NetRtg +5.2) with Aaron Gordon OUT.

WEST Semifinals — Series B:
- Oklahoma City Thunder leads 1-0 (Game 2 next)
  OKC (NetRtg +11.1, 64-18) — strongest statistical team in playoffs. Swept PHX 4-0 in Round 1.
  Jalen Williams (G): OUT [roster-only] — FRANCHISE PLAYER. Re-verify SGA, Chet Holmgren. MANDATORY.
  Thomas Sorber (C): OUT [roster-only].
  VERIFY opponent from ESPN — likely SAS (if SAS beat POR) or another West team.
  If OKC vs SAS: OKC (+11.1) vs SAS (+8.3) — OKC statistical edge; both strong defensive teams.
  Re-verify Victor Wembanyama active for SAS. MANDATORY.

--- ROUND 1 FINAL ---

WEST Round 1 — GAME 7:
- Los Angeles Lakers vs Houston Rockets: LAL leads 4-2 — GAME 7 CONFIRMED (ESPN live).
  Luka Doncic (LAL): OUT [roster-only] — LAL winning without him across series.
  Kevin Durant (HOU): OUT [roster-only] — CRITICAL. Do NOT draft HOU ML without Durant confirmed active via NBA official PDF.
  LAL (+1.7 NetRtg) vs HOU (+5.4 NetRtg) — LAL in-series dominance overrides NetRtg.
  Game 7: ML only. Do NOT bet LAL spread. HOU valid only if Durant confirmed active + home court + odds ≥ 2.00.
  Verify home court from ESPN. Re-verify Alperen Sengun.

--- ROUND 1 COMPLETED (inferred from ESPN Semifinals feed) ---

- OKC 4-0 PHX: CONFIRMED COMPLETE. PHX eliminated.
- NYK 4-2 ATL: CONFIRMED COMPLETE (NYK in Semifinals). ATL eliminated.
- MIN 4-x DEN: LIKELY COMPLETE (MIN in Semifinals). DEN likely eliminated — verify.
- DET 4-3 ORL: LIKELY COMPLETE (DET in Semifinals). ORL likely eliminated — verify.
- CLE 4-3 TOR: LIKELY COMPLETE — verify if CLE in Semifinals.
- PHI 4-3 BOS: LIKELY COMPLETE — verify which team (PHI or BOS) is in East Semifinals.
- SAS 4-x POR: LIKELY COMPLETE (SAS in West Semifinals). POR eliminated — verify.

KEY DATA NOTE: The four confirmed Round 2 series participants are NYK, DET, MIN, OKC. Their Round 1 opponents are eliminated. The four other Semifinals slots must come from: SAS/POR, CLE/TOR, PHI/BOS survivors, and DEN/MIN loser slot is taken by MIN. Verify full bracket from ESPN.

## SECTION:elimination_flags
PLAYOFFS ELIMINATION FLAGS (updated from ESPN live feed)

DATA NOTE: Four teams confirmed in Round 2 (NYK, DET, MIN, OKC) — their Round 1 opponents are therefore eliminated. ESPN 'Game 8' anomalies in Round 1 series are feed errors — those series are complete.

Teams CONFIRMED ELIMINATED:
- Phoenix Suns: OKC won 4-0. CONFIRMED. No further picks.
- Atlanta Hawks: NYK won 4-2 (ESPN confirms NYK in Semifinals). CONFIRMED eliminated.
- Portland Trail Blazers: SAS likely completed series (SAS in West Semifinals per ESPN). VERIFY.
- Orlando Magic: DET in East Semifinals confirmed — ORL LIKELY ELIMINATED. Verify.
- Toronto Raptors: CLE likely completed series — verify from ESPN.
- Boston Celtics or Philadelphia 76ers: ONE of these teams is eliminated (the other is in East Semifinals with DET). PHI led BOS 4-3 per ESPN — if confirmed, BOS ELIMINATED (Tatum OUT decisive). VERIFY which team advanced.
- Denver Nuggets: MIN in West Semifinals confirmed — DEN LIKELY ELIMINATED (MIN led 4-2). Verify.

Teams facing elimination (Round 1 Game 7 — confirmed active):
- Houston Rockets: LAL leads 4-2, Game 7 next. Kevin Durant OUT is critical — HOU survival hinges on his return.

Teams in Round 2 (confirmed active — DO NOT apply elimination logic):
- New York Knicks: leads Round 2 Series 1-0 (East)
- Detroit Pistons: leads Round 2 Series 1-0 (East)
- Minnesota Timberwolves: leads Round 2 Series 1-0 (West)
- Oklahoma City Thunder: leads Round 2 Series 1-0 (West)
- San Antonio Spurs: in West Semifinals (verify opponent and series score)
- Cleveland Cavaliers or Philadelphia 76ers: one of these is in East Semifinals (verify)
- Los Angeles Lakers: will advance if they win Game 7 vs HOU

Do NOT bet on any team confirmed eliminated. Do NOT apply elimination logic to any Round 2 participant.

## SECTION:playoff_rest
PLAYOFF REST RULES (active — Round 1 final / Round 2 early games):
- True B2B does NOT exist in playoffs — NBA mandates minimum 1 day off between games.
- 1 rest day (minimum): short rest — confidence -10 on spread picks for road team.
- 2 rest days: standard rest — no adjustment.
- 3+ rest days: extended rest — slight rust risk for hot teams; confidence -5.
- Home court advantage in playoffs worth ~3-4 points (stronger than regular season ~2-3pts).

ROUND 2 REST NOTE:
- Teams advancing from Round 1 may have 2-7 days rest before Round 2 Game 1.
- Extended rest rust applies if gap ≥ 5 days between last Round 1 game and Round 2 Game 1 — flag in scout_report.
- By Game 3 of Round 2, rust is fully dissipated — remove the -5 rust adjustment.
- Teams in Game 7 (LAL/HOU) will have less rest entering Round 2 than opponents who closed early — this is a meaningful edge in Round 2 Game 1 for the opponent.

Game 7 rest: both teams had identical rest by definition. Home court is the primary differentiator.

Verify actual rest days from ESPN scoreboard — do not assume.

CURRENT REST CONTEXT (approximate — verify from ESPN):
- NYK/DET: in Round 2 with 1 game played; track inter-game rest.
- MIN/OKC: in Round 2 with 1 game played; track inter-game rest.
- LAL/HOU: Game 7 — identical rest. Home court is decisive.
- SAS/CLE/PHI: if advanced, check days since last Round 1 game for Round 2 rust.

## SECTION:playoff_motivation
PLAYOFF MOTIVATION HIERARCHY (Round 1 Final + Round 2 Underway)

1. ROUND 2 — GAME 2 OR 3 (series early stage, 1-0 leads):
   East: NYK leads 1-0 (Game 3 next), DET leads 1-0 (Game 2 next)
   West: MIN leads 1-0 (Game 3 next), OKC leads 1-0 (Game 2 next)
   → Early series: the team leading 1-0 has momentum + home court narrative advantage.
   → Season NetRtg + current franchise player status are primary inputs (in-series signal thin at 1 game).
   → Home court (higher seed) is decisive tiebreaker.
   → Do NOT over-weight single-game Round 2 results — teams adjust tactically game to game.
   → Verify full roster availability — new injuries may have emerged between rounds.
   → Apply Round 2 rust rule: if a team had 4+ days off between rounds, confidence -5 on spread picks.

2. GAME 7 (maximum desperation — season on the line):
   Active confirmed Game 7: LAL vs HOU.
   → Home team in Game 7: add confidence +8 (historically ~60-65% win rate).
   → Road team in Game 7: require odds ≥ 1.90.
   → Do NOT bet spread in Game 7 — ML only.
   → In-series result + home court are primary inputs.

3. DURANT WILDCARD — LAL vs HOU Game 7:
   → Kevin Durant (HOU): roster-only OUT. Do NOT draft HOU ML without Durant confirmed active via NBA official PDF.
   → LAL tactical dominance across 5 games without Doncic is the baseline.
   → If Durant confirmed active + HOU home: legitimate upset risk. Require HOU odds ≥ 2.00.
   → Do NOT bet LAL spread — garbage-time risk.

4. EDWARDS STATUS — MIN Round 2:
   → Anthony Edwards (MIN): was roster-only OUT in Round 1. Re-verify for Round 2.
   → If Edwards confirmed active: MIN offensive ceiling significantly higher — recalibrate MIN confidence.
   → If still OUT: MIN leading Round 2 opponent means team depth is holding — adjust accordingly.

5. OKC DOMINANCE SIGNAL:
   → OKC (NetRtg +11.1) is strongest statistical team. Jalen Williams OUT but SGA + Chet depth is real.
   → OKC leading Round 2 1-0. Home court + NetRtg gap make OKC ML a reliable lean if odds ≥ 1.65.
   → Re-verify SGA, Chet Holmgren active before any OKC pick. MANDATORY.

6. HOME COURT (all games):
   → Playoff home court worth 3-4 points — decisive in close matchups.
   → Game 7 home court historically ~60-65% win rate.
   → Round 2: higher seed has home court — verify from ESPN for each series.
   → Verify home court for EVERY pick before drafting.

7. ROUND 2 RUST FACTOR:
   → Teams with 4+ days off between rounds may show early rust.
   → Apply confidence -5 if rest gap ≥ 5 days for the longer-resting team.
   → By Game 3 or later of Round 2, rust fully dissipated — remove this adjustment.

## SECTION:playin_rules
INACTIVE — Play-In Tournament is over. Do NOT apply any play-in rules.
All series are now best-of-7 Round 1. Use playoff_motivation and playoff_rest sections only.

## SECTION:h2h_playoff
PLAYOFF H2H AND IN-SERIES SIGNALS (updated from ESPN live feed)

CRITICAL CAVEAT: In-series results are the PRIMARY signal in playoff analysis.
Regular season H2H is a last-resort tiebreaker only — heavily discounted.
Round 2 Game 1/2/3: only 1 game of in-series signal. Season NetRtg + home court + rest are primary.

--- ROUND 2 IN-SERIES STATUS ---

East Semifinals — Series A: NYK leads 1-0 (Game 3 next)
- 1 game of in-series data — directional only. NYK won Game 1 on home court (verify score).
- VERIFY opponent from ESPN. If NYK vs PHI: NYK (+6.5 NetRtg) vs PHI (-0.2) — NYK statistical edge; PHI playoff resilience is real. If NYK vs CLE: NYK (+6.5) vs CLE (+4.0) — moderate gap; home court decisive.
- NYK home court as higher seed favoured for Game 3 (if home). Verify.

East Semifinals — Series B: DET leads 1-0 (Game 2 next)
- 1 game of in-series data — very thin. DET won Game 1.
- VERIFY opponent from ESPN. If DET vs CLE: DET (+8.2 NetRtg) vs CLE (+4.0) — DET statistical edge.
- Kevin Huerter (DET) OUT. Re-verify Cade Cunningham, Isaiah Stewart, Jalen Duren. MANDATORY.

West Semifinals — Series A: MIN leads 1-0 (Game 3 next)
- 1 game of in-series data. MIN won Game 1.
- VERIFY opponent from ESPN. Likely DEN (if MIN won Game 7 to close Round 1).
- If MIN vs DEN: MIN (+3.1 NetRtg) vs DEN (+5.2) — DEN season edge; but MIN leads 1-0 in Round 2.
- Edwards re-verification is critical — if active, MIN's effective NetRtg is meaningfully higher.
- Aaron Gordon (DEN): OUT [roster-only]. DEN playing without key defensive forward.

West Semifinals — Series B: OKC leads 1-0 (Game 2 next)
- 1 game of in-series data. OKC won Game 1.
- VERIFY opponent from ESPN. Likely SAS (leads 4-1 in Round 1 — verify if SAS completed series).
- If OKC vs SAS: OKC (+11.1 NetRtg, 64-18) vs SAS (+8.3, 62-20) — OKC statistical favourite; 2.8pt NetRtg gap.
- Jalen Williams (OKC) OUT. Re-verify SGA, Chet Holmgren. MANDATORY.
- Re-verify Victor Wembanyama active for SAS. MANDATORY.

--- ROUND 1 FINAL IN-SERIES STATUS ---

LAL vs HOU (Game 7 — LAL leads 4-2):
- LAL tactical dominance across 5 games with Doncic OUT is definitive in-series signal.
- HOU had better season NetRtg (+5.4 vs +1.7) but in-series result overrides completely.
- Durant (HOU) OUT is the sole wildcard. Verify before any HOU pick.

--- ROUND 1 COMPLETED (inferred from Round 2 bracket) ---

KEY LESSONS FROM ROUND 1 (updated):
1. Franchise player absence > NetRtg gap: Tatum OUT (if BOS eliminated) negated 8.4pt BOS advantage.
2. OKC +11.1 NetRtg is the most reliable signal this postseason — validated by 4-0 sweep.
3. Scheme/in-series execution overrides season stats by Game 5+: LAL, MIN, potentially PHI all confirmed.
4. Edwards OUT (MIN) in Round 1 did not prevent MIN advancing — team depth compensated in-series.
5. Round 2 early games: season NetRtg + home court are primary inputs (1 game of in-series data is thin).
6. ESPN feed anomalies persist: ALWAYS verify series status before drafting.
7. OKC vs SAS (likely Round 2 West matchup): both teams have elite NetRtg; home court and key player availability are tiebreakers. Do NOT over-lean on NetRtg gap alone (only 2.8pts).

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

Teams CONFIRMED ELIMINATED (no further picks):
- Phoenix Suns: eliminated (OKC won 4-0).
- Atlanta Hawks: eliminated (NYK won 4-2 in Round 1).
- Portland Trail Blazers: LIKELY eliminated (SAS in West Semifinals — verify).
- Orlando Magic: LIKELY eliminated (DET in East Semifinals — verify).
- Denver Nuggets: LIKELY eliminated (MIN in West Semifinals, led 4-2 — verify).
- Toronto Raptors: LIKELY eliminated (CLE led 4-3 — verify).
- Boston Celtics or Philadelphia 76ers (one eliminated — verify which via ESPN).
- Washington Wizards: did not qualify for playoffs.

Teams STILL ACTIVE:
- Round 2: NYK, DET, MIN, OKC (all leading 1-0) + their opponents (verify from ESPN)
- Round 1 Game 7: LAL, HOU
- Advancing from Round 1 to Round 2: SAS (likely), CLE or PHI (one of them)
