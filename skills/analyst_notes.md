---
date: 2026-05-01
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (34 bets)
---

## Today's Analysis — 2026-05-01

Major bracket movement: Minnesota eliminated Denver 4-2 (Jokic neutralised by MIN scheme despite DEN's superior NetRtg — strongest confirmation this round that in-series execution overrides seasonal stats) and New York eliminated Atlanta 4-2 (Trae Young data conflict was never resolved, validating the high-risk flag). Four Game 7s are now set — BOS/PHI, ORL/DET, CLE/TOR, LAL/HOU — creating a high-value slate where home court (~60-65% G7 win rate) and Durant's confirmed status for HOU are the two most actionable unknowns. Performance data shows ML bets are deeply underwater (9W/13L, -€930) while spreads are profitable (13W/12L, +€103) and high-confidence bets are the worst-performing tier (6W/11L, -€1099) — in Game 7 ML-only environments this is a critical tension to monitor, as the rules already mandate ML-only in G7s but the ML market is our weakest historically.

## Performance Stats
ALL-TIME: 25W / 27L | Win rate: 48.1% | P&L: €-615.71 | Avg odds: 1.94 | Avg conf: 65.8/100
RECENT 20: 10W / 10L | 50.0% WR | P&L: €-303.54
By market:      ML 22bets 9W/13L 40.9% €-930.10  |  SPREAD 25bets 13W/12L 52.0% €+102.94  |  TOTAL 5bets 3W/2L 60.0% €+211.45
By confidence:  High 17bets 6W/11L 35.3% €-1099.81  |  Medium 33bets 19W/14L 57.6% €+625.41  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 17bets 7W/10L 41.2% €-1194.45  |  1.90-2.09 31bets 17W/14L 54.8% €+520.75  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] ESPN scoreboard shows series updates requiring franchise_player_rules to reflect: NYK leads 4-2 (series complete per data), MIN leads 4-2 (series complete per data), LAL leads 3-2 (Game 7 next per ESPN), ORL leads 3-2 now a Game 7, CLE leads 3-2 now a Game 7, and PHI/BOS tied 3-3 Game 7 — all franchise player notes must align with current series state.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] ESPN scoreboard confirms critical series changes: NYK leads 4-2 (ATL eliminated), MIN leads 4-2 (DEN eliminated), LAL leads 3-2 (Game 7 next — HOU survived), BOS/PHI tied 3-3 (PHI won Game 6 — Game 7 set), ORL/DET updated to Game 7 next, CLE/TOR updated to Game 7 next.
- [elimination_flags] ESPN scoreboard confirms NYK (4-2), MIN (4-2) series complete and DEN/ATL eliminated; LAL now leads 3-2 creating a Game 7 vs HOU; PHI/BOS tied 3-3 for Game 7; ORL/DET and CLE/TOR also advance to Game 7 — all flags must reflect current bracket state.
- [h2h_playoff] Series completions (NYK 4-2, MIN 4-2) require those series cleared; LAL now leads 3-2 (HOU survived — Game 7 set); PHI/BOS tied 3-3 with PHI winning two consecutive elimination games changes the in-series momentum signal significantly; all Game 7 series must be flagged as such.
- [playoff_motivation] ESPN confirms four active Game 7s (BOS/PHI, ORL/DET, CLE/TOR, LAL/HOU after HOU survived), two series complete (NYK 4-2, MIN 4-2), requiring motivation hierarchy to reflect pure Game 7 context and removal of series-closer motivation for NYK and MIN.
- [l15_caveat] Series state changed materially — MIN won 4-2 (DEN eliminated), NYK won 4-2 (ATL eliminated), LAL leads 3-2 (Game 7 next), BOS/PHI tied 3-3 (PHI won consecutive elimination games) — all L15 caveat divergence analysis must reflect current series outcomes.
- [phase] ESPN scoreboard confirms four active Game 7 situations and two series completions, requiring phase section to accurately reflect the Game 7 stage of Round 1.

## Intelligence gaps identified
- **High-confidence bets (conf 70-84+) are producing the worst outcomes (6W/11L at -€1099) while medium confidence (55-69) is profitable (19W/14L at +€625)** — This directly contradicts the confidence-staking model — higher confidence bets should produce better outcomes, not worse; if this pattern holds, the staking tiers are misaligned with actual edge identification quality → After 5 more settled bets at high confidence tier, audit what signals are driving high-confidence picks — if ML at short odds (1.70-1.89) is the primary culprit (17 bets, 7W/10L at -€1194), consider adding a selectivity rule that caps high-confidence designation when odds are in the 1.70-1.89 range unless EV ≥ 0.12
- **Game 7 ML-only rule exists but no explicit confidence adjustment for the home team in Game 7 is built into market_rules — it only lives in playoff_motivation** — Scout reads priority_stats and market_rules before playoff_motivation context; if the Game 7 home court +8 confidence boost isn't in market_rules, Scout may under-weight it when calculating EV and confidence floors for ML picks tonight → Add a Game 7 section to market_rules explicitly stating: in confirmed Game 7 games, apply home team confidence +8 and road team confidence +5 before EV calculation; do not bet spreads; verify home court from ESPN before drafting
- **Durant's status for HOU in Game 7 vs LAL is the single most valuable piece of information for tonight's slate but the data pipeline shows him as not-in-verified-feed — no mechanism exists to auto-escalate when a franchise player status is both unresolved AND game-decisive** — HOU vs LAL Game 7 is a legitimate potential pick (HOU home + Durant active would make it a credible underdog bet at ≥ 2.00) but we cannot draft it without Durant's confirmation — the current rules require re-verification but don't escalate urgency for game-deciding unknowns → Infrastructure fix needed: add an escalation flag in franchise_player_rules for 'GAME 7 FRANCHISE PLAYER UNRESOLVED' that triggers a mandatory Commit-phase verification halt on that pick until confirmed — currently only Scout gets the re-verify note but Commit should also hard-block on unresolved G7 franchise players
