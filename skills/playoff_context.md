---
version: 1
updated_at: 2026-04-13T00:00:00+00:00
updated_by: system
---

## SECTION:phase
playoffs

## SECTION:series_context
[Analyst updates this section daily with current series scores and home court info.]

No series data yet — Analyst will populate on first playoff run.

## SECTION:elimination_flags
[Analyst flags any team facing elimination (down 3-0 or 3-1 in a best-of-7, or in a win-or-go-home play-in game).]

No elimination data yet.

## SECTION:playoff_rest
Playoff schedule rest rules (replaces regular-season B2B rules):
- True B2B does NOT exist in playoffs — NBA mandates minimum 1 day off between games.
- 1 rest day (minimum): short rest — confidence -10 on spread picks for the road team.
- 2 rest days: standard rest — no adjustment.
- 3+ rest days: extended rest — slight rust risk for hot teams; confidence -5.
- Home court advantage in playoffs is worth ~3-4 points (stronger than regular season ~2-3pts).

## SECTION:playoff_motivation
Playoff motivation hierarchy (replaces regular-season play-in/tank motivation):
1. ELIMINATION GAME: team facing series elimination — maximum desperation factor.
   → Road underdog facing elimination: add confidence +10 (historically covers at higher rate).
   → Home favourite to close: add confidence +5.
2. SERIES MOMENTUM: team up 3-0 or 3-1 — closing-out focus, may rest starters in blowouts.
   → Do NOT bet the team up 3-0 at short spread odds — closing games can be looser.
3. HOME COURT SERIES SWING: home team that lost Game 1 — historically very motivated to respond.
   → Add confidence +5 for home team coming off Game 1 loss.
4. ROAD TEAM UP IN SERIES: rare and high-signal — add confidence +5 on road team to continue run.
5. NORMAL PLAYOFF GAME: no series-specific adjustment.

## SECTION:playin_rules
Play-in specific rules (applies only during play-in phase):
- Win-or-go-home for 8-seed (loser of 7v8 game): maximum desperation, treat as elimination game.
- 9-seed and 10-seed: both games are win-or-go-home — full elimination urgency.
- Teams playing in the play-in have been motivated all season — their regular season L15 form is relevant.
- Home court in play-in is meaningful — home team has historically covered at higher rate in play-in games.

## SECTION:l15_caveat
L15 NetRtg caveat for playoffs:
- Regular season margins against eliminated/tanking opponents are less predictive in playoffs.
- Weight the most recent 5-7 games (playoff games if available) more heavily than the full L15.
- If a team played multiple playoff games already this series, those margins are more predictive than regular season ones.
- L15 remains the primary directional signal but apply with playoff context awareness.

## SECTION:no_tanking
Tanking does not exist in playoffs or play-in. All remaining teams are motivated.
Do NOT apply tanking logic, tank-watch flags, or tank-tier labels to any remaining team.
Ignore the regular-season tanking_teams section entirely during this phase.
