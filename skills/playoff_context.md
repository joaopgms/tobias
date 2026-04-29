---
version: 19
updated_at: 2026-04-29T12:16:16.849956+00:00
updated_by: analyst_2026-04-29
llm: claude-sonnet-4-6
---

## SECTION:phase
First Round Playoffs

Play-In Tournament is OVER. First Round Playoffs (best-of-7) are active.
Apply series context, elimination urgency, and Round 1 rest rules — NOT play-in rules.
playin_rules section is INACTIVE this phase — ignore it entirely.

## SECTION:series_context
FIRST ROUND PLAYOFFS — Active (updated 2026-04-29)

Play-in results: Phoenix Suns won West 7-seed, Orlando Magic won East 8-seed.

EAST Round 1 (home team listed first in series):
- Boston Celtics vs Philadelphia 76ers: BOS leads 3-2 — Game 6 next (verify home court per ESPN — if BOS home, BOS closes; if PHI home, PHI survival game)
  NOTE: Series alive — PHI survived Game 5. BOS (+8.2 NetRtg) vs PHI (-0.2 NetRtg) — BOS statistical edge massive. Re-verify Tatum, Brown active before any pick. PHI facing road elimination if at BOS.
- Orlando Magic vs Detroit Pistons: ORL leads 3-1 — Game 6 next (likely at DET — DET survival game)
  NOTE: ORL can close on road. DET facing elimination. Re-verify DET franchise players. ORL (NetRtg +0.6) vs DET (NetRtg +8.2) — DET holds statistical edge despite being down 3-1. In-series results override NetRtg here.
- Atlanta Hawks vs New York Knicks: NYK leads 3-2 — Game 6 next (verify home court per ESPN — likely at ATL, ATL survival game)
  ALERT: DATA CONFLICT — Trae Young appears in WAS verified absence feed. Do not assume ATL roster composition. ATL (NetRtg +2.4) vs NYK (NetRtg +6.5). ATL facing road elimination if at NYK or survival game at home.
- Cleveland Cavaliers vs Toronto Raptors: Verify current score per ESPN — ESPN scoreboard shows play-in style 0-0 entry; CLE (NetRtg +4.0) likely leads given record differential (+6 wins). TOR Quickley OUT reduces offensive load significantly. Verify before any pick.

WEST Round 1 (home team listed first in series):
- Oklahoma City Thunder vs Phoenix Suns: OKC leads 4-0 — SERIES COMPLETE or Game 5 is series-ending game. Verify series conclusion via NBA official. OKC advances to Round 2 if confirmed 4-0.
- Los Angeles Lakers vs Houston Rockets: LAL leads 3-1 — Game 5 next at LAL (LAL can close at home)
  MAJOR ALERT: LAL dominating HOU despite Doncic + Reaves both OUT. HOU facing road elimination.
  Durant status unresolved — do not draft HOU without Durant confirmed active. Require HOU odds ≥ 2.20.
- San Antonio Spurs vs Portland Trail Blazers: SAS leads 4-1 — SERIES COMPLETE or Game 6 is series-ending. Verify series conclusion. SAS advances to Round 2 if confirmed. POR (NetRtg -0.2) vs SAS (NetRtg +8.3) — 8.5pt gap fully reflected in series score.
- Minnesota Timberwolves vs Denver Nuggets: MIN leads 3-2 — Game 6 next at MIN (MIN can close on home floor)
  NOTE: DEN survived Game 5 elimination at home. Game 6 at MIN — MIN home court (+3-4 pts playoff) + potential Edwards factor. Jokic historically elevates in elimination games but faces road elimination. Edwards status CRITICAL — was listed OUT but appeared active; re-verify vs NBA official PDF.

PLAY-IN GAMES (ESPN shows 4 x Tied 0-0 entries):
- East 7th Place vs 8th Place: 0-0 — verify participating teams and date from ESPN
- East 8th Seed Game: 0-0 — verify participating teams and date from ESPN
- West 9th Place vs 10th Place: 0-0 — verify participating teams and date from ESPN
- West 8th Seed Game: 0-0 — verify participating teams and date from ESPN
NOTE: These may be upcoming play-in games for unseeded teams or data artefacts — verify against NBA schedule. If active, treat all teams as fully motivated (win-or-go-home).

