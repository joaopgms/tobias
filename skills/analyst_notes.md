---
date: 2026-04-10
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (7 bets)
---

## Today's Analysis — 2026-04-10

This session reveals an extraordinary end-of-season rest cascade: OKC has flagged 10 players OUT [roster-only] including SGA, Jalen Williams, and Chet Holmgren — effectively the entire rotation — which is almost certainly deliberate load management with the #1 seed locked at 64-16. Similarly, Cleveland has Donovan Mitchell AND Jarrett Allen both flagged OUT while on a W4 streak, and Minnesota has Edwards AND Gobert out simultaneously. Scout must treat all three teams as severely depleted and refuse to draft picks without mandatory NBA official PDF re-verification. Denver's W10 streak at +4.9 NetRtg is the most compelling active trend — they remain bet-eligible but the hot streak regression rule should be applied contextually given their elite record. The 2.10+ odds range is 0W/3L (€-229.31) representing a significant loss concentration — Scout should apply additional scrutiny before drafting any pick at odds above 2.10.

## Performance Stats
ALL-TIME: 11W / 14L | Win rate: 44.0% | P&L: €-211.64 | Avg odds: 1.99 | Avg conf: 65.7/100
RECENT 20: 10W / 10L | 50.0% WR | P&L: €+249.25
By market:      ML 12bets 5W/7L 41.7% €-256.91  |  SPREAD 10bets 5W/5L 50.0% €+68.54  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 8bets 3W/5L 37.5% €+32.90  |  Medium 15bets 8W/7L 53.3% €-103.23  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 5bets 3W/2L 60.0% €+115.05  |  1.90-2.09 17bets 8W/9L 47.1% €-97.38  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Verified absence feed now shows major new absences vs last session: SGA, Jalen Williams, Chet Holmgren, Isaiah Hartenstein, Cason Wallace, Isaiah Joe, Alex Caruso, Jaylin Williams (OKC); Donovan Mitchell, Jarrett Allen, Thomas Bryant, Sam Merrill (CLE); Rudy Gobert, Joe Ingles (MIN); Tre Johnson (WAS confirmed via injury landscape) — all must be reflected accurately with appropriate franchise player alerts.
- [tanking_teams] Standings updated per current data; major new absences across OKC (full roster rest), CLE (Mitchell + Allen), MIN (Edwards + Gobert) require full tanking_teams refresh with appropriate alerts and re-verification flags.

## Commit patches applied
None

## Intelligence gaps identified
- **Odds range 2.10–2.50 is 0W/3L (€-229.31) — a clear performance cliff above 2.10 that current rules do not address.** — Three consecutive losses at 2.10+ odds have cost €229.31; the current odds_targets ceiling of 2.50 and no differentiated rules above 2.10 means Scout continues drafting into a demonstrated loss zone without additional scrutiny. → Add a soft ceiling rule in odds_targets or market_rules: picks at odds 2.10–2.50 require confidence ≥ 70 AND NetRtg gap ≥ 5.0 AND no franchise player uncertainty — raising the bar before Scout can draft in this range.
- **ML market is 5W/7L (€-256.91) while Spread is 5W/5L (€+68.54) — Scout is drafting too many ML bets relative to spreads despite spread outperforming.** — The gap in profitability between ML (-€256.91) and Spread (+€68.54) over the same recent period suggests Scout is not fully applying the 'evaluate spread first when NetRtg gap > 6pts' rule from selectivity, defaulting to ML when a spread edge may be stronger. → Reinforce in selectivity that spread evaluation is MANDATORY (not optional) when NetRtg gap > 5.0 or a B2B situation exists; ML should only be chosen over spread when odds_targets or confidence floor for spread is not met.
- **Speculative tier (confidence 50-54) is 0W/2L (€-141.31) — a 0% win rate tier that is consuming disproportionate capital.** — Two speculative bets have produced zero wins and €141.31 in losses; the current staking rule allows 10% bankroll at speculative tier but the evidence suggests speculative picks are strongly negative-EV in practice. → Once 5+ speculative bets are settled, evaluate raising the speculative minimum confidence from 50 to 55, effectively eliminating the speculative tier and requiring all picks to meet the medium confidence floor.
- **OKC's mass absence situation (10 players flagged OUT including SGA and Jalen Williams) may produce line anomalies where OKC is still priced as a heavy favourite based on season record rather than actual available roster.** — A team missing its top-2 stars and 8 other players could be mispriced as -1.35 or shorter due to market anchoring to 64-16 record; this would trigger Scout's line anomaly rule but Scout needs explicit guidance that record-based pricing without roster-adjustment is an anomaly signal. → Add to priority_stats or line anomaly check: 'If a team with 4+ verified absences including franchise players is priced at ≤ 1.50 favourite, flag as potential stale-line anomaly and require Commit-time verification before confirming.'
