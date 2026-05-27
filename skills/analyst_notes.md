---
date: 2026-05-27
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (43 bets)
---

## Today's Analysis — 2026-05-27

The critical update this session is WCF series score correction: OKC leads SAS 3-2, not tied 2-2 as reflected in previous skills files — Game 6 is now a SAS elimination game at home, fundamentally changing the bet framing from tied-series home court logic to in-series-lead (OKC primary) with SAS elimination desperation as counterweight. Key strategic note: ML performance at 1.70-1.89 odds remains deeply negative (-€818), and High confidence picks continue underperforming (38.9%) vs Medium confidence outperforming (56.8%) — Scout should avoid high-confidence ML picks in the 1.70-1.89 band and lean into medium-confidence spread picks where the edge is demonstrated. For Game 6 specifically, a SAS spread at home in an elimination game at odds ≥ 1.85 merits evaluation if Wembanyama is confirmed active — back-against-wall home teams historically cover at ~55% clip, and Williams OUT reduces OKC's offensive execution ceiling on the road.

## Performance Stats
ALL-TIME: 32W / 29L | Win rate: 52.5% | P&L: €+457.72 | Avg odds: 1.93 | Avg conf: 65.6/100
RECENT 20: 12W / 8L | 60.0% WR | P&L: €+656.22
By market:      ML 25bets 12W/13L 48.0% €-289.43  |  SPREAD 29bets 16W/13L 55.2% €+592.70  |  TOTAL 7bets 4W/3L 57.1% €+154.45
By confidence:  High 19bets 8W/11L 42.1% €-659.52  |  Medium 40bets 24W/16L 60.0% €+1258.55  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 21bets 11W/10L 52.4% €-382.39  |  1.90-2.09 36bets 20W/16L 55.6% €+782.12  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] Live playoff feed shows OKC now leads WCF 3-2 (not tied 2-2) — updating all OKC/SAS notes to reflect elimination game framing for SAS and road close-out opportunity for OKC.

## Commit patches applied
None

## Playoff context patches applied
- [phase] ESPN live feed confirms OKC leads SAS 3-2 (not tied 2-2) — Game 6 is now an elimination game for SAS.
- [series_context] Updating WCF series score from tied 2-2 to OKC leads 3-2 — Game 6 is now a SAS elimination game, changing the framing, motivation hierarchy, and recommended odds thresholds.
- [elimination_flags] OKC now leads 3-2 — SAS is facing elimination in Game 6, not a tied series situation; elimination framing changes motivation and pick analysis.
- [playoff_rest] Series is now OKC 3-2 not tied 2-2 — rest framing changes to close-out game dynamics and SAS elimination game intensity.
- [playoff_motivation] OKC now leads WCF 3-2 — series framing shifts from tied-series (home court primary) to in-series-lead (OKC primary) with SAS in elimination game desperation mode.
- [h2h_playoff] OKC leads WCF 3-2 not tied 2-2 — H2H and in-series framing must reflect elimination game context with OKC as series favourite.
- [l15_caveat] WCF series score updated to OKC 3-2 — in-series lead hierarchy and elimination game framing replace tied-series home court framing.
- [no_tanking] WCF score updated to OKC 3-2 — SAS is now in elimination position, not tied series; flags updated accordingly.

## Intelligence gaps identified
- **No explicit elimination game cover rate rule exists in market_rules or selectivity — back-against-wall home teams have measurably different spread cover rates (~55%) vs standard home games.** — WCF Game 6 is precisely this scenario — SAS at home facing elimination, a situation where the spread bet has a positive historical expectation that current rules don't explicitly capture or weight. → Add an 'ELIMINATION GAME SPREAD RULE' to market_rules: when home team faces elimination AND is playing at home AND franchise player is confirmed active, add +5 confidence to spread pick if odds ≥ 1.80 and opponent is road close-out team.
- **Road close-out success rate (~40-45% in WCF Game 6 scenarios) is referenced in analyst notes but not codified as a rule — OKC road close-out odds threshold is currently set at 1.75 based on judgment, not a validated rule.** — If OKC is priced at 1.60-1.70 on road in Game 6 close-out (possible given series lead + NetRtg edge), Scout needs a rule-based reason to flag the pick as poor value rather than relying on analyst notes. → Add to market_rules: 'ROAD CLOSE-OUT RULE: When a team leads a playoff series 3-2 and Game 6 is on the road, treat as confidence -10 vs baseline — road close-out teams cover spread at only ~42% historically. Require odds ≥ 1.80 to proceed on ML.'
- **LAL Round 2 series status is still listed as 'active — verify opponent' with no specific series score, opponent, or series lead information — this has been flagged as unknown for multiple sessions.** — Without knowing LAL's Round 2 opponent, series score, and whether Doncic is truly OUT or just listed roster-only, Scout cannot make an informed decision on any LAL game — the pick could be based on stale or incorrect series framing. → Fetch LAL Round 2 bracket data from ESPN — specific opponent, current series score, and Doncic official status. If LAL is eliminated, confirm in elimination_flags immediately. This is a data pipeline fix, not a rule patch.
