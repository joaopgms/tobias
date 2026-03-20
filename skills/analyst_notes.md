---
date: 2026-03-20
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
---

## Today's Analysis — 2026-03-20

Atlanta Hawks' 11-game win streak is the most significant analytical signal today — a team with a true talent W% around .500-.550 sustaining this run is historically anomalous, and any opponent priced ≥ 1.80 warrants explicit regression-fade evaluation by Scout. The Pace=0.0 data quality issue persists across all 30 teams, which continues to block totals betting and pace-based spread analysis — this is a systemic gap that must be resolved for full market coverage. With OKC, Spurs, and Pistons all likely resting stars as they lock in seeding, the play-in bubble teams (Charlotte, Portland, Clippers, Philadelphia) entering high-motivation stretches represent an underexplored edge source for the next 2-3 weeks.



## Scout patches applied
- [franchise_player_rules] Verified franchise player list updated this session — removed players not present in ESPN/NBA injury feed cross-reference (Hartenstein, Dort, Aaron Gordon, Wendell Moore Jr.) and added newly confirmed absences (Josh Hart NYK, Isaiah Stewart DET) per verified list.
- [tanking_teams] Standings updated with current session data — Wizards now L14 streak, Spurs 52-18, Lakers 45-25 W8, Pistons 50-19, Hawks W11 confirmed, Warriors L10 2-8 now elevated to tank-watch risk.

## Commit patches applied
None

## Intelligence gaps identified
- **Pace data is 0.0 for all 30 teams across every session — this appears to be a persistent data pipeline failure, not a one-off.** — Totals betting is currently blocked by market_rules ('Only bet totals when advanced stats including Pace are available'), and pace-based spread signals (pace mismatch > 5, both teams > 100) cannot be evaluated — Scout is systematically excluded from the O/U market. → Escalate as a data pipeline fix priority; in the interim, add a fallback rule to market_rules that allows totals evaluation using OffRtg + DefRtg alone (without Pace) when Pace=0.0 across the board, with a confidence penalty of -10 to account for missing pace context.
- **No NetRtg L15 data is available — only season NetRtg — despite priority_stats ranking it as the #1 predictive signal.** — Scout is instructed to prioritise NetRtg L15 above all other stats, but is actually evaluating picks using season NetRtg as a proxy, which is a materially weaker signal especially late in the season when teams have changed rosters or motivation. → Add a data_quality_rules note that when NetRtg L15 is unavailable, season NetRtg may be used as fallback but confidence should be reduced by -5 on any pick where the L15 signal would have been decisive.
- **No rule currently addresses the scenario where a top-seeded team (OKC, Spurs, Pistons) rests stars for load management in the final 3 weeks of the regular season.** — OKC (55-15), Spurs (52-18), and Pistons (50-19) are all locked into top seeds — the probability of scheduled rest nights increases sharply, which could create same-day line movement that Scout at 14:00 UTC won't anticipate if the rest decision comes after Scout runs. → Add a note to franchise_player_rules and tanking_teams: teams with ≥ 50 wins and locked seeding in final 3 weeks of season carry elevated unannounced rest risk — Commit should apply an additional confidence -10 for any pick on these teams if the game is in their final 15 regular season games and the player's injury status is not confirmed active by tip-off.
- **The HOT STREAK FADE RULE requires opponent odds ≥ 1.80, but does not define how to handle cases where the hot team is also a legitimate top-10 team by NetRtg (e.g. if a team with NetRtg +5 goes on a W10 streak — the streak may be skill, not luck).** — Atlanta's W11 streak is correctly flagged as regression risk because their NetRtg (+1.5) is mediocre, but the rule as written would also trigger on OKC (W10, NetRtg +10.9), which would be analytically incorrect — OKC's streak reflects genuine elite quality. → Add a qualifier to the HOT STREAK FADE RULE: only apply regression-fade logic when the hot team's NetRtg is below +5.0 — teams with NetRtg ≥ +5.0 on a win streak are more likely sustaining genuine quality than running above true talent.
