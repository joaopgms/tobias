---
date: 2026-04-19
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (16 bets)
---

## Today's Analysis — 2026-04-19

Major roster status shift this session: multiple franchise players previously in roster-only OUT feed (SGA, Jalen Williams, Chet Holmgren, Wembanyama, Jayson Tatum, Anthony Edwards) no longer appear in the current verified absence feed — this fundamentally changes the competitive landscape entering the play-in tournament and Scout must re-verify all of these via NBA official PDF before drafting any picks. Performance data shows a clear and actionable pattern: High confidence bets are severely underperforming (4W/7L, 36.4%, €-356 at the High tier), while Medium confidence bets are the profitable sweet spot (13W/8L, 61.9%, €+677) — this is the most important signal in the performance data and suggests the confidence calibration at the top end is too aggressive. Odds range 2.10-2.50 is 0W/3L (€-229) — this range is bleeding money and warrants serious scrutiny before any pick in that range is drafted.

## Performance Stats
ALL-TIME: 17W / 17L | Win rate: 50.0% | P&L: €+179.33 | Avg odds: 1.96 | Avg conf: 65.6/100
RECENT 20: 11W / 9L | 55.0% WR | P&L: €+678.26
By market:      ML 15bets 7W/8L 46.7% €-275.39  |  SPREAD 16bets 9W/7L 56.2% €+477.99  |  TOTAL 3bets 1W/2L 33.3% €-23.27
By confidence:  High 11bets 4W/7L 36.4% €-356.08  |  Medium 21bets 13W/8L 61.9% €+676.72  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 9bets 5W/4L 55.6% €-86.43  |  1.90-2.09 22bets 12W/10L 54.5% €+495.07  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Updated verified franchise player statuses: multiple previously OUT players (Wembanyama, Tatum, SGA, Jalen Williams, Chet Holmgren, Anthony Edwards) no longer appear in current verified absence feed — their status must be treated as changed and re-verified, not assumed OUT.
- [tanking_teams] Season is in play-in/playoff phase — tanking logic must be suppressed for all remaining motivated teams and the section clarified to reflect the active bracket.

## Commit patches applied
None

## Playoff context patches applied
- [series_context] Updated to reflect current session verified absence feed changes — multiple previously OUT franchise players no longer confirmed absent, requiring re-verification flags, and Denver hot streak updated with current W12/L10 data.
- [elimination_flags] Updated elimination flags to reflect current session status and clarify the GSW motivation paradox (motivated but statistically weak), with updated roster uncertainty context.
- [h2h_playoff] Updated to reflect current session's roster status changes — previously assumed absences during regular season H2H may no longer apply, requiring fresh H2H evaluation once matchups are confirmed.
- [playoff_rest] Updated rest context to reflect current session date and clarify that previous widespread absence flags may have cleared, changing rest-based edge calculations.

## Intelligence gaps identified
- **High confidence tier (70-84) is producing catastrophic results: 4W/7L, 36.4%, €-356 — worse than speculative picks on a per-bet basis** — This is the single largest P&L drag in the system. If the confidence calibration at the 70-84 tier is systematically over-confident, every 'High' pick is destroying value. The pattern suggests scouts are reaching for High confidence on marginal edges. → Raise the High confidence floor threshold for drafting from 70 to 73, or add a secondary validation gate for High-tier picks requiring NetRtg gap ≥ 5 AND clean injury feed (nba_official) — this would filter the marginal High-tier picks that are losing. Confidence in this patch: 0.68 — just below the 0.70 threshold (11 bets is a moderate but not fully conclusive sample at this tier).
- **Odds range 2.10-2.50 is 0W/3L (100% loss rate, €-229) — no wins at all in this range across the full dataset** — This range produces systematically negative outcomes — possibly because odds above 2.10 indicate the market has already priced in significant uncertainty that the agents are not adequately discounting. Three losses at this range with no wins is a clear pattern. → Lower the ML odds ceiling target from 2.50 to 2.10, or require EV ≥ 0.12 (doubled floor) for any pick with odds ≥ 2.10 to compensate for the elevated uncertainty. Confidence in this patch: 0.68 — just below 0.70 threshold (only 3 bets in this range is a thin sample).
- **ML market is 7W/8L (46.7%, €-275) while Spread is 9W/7L (56.2%, €+478) — agents may be defaulting to ML when spread offers the better edge** — Spread bets are clearly the most profitable market type. If scouts are selecting ML over spread on the same game due to lower confidence requirements, they are leaving value on the table and taking on worse-EV bets. → The selectivity section already instructs spread-first evaluation — verify via scout_report logs whether agents are actually evaluating spreads first or defaulting to ML. If they are defaulting to ML, consider adding a mandatory spread-evaluation gate: 'If a game meets ML criteria AND NetRtg gap ≥ 4, the spread MUST be evaluated before drafting ML.' No patch needed yet — this is a process audit gap.
- **Multiple play-in teams' regular season H2H records are unpopulated — play-in matchups not yet officially announced** — Without confirmed matchups, Scout cannot apply H2H confidence adjustments (+8) that could be decisive in close single-elimination games where every edge matters. → Infrastructure/data pipeline fix needed — requires official NBA play-in matchup announcement. Once announced, Analyst should immediately populate h2h_playoff section with verified H2H records for each confirmed matchup. No rule patch available until data exists.
