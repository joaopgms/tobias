---
date: 2026-04-07
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (3 bets)
---

## Today's Analysis — 2026-04-07

Two major franchise player additions this session: Anthony Edwards (MIN) and Jalen Williams (OKC) are both OUT [roster-only], materially changing the outlook for those teams — Minnesota is now a confirmed fade candidate on a 3-game losing streak with both stars absent, while OKC's dominant NetRtg +11.6 must be re-contextualised without their franchise SG. Performance data continues to show SPREAD bets as the weakest market (3W/5L, -€319) and HIGH confidence picks underperforming (2W/5L, 28.6% WR), suggesting the system is over-confident on spread selections and should prioritise ML edges in the 1.70-1.89 range where the only profitable odds band sits (60% WR, +€115). The late-season motivational picture is clarifying: OKC/Spurs/Pistons are rest-risk teams, play-in bubble teams like Charlotte and Portland have positive motivation, and Washington/GS/Toronto/Miami are all fade candidates on form and roster depletion.

## Performance Stats
ALL-TIME: 8W / 13L | Win rate: 38.1% | P&L: €-560.24 | Avg odds: 1.99 | Avg conf: 65.6/100
RECENT 20: 8W / 12L | 40.0% WR | P&L: €-460.24
By market:      ML 11bets 5W/6L 45.5% €-56.91  |  SPREAD 8bets 3W/5L 37.5% €-319.06  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 7bets 2W/5L 28.6% €-190.54  |  Medium 12bets 6W/6L 50.0% €-228.39  |  Speculative 2bets 0W/2L 0.0% €-141.31
By odds range:  1.70-1.89 5bets 3W/2L 60.0% €+115.05  |  1.90-2.09 13bets 5W/8L 38.5% €-445.98  |  2.10-2.50 3bets 0W/3L 0.0% €-229.31



## Scout patches applied
- [franchise_player_rules] Verified feed adds Jalen Williams (OKC) and Anthony Edwards (MIN) as OUT [roster-only] this session, and removes Jarrett Allen, Evan Mobley, Zeke Nnaji, and Sam Merrill who are no longer in the verified list — all entries must reflect only current verified data.
- [tanking_teams] Standings updated with current data; Anthony Edwards (MIN) and Jalen Williams (OKC) added as verified OUT [roster-only]; Allen/Mobley/Nnaji removed from CLE/DEN as not in current verified feed; streak/record figures corrected throughout.

## Commit patches applied
None

## Intelligence gaps identified
- **HIGH confidence picks are the worst-performing tier (2W/5L, 28.6% WR, -€190) — suggesting the system is systematically over-confident when assigning confidence 70-84.** — The current confidence_staking section treats High confidence (70-84) as a reliable tier deserving 20-25% stake, but historical data shows it performs worse than Medium confidence (50% WR); tightening EV requirements at high confidence would reduce exposure on these miscalibrated picks. → Consider raising EV floor for High-confidence picks to ≥ 0.08 (vs 0.05 standard) to require stronger market edge before committing larger stakes — but need 20+ settled bets in this tier before patching confidence_staking per rules.
- **SPREAD market is severely underperforming (3W/5L, 37.5% WR, -€319) but no spread-specific EV floor exists separate from ML.** — Spreads require line precision that ML does not — a shared EV floor of 0.05 may be insufficient to filter marginal spread edges, particularly when injury feed coverage is partial; a higher EV floor for spreads (e.g. 0.08) would have reduced losing exposure. → Raise spread-specific EV floor to ≥ 0.08 in market_rules — this requires confidence ≥ 0.7 with 8 bets settled in the market; currently at borderline confidence given small sample.
- **TOTALS market shows 0W/2L (100% loss rate, -€184) but sample is too small to determine if this is signal or variance.** — Both totals losses occurred — if both relied on pace signals or pace was unavailable, existing data_quality_rules may already address this; but if they were non-pace-dependent, a higher confidence floor may be warranted. → Track the specific thesis of each settled totals bet to determine if Pace unavailability or OffRtg/DefRtg misreads caused losses — until then, the existing confidence floor of 65 (70 when Pace absent) should remain.
- **Anthony Edwards (MIN) absence is a fresh roster-only flag without confirmation via NBA official PDF — books may not have fully priced this into the line for tonight's games.** — A franchise player absence that books haven't priced creates a potential late-commit edge opportunity on Minnesota opponents if MIN is priced assuming Edwards plays; this is exactly the late_scout_triggers scenario. → Commit agent should specifically check MIN lines at commit time against current markets — if MIN is priced as though Edwards is playing and roster-only absence is confirmed, opponent ML may offer +EV; re-verify via NBA official PDF first.
- **The 1.90-2.09 odds range is the system's highest-volume band (13 bets) but worst-performing (38.5% WR, -€446), while 1.70-1.89 is the only profitable range (60% WR, +€115).** — This suggests the system is finding better calibrated edges at shorter odds (stronger favourites) but is over-drafting in the 1.90-2.09 band where implied probability vs actual edge is miscalibrated; tightening selectivity or EV requirements in this odds range would improve P&L. → Add an odds-band note to selectivity: picks in the 1.90-2.09 range require EV ≥ 0.08 (vs standard 0.05) given historical underperformance — this is a targeted band-specific tightening.
