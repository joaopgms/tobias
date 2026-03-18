"""
core/espn.py
ESPN hidden API helpers for Tobias.
Scores, schedules, injuries, standings — all free, no API key.
"""

import ssl
import json
import logging
import urllib.request
import urllib.parse
from datetime import date, datetime, timezone, timedelta

log = logging.getLogger(__name__)

_SSL = ssl.create_default_context()
_SSL.check_hostname = False
_SSL.verify_mode    = ssl.CERT_NONE

_HEADERS = {
    "User-Agent":      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept":          "application/json, */*",
    "Accept-Language": "en-US,en;q=0.9",
}


def _get(url: str, timeout: int = 15) -> dict:
    req = urllib.request.Request(url, headers=_HEADERS)
    with urllib.request.urlopen(req, timeout=timeout, context=_SSL) as r:
        return json.loads(r.read().decode())


# ── Scoreboard ─────────────────────────────────────────────────────────────────

def fetch_scoreboard(target_date: date | None = None) -> list[dict]:
    """Today's NBA scoreboard from ESPN. Returns list of game dicts."""
    d = (target_date or date.today()).strftime("%Y%m%d")
    url = f"https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates={d}"
    try:
        data = _get(url)
        games = []
        for evt in data.get("events", []):
            comp  = evt["competitions"][0]
            teams = comp["competitors"]
            home  = next(t for t in teams if t["homeAway"] == "home")
            away  = next(t for t in teams if t["homeAway"] == "away")
            status = evt["status"]["type"]

            games.append({
                "id":        evt["id"],
                "home":      home["team"]["displayName"],
                "home_abbr": home["team"]["abbreviation"],
                "away":      away["team"]["displayName"],
                "away_abbr": away["team"]["abbreviation"],
                "time":      evt.get("date", ""),
                "status":    status.get("description", ""),
                "completed": status.get("completed", False),
                "home_score": int(home.get("score") or 0),
                "away_score": int(away.get("score") or 0),
                "venue":     comp.get("venue", {}).get("fullName", ""),
            })
        log.info(f"ESPN scoreboard {d}: {len(games)} games")
        return games
    except Exception as e:
        log.warning(f"ESPN scoreboard error: {e}")
        return []


# ── Injuries ───────────────────────────────────────────────────────────────────

INJURY_MISS_PROB = {
    "Out": 1.00, "Doubtful": 0.75, "Questionable": 0.50,
    "Day-To-Day": 0.40, "Game-Time Decision": 0.50, "Probable": 0.15,
}

def fetch_injuries() -> dict[str, list[dict]]:
    """Returns {team_name: [{name, pos, status, detail, miss_prob}]}"""
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/injuries"
    try:
        data = _get(url)
        result = {}
        for team in data.get("injuries", []):
            name   = team.get("team", {}).get("displayName", "")
            players = []
            for item in team.get("injuries", []):
                athlete = item.get("athlete", {})
                status  = item.get("status", "")
                detail  = item.get("details", {}).get("detail", "")
                players.append({
                    "name":      athlete.get("displayName", ""),
                    "pos":       athlete.get("position", {}).get("abbreviation", ""),
                    "status":    status,
                    "detail":    detail,
                    "miss_prob": INJURY_MISS_PROB.get(status, 0.5),
                })
            if players:
                result[name] = players
        log.info(f"ESPN injuries: {len(result)} teams with reports")
        return result
    except Exception as e:
        log.warning(f"ESPN injuries error: {e}")
        return {}


# ── Standings ──────────────────────────────────────────────────────────────────

def fetch_standings() -> dict[str, dict]:
    """Returns {team_name: {wins, losses, pct, streak, l10, ...}}"""
    url = "https://site.api.espn.com/apis/v2/sports/basketball/nba/standings"
    try:
        data = _get(url)
        result = {}
        for group in data.get("children", []):
            conf = group.get("abbreviation", "")
            for entry in group.get("standings", {}).get("entries", []):
                team = entry.get("team", {}).get("displayName", "")
                abbr = entry.get("team", {}).get("abbreviation", "")
                stats = {s["name"]: s.get("displayValue", s.get("value"))
                         for s in entry.get("stats", [])}
                record = {
                    "wins":    stats.get("wins", 0),
                    "losses":  stats.get("losses", 0),
                    "pct":     stats.get("winPercent", 0),
                    "gb":      stats.get("gamesBehind", 0),
                    "streak":  stats.get("streak", ""),
                    "l10":     stats.get("Last Ten Games", ""),
                    "home_rec": stats.get("Home", ""),
                    "away_rec": stats.get("Road", ""),
                    "conf":    conf,
                    "abbr":    abbr,
                }
                result[team] = record
                if abbr:
                    result[abbr] = record
        log.info(f"ESPN standings: {len(result)//2} teams")
        return result
    except Exception as e:
        log.warning(f"ESPN standings error: {e}")
        return {}


# ── Scores for settlement ──────────────────────────────────────────────────────

def fetch_final_scores(target_date: date) -> dict[str, dict]:
    """
    Returns map of final scores for settlement.
    Keys: 'Away @ Home', 'Away vs Home', away_name, home_name (multiple for flexibility).
    """
    games = fetch_scoreboard(target_date)
    result = {}
    for g in games:
        # Only include truly final games
        status = g.get("status", "").lower()
        is_final = "final" in status or g.get("completed", False)
        if not is_final:
            continue
        if g["home_score"] == 0 and g["away_score"] == 0:
            continue  # Not finished

        payload = {
            "home":       g["home"],
            "away":       g["away"],
            "home_score": g["home_score"],
            "away_score": g["away_score"],
            "home_won":   g["home_score"] > g["away_score"],
        }
        result[f"{g['away']} @ {g['home']}"]  = payload
        result[f"{g['away']} vs {g['home']}"] = payload
        result[f"{g['home']} vs {g['away']}"] = payload
        result[g["home"]]  = payload
        result[g["away"]]  = payload
        result[f"{g['away_abbr']} @ {g['home_abbr']}"] = payload

    log.info(f"ESPN final scores for {target_date}: {len(payload) if result else 0} games settled")
    return result


# ── First game time ────────────────────────────────────────────────────────────

def fetch_first_game_time_utc(target_date: date | None = None) -> str | None:
    """Returns ISO UTC string of the earliest game tip-off tonight, or None."""
    games = fetch_scoreboard(target_date)
    times = []
    for g in games:
        t = g.get("time", "")
        if t:
            try:
                dt = datetime.fromisoformat(t.replace("Z", "+00:00"))
                times.append(dt)
            except ValueError:
                pass
    if not times:
        return None
    earliest = min(times)
    return earliest.strftime("%Y-%m-%dT%H:%M:%SZ")


# ── Advanced stats (NBA.com) ───────────────────────────────────────────────────

_NBA_STATS_HEADERS = {
    "User-Agent":        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer":           "https://www.nba.com/stats/teams/advanced",
    "Accept":            "application/json, text/plain, */*",
    "Accept-Language":   "en-US,en;q=0.9",
    "Accept-Encoding":   "gzip, deflate, br",
    "Origin":            "https://www.nba.com",
    "Connection":        "keep-alive",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token":  "true",
    "Cache-Control":     "no-cache",
    "Pragma":            "no-cache",
}


