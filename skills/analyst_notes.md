---
date: 2026-03-26
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
milestone: daily (5 bets)
---

## Today's Analysis — 2026-03-26

The most significant factual update this session is De'Aaron Fox confirmed OUT [roster-only] for San Antonio — a franchise-level absence on a team currently riding a W7 streak and sitting 55-18; any San Antonio pick must trigger mandatory re-verification before commitment. Detroit (Cade Cunningham OUT) and Minnesota (Anthony Edwards OUT) remain the other two high-risk teams where ML bets are effectively blocked without official confirmation. Performance data remains too thin (5 bets, 1W/4L) to justify strategic rule changes — the losing pattern is spread across all market types and confidence tiers, suggesting general early-sample variance rather than a structural rule failure; no strategic patches are warranted at this sample size.

## Performance Stats
ALL-TIME: 1W / 4L | Win rate: 20.0% | P&L: €-460.89 | Avg odds: 1.98 | Avg conf: 65.8/100
RECENT 5: 1W / 4L | 20.0% WR | P&L: €-460.89
By market:      ML 1bets 0W/1L 0.0% €-100.00  |  SPREAD 3bets 1W/2L 33.3% €-245.36  |  TOTAL 1bets 0W/1L 0.0% €-115.53
By confidence:  High 1bets 0W/1L 0.0% €-225.00  |  Medium 3bets 1W/2L 33.3% €-135.89  |  Speculative 1bets 0W/1L 0.0% €-100.00
By odds range:  1.70-1.89 1bets 0W/1L 0.0% €-115.53  |  1.90-2.09 3bets 1W/2L 33.3% €-245.36  |  2.10-2.50 1bets 0W/1L 0.0% €-100.00



## Scout patches applied
- [franchise_player_rules] Verified franchise player list updated from ESPN+NBA injury feed cross-reference: De'Aaron Fox (SAS), Immanuel Quickley (TOR), Alex Sarr (WAS), Tre Johnson (WAS), Tristan Vukcevic (WAS) added; multiple prior-version names not in verified feed removed to prevent phantom injury application.
- [tanking_teams] Standings updated to current verified data; De'Aaron Fox (SAS) added as major franchise player absence; Atlanta Hawks hot-streak-fade rule correctly evaluated against .562 W% threshold; Cleveland and Minnesota depth depletion noted; Golden State streak updated to W2 but L10 context maintained.

## Commit patches applied
None

## Intelligence gaps identified
- **De'Aaron Fox is listed OUT [roster-only] for San Antonio yet the Spurs are on a W7 streak at 55-18 — there is no rule that handles a team performing at elite level while missing their franchise player for an extended stretch (i.e. 'franchise player already priced in' scenario).** — If Fox has been out for multiple games and the Spurs keep winning, the market has already adjusted; applying a raw confidence penalty for his absence may over-discount SAS picks and create false negatives. → Add a rule to franchise_player_rules: if a franchise player has been OUT for 5+ consecutive games AND team W% during that stretch is ≥ .600, reduce confidence penalty from standard to -5 (instead of -15/-20) as market has repriced. Flag this as a data-pipeline gap — need game-by-game Fox absence tracking to confirm.
- **Cleveland Cavaliers have 5 players OUT [roster-only] (Jarrett Allen, Craig Porter Jr., Max Strus, Jaylon Tyson, Dean Wade) but there is no multi-player depletion rule — the current franchise_player_rules only adjusts for individual franchise players, not cumulative roster depth loss.** — A team missing 5 rotation players faces compounding fatigue and lineup instability that a single -15 confidence adjustment doesn't capture; this could lead to over-confidence on Cleveland picks. → Add to franchise_player_rules: if 4+ rotation players are OUT simultaneously for a team, apply an additional confidence -10 on top of any franchise player adjustments, capped at -30 total. Confidence ≥ 0.7 this is correct directionally.
- **Atlanta Hawks L10: 9-1 with NetRtg +1.8 — the hot-streak-fade rule currently requires overall W% below .550, and Atlanta at .562 falls just above the threshold, but their NetRtg sharply contradicts their record, suggesting meaningful regression risk that the rule currently ignores.** — A team with NetRtg +1.8 going 9-1 in L10 is almost certainly experiencing a luck spike (close-game wins, opponent injuries, schedule); the .550 W% threshold alone may be too lenient when NetRtg vs record gap is large. → Add a secondary trigger to the HOT STREAK FADE RULE in selectivity: if L10 ≥ 8-2 AND season NetRtg is < +3.0 (regardless of W%), the fade candidate flag activates at a reduced confidence bonus of +5 (instead of +10), acknowledging weaker signal strength.
- **Injury feed for today's session contains only 3 named players in the CURRENT INJURY LANDSCAPE section (Kyshawn George, Tristan Vukcevic, Tre Johnson — all Wizards), which is far below the 10-team coverage threshold defined in data_quality_rules.** — The verified franchise player absences section is populated via ESPN roster cross-reference, but the live injury landscape feed being critically sparse means game-time decisions and late scratches for non-Wizards teams are effectively invisible today. → Flag for data pipeline: the live injury landscape feed needs to be sourced from the NBA official PDF rather than a separate feed. Until fixed, Scout should default to ESPN-fallback rules (confidence cap 50, spreads/totals banned) on any session where the injury landscape lists fewer than 10 players across 5+ teams.
