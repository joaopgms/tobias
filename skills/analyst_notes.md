---
date: 2026-05-31
llm: claude-sonnet-4-6
scout_patches: 1
commit_patches: 0
milestone: daily (46 bets)
---

## Today's Analysis — 2026-05-31

The WCF is now complete with San Antonio winning Game 7 on the road at OKC — a significant result that recalibrates our home court premium rule, as OKC had home court + superior NetRtg (+2.8pt) and still lost; this means in close-NetRtg Finals matchups, we should not treat home court as near-deterministic. The NBA Finals (SAS vs NYK) presents a genuinely competitive matchup: SAS has a +1.8pt NetRtg edge but NYK has maximum rest advantage (7-10 days) and home court for Games 1, 2, 5, 7 — the early series games strongly favour NYK situationally, but SAS's proven road resilience means we must require confluence of 2+ signals before backing NYK at short odds. Wembanyama's health and fatigue from the 7-game WCF grind is the single most important variable to monitor before any Finals pick is drafted.

## Performance Stats
ALL-TIME: 32W / 32L | Win rate: 50.0% | P&L: €-254.88 | Avg odds: 1.94 | Avg conf: 65.4/100
RECENT 20: 11W / 9L | 55.0% WR | P&L: €+221.62
By market:      ML 25bets 12W/13L 48.0% €-289.43  |  SPREAD 29bets 16W/13L 55.2% €+592.70  |  TOTAL 10bets 4W/6L 40.0% €-558.15
By confidence:  High 20bets 8W/12L 40.0% €-955.52  |  Medium 41bets 24W/17L 58.5% €+1061.55  |  Speculative 3bets 0W/3L 0.0% €-360.91
By odds range:  1.70-1.89 22bets 11W/11L 50.0% €-678.39  |  1.90-2.09 37bets 20W/17L 54.1% €+585.12  |  2.10-2.50 5bets 1W/4L 20.0% €-161.61



## Scout patches applied
- [franchise_player_rules] WCF is now COMPLETE per ESPN feed (SAS leads 4-3 marked COMPLETE), updating SAS to eliminated and OKC to NBA Finals participant; NYK already confirmed; franchise player rules must reflect Finals context.

## Commit patches applied
None

## Playoff context patches applied
- [phase] ESPN live feed confirms SAS leads 4-3 [COMPLETE] in West Finals, meaning SAS won WCF and OKC is eliminated; phase must be updated to NBA Finals.
- [series_context] ESPN confirms WCF complete with SAS winning 4-3; series_context must be updated to reflect NBA Finals (SAS vs NYK) and capture rest/NetRtg dynamics for Finals framing.
- [elimination_flags] OKC is now eliminated (SAS won WCF 4-3 per ESPN); both Finals participants must be correctly flagged with mandatory verification requirements.
- [playoff_rest] WCF complete; Finals rest dynamics (NYK maximum rest vs SAS 7-game fatigue) now govern this section and replace the Game 7 WCF rest framing.
- [playoff_motivation] WCF is complete; motivation section must be updated to reflect NBA Finals (SAS vs NYK) with correct rest dynamics, home court structure, and motivational framing.
- [h2h_playoff] WCF complete with SAS winning; h2h_playoff must clear WCF and establish NBA Finals H2H framing, including the key lesson that home court did not determine WCF Game 7.
- [l15_caveat] WCF complete; l15_caveat must be updated to NBA Finals framing, incorporating the critical lesson that home court did not determine WCF Game 7 and calibrating the small SAS-NYK NetRtg gap correctly.
- [no_tanking] OKC is now eliminated; both NBA Finals participants must be correctly identified with SAS replacing OKC as the WCF winner.

## Intelligence gaps identified
- **No rule exists to quantify the expected accuracy of home court premium when series NetRtg gap is small (< 2.5 pts) — WCF Game 7 showed OKC's +2.8pt NetRtg edge + home court was insufficient to overcome SAS resilience.** — A rule treating home court + small NetRtg gap as 'compound OKC edge' likely inflated confidence on OKC WCF Game 7 picks; the correct framework should require NetRtg gap ≥ 4.0pts before home court becomes a 'compound' (rather than additive) edge signal. → Add a nuance to playoff_motivation and l15_caveat: when NetRtg gap < 3.0pts AND series is tied or one team has proven road wins in the series, treat home court as additive (+3-4pts) but NOT compounding — do not label it a 'compound edge'. Require NetRtg gap ≥ 4.0pts for compound edge framing.
- **Wembanyama's actual minutes load and efficiency across WCF Games 5-7 is unknown — this is the #1 swing factor for SAS in Finals Games 1-3 but we have no quantitative fatigue signal.** — If Wembanyama played 40+ minutes in Games 5-7 under heavy defensive load, his Finals Game 1 efficiency is meaningfully lower — a pick on SAS in Games 1-2 without this data risks backing a fatigued franchise player. → Fetch Wembanyama minutes-per-game from WCF Games 5, 6, 7 from ESPN box scores before drafting any Finals SAS pick. Flag as mandatory pre-draft data requirement in franchise_player_rules for Finals.
- **ML market at 1.70-1.89 odds range continues to be the worst-performing segment (-€818.05, 9W/10L) but no rule currently prohibits ML bets in this range for Games 1-2 of the Finals where SAS or NYK might be priced there.** — Finals Game 1-2 lines for NYK (home favourite) will likely fall in the 1.65-1.85 range — the exact danger zone where ML underperforms; backing NYK ML at 1.75 in Games 1-2 would repeat the pattern the confidence_staking section already flags. → The existing EV ≥ 0.08 rule for ML at 1.70-1.89 in confidence_staking already addresses this — ensure Scout applies it strictly for Finals early games. No additional patch needed; flag as active enforcement reminder.