## SECTION:elimination_flags
ROUND 1 ELIMINATION FLAGS (as of 2026-04-29):

Series likely complete (verify via NBA official):
- Oklahoma City Thunder eliminated Phoenix Suns: OKC leads 4-0. Game 5 may be series-ending formality. Verify — if complete, OKC advances to Round 2.
- San Antonio Spurs vs Portland Trail Blazers: SAS leads 4-1. Game 6 may be series-ending. Verify — if complete, SAS advances to Round 2.

Teams facing elimination (one loss = series over):
- Houston Rockets: down 3-1 vs LAL. Next game at LAL (road elimination). Historical: teams down 3-1 win series ~4% of time. Durant status unresolved — do NOT bet HOU ML unless Durant confirmed active + odds ≥ 2.20.
- Denver Nuggets: down 3-2 vs MIN. Next game at MIN (road Game 6 elimination). DEN survived Game 5 — Jokic factor elevated. Road elimination game. Re-verify Edwards status for MIN.
- Philadelphia 76ers: down 3-2 vs BOS. Next game is elimination game (verify location). PHI depleted roster — do NOT bet PHI ML unless BOS has key absences confirmed.
- Portland Trail Blazers: down 4-1 vs SAS. Series near-complete — verify if Game 6 is being played. POR motivated but SAS dominance confirms elimination.
- Detroit Pistons: down 3-1 vs ORL. Next game at DET (home survival). DET (NetRtg +8.2) statistical advantage has not translated to series results — ORL's scheme overriding stats. DET must win or eliminated.
- Atlanta Hawks: down 2-3 vs NYK. Facing elimination. Trae Young affiliation DATA CONFLICT makes ATL picks very high risk — do not draft without verification.

Teams that can CLOSE OUT:
- Los Angeles Lakers (vs HOU): can clinch at home (3-1). WARNING: closing-game looseness risk — ML only if value exists. Do NOT bet LAL spread at short odds.
- Minnesota Timberwolves (vs DEN): leads 3-2, can clinch at home (Game 6). Edwards re-verify critical. Home-close advantage + playoff motivation peak.
- Boston Celtics (vs PHI): leads 3-2, next elimination game (verify if at BOS — closing out or survival). BOS should win on statistical merit.
- Orlando Magic (vs DET): leads 3-1, can clinch on road at DET. ORL road-close scenario — same closing looseness caution applies.
- New York Knicks (vs ATL): leads 3-2, can clinch (verify location). If at ATL, NYK road closing; if at NYK, NYK home close.

Applying elimination/desperation adjustments:
→ Road team facing elimination (HOU at LAL, DEN at MIN): confidence +10, stake conservatively, require odds ≥ 2.00.
→ Home team facing elimination (DET vs ORL, ATL if home Game 6): confidence +5, desperation home bounce.
→ Home team closing out (MIN vs DEN at home, BOS if at home): avoid spread — ML only if value. Garbage time risk.
→ ORL road close at DET: ORL closing away — apply closing-team caution, no spread.

HIGH-RISK FLAGS:
- DEN Game 6 at MIN: Jokic proven elimination-game performer. Do not dismiss DEN ML at ≥ 2.00 odds even on road. MIN home court (+3-4 pts) + Edwards (if active) = formidable counter. Confidence +10 for DEN (road elimination) but require odds ≥ 2.00.
- HOU down 3-1: historically near-hopeless without Durant confirmed. Requires Durant confirmed active + odds ≥ 2.20.
- ATL vs NYK: DATA CONFLICT on Trae Young affiliation makes ATL picks VERY HIGH RISK — do not draft ATL picks until verified.
- DET vs ORL Game 6: DET home elimination. DET NetRtg +8.2 vs ORL +0.6 — stats say DET should win but in-series ORL leads 3-1. Home elimination desperation vs ORL's series momentum creates genuine uncertainty.
- BOS vs PHI: BOS can close — if at PHI it's PHI's survival game; if at BOS it's BOS closing. Check home court carefully.

