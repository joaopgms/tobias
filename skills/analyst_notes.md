---
date: 2026-05-13
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (38 bets)
---

## Today's Analysis — 2026-05-13

ESPN confirms OKC completed an 8-game sweep run (Round 1 + Round 2) making them the dominant WCF favourite at NetRtg +11.1 — their WCF opponent will face the same statistical wall regardless of who emerges. The DET/CLE tied 2-2 series is the session's key betting opportunity: CLE fighting back from 1-2 shows Mitchell and their core can compete despite the 4.2pt NetRtg gap, making Game 5 home court the decisive variable — verify venue from ESPN before any pick. SAS leads MIN 3-2 but MIN won Game 5 survival, which is a significant signal that elimination urgency overrides statistical disadvantage and Edwards may be active — do not back SAS at short odds in Game 6 without Edwards OUT confirmation; performance data shows ML market is -€725 overall (10W/13L, 43.5%) while SPREAD is strongly positive (14W/12L, €+274) suggesting pivot toward spread picks in remaining series.

## Performance Stats
ALL-TIME: 28W / 28L | Win rate: 50.0% | P&L: €-296.31 | Avg odds: 1.94 | Avg conf: 65.7/100
RECENT 20: 10W / 10L | 50.0% WR | P&L: €-351.01
By market:      ML 23bets 10W/13L 43.5% €-725.09  |  SPREAD 26bets 14W/12L 53.8% €+274.33  |  TOTAL 7bets 4W/3L 57.1% €+154.45
By confidence:  High 18bets 7W/11L 38.9% €-894.80  |  Medium 36bets 21W/15L 58.3% €+739.80  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 19bets 9W/10L 47.4% €-818.05  |  1.90-2.09 33bets 18W/15L 54.5% €+463.75  |  2.10-2.50 4bets 1W/3L 25.0% €+57.99



## Scout patches applied
- [franchise_player_rules] ESPN live feed confirms OKC leads 4-0 (COMPLETE sweeping WCF), DET/CLE now Tied 2-2 (Game 5/6 next), SAS leads 3-2 (Game 6 next), MIN trails 2-3 (must-win/elimination context) — all series scores updated to match verified ESPN data.

## Commit patches applied
None

## Playoff context patches applied
- [phase] ESPN live feed confirms OKC 4-0 sweep (COMPLETE), DET/CLE tied 2-2, SAS leads MIN 3-2 with Game 6 as a MIN elimination game — all phase descriptions updated to match current bracket reality.
- [series_context] ESPN live feed confirms OKC sweep complete (4-0), DET/CLE tied 2-2, SAS leads MIN 3-2 with Game 6 as MIN elimination game — series contexts updated with correct scores and appropriate elimination game rules applied.
- [elimination_flags] OKC sweep complete (Round 2 opponent eliminated), DET/CLE series now tied 2-2 (neither team facing elimination but CLE motivation context changes), MIN now trailing 2-3 and facing elimination in Game 6 — all flags updated to match verified ESPN standings.
- [playoff_rest] Series scores have advanced to Game 5-6 range — rest context updated for OKC sweep completion (extended rest entering WCF), DET/CLE tied series (Game 5 next), and MIN facing elimination in Game 6.
- [playoff_motivation] Series scores updated to reflect OKC sweep complete, DET/CLE tied 2-2 (swing game context), and MIN facing elimination in Game 6 — motivation hierarchy restructured to reflect current series states.
- [h2h_playoff] Series scores updated — DET/CLE now tied 2-2 (key series shift showing CLE resilience), SAS leads MIN 3-2 with MIN winning Game 5 (shows elimination urgency effectiveness), OKC sweep complete — all in-series signals and lessons updated to reflect current data.
- [l15_caveat] Series updated to reflect DET/CLE tied 2-2, SAS leads MIN 3-2 (MIN won Game 5 survival), OKC sweep complete (8 consecutive wins) — all NetRtg vs in-series analysis updated to reflect current Game 5-6 stage dynamics.
- [no_tanking] OKC Round 2 sweep complete adds another eliminated team, teams still active updated to reflect current bracket state with DET/CLE tied and SAS/MIN at 3-2.

## Intelligence gaps identified
- **Edwards (MIN) Round 2 active/inactive status is unknown — the verified list shows him absent from the franchise_player_rules verified feed but he was listed as roster-only OUT in Round 1** — If Edwards is active for MIN in Games 5-6, MIN's effective NetRtg rises from ~1.5-2.0 to ~3.1+, making SAS vs MIN a more competitive betting proposition and potentially creating value on MIN in the elimination game at home → Fetch NBA official injury PDF for MIN Round 2 roster before any SAS/MIN pick — flag Edwards as mandatory re-verification with binary outcome impact on MIN confidence (±15 confidence swing depending on status)
- **OKC's WCF opponent identity is unconfirmed in the current data feed — the bracket shows OKC swept their Round 2 opponent 4-0 but the opponent's identity is listed as TBD** — Without knowing the WCF opponent, Scout cannot evaluate NetRtg gaps, home court assignments, franchise player statuses, or series context for any OKC WCF pick → Fetch ESPN bracket data to confirm OKC's WCF opponent — likely LAL (who won Round 1 and is listed as entering Round 2) but must be confirmed before any WCF pick is drafted
- **ML market is deeply negative at -€725 (10W/13L, 43.5%) while SPREAD market is strongly positive at +€274 (14W/12L, 53.8%) — this systematic divergence suggests ML picks are consistently being placed at marginal or negative EV odds** — At average odds 1.94 and confidence ~65.7, many ML picks require 52%+ true probability to break even — the 43.5% win rate suggests the EV calculation is not adequately penalising ML bets at shorter odds where the confidence floor of 50 creates false positive picks → Consider raising ML confidence floor from 50 to 55 and requiring EV ≥ 0.08 for ML picks in the 1.70-1.89 odds range (which shows 9W/10L, -€818 — the worst bucket) — the spread market outperformance at 53.8% with the existing rules suggests spread confidence floors are calibrated correctly
