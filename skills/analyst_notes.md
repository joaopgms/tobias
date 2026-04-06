---
date: 2026-04-06
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (0 bets)
---

## Today's Analysis — 2026-04-06

Performance data shows a clear and severe pattern: High-confidence picks (5 bets, 0W/5L, €-518) are catastrophically underperforming versus Medium picks (11 bets, 6W/5L, 54.5% WR) — the system is paradoxically most accurate at medium confidence and worst at high confidence, suggesting calibration issues at the top tier. Odds range 2.10–2.50 is 0W/3L (€-229) flagging that longer shots are not delivering value, while 1.90–2.09 range (36.4% WR) is also underwater, with only 1.70–1.89 showing positive cover rate; Scout should bias toward the 1.70–1.89 range until higher-odds performance improves. Macro NBA context: late-season star resting is accelerating (OKC clinch near, CLE dual-big absence, LAL dual-star absence) — franchise player verification before every pick is more critical than any previous session this season.

## Performance Stats
ALL-TIME: 6W / 12L | Win rate: 33.3% | P&L: €-738.24 | Avg odds: 2.0 | Avg conf: 64.9/100
RECENT 18: 6W / 12L | 33.3% WR | P&L: €-738.24
By market:      ML 10bets 4W/6L 40.0% €-206.91  |  SPREAD 6bets 2W/4L 33.3% €-347.06  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 5bets 0W/5L 0.0% €-518.54  |  Medium 11bets 6W/5L 54.5% €-78.39  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 4bets 2W/2L 50.0% €-62.95  |  1.90-2.09 11bets 4W/7L 36.4% €-445.98  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Verified feed this session does not include Tristan Vukcevic or Nikola Vucevic — removing per MANDATORY rule to only list verified names; all other absences updated to match current ESPN+injury feed cross-reference.
- [tanking_teams] Standings updated to match current feed (OKC 62-16, CLE 49-29, HOU 49-29, CHA 43-36, TOR 43-35, etc.) and Tristan Vukcevic removed from Washington confirmed list per verified-names-only rule.

## Commit patches applied
None

## Intelligence gaps identified
- **High-confidence picks (conf 70–100) are 0W/5L while medium-confidence picks (conf 55–69) are 6W/5L — a complete inversion of expected performance suggesting the confidence calibration is structurally wrong at the top tier.** — If high-confidence picks fail at 0% and medium succeeds at 54.5%, the system is systematically overconfident — picks reaching 70+ confidence are likely being pushed there by compounding signals that don't actually compound win probability. → After reaching 10 more high-confidence settled bets, consider capping the confidence boost from stacking signals (e.g. NetRtg + streak + B2B) at +15 total rather than additive unbounded stacking; flag for milestone review at 25 total bets.
- **Odds range 2.10–2.50 is 0W/3L (€-229) and 1.90–2.09 is 4W/7L (36.4%) — both above-average odds tiers are underwater, suggesting the system is finding false edges in longer prices.** — The only profitable odds range is 1.70–1.89 (50% WR) — Scout may be chasing EV at longer prices where the probability estimate is structurally too optimistic. → Consider tightening the ML ceiling from 2.50 to 2.30 for picks with confidence below 70, restricting longer-odds picks to Elite-tier confidence only; review at 25 total bets for milestone patch.
- **Spread market is 2W/4L (33.3%, €-347) and Total market is 0W/2L (0%, €-184) — both non-ML markets are producing most of the losses despite having higher confidence floors.** — If spreads require confidence 60+ but are losing at 33.3%, either the confidence floor is too low or the spread signal sources (NetRtg gap, B2B) are not translating to cover-rate accuracy as expected. → Raise spread confidence floor from 60 to 65 and total confidence floor from 65 to 70 on a trial basis; revisit after 5 more spread bets settle.
- **Toronto Raptors standings show L10: 4-6 and streak: L1 in the current feed, but the previous tanking_teams entry reflected a more neutral status — the team's cold slide with Quickley and Hepburn both out has not been flagged as a fade candidate until now.** — A team with two key guards out, L10 4-6, and a losing streak should be treated as a fade candidate, not neutral — Scout may have missed value backing opponents against Toronto. → Added Toronto to HOT STREAK FADE CANDIDATES section in this session's tanking_teams patch; no additional infrastructure change needed.
- **Charlotte Hornets (43-36, L10: 8-2, NetRtg +5.3) show a strong hot streak but their season record (.544 W%) implies ~.500 true talent — this mirrors the Atlanta fade pattern but Charlotte is not currently flagged as a fade candidate.** — If Atlanta at .577 W% triggers the hot-streak-fade rule, Charlotte at .544 W% with an even hotter L10 should also qualify — opponents may offer value at ≥ 1.80 against Charlotte. → Add Charlotte Hornets to HOT STREAK FADE CANDIDATES in next session if L10 form persists — confidence currently 0.68, just below the 0.70 threshold for patching selectivity rule.
