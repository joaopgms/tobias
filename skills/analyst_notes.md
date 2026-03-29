---
date: 2026-03-29
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (8 bets)
---

## Today's Analysis — 2026-03-29

Overall record stands at 2W/6L (25% WR, €-564.69 P&L) with totals going 0-2 and high-confidence bets going 0-1 — the most urgent signal is that Totals bets are a losing market for this system (0W/2L, €-184.27) and should be treated with maximum skepticism until the sample improves. The Philadelphia 76ers present the most extreme NetRtg-vs-record divergence in the league (NetRtg -0.2, record 41-33), making them a priority fade candidate regardless of their L10 7-3 streak or play-in motivation narrative. Late-season rest risk is now material for OKC, Spurs, and Pistons (top-3 seeds locked), while play-in teams Charlotte, Portland, Clippers, and GSW have strong motivation upside worth tracking against lower-ceiling opponents.

## Performance Stats
ALL-TIME: 2W / 6L | Win rate: 25.0% | P&L: €-564.69 | Avg odds: 1.99 | Avg conf: 65.8/100
RECENT 8: 2W / 6L | 25.0% WR | P&L: €-564.69
By market:      ML 3bets 1W/2L 33.3% €-135.06  |  SPREAD 3bets 1W/2L 33.3% €-245.36  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 1bets 0W/1L 0.0% €-225.00  |  Medium 6bets 2W/4L 33.3% €-239.69  |  Speculative 1bets 0W/1L 0.0% €-100.00
By odds range:  1.70-1.89 1bets 0W/1L 0.0% €-115.53  |  1.90-2.09 6bets 2W/4L 33.3% €-349.16  |  2.10-2.50 1bets 0W/1L 0.0% €-100.00



## Scout patches applied
- [franchise_player_rules] Verified franchise player statuses are identical to prior session — no additions or removals detected; content preserved with no changes to names.
- [tanking_teams] Philadelphia 76ers added explicitly to HOT STREAK FADE CANDIDATES given NetRtg -0.2 combined with 41-33 record and L10 7-3 hot streak represents an extreme NetRtg-record divergence warranting a dedicated fade flag.

## Commit patches applied
None

## Intelligence gaps identified
- **Totals market has gone 0W/2L (€-184.27) but there is no explicit Totals ban or raised threshold beyond the existing confidence floor of 65 (70 when pace unavailable).** — With only 2 settled Totals bets, the sample is too small to definitively tighten the rule, but the 0% win rate warrants explicit tracking — one more loss would cross the 3-loss threshold for a targeted tightening patch. → Flag Totals as a 'loss-watch' market internally; if one more Totals loss settles, raise confidence floor to 70 universally (not just when pace is unavailable) and require TWO independent signals (pace + OffRtg + DefRtg all aligned) before drafting any Total.
- **High-confidence tier (85-100) has gone 0W/1L but the single bet is insufficient to evaluate the tier's reliability.** — A 0% win rate at the highest stake tier is the highest-risk pattern — one more loss would represent a structural problem with how elite-confidence picks are being selected. → Monitor closely; if high-confidence tier reaches 0W/2L, audit which section produced the overconfident signal and add an explicit 'elite confidence requires NetRtg gap ≥ 8 AND franchise player status confirmed via NBA official PDF' gate.
- **NetRtg L15 is referenced as the primary signal but there is no fallback rule for when L15 data is absent — the current rule only applies a -5 confidence penalty, which may be insufficient.** — Without L15 data, Scout is forced to rely on season NetRtg which is less predictive for hot/cold streaks — several of our losses may have benefited from stronger L15 unavailability gates. → Add a rule: if NetRtg L15 is unavailable AND season NetRtg gap between teams is < 5 points, do NOT draft spread or totals — ML only with confidence capped at 55.
- **The standings data shows San Antonio Spurs at 56-18 (2nd best record) with a W8 streak but no explicit rest/load-management flag for their stars in the late-season context.** — SAS at 56-18 with clinched high seeding are prime candidates for star rest in the final 8 games — any SAS pick without explicit roster verification could be invalidated by undisclosed rest decisions. → Add SAS to the 'mandatory star-rest verification' list alongside OKC and Detroit — require explicit confirmation that key SAS rotation players are active before any SAS pick is drafted.
