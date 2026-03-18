---
date: 2026-03-18
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
---

## Today's Analysis — 2026-03-18

Washington Wizards have extended their losing streak to L13 with 6 confirmed absences including all franchise players — they are a near-automatic fade target whenever odds permit. The OKC Thunder's Jalen Williams roster-only OUT flag is the most consequential uncertainty this session: OKC is the #1 seed at 54-15 and Williams is their second-best player, so any pick involving OKC requires NBA official PDF re-verification before drafting. Atlanta Hawks' W10 streak on a .544 overall record continues to represent the clearest regression-fade opportunity in the league — any opponent priced at ≥ 1.80 against Atlanta warrants explicit evaluation per the hot streak fade rule.



## Scout patches applied
- [franchise_player_rules] Verified franchise player absences updated from ESPN roster cross-reference; all entries marked ⚠ roster only per feed, including new franchise-level flags for Jalen Williams (OKC) and Anthony Edwards (MIN) which have major confidence implications.
- [tanking_teams] Standings updated to current session data; Washington streak extended to L13, Memphis streak at L8 confirmed deepening tank; Lakers hot streak (W6) added; OKC Jalen Williams absence flagged as franchise-level concern; play-in seeding race context added for late-season scout accuracy.

## Commit patches applied
None

## Intelligence gaps identified
- **Advanced stats (OffRtg, DefRtg, NetRtg, Pace) are unavailable this session for all 30 teams.** — Without these stats, Scout cannot bet spreads or totals per data_quality_rules, limiting the session to ML-only picks and reducing potential edge identification — particularly for the Pace-based O/U signals and DefRtg gap spread signals. → Ensure the advanced stats pipeline is verified before 14:00 UTC Scout run; if unavailable again, Scout should log 'ML-only session — advanced stats unavailable' and skip all spread/total evaluation explicitly.
- **All injury entries this session are flagged ⚠ roster only, meaning none are confirmed via NBA official injury report PDF — the highest-quality source.** — Roster-only flags cannot confirm injury severity, timeline, or whether a player is genuinely OUT vs listed for rest/load management; this is especially critical for Jalen Williams (OKC) and Cade Cunningham (Detroit) where franchise-player rules require high confidence before drafting. → Add an explicit rule in data_quality_rules: if ALL injuries for a game's two teams are ⚠ roster only with no nba_official confirmation, apply ESPN-fallback confidence cap (50) and ban spreads/totals for that specific game, not just session-wide.
- **No rule currently addresses star rest probability for teams clinched into top-3 seeds in late March (OKC 54-15, Spurs 51-18, Pistons 49-19).** — Clinched top seeds have strong incentive to rest stars in meaningless late-season games, but current priority_stats only checks play-in motivation — it does not flag the inverse risk for already-clinched teams, which could produce false confidence on those teams as favourites. → Add to priority_stats step 4 (Late Season Flag): 'Teams clinched into top-3 seeds after March 15 — flag star rest risk explicitly. If opponent is a competitive team (≥ .500 record), require re-verification of franchise player status before drafting picks on the clinched team.'
- **Memphis Grizzlies are on an L8 streak but their confirmed tank status and roster health are not verified beyond record — no specific player absences are listed in the verified injury feed for Memphis.** — Memphis being a confirmed tank with L8 streak but no injury data means Scout cannot distinguish between 'losing due to tanking' vs 'losing due to injuries' — the edge type differs (injury-driven losses may reverse when players return, tank-driven losses are intentional). → Flag Memphis as requiring roster verification before any pick: if no Memphis players appear in the injury feed, treat as ESPN-fallback quality for Memphis-specific picks and cap confidence at 50.
