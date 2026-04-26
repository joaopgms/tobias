---
version: 16
updated_at: 2026-04-26T11:37:52.009061+00:00
updated_by: analyst_2026-04-26
llm: claude-sonnet-4-6
---

## SECTION:phase
First Round Playoffs

Play-In Tournament is OVER. First Round Playoffs (best-of-7) are active.
Apply series context, elimination urgency, and Round 1 rest rules — NOT play-in rules.
playin_rules section is INACTIVE this phase — ignore it entirely.

## SECTION:series_context
FIRST ROUND PLAYOFFS — Active (updated 2026-04-26)

Play-in results: Phoenix Suns won West 7-seed, Orlando Magic won East 8-seed.

EAST Round 1 (home team listed first in series):
- Boston Celtics vs Philadelphia 76ers: BOS leads 2-1 — Game 4 at PHI upcoming
- Orlando Magic vs Detroit Pistons: Tied 2-2 — Game 5 next [series flipped since last update]
  NOTE: ORL had leads 2-1 last session; DET responded. Series now dead even.
- Atlanta Hawks vs New York Knicks: ATL leads 2-1 — Game 4 upcoming at ATL
  ALERT: 6-seed ATL (NetRtg +2.4) leading 3-seed NYK (NetRtg +6.5). ATL home court physical style neutralising NYK.
- Cleveland Cavaliers vs Toronto Raptors: CLE leads 2-1 — Game 4 at TOR upcoming

WEST Round 1 (home team listed first in series):
- Oklahoma City Thunder vs Phoenix Suns: OKC leads 3-0 — Game 4 next at PHX
  NOTE: OKC dominant without Jalen Williams. SGA + Holmgren carrying. PHX facing elimination at home.
- Los Angeles Lakers vs Houston Rockets: LAL leads 3-0 — Game 4 at HOU upcoming
  MAJOR ALERT: LAL sweeping HOU despite Doncic + Reaves both OUT. HOU facing elimination at home.
- San Antonio Spurs vs Portland Trail Blazers: SAS leads 2-1 — Game 4 at POR upcoming
- Minnesota Timberwolves vs Denver Nuggets: MIN leads 3-1 — Game 5 next at DEN
  NOTE: DEN (NetRtg +5.2, W12 regular season) has collapsed vs MIN. DEN facing elimination on home floor.
  Edwards factor: MIN's defensive intensity has disrupted Jokic rhythm.

## SECTION:elimination_flags
ROUND 1 ELIMINATION FLAGS (as of 2026-04-26):

Teams facing elimination (down 3-0 — one loss = series over):
- Houston Rockets: down 3-0 vs LAL. Next game at HOU (home). Maximum desperation — home court with backs against wall. Without Durant confirmed active, HOU lacks firepower. Historical: teams down 3-0 win the series < 3% of the time.
- Phoenix Suns: down 3-0 vs OKC. Next game at PHX (home). Home court urgency but OKC dominant. Suns must extend or exit.

Teams facing elimination (down 3-1 — one loss = series over):
- Denver Nuggets: down 3-1 vs MIN. Next game at DEN (home). Home court must-win for DEN. Jokic historically elevates in elimination games — apply +5 desperation edge if betting DEN.

Teams at risk (down 2-1 — series still very alive):
- Philadelphia 76ers: down 2-1 vs BOS, Game 4 at home. PHI must win to stay alive.
- New York Knicks: down 2-1 vs ATL, Game 4 at ATL. Road must-win.
- Toronto Raptors: down 2-1 vs CLE, Game 4 at home. Home must-win.

Applying elimination/desperation adjustments:
→ Home team facing elimination (HOU, PHX, DEN): confidence +5 (home floor + desperation).
→ Road team facing elimination (rare in playoffs): confidence +10 but stake conservatively.
→ Do NOT blindly take the team up 3-0 (LAL, OKC) or 3-1 (MIN) at short spread odds — blowout risk in garbage time, starters may be rested.
→ Series-closing games (team can clinch): closing team may play conservatively if big lead; fade spreads on heavy favourites closing out.

HIGH-RISK FLAGS:
- DEN elimination game at home: Jokic is a proven elimination-game performer. Do not dismiss DEN ML at reasonable odds.
- HOU down 3-0: historically near-hopeless but home desperation factor exists. Requires Durant confirmed.
- OKC-PHX Game 4: PHX desperate at home — if Suns have key players active, value on PHX ML if odds ≥ 2.00.

## SECTION:playoff_rest
ROUND 1 REST RULES (active):
- True B2B does NOT exist in playoffs — NBA mandates minimum 1 day off between games.
- 1 rest day (minimum): short rest — confidence -10 on spread picks for the road team.
- 2 rest days: standard rest — no adjustment.
- 3+ rest days: extended rest — slight rust risk for hot teams; confidence -5.
- Home court advantage in playoffs worth ~3-4 points (stronger than regular season ~2-3pts).

