"""
core/odds.py
NBA odds fetcher — 3-tier fallback strategy.

Tier 1: OddsPapi (Betano) — primary, requires ODDSPAPI_KEY
Tier 2: The-Odds-API (best available EU bookmaker) — requires THE_ODDS_API_KEY
Tier 3: No odds — Scout produces report but 0 picks
"""

import os
import logging
import requests
from datetime import date, timezone

log = logging.getLogger(__name__)

ODDSPAPI_BASE   = "https://api.oddspapi.com"
THEODDS_BASE    = "https://api.the-odds-api.com/v4"
BETANO_KEY      = "betano"

# Preferred EU bookmakers in priority order for The-Odds-API fallback
EU_BOOKMAKERS   = ["betano", "unibet", "williamhill", "bet365", "pinnacle", "betfair"]
NBA_SPORT_KEY   = "basketball_nba"


# ── American → decimal ─────────────────────────────────────────────────────────
def american_to_decimal(ml) -> float | None:
    if ml is None:
        return None
    try:
        ml = int(ml)
        return round(ml / 100 + 1, 2) if ml > 0 else round(100 / abs(ml) + 1, 2)
    except (ValueError, ZeroDivisionError):
        return None


# ── TIER 1: OddsPapi (Betano) ──────────────────────────────────────────────────
def _oddspapi_nba_odds(api_key: str, target_date: date) -> list[dict]:
    url = f"{ODDSPAPI_BASE}/odds"
    params = {
        "apiKey":     api_key,
        "sport":      "basketball",
        "league":     "NBA",
        "bookmakers": BETANO_KEY,
        "markets":    "moneyline,spreads,totals",
        "oddsFormat": "decimal",
        "date":       target_date.strftime("%Y-%m-%d"),
    }
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        games = data.get("data", [])
        log.info(f"OddsPapi: {len(games)} NBA games")
        return [_normalise_oddspapi(g) for g in games if g]
    except Exception as e:
        log.warning(f"OddsPapi error: {e}")
        return []


def _normalise_oddspapi(g: dict) -> dict:
    home = g.get("home_team", "")
    away = g.get("away_team", "")
    start = g.get("commence_time", "")
    ml_home = ml_away = spread = spread_odds_home = spread_odds_away = ou = None
    for bm in g.get("bookmakers", []):
        if bm.get("key", "").lower() != BETANO_KEY:
            continue
        for market in bm.get("markets", []):
            key = market.get("key", "")
            outcomes = market.get("outcomes", [])
            if key == "h2h":
                for o in outcomes:
                    if o["name"] == home:   ml_home = o.get("price")
                    elif o["name"] == away: ml_away = o.get("price")
            elif key == "spreads":
                for o in outcomes:
                    if o["name"] == home:
                        spread = o.get("point"); spread_odds_home = o.get("price")
                    elif o["name"] == away:
                        spread_odds_away = o.get("price")
            elif key == "totals":
                for o in outcomes:
                    if o["name"] == "Over": ou = o.get("point")
    return {
        "home": home, "away": away, "time": start,
        "ml_home_dec": ml_home, "ml_away_dec": ml_away,
        "spread": spread, "spread_odds_home": spread_odds_home,
        "spread_odds_away": spread_odds_away, "over_under": ou,
        "odds_source": "oddspapi_betano", "odds_estimated": False,
    }


# ── TIER 2: The-Odds-API (best available EU bookmaker) ────────────────────────
def _theodds_nba_odds(api_key: str) -> list[dict]:
    """
    Fetch NBA odds from The-Odds-API using best available EU bookmaker.
    Free tier: 500 requests/month. Each call uses ~1 request.
    """
    url = f"{THEODDS_BASE}/sports/{NBA_SPORT_KEY}/odds"
    params = {
        "apiKey":     api_key,
        "regions":    "eu",
        "markets":    "h2h,spreads,totals",
        "oddsFormat": "decimal",
        "bookmakers": ",".join(EU_BOOKMAKERS),
    }
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        games = resp.json()
        remaining = resp.headers.get("x-requests-remaining", "?")
        log.info(f"The-Odds-API: {len(games)} NBA games | requests remaining: {remaining}")
        if not games:
            return []
        return [_normalise_theodds(g) for g in games if g]
    except Exception as e:
        log.warning(f"The-Odds-API error: {e}")
        return []