def fetch_advanced_stats() -> dict[str, dict]:
    """
    Fetch team advanced stats.
    Primary: ESPN team statistics endpoint (cloud-friendly, no IP blocking).
    Fallback: Basketball-Reference HTML scrape.
    Returns {team_name: {net_rtg, off_rtg, def_rtg, pace, ts_pct}}
    """
    result = _fetch_advanced_stats_espn()
    if result:
        log.info(f"Advanced stats: ESPN — {len(result)} teams")
        return result

    log.warning("Advanced stats: ESPN failed — trying Basketball-Reference")
    result = _fetch_advanced_stats_bref()
    if result:
        log.info(f"Advanced stats: Basketball-Reference — {len(result)} teams")
        return result

    log.warning("Advanced stats: all sources failed — ML only session")
    return {}


def _fetch_advanced_stats_espn() -> dict[str, dict]:
    """
    Fetch advanced stats from ESPN team statistics endpoint.
    Uses the same ESPN API we already use for injuries/standings — no IP blocking.
    """
    result = {}
    for team_name, team_id in ESPN_TEAM_IDS.items():
        url = (f"https://site.api.espn.com/apis/site/v2/sports/basketball/nba"
               f"/teams/{team_id}/statistics")
        try:
            data = _get(url, timeout=8)
            splits = data.get("splits", {}).get("categories", [])
            stats = {}
            for cat in splits:
                for s in cat.get("stats", []):
                    stats[s.get("name","")] = s.get("value", s.get("displayValue"))

            # ESPN stat name mapping — try multiple possible field names
            def _get(*keys):
                for k in keys:
                    v = stats.get(k)
                    if v is not None:
                        try: return float(v)
                        except: pass
                return None

            net_rtg = _get("netRating","netRtg","net_rtg","netrtg")
            off_rtg = _get("offensiveRating","offRating","offRtg","off_rtg","oppg")
            def_rtg = _get("defensiveRating","defRating","defRtg","def_rtg","dppg")
            pace    = _get("pace","paceAdjust","possessions","poss")
            ts_pct  = _get("trueShootingPercentage","tsPct","ts_pct","trueshooting")

            if any(v is not None for v in [net_rtg, off_rtg, def_rtg, pace]):
                result[team_name] = {
                    "net_rtg": round(float(net_rtg), 1) if net_rtg is not None else 0.0,
                    "off_rtg": round(float(off_rtg), 1) if off_rtg is not None else 0.0,
                    "def_rtg": round(float(def_rtg), 1) if def_rtg is not None else 0.0,
                    "pace":    round(float(pace),    1) if pace    is not None else 0.0,
                    "ts_pct":  round(float(ts_pct),  3) if ts_pct  is not None else 0.0,
                }
        except Exception as e:
            log.debug(f"ESPN stats {team_name}: {e}")
            continue

    # Need at least 20 teams to be useful
    return result if len(result) >= 20 else {}


