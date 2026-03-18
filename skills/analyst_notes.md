---
date: 2026-03-18
llm: claude-sonnet-4-6
scout_patches: 2
commit_patches: 0
---

## Today's Analysis — 2026-03-18

No settled bets exist yet so no performance-based rule changes are warranted. The standings reveal a historically compressed top of the league (OKC 54-15, Spurs 51-18, Pistons 49-19) which will price these teams efficiently — Scout should expect short ML odds and focus value-hunting on underdog situations or spread/totals. Atlanta's perfect L10 (10-0, W10) is a significant regression flag; any game featuring the Hawks should trigger heightened scrutiny for fade opportunities on the Hawks side at inflated odds.



## Scout patches applied
- [franchise_player_rules] Injury feed confirms Leaky Black, Anthony Davis, and Kyshawn George remain OUT; records are unchanged so existing Lakers/Wizards notes stand, but entries are current-session verified.
- [tanking_teams] Standings updated across all teams to reflect current W-L records, L10, and streaks including Wizards now L13, Bucks L1, OKC W9, Spurs 51-18, and Lakers W6.

## Commit patches applied
None

## Intelligence gaps identified
- **Advanced stats (NetRtg L15, Pace, OffRtg, DefRtg) are unavailable this session despite being the top scouting priority.** — Without NetRtg L15 and Pace data, Scout cannot legally bet spreads or totals per current rules, effectively limiting all picks to ML only — this significantly narrows the opportunity set and may cause sessions with zero draftable picks. → Establish a reliable advanced stats fetch (e.g. Basketball-Reference or NBA.com stats endpoint) as a required pre-Scout data pull; if unavailable, Scout should log 'advanced stats missing — ML only session' explicitly in the scout report.
- **Detroit Pistons at 49-19 (3rd overall) have no franchise player injury status on record and no advanced stats context.** — A team with the 3rd-best record in the NBA will appear in matchups frequently; without knowing their key player health (Cade Cunningham status) and NetRtg, Scout cannot properly evaluate games involving them. → Add Detroit Pistons (Cade Cunningham) to franchise_player_rules monitoring list and flag as a team requiring per-session injury verification before drafting any pick involving Detroit.
- **Atlanta Hawks' 10-game winning streak creates a potential line inefficiency pattern that no current section addresses systematically.** — Books may be slow to fully price in a regression-to-mean risk for a team that was 37-21 pace two weeks ago and is now 37-31 — hot-streak fade edges are historically profitable but require a defined rule for when to act. → Add a 'hot streak fade' sub-rule under priority_stats or tanking_teams: when a non-elite team (outside top-8 record) has L10 ≥ 9-1 and season record implies sub-.550 true talent, flag opponent as having regression-based edge and require Scout to check current ML odds explicitly.
