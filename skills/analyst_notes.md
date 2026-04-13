---
date: 2026-04-13
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (9 bets)
---

## Today's Analysis — 2026-04-13

Play-In Tournament phase is now active, with the most notable structural change being Victor Wembanyama's addition to the SAS verified absence feed and additional Hawks role players (CJ McCollum, Onyeka Okongwu, Gabe Vincent) now confirmed OUT — these significantly thin two of the top play-in/playoff contenders' depth. Denver's W12 streak is the dominant macro trend: with Jamal Murray out but Jokic's status unverified, any play-in or early playoff DEN bet requires mandatory verification before drafting. The odds performance data shows a critical pattern worth watching: bets at 2.10-2.50 are 0W/3L (0.0%, -€229) while speculative bets are 0W/2L — both suggest Scout must avoid high-odds and low-confidence picks in the play-in phase when volatility is maximum.

## Performance Stats
ALL-TIME: 12W / 15L | Win rate: 44.4% | P&L: €-202.64 | Avg odds: 1.98 | Avg conf: 65.4/100
RECENT 20: 11W / 9L | 55.0% WR | P&L: €+407.86
By market:      ML 12bets 5W/7L 41.7% €-256.91  |  SPREAD 12bets 6W/6L 50.0% €+77.54  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 8bets 3W/5L 37.5% €+32.90  |  Medium 17bets 9W/8L 52.9% €-94.23  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 6bets 3W/3L 50.0% €-67.95  |  1.90-2.09 18bets 9W/9L 50.0% €+94.62  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Updated to reflect new session's verified absence feed: Victor Wembanyama now confirmed in roster-only OUT for SAS, multiple additional Hawks players (CJ McCollum, Onyeka Okongwu, Gabe Vincent) added, Trae Young flagged as Washington roster-only OUT, and Hugo Gonzalez/Sam Hauser/Payton Pritchard/Nikola Vucevic/Landry Shamet added for their respective teams per verified feed.
- [tanking_teams] Updated all standings to reflect current session data (standings show incremental changes from prior session), added play-in phase caveat referencing playoff_context no_tanking section, updated Victor Wembanyama to confirmed OUT in SAS feed, and refreshed GS Warriors confirmed losing streak to L3.

## Commit patches applied
None

## Playoff context patches applied
- [phase] Updating phase description to accurately reflect that we are now in the Play-In Tournament phase, not full playoffs yet.
- [series_context] Play-In Tournament is the current phase; populating series_context with estimated play-in participants based on current standings and explaining bracket format for Scout/Commit context.
- [elimination_flags] Populating elimination_flags with play-in specific elimination risk context based on current standings and confirmed play-in phase.
- [h2h_playoff] Updating h2h_playoff section for play-in phase with placeholder structure and important caveat that many regular season H2H records were compiled with depleted rosters due to widespread rest/injury patterns.
- [playoff_rest] Adding play-in specific rest rules as a distinct tier from full playoff rest rules, given the single-elimination format changes how rest impacts momentum and confidence.

## Intelligence gaps identified
- **No confirmed play-in matchups or game times are available in the current data feed — only estimated seedings based on standings.** — Scout cannot draft play-in picks without knowing which teams are actually playing each other and when — wrong matchup analysis would produce incorrect injury, H2H, and motivation signals. → Add a mandatory pre-draft check: Scout must confirm official play-in matchup bracket before drafting any picks. If matchups unconfirmed, 0 picks until official announcement.
- **Atlanta Hawks now have CJ McCollum, Onyeka Okongwu, and Gabe Vincent all in the verified absence feed but Trae Young's status is unconfirmed — Hawks are a likely play-in participant and their true roster strength is unclear.** — ATL at 46-36 may be seeded 5th or 6th in the East, meaning they could face a first-round opponent, or they could be the 7/8 seed depending on final standings — incorrect roster assessment would corrupt any ATL directional bet. → Require NBA official PDF verification for any ATL pick and apply confidence -10 baseline for the multiple role player absences regardless of Trae Young's status.
- **The 2.10-2.50 odds tier is 0W/3L (-€229) but there is no rule explicitly warning Scout away from this range in high-uncertainty contexts like play-in games.** — Three losses at odds 2.10-2.50 with zero wins represents a clear pattern suggesting Scout is overconfident when taking long shots — in the play-in phase where rosters are unclear, this risk amplifies. → Add a play-in specific selectivity rule: avoid odds > 2.10 unless confidence ≥ 75 AND NBA official PDF has been verified for both teams — the higher odds likely reflect genuine uncertainty that Scout's model isn't fully capturing.
- **Golden State Warriors at 37-45 with NetRtg -0.4 and L3 losing streak may mathematically qualify for the Western Conference play-in as a 9 or 10 seed, but there is no verification of their exact playoff eligibility status.** — If Warriors qualify for play-in they would be the weakest play-in participant by NetRtg, creating potential edge on their opponents — but drafting a pick on a matchup where GS eligibility is uncertain would be an error. → Verify Warriors' mathematical play-in eligibility before any GS pick at commit time; if confirmed as play-in participant treat as maximum fade candidate with opponent confidence +10.