## SECTION:playoff_rest
ROUND 1 REST RULES (active):
- True B2B does NOT exist in playoffs — NBA mandates minimum 1 day off between games.
- 1 rest day (minimum): short rest — confidence -10 on spread picks for the road team.
- 2 rest days: standard rest — no adjustment.
- 3+ rest days: extended rest — slight rust risk for hot teams; confidence -5.
- Home court advantage in playoffs worth ~3-4 points (stronger than regular season ~2-3pts).

Verify actual rest days from ESPN scoreboard — do not assume.

## SECTION:playoff_motivation
Playoff motivation hierarchy (Round 1 — best-of-7, Games 5-7 stage):

1. ELIMINATION GAME: team facing series elimination — maximum desperation factor.
   → Home team facing elimination: add confidence +5 (home floor + desperation).
   → Road team facing elimination: add confidence +10 (nothing-to-lose factor) BUT stake conservatively.
     Require odds ≥ 2.00 for road elimination plays.
   → Do NOT over-pay for the team about to close — blowout risk and star-resting in garbage time.

2. SERIES MOMENTUM (up 3-1 closing): closing team adds +5 IF road (road dominance signal).
   → Do NOT bet the closing team at short spread odds — closing looseness risk.
   → If closing team is heavy spread favourite (< 1.65), avoid spread — take ML only if value exists.

3. SURVIVED ELIMINATION GAME MOMENTUM: team that just survived an elimination game carries confidence.
   → Apply confidence +5 for the team that survived elimination in the prior game, IF they are at home next.
   → Road survival momentum less predictive — no additional bonus for road Game 6 after road Game 5 survival.
   → DEN survived Game 5 at home, now faces road Game 6 — no survival bonus (road context).

4. HOME COURT SERIES SWING: home team coming off a loss — historically very motivated to respond.
   → Add confidence +5 for home team coming off a loss in series.

5. TIED SERIES (2-2): both teams fully motivated. Home court worth 3-4 pts in playoffs. Treat as baseline — no desperation adjustment. Standard home court edge applies.

6. JOKIC ELIMINATION FACTOR: Nikola Jokic historically elevates in playoff elimination games.
   Apply additional confidence +5 for DEN if facing elimination. NOTE: DEN faces road elimination (Game 6 at MIN) — road elimination = highest desperation, MIN home court partially offsets. Stack: road elimination +10 + Jokic factor +5 = net +15 raw, BUT MIN home court -3 to -4 pts effective = temper enthusiasm.

7. CLOSING TEAM CAUTION (up 3-0, 3-1, or 3-2 closing): teams may lose focus in blowouts, starters may rest.
   Do NOT bet spread on these teams at < 1.70. ML only where genuine value exists.
   Current closing teams: LAL (3-1 at home), MIN (3-2 at home), ORL (3-1 on road), NYK (3-2 — verify location), BOS (3-2 — verify location).

8. SERIES 3-2 DYNAMIC: Both teams in must-win mode effectively. Home team has historical advantage.
   BOS vs PHI (3-2), MIN vs DEN (3-2), NYK vs ATL (3-2): all are high-intensity must-win situations.
   Do not assume closing team wins — treat as genuine coin-flips modified by NetRtg and home court.

9. NORMAL PLAYOFF GAME: no series-specific adjustment.

## SECTION:playin_rules
INACTIVE — Play-In Tournament is over. Do NOT apply any play-in rules.
All series are now best-of-7 Round 1. Use playoff_motivation and playoff_rest sections only.

## SECTION:h2h_playoff
Regular season H2H as a Round 1 signal — Games 5-6 stage:

CRITICAL CAVEAT: At Games 5-7 of any series, in-series results are THE primary signal.
Regular season H2H is near-irrelevant at this stage. Coaching adjustments have fully operated.
Only use regular season H2H as a last-resort tiebreaker, heavily discounted.

Multiple teams had franchise players OUT for extended regular season periods.
H2H records compiled with depleted rosters must be discounted:
- LAL (Doncic + Reaves both OUT) — any H2H vs HOU with Doncic absent is irrelevant
- OKC (Williams OUT) — H2H vs PHX compiled with different roster; use with caution
- HOU (Durant status unresolved) — H2H may reflect different lineup than current
- MIN (Edwards was OUT) — H2H vs DEN compiled with significantly different roster; heavy discount required
- ATL (Trae Young affiliation unresolved) — H2H data unreliable until affiliation confirmed