def _fetch_advanced_stats_bref() -> dict[str, dict]:
    """
    Fallback: scrape Basketball-Reference team advanced stats table.
    URL: https://www.basketball-reference.com/leagues/NBA_2026.html
    """
    try:
        import re
        url = "https://www.basketball-reference.com/leagues/NBA_2026.html"
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en-US,en;q=0.9",
        })
        with urllib.request.urlopen(req, timeout=20, context=_SSL) as r:
            html = r.read().decode("utf-8", errors="ignore")

        # Find the misc/advanced stats table — has NRtg, Pace, ORtg, DRtg
        # Table id: div_misc_stats or div_team-stats-per_poss
        table_match = re.search(
            r'id="div_misc_stats".*?<table.*?>(.*?)</table>',
            html, re.DOTALL
        )
        if not table_match:
            # Try alternate table
            table_match = re.search(
                r'<table[^>]*id="misc_stats"[^>]*>(.*?)</table>',
                html, re.DOTALL
            )
        if not table_match:
            log.warning("Basketball-Reference: misc_stats table not found")
            return {}

        table_html = table_match.group(1)

        # Extract headers
        headers = re.findall(r'<th[^>]*data-stat="([^"]*)"[^>]*>', table_html)

        # Extract rows
        result = {}
        rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_html, re.DOTALL)
        for row in rows:
            cells = re.findall(r'<td[^>]*data-stat="([^"]*)"[^>]*>([^<]*)', row)
            if not cells:
                continue
            row_data = {k: v.strip() for k, v in cells}

            team_raw = row_data.get("team_name_abbr") or row_data.get("team")
            if not team_raw:
                continue

            # Map bref abbr to full name
            team_name = _bref_abbr_to_full(team_raw)
            if not team_name:
                continue

            def _safe(key):
                try: return float(row_data.get(key, "") or 0)
                except: return 0.0

            result[team_name] = {
                "net_rtg": _safe("net_rtg"),
                "off_rtg": _safe("off_rtg"),
                "def_rtg": _safe("def_rtg"),
                "pace":    _safe("pace"),
                "ts_pct":  _safe("ts_pct") / 100 if _safe("ts_pct") > 1 else _safe("ts_pct"),
            }

        return result if len(result) >= 20 else {}

    except Exception as e:
        log.warning(f"Basketball-Reference scrape failed: {e}")
        return {}


# Basketball-Reference abbreviation → full team name
_BREF_ABBR = {
    "ATL":"Atlanta Hawks","BOS":"Boston Celtics","BRK":"Brooklyn Nets",
    "CHO":"Charlotte Hornets","CHI":"Chicago Bulls","CLE":"Cleveland Cavaliers",
    "DAL":"Dallas Mavericks","DEN":"Denver Nuggets","DET":"Detroit Pistons",
    "GSW":"Golden State Warriors","HOU":"Houston Rockets","IND":"Indiana Pacers",
    "LAC":"Los Angeles Clippers","LAL":"Los Angeles Lakers","MEM":"Memphis Grizzlies",
    "MIA":"Miami Heat","MIL":"Milwaukee Bucks","MIN":"Minnesota Timberwolves",
    "NOP":"New Orleans Pelicans","NYK":"New York Knicks","OKC":"Oklahoma City Thunder",
    "ORL":"Orlando Magic","PHI":"Philadelphia 76ers","PHO":"Phoenix Suns",
    "POR":"Portland Trail Blazers","SAC":"Sacramento Kings","SAS":"San Antonio Spurs",
    "TOR":"Toronto Raptors","UTA":"Utah Jazz","WAS":"Washington Wizards",
}

def _bref_abbr_to_full(abbr: str) -> str | None:
    return _BREF_ABBR.get(abbr.upper().strip())



