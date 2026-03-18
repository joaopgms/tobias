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
    "User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer":     "https://www.nba.com/",
    "Accept":      "application/json, */*",
    "Origin":      "https://www.nba.com",
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token":  "true",
}

def fetch_advanced_stats() -> dict[str, dict]:
    """
    Fetch team advanced stats from NBA.com stats API.
    Returns {team_name: {net_rtg, off_rtg, def_rtg, pace, ts_pct, ...}}
    No API key required — public endpoint.
    """
    url = (
        "https://stats.nba.com/stats/leaguedashteamstats"
        "?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment="
        "&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Advanced"
        "&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N"
        "&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition="
        "&PlusMinus=N&Rank=N&Season=2025-26&SeasonSegment=&SeasonType=Regular+Season"
        "&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision="
    )
    try:
        req = urllib.request.Request(url, headers=_NBA_STATS_HEADERS)
        with urllib.request.urlopen(req, timeout=15, context=_SSL) as r:
            data = json.loads(r.read().decode())

        rs = data.get("resultSets", [{}])[0]
        headers = rs.get("headers", [])
        rows    = rs.get("rowSet", [])

        # Map header → index
        h = {name: i for i, name in enumerate(headers)}

        result = {}
        for row in rows:
            team_name = row[h.get("TEAM_NAME", 1)] if "TEAM_NAME" in h else None
            if not team_name:
                continue
            result[team_name] = {
                "net_rtg":  round(float(row[h["NET_RATING"]]  if "NET_RATING"  in h else 0), 1),
                "off_rtg":  round(float(row[h["OFF_RATING"]]  if "OFF_RATING"  in h else 0), 1),
                "def_rtg":  round(float(row[h["DEF_RATING"]]  if "DEF_RATING"  in h else 0), 1),
                "pace":     round(float(row[h["PACE"]]         if "PACE"        in h else 0), 1),
                "ts_pct":   round(float(row[h["TS_PCT"]]       if "TS_PCT"      in h else 0), 3),
                "ast_pct":  round(float(row[h["AST_PCT"]]      if "AST_PCT"     in h else 0), 3),
                "reb_pct":  round(float(row[h["REB_PCT"]]      if "REB_PCT"     in h else 0), 3),
            }

        log.info(f"NBA advanced stats: {len(result)} teams")
        return result

    except Exception as e:
        log.warning(f"NBA advanced stats error: {e}")
        return {}


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
