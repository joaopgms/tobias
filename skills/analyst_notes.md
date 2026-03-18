---
date: 2026-03-18
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
---

## Today's Analysis — 2026-03-18

No settled bets exist yet so strategic patches are withheld per performance feedback rule. The most notable structural anomaly in today's standings is Detroit Pistons at 49-19 with Cade Cunningham confirmed OUT [roster only] — books may be pricing the Pistons on their record rather than current roster, creating potential fade value. Atlanta Hawks' 10-0 L10 streak against a .544 season W% remains the highest-priority regression fade target and should be evaluated every session until the streak breaks. Advanced stats are unavailable this session, which means spreads and totals must be banned per data_quality_rules if Scout runs today.



## Scout patches applied
- [franchise_player_rules] Verified franchise player absences unchanged from prior session per ESPN roster cross-reference; no new additions or removals detected in today's feed — content preserved exactly with [roster only] flags intact.
- [tanking_teams] Detroit Pistons have risen to 49-19 (third-best record in the league) but Cade Cunningham is OUT [roster only], creating a material line distortion risk worth flagging explicitly in the hot streaks section.

## Commit patches applied
None

## Intelligence gaps identified
- **Advanced stats (OffRtg, DefRtg, NetRtg L15, Pace) are unavailable this session for all 30 teams.** — Without these stats, Scout cannot evaluate spreads, totals, or pace-based O/U edges — the session is effectively ML-only, reducing pick universe and edge quality significantly. → Add a pre-session advanced stats fetch step (e.g. Basketball Reference or NBA.com/stats API) and surface NetRtg L15 and Pace per team before Scout runs; if unavailable, log 'ML-only session' explicitly in scout_report.
- **Detroit Pistons are 49-19 (3rd best record) with Cade Cunningham OUT [roster only] — no rule currently addresses the scenario where a top-record team's franchise anchor is absent and books may not have adjusted.** — This creates an asymmetric mispricing risk: if books price Detroit as a strong favourite based on record but Cunningham is confirmed OUT, the opponent may have genuine ML value at inflated underdog odds. → Add a rule in franchise_player_rules or market_rules: when a top-8 record team has their franchise anchor OUT confirmed, flag their opponent for explicit ML value check if opponent odds are ≥ 1.80.
- **Atlanta Hawks 10-0 L10 streak has no explicit decay trigger — the HOT STREAK FADE RULE applies but there is no mechanism to escalate urgency as the streak lengthens beyond 10 games.** — A team sustaining a 10+ game hot streak at .544 true talent represents an increasingly extreme regression setup; the longer it extends, the stronger the fade edge, but current rules treat all streaks ≥ 9-1 identically. → Add a streak length multiplier to the HOT STREAK FADE RULE: if streak ≥ 10 AND overall W% < .550, boost opponent confidence bonus from +10 to +15 and lower the odds threshold to ≥ 1.70.
- **The injury feed this session contains only 3 named players in the raw injury landscape (Leaky Black, Anthony Davis, Kyshawn George — all Wizards), with all other absences sourced from roster-only cross-reference, suggesting the NBA official PDF feed may not have been retrieved.** — If the NBA official PDF was unavailable and the session is running on ESPN fallback with fewer than 5 teams confirmed, the data_quality_rules mandate a confidence cap of 40 and odds ≥ 2.00 — Scout needs to know the actual feed source before drafting. → Surface the explicit injury feed source (nba_official / espn / none) as a mandatory field in Scout's input context so the data_quality_rules gate is applied correctly at the start of every session.