def format_advanced_stats_for_prompt(stats: dict, games: list[dict]) -> str:
    """
    Format advanced stats for only the teams playing tonight.
    Compact — only relevant matchups.
    """
    if not stats or not games:
        return "Advanced stats unavailable."

    lines = ["Source: NBA.com Advanced Stats (OffRtg / DefRtg / NetRtg / Pace)"]
    seen = set()
    for g in games:
        for team in [g.get("home",""), g.get("away","")]:
            if not team or team in seen:
                continue
            seen.add(team)
            s = stats.get(team)
            if s:
                lines.append(
                    f"{team}: OffRtg {s['off_rtg']} | DefRtg {s['def_rtg']} "
                    f"| NetRtg {s['net_rtg']:+.1f} | Pace {s['pace']}"
                )
            else:
                lines.append(f"{team}: stats unavailable")

    return "\n".join(lines)


# ── Team rosters ───────────────────────────────────────────────────────────────

# ESPN team ID map — all 30 NBA teams
ESPN_TEAM_IDS = {
    "Atlanta Hawks": 1, "Boston Celtics": 2, "Brooklyn Nets": 17,
    "Charlotte Hornets": 30, "Chicago Bulls": 4, "Cleveland Cavaliers": 5,
    "Dallas Mavericks": 6, "Denver Nuggets": 7, "Detroit Pistons": 8,
    "Golden State Warriors": 9, "Houston Rockets": 10, "Indiana Pacers": 11,
    "Los Angeles Clippers": 12, "Los Angeles Lakers": 13, "Memphis Grizzlies": 29,
    "Miami Heat": 14, "Milwaukee Bucks": 15, "Minnesota Timberwolves": 16,
    "New Orleans Pelicans": 3, "New York Knicks": 18, "Oklahoma City Thunder": 25,
    "Orlando Magic": 19, "Philadelphia 76ers": 20, "Phoenix Suns": 21,
    "Portland Trail Blazers": 22, "Sacramento Kings": 23, "San Antonio Spurs": 24,
    "Toronto Raptors": 28, "Utah Jazz": 26, "Washington Wizards": 27,
}

def fetch_team_roster(team_name: str) -> list[dict]:
    """
    Fetch current roster for a team from ESPN.
    Returns list of {name, position, jersey, status} dicts.
    """
    team_id = ESPN_TEAM_IDS.get(team_name)
    if not team_id:
        # Try partial match
        for name, tid in ESPN_TEAM_IDS.items():
            if team_name.lower() in name.lower() or name.lower() in team_name.lower():
                team_id = tid
                break
    if not team_id:
        log.warning(f"ESPN roster: unknown team '{team_name}'")
        return []

    url = f"https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/{team_id}/roster"
    try:
        data = _get(url)
        roster = []
        for group in data.get("athletes", []):
            # ESPN returns athletes grouped by position
            items = group if isinstance(group, list) else group.get("items", [group])
            for athlete in items:
                if not isinstance(athlete, dict):
                    continue
                injuries = athlete.get("injuries", [])
                inj_status = injuries[0].get("status", "") if injuries else ""
                roster.append({
                    "name":     athlete.get("displayName", athlete.get("fullName", "")),
                    "position": athlete.get("position", {}).get("abbreviation", ""),
                    "jersey":   athlete.get("jersey", ""),
                    "status":   inj_status,
                })
        log.info(f"ESPN roster {team_name}: {len(roster)} players")
        return roster
    except Exception as e:
        log.warning(f"ESPN roster error for {team_name}: {e}")
        return []


def fetch_franchise_player_statuses(franchise_teams: list[str],
                                     injuries: dict) -> dict[str, list[dict]]:
    """
    For each franchise-tier team, fetch roster and cross-reference with injury feed.
    Returns {team_name: [{name, position, status, reason, verified}]}
    verified=True means confirmed from both roster + injury feed.
    """
    result = {}
    for team in franchise_teams:
        roster = fetch_team_roster(team)
        if not roster:
            log.warning(f"Franchise player check: no roster for {team}")
            continue

        team_injuries = injuries.get(team, [])
        inj_by_name = {p["name"].lower(): p for p in team_injuries}

        notable = []
        for player in roster:
            name_lower = player["name"].lower()
            # Check injury feed
            inj = inj_by_name.get(name_lower)
            # Also try last name match
            if not inj:
                last = name_lower.split()[-1]
                inj = next((p for n, p in inj_by_name.items() if last in n), None)

            status = inj["status"] if inj else player.get("status", "")
            if status.lower() in ("out", "doubtful", "questionable", "game time decision", "gtd"):
                notable.append({
                    "name":     player["name"],
                    "position": player["position"],
                    "status":   status,
                    "reason":   inj.get("reason", "") if inj else "",
                    "verified": bool(inj),  # True = confirmed in injury feed
                })

        if notable:
            result[team] = notable
        log.info(f"Franchise check {team}: {len(notable)} notable absences")

    return result
