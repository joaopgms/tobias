---
date: 2026-04-05
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (0 bets)
---

## Today's Analysis — 2026-04-05

The two most significant factual developments this session are Cleveland's dual franchise big man absence (Jarrett Allen + Evan Mobley both OUT roster-only) and the Lakers losing both Doncic and Austin Reaves — both teams' NetRtg figures are effectively misleading until these absences are confirmed via NBA official PDF. Performance data continues to show a severe High-confidence bet problem (0W/5L, -€518.54) with all losses concentrated in the 1.90–2.10 odds band, reinforcing that the system is over-confident on picks that the market has efficiently priced — the strategic implication is that genuine edge at these odds is rarer than current confidence scores suggest. Denver's W8 streak with a +4.8 NetRtg and intact roster is the cleanest directional signal in the league right now alongside OKC.

## Performance Stats
ALL-TIME: 6W / 12L | Win rate: 33.3% | P&L: €-738.24 | Avg odds: 2.0 | Avg conf: 64.9/100
RECENT 18: 6W / 12L | 33.3% WR | P&L: €-738.24
By market:      ML 10bets 4W/6L 40.0% €-206.91  |  SPREAD 6bets 2W/4L 33.3% €-347.06  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 5bets 0W/5L 0.0% €-518.54  |  Medium 11bets 6W/5L 54.5% €-78.39  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 4bets 2W/2L 50.0% €-62.95  |  1.90-2.09 11bets 4W/7L 36.4% €-445.98  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Verified feed adds Austin Reaves, Jarrett Allen, Evan Mobley, Sam Merrill, Tristan Vukcevic as new OUT entries; Emanuel Miller removed from SAS list; dual CLE big man absence is a critical franchise-level risk requiring explicit agent warning.
- [tanking_teams] Standings updated from feed (Spurs 59-19 streak now L1, Nuggets updated to 50-28 W8, Pistons 57-21 W3, 76ers updated record/streak); new franchise absences (Austin Reaves, Jarrett Allen, Evan Mobley) materially change CLE and LAL threat assessments; Tristan Vukcevic confirmed OUT via injury landscape.

## Commit patches applied
None

## Intelligence gaps identified
- **High-confidence bets (conf 70-84+) are 0W/5L for -€518.54, suggesting confidence calibration is systematically inflated relative to actual edge in the 1.90-2.10 odds band.** — Every strategic section (ev_requirement, confidence_staking, selectivity) assumes confidence scores are calibrated; if the market is consistently pricing these games correctly and our high-conf picks are 0%, the confidence floor for high-stake picks should be materially higher or the staking for 'High' tier should be reduced. → After reaching 30+ total settled bets (milestone threshold), run a full calibration audit: compare conf tier vs actual win rate and reduce 'High' tier staking from 20-25% to 15-20% if the 0% win rate persists past 10 high-conf bets. Currently at 5 bets — below the 20-bet evidence threshold to patch.
- **Spread market is 2W/4L (33.3%, -€347.06) and Totals are 0W/2L (0%, -€184.27) — both alternative markets are underperforming ML despite the system actively targeting them.** — The market_rules section has confidence floors (60 for spread, 65 for totals) set below what may be required for genuine edge; if spreads and totals continue losing at current rates, these floors should be tightened or the markets avoided until sample quality improves. → Raise spread confidence floor to 65 and totals confidence floor to 70 when the sample reaches 10+ bets per market; currently spread at 6 bets — approaching threshold. Flag for reassessment at 10 spread bets settled.
- **Cleveland Cavaliers are listed with both franchise-level bigs (Jarrett Allen + Evan Mobley) OUT via roster-only flags, but their published NetRtg (+4.0) and record (48-29) were built with those players — creating a significant line mispricing risk that no current rule explicitly addresses.** — Scout's NetRtg-based confidence assessment would see CLE at +4.0 and treat them as a solid team, but the actual roster they'll field is radically different; a rule explicitly flagging 'dual franchise-level absence = treat NetRtg as unreliable' would prevent overconfident CLE picks. → Add a rule to franchise_player_rules: when 2+ roster-only OUT flags affect the same team's frontcourt or primary ball-handlers, cap confidence at 45 and require NBA official PDF verification before any pick on that team regardless of other signals. Confidence in this suggestion is ~0.75.
- **San Antonio Spurs streak snapped (now L1 after being listed as W11 in prior session) but no L10 regression signal is currently tracked for teams exiting very long win streaks.** — Teams exiting 10+ game win streaks show elevated regression probability in the following 5 games; Scout has a hot-streak fade rule but it targets sub-.550 W% teams — SAS at 59-19 (.756) wouldn't trigger it despite the streak-end signal being potentially valuable. → Add a 'post-streak cooldown' note to selectivity or tanking_teams: when an elite team (W% > .700) ends a streak of 8+ games, flag the next 3 games as requiring +5 confidence buffer before backing them at odds < 1.60.
