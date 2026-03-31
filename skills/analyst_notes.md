---
date: 2026-03-31
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (11 bets)
---

## Today's Analysis — 2026-03-31

The most significant factual update this session is Jalen Williams (OKC) appearing as OUT in the verified roster feed — if confirmed via NBA official PDF, this is a major star absence for the league's best team (NetRtg +10.9) and should suppress OKC confidence substantially. Detroit now has 5 confirmed roster-only absences including Cade Cunningham, Jalen Duren, Tobias Harris, Duncan Robinson, and Isaiah Stewart — their 54-21 record is increasingly fragile and any Detroit pick requires aggressive verification. The Philadelphia 76ers (NetRtg -0.3, 41-34 record) remain the most extreme fade signal in the league — a team with a negative net rating holding a winning record is a textbook regression candidate heading into the final stretch.

## Performance Stats
ALL-TIME: 4W / 7L | Win rate: 36.4% | P&L: €-522.32 | Avg odds: 1.99 | Avg conf: 64.4/100
RECENT 11: 4W / 7L | 36.4% WR | P&L: €-522.32
By market:      ML 5bets 2W/3L 40.0% €-141.53  |  SPREAD 4bets 2W/2L 50.0% €-196.52  |  TOTAL 2bets 0W/2L 0.0% €-184.27
By confidence:  High 1bets 0W/1L 0.0% €-225.00  |  Medium 9bets 4W/5L 44.4% €-197.32  |  Speculative 1bets 0W/1L 0.0% €-100.00
By odds range:  1.70-1.89 2bets 1W/1L 50.0% €-66.69  |  1.90-2.09 8bets 3W/5L 37.5% €-355.63  |  2.10-2.50 1bets 0W/1L 0.0% €-100.00



## Scout patches applied
- [franchise_player_rules] Verified feed updated: Isaiah Hartenstein and Jalen Williams added to OKC absences, Jalen Duren/Tobias Harris/Duncan Robinson added to Detroit, Jamison Battle added to Toronto, Bilal Coulibaly/Alex Sarr confirmed via injury landscape for Washington; several prior names (Anthony Edwards, Craig Porter Jr., Miles McBride, Kevin McCullar Jr.) not in current verified list and must be removed.
- [tanking_teams] Standings updated to current session data (OKC 60-16, Spurs 57-18, etc.); OKC Jalen Williams confirmed OUT via verified feed — critical franchise player absence added; Detroit multi-player absences updated; Anthony Edwards removed from confirmed absences as not in current verified feed.

## Commit patches applied
None

## Intelligence gaps identified
- **Jalen Williams (OKC) appears as OUT [roster-only] in the verified feed but this is an enormous star absence that is unconfirmed via NBA official PDF.** — OKC is the top team in the league (NetRtg +10.9, 60-16); Williams being out would fundamentally change any OKC pick confidence and potentially create value on opponents — Scout needs this confirmed before the 14:00 draft window. → Flag OKC as DO NOT DRAFT until NBA official PDF confirms Williams status; if confirmed OUT, evaluate opponent odds for potential fade value.
- **Anthony Edwards (Minnesota) was listed as OUT [roster-only] in the previous session's skills file but is NOT present in the current verified feed — his status is now unknown.** — Edwards is Minnesota's franchise player; if he's returned to active, Minnesota picks that were previously blocked may now be viable — but if he's still out and just dropped from the feed, betting Minnesota would be a significant error. → Add a mandatory re-verification flag for Anthony Edwards before any Minnesota pick; treat his status as unknown (not confirmed OUT, not confirmed active) until NBA official PDF is checked.
- **Totals market is 0W/2L (0% win rate, €-184.27 loss) but sample size is only 2 bets — insufficient to patch rules but pattern is consistent with the known issue of pace/style data quality.** — Both total losses may reflect the difficulty of O/U picks without reliable pace data; the existing data_quality_rules already raise the totals confidence floor when pace is unavailable, but if pace data remains 0.0 consistently, totals may need to be effectively banned. → Continue tracking totals separately; if a third total loss occurs, evaluate whether to raise the confidence floor from 65/70 to 75 or ban totals entirely when pace data is unavailable.
- **High confidence tier (85-100) has 0W/1L record and the single high-confidence pick lost €225 — the staking tier may be over-sizing stakes relative to actual edge quality at this sample stage.** — A single high-confidence loss at 30% bankroll is a significant drawdown; with only 11 total bets settled, the confidence calibration has not been validated and the high tier staking is particularly risky. → Monitor high confidence picks specifically; if a second high-confidence loss occurs, consider capping high tier at 20% until 20+ bets are settled to validate calibration.