Active series in-series signals (primary):
- ORL vs DET: ORL leads 3-1. In-series dominance is the signal — ORL's scheme overriding DET's better NetRtg. Regular season H2H adds no edge at Game 6.
- OKC vs PHX: OKC leads 4-0. In-series dominance definitive. Series likely complete — no further H2H needed.
- ATL vs NYK: NYK leads 3-2. In-series result is the signal — NYK edge confirmed despite ATL's periodic wins. DATA CONFLICT on ATL roster makes any H2H analysis unreliable.
- MIN vs DEN: MIN leads 3-2. DEN's W12 regular season streak did NOT translate. In-series is definitive signal — MIN has neutralised Jokic. Edwards (if active) critical to MIN defensive scheme.
- CLE vs TOR: Verify exact series score from ESPN. CLE likely leads given record/NetRtg differential (+4.0 vs +2.6). Regular season H2H likely CLE dominant but verify.
- BOS vs PHI: BOS leads 3-2. In-series confirms BOS edge despite PHI survival. PHI depleted roster discounts any H2H.
- SAS vs POR: SAS leads 4-1. Series near-complete. NetRtg gap (+8.5pts) reflected in series outcome. No further H2H analysis needed.
- LAL vs HOU: LAL leads 3-1. H2H fully irrelevant — series result confirms LAL tactical dominance. HOU in-series collapse is the operative signal.

## SECTION:l15_caveat
L15 NetRtg caveat for Round 1 playoffs (Games 5-7 stage):

CRITICAL: At Games 5-7, in-series results are the PRIMARY signal. Regular season L15 is directional context only.
Weight the most recent in-series playoff games MORE heavily than any regular season metric.

Key NetRtg vs series result divergences (confirmed as of 2026-04-29):

- DEN (+5.2 NetRtg) vs MIN (+3.1 NetRtg): DEN's statistical edge has NOT translated — MIN leads 3-2. DEN's W12 regular season streak was misleading. MIN scheme/Edwards factor (when healthy) is the operative signal. Do not over-weight DEN's NetRtg advantage.

- LAL (+1.7 NetRtg) vs HOU (+5.4 NetRtg): HOU had better season NetRtg yet LAL leads 3-1. LAL tactical scheme and defensive identity have overridden HOU's statistical advantage. In-series result is definitive.

- ORL (+0.6 NetRtg) vs DET (+8.2 NetRtg): ORL leads 3-1 despite massive NetRtg disadvantage. This is the largest NetRtg-vs-series-result divergence in Round 1. ORL's pace, defensive scheme, and execution have completely overridden DET's season rating. Do NOT use DET's NetRtg as a primary signal — in-series performance is the only valid metric here.

- SAS (+8.3 NetRtg) vs POR (-0.2 NetRtg): SAS leads 4-1 — NetRtg gap (+8.5pts) IS reflected in series outcome. L15 directional confirmed by series result. Consistent case.

- BOS (+8.2 NetRtg) vs PHI (-0.2 NetRtg): BOS leads 3-2 — PHI survived Game 5. NetRtg gap partially reflected but PHI's desperation has tightened the series. L15 directional remains valid for BOS but PHI survival factor adds uncertainty.

- ATL (+2.4 NetRtg) vs NYK (+6.5 NetRtg): NYK leads 3-2 — NYK's NetRtg advantage IS being reflected. In-series validates the L15 directional signal for NYK.

- OKC (+11.1 NetRtg) vs PHX (+1.4 NetRtg): OKC leads 4-0. Massive NetRtg gap fully reflected. L15 directional completely validated.

KEY LESSON: ORL vs DET is the clearest example of why in-series results must override NetRtg at late playoff stages. A team leading 3-1 has solved their opponent tactically regardless of season metrics.

## SECTION:no_tanking
Tanking does not exist in playoffs. All remaining teams are fully motivated.
Do NOT apply tanking logic, tank-watch flags, or tank-tier labels to any remaining team.
Ignore the regular-season tanking_teams section entirely.