def _normalise_theodds(g: dict) -> dict:
    home = g.get("home_team", "")
    away = g.get("away_team", "")
    start = g.get("commence_time", "")
    ml_home = ml_away = spread = spread_odds_home = spread_odds_away = ou = None
    bookmaker_used = "unknown"

    # Try bookmakers in priority order
    bookmakers = g.get("bookmakers", [])
    bm_map = {b["key"]: b for b in bookmakers}
    selected_bm = None
    for key in EU_BOOKMAKERS:
        if key in bm_map:
            selected_bm = bm_map[key]
            bookmaker_used = key
            break
    if not selected_bm and bookmakers:
        selected_bm = bookmakers[0]
        bookmaker_used = selected_bm.get("key", "unknown")

    if selected_bm:
        for market in selected_bm.get("markets", []):
            key = market.get("key", "")
            outcomes = market.get("outcomes", [])
            if key == "h2h":
                for o in outcomes:
                    if o["name"] == home:   ml_home = o.get("price")
                    elif o["name"] == away: ml_away = o.get("price")
            elif key == "spreads":
                for o in outcomes:
                    if o["name"] == home:
                        spread = o.get("point"); spread_odds_home = o.get("price")
                    elif o["name"] == away:
                        spread_odds_away = o.get("price")
            elif key == "totals":
                for o in outcomes:
                    if o["name"] == "Over": ou = o.get("point")

    return {
        "home": home, "away": away, "time": start,
        "ml_home_dec": ml_home, "ml_away_dec": ml_away,
        "spread": spread, "spread_odds_home": spread_odds_home,
        "spread_odds_away": spread_odds_away, "over_under": ou,
        "odds_source": f"theodds_{bookmaker_used}", "odds_estimated": False,
    }


# ── TIER 3: No odds sentinel ───────────────────────────────────────────────────
NO_ODDS_SENTINEL = [{"odds_source": "no_odds", "odds_estimated": True,
                     "reason": "No odds API available"}]

# Track failure reasons across tiers for diagnostics
_odds_failure_reasons: list[str] = []


# ── Public interface ────────────────────────────────────────────────────────────
def fetch_betano_nba_odds(target_date: date | None = None) -> list[dict]:
    """
    Fetch NBA odds using 3-tier fallback:
      1. OddsPapi (Betano) — if ODDSPAPI_KEY set
      2. The-Odds-API (best EU bookmaker) — if THE_ODDS_API_KEY set
      3. No odds — Scout will analyse games but draft 0 picks
    """
    if target_date is None:
        target_date = date.today()

    # Tier 1: OddsPapi
    oddspapi_key = os.getenv("ODDSPAPI_KEY", "")
    if oddspapi_key:
        games = _oddspapi_nba_odds(oddspapi_key, target_date)
        if games:
            log.info("Odds source: OddsPapi (Betano)")
            return games
        log.warning("OddsPapi returned no games — trying The-Odds-API")

    # Tier 2: The-Odds-API
    theodds_key = os.getenv("THE_ODDS_API_KEY", "")
    if theodds_key:
        games = _theodds_nba_odds(theodds_key)
        if games:
            log.info(f"Odds source: The-Odds-API ({games[0].get('odds_source','?')})")
            return games
        log.warning("The-Odds-API returned no games — no odds available")
    else:
        log.warning("THE_ODDS_API_KEY not set — skipping Tier 2")

    # Tier 3: No odds
    log.warning("No odds available from any source — Scout will report but draft 0 picks")
    return NO_ODDS_SENTINEL


def get_odds_failure_reasons() -> list[str]:
    """Return the failure reasons from the last fetch_betano_nba_odds call."""
    return list(_odds_failure_reasons)


def odds_available(games: list[dict]) -> bool:
    """Returns True if real odds are available (not the no-odds sentinel)."""
    if not games:
        return False
    return not (len(games) == 1 and games[0].get("odds_source") == "no_odds")


def format_odds_for_prompt(games: list[dict]) -> str:
    """Format odds for LLM prompt. Returns clear message if no odds available."""
    if not games:
        return "No odds data available."

    if not odds_available(games):
        return (
            "NO LIVE ODDS AVAILABLE — Both OddsPapi and The-Odds-API are unavailable.\n"
            "INSTRUCTION: Produce the full per-game scouting report as normal, "
            "but output draft_picks: [] — do NOT invent or estimate odds. "
            "Note in your scout_report that picks were deferred due to no live odds."
        )

    lines = [f"Source: {games[0].get('odds_source', 'unknown')}"]
    for g in games:
        home = g.get("home", "?"); away = g.get("away", "?")
        ml_h = g.get("ml_home_dec", "?"); ml_a = g.get("ml_away_dec", "?")
        sp   = g.get("spread", "N/A"); ou = g.get("over_under", "N/A")
        lines.append(f"{away} @ {home} | ML: {ml_h}/{ml_a} | Spread: {sp} | O/U: {ou}")
    return "\n".join(lines)