Verify actual rest days from ESPN scoreboard — do not assume.

## SECTION:playoff_motivation
Playoff motivation hierarchy (Round 1 — best-of-7):
1. ELIMINATION GAME: team facing series elimination — maximum desperation factor.
   → Home team facing elimination: add confidence +5 (home floor + desperation).
   → Road underdog facing elimination: add confidence +10 (historically covers at higher rate — nothing to lose).
   → Do NOT over-pay for the team about to close — blowout risk and star-resting in garbage time.
2. SERIES MOMENTUM: team up 3-0 or 3-1 — closing-out focus, may rest starters in blowouts.
   → Do NOT bet the team up 3-0 or 3-1 at short spread odds — closing games can be loose.
   → If closing team is heavy spread favourite (< 1.65), avoid spread — take ML only if value exists.
3. HOME COURT SERIES SWING: home team that lost Game 1 — historically very motivated to respond.
   → Add confidence +5 for home team coming off Game 1 loss.
4. ROAD TEAM UP IN SERIES: rare and high-signal — add confidence +5 on road team to continue run.
5. ELIMINATION GAME — HOME JOKIC FACTOR: Nikola Jokic historically elevates in playoff elimination games at home. Apply additional confidence +5 for DEN at home if facing elimination (stacks with +5 home elimination bonus = +10 total).
6. NORMAL PLAYOFF GAME: no series-specific adjustment.

## SECTION:playin_rules
INACTIVE — Play-In Tournament is over. Do NOT apply any play-in rules.
All series are now best-of-7 Round 1. Use playoff_motivation and playoff_rest sections only.

## SECTION:h2h_playoff
Regular season H2H as a Round 1 signal:

How to use H2H:
- 3-1 or 4-0 regular season H2H dominance → confidence +8 on the dominant team.
  Apply in Games 1-3 only — coaching adjustments diminish edge by Game 4+.
- 2-2 split → neutral, no adjustment.
- 1-3 or 0-4 → confidence +8 on the team that dominated.
- H2H games played with significantly different rosters → flag and heavily discount.

CRITICAL CAVEAT: Multiple teams had franchise players OUT for extended regular season periods.
H2H records compiled with depleted rosters must be discounted:
- LAL (Doncic + Reaves both OUT all series) — any H2H vs HOU with Doncic absent is irrelevant
- OKC (Williams now OUT) — H2H vs PHX compiled with different roster; use with caution
- HOU (Durant status unresolved) — H2H may reflect roster not matching current lineup

Active series H2H — verify from ESPN before each game (these are approximations, not confirmed):
- ORL vs DET: Series tied 2-2. Regular season H2H — re-verify from ESPN. Both teams relatively healthy.
- OKC vs PHX: OKC leads 3-0. Regular season H2H — discount any game where Williams was absent. PHX home for Game 4.
- ATL vs NYK: ATL leads 2-1. Regular season H2H — discount any NYK game with Brunson absent. Physical ATL style.
- MIN vs DEN: MIN leads 3-1. DEN's regular season W12 streak did NOT translate. MIN defensive physicality has neutralised Jokic enough to lead 3-1.
- CLE vs TOR: CLE leads 2-1. Re-verify regular season H2H — likely CLE dominant given season records.
- BOS vs PHI: BOS leads 2-1. Re-verify regular season H2H — PHI depleted roster may discount H2H.
- SAS vs POR: SAS leads 2-1. Re-verify from ESPN.
- LAL vs HOU: LAL leads 3-0. H2H largely irrelevant — LAL depleted roster with no Doncic/Reaves; HOU without Durant; series result speaks louder than H2H.

NOTE: By Game 4+ of any series, coaching adjustments have largely neutralised H2H edge. Weight in-series results more heavily than regular season H2H at this stage.

## SECTION:l15_caveat
L15 NetRtg caveat for Round 1 playoffs:
- Regular season margins against eliminated/tanking opponents are less predictive in playoffs.
- Weight the most recent 5-7 games (playoff games if available) more heavily than full L15.
- Playoff games played so far in this series are MORE predictive than regular season L15.
- L15 remains the primary directional signal but apply with playoff context awareness.
- DEN W12 regular season streak has NOT translated (down 2-1 to MIN) — do not over-weight.
- LAL leading 3-0 without stars is anomalous — their regular season metrics with depleted
  roster do not predict this; HOU's collapse may be the bigger factor.

## SECTION:no_tanking
Tanking does not exist in playoffs. All remaining teams are fully motivated.
Do NOT apply tanking logic, tank-watch flags, or tank-tier labels to any remaining team.
Ignore the regular-season tanking_teams section entirely.
