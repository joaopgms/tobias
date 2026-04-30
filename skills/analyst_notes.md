---
date: 2026-04-30
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (33 bets)
---

## Today's Analysis — 2026-04-30

Multiple series have reached Game 7 simultaneously (BOS/PHI, NYK/ATL, MIN/DEN), creating a rare high-volatility slate where home court advantage (~60-65% G7 win rate) becomes the dominant factor — verify exact home courts from ESPN before any pick. The ORL vs DET series (ORL leads 3-2 despite DET's +8.2 NetRtg) and MIN vs DEN (MIN leads 3-2 despite DEN's superior NetRtg) continue to validate the core playoff lesson that in-series tactical execution overrides season metrics at this stage. Performance data shows ML bets are significantly underwater (-€930 on 22 bets, 40.9% WR) while spreads are profitable (+€102.94, 52%), strongly suggesting Game 7 picks should prioritise spread evaluation where genuine edges exist — though closing-looseness risk in elimination games warrants ML-only in close-out scenarios.

## Performance Stats
ALL-TIME: 24W / 27L | Win rate: 47.1% | P&L: €-754.43 | Avg odds: 1.94 | Avg conf: 65.8/100
RECENT 20: 9W / 11L | 45.0% WR | P&L: €-713.89
By market:      ML 22bets 9W/13L 40.9% €-930.10  |  SPREAD 25bets 13W/12L 52.0% €+102.94  |  TOTAL 4bets 2W/2L 50.0% €+72.73
By confidence:  High 17bets 6W/11L 35.3% €-1099.81  |  Medium 32bets 18W/14L 56.2% €+486.69  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 17bets 7W/10L 41.2% €-1194.45  |  1.90-2.09 30bets 16W/14L 53.3% €+382.03  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] ESPN live series data shows Game 7s for BOS/PHI, NYK/ATL, MIN/DEN; Game 6s for CLE/TOR, LAL/HOU, ORL/DET, SAS/POR — all series contexts require updating to reflect current state.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] ESPN live series data shows all series have advanced: BOS/PHI to G7, NYK/ATL to G7, MIN/DEN to G7 (DEN survived), CLE/TOR to G6, LAL/HOU to G6, ORL/DET to G6, SAS/POR to G6, OKC complete at 4-0.
- [elimination_flags] ESPN series data updated — series no longer at G5/G6 as previously flagged; multiple Game 7s confirmed (BOS/PHI, NYK/ATL, MIN/DEN) and OKC complete.
- [playoff_motivation] Multiple series have advanced to Game 7 (BOS/PHI, NYK/ATL, MIN/DEN), requiring updated motivation hierarchy with Game 7 specific rules; PHI survival momentum is now a confirmed pattern (two consecutive elimination game wins).
- [h2h_playoff] Series have advanced with BOS/PHI, NYK/ATL, MIN/DEN all at Game 7; PHI has demonstrated consecutive survival game wins which creates meaningful pattern; OKC series complete.
- [l15_caveat] PHI won consecutive elimination games (G5 and G6), establishing a survival momentum pattern worth codifying; DEN survived G6 to reach G7; series data fully updated to current state.

## Intelligence gaps identified
- **Trae Young team affiliation remains unresolved — appears in both WAS and ATL verified absence feeds, making all ATL Game 7 picks untradeable** — NYK vs ATL Game 7 is one of tonight's highest-profile games; without knowing if ATL has Trae Young (franchise player), the entire pick thesis is undefined — ATL with Young is completely different from ATL without Young → Fetch NBA official PDF for ATL roster and verify Young's team affiliation before Scout runs; if confirmed ATL-OUT, ATL confidence should be capped at high-risk tier; if confirmed playing, standard franchise_player_rules apply
- **Anthony Edwards status for MIN remains unresolved (roster-only OUT vs apparent active in-series activity) with Game 7 vs DEN as next game** — Edwards is MIN's primary offensive and defensive anchor — his presence/absence completely changes MIN's Game 7 ceiling and the DEN spread/ML pricing; current odds may be mispriced relative to his true status → Mandatory NBA official PDF verification of Edwards status before any MIN pick; if confirmed OUT, DEN ML at ≥ 2.00 becomes significantly more attractive and DEN confidence should be boosted further beyond current +15 framework
- **Kevin Durant HOU status remains ambiguous — was roster-only OUT but NOT in current verified absence feed, creating genuine uncertainty for LAL Game 6 pick valuation** — HOU ML pricing in Game 6 should be very different if Durant is active (competitive elimination game) vs absent (near-hopeless road elimination); current pricing likely already reflects this but Durant activation would shift the bet thesis → Fetch NBA official injury report before Scout runs; if Durant confirmed active, evaluate HOU ML at ≥ 2.20 as genuine Game 6 elimination play; if confirmed OUT, fade HOU entirely and LAL ML only if value exists
- **High-confidence bets are significantly underperforming vs medium-confidence bets (High: 35.3% WR, -€1099; Medium: 56.2% WR, +€487) suggesting confidence calibration may be systematically overconfident** — High-confidence picks (70-84 range) are generating losses while medium-confidence picks (55-69) are profitable — this is a classic overconfidence pattern where signal strength is being overstated in the 70-84 range → After 10 more settled high-confidence bets, consider raising the High confidence threshold to require EV ≥ 0.10 (instead of 0.05) — the current EV floor is too loose for the confidence tier; alternatively consider re-labelling borderline 70-74 picks as medium-confidence
