"""
core/odds.py
Betano NBA odds fetcher.

Primary:  OddsPapi free tier (oddspapi.io) — Betano among 348 bookmakers, no credit card.
Fallback: DuckDuckGo search for Betano odds when OddsPapi is unavailable.
"""

import os
import re
import logging
import requests
from datetime import date, datetime, timezone
from duckduckgo_search import DDGS

log = logging.getLogger(__name__)

ODDSPAPI_BASE = "https://api.oddspapi.com"
BETANO_KEY    = "betano"   # OddsPapi bookmaker key for Betano


# ── American → decimal conversion ─────────────────────────────────────────────

def american_to_decimal(ml) -> float | None:
    if ml is None:
        return None
    try:
        ml = int(ml)
        return round(ml / 100 + 1, 2) if ml > 0 else round(100 / abs(ml) + 1, 2)
    except (ValueError, ZeroDivisionError):
        return None


# ── OddsPapi primary ───────────────────────────────────────────────────────────

def _oddspapi_nba_odds(api_key: str, target_date: date) -> list[dict]:
    """
    Fetch NBA odds from OddsPapi for a given date.
    Returns list of normalised game dicts.
    """
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
        log.info(f"OddsPapi: {len(games)} NBA games for {target_date}")
        return [_normalise_oddspapi(g) for g in games if g]
    except Exception as e:
        log.warning(f"OddsPapi error: {e}")
        return []


def _normalise_oddspapi(g: dict) -> dict:
    """Normalise an OddsPapi game object into Tobias game format."""
    home = g.get("home_team", "")
    away = g.get("away_team", "")
    start = g.get("commence_time", "")

    # Extract Betano odds from bookmakers list
    ml_home = ml_away = spread = spread_odds_home = spread_odds_away = ou = None
    for bm in g.get("bookmakers", []):
        if bm.get("key", "").lower() != BETANO_KEY:
            continue
        for market in bm.get("markets", []):
            key = market.get("key", "")
            outcomes = market.get("outcomes", [])
            if key == "h2h":
                for o in outcomes:
                    if o["name"] == home:
                        ml_home = o.get("price")
                    elif o["name"] == away:
                        ml_away = o.get("price")
            elif key == "spreads":
                for o in outcomes:
                    if o["name"] == home:
                        spread          = o.get("point")
                        spread_odds_home = o.get("price")
                    elif o["name"] == away:
                        spread_odds_away = o.get("price")
            elif key == "totals":
                for o in outcomes:
                    if o["name"] == "Over":
                        ou = o.get("point")

    return {
        "home":             home,
        "away":             away,
        "time":             start,
        "ml_home_dec":      ml_home,
        "ml_away_dec":      ml_away,
        "spread":           spread,
        "spread_odds_home": spread_odds_home,
        "spread_odds_away": spread_odds_away,
        "over_under":       ou,
        "odds_source":      "oddspapi_betano",
        "odds_estimated":   False,
    }


# ── DuckDuckGo fallback ────────────────────────────────────────────────────────

def _ddg_betano_odds(target_date: date) -> list[dict]:
    """
    Fallback: search DuckDuckGo for Betano NBA odds.
    Returns a best-effort list — odds may be incomplete or estimated.
    """
    date_str = target_date.strftime("%B %d %Y")
    queries = [
        f"Betano NBA odds {date_str} moneyline",
        f"NBA odds tonight {date_str} Betano basketball",
    ]
    results_text = []
    with DDGS() as ddgs:
        for q in queries:
            try:
                hits = list(ddgs.text(q, max_results=5))
                for h in hits:
                    results_text.append(h.get("body", ""))
            except Exception as e:
                log.warning(f"DDG search error ({q}): {e}")

    combined = "\n".join(results_text)
    log.info(f"DDG fallback: fetched {len(results_text)} snippets for odds")

    # Return raw text for the LLM agents to parse — they handle this well
    return [{"raw_search_text": combined, "odds_source": "ddg_fallback", "odds_estimated": True}]


# ── Public interface ───────────────────────────────────────────────────────────

def fetch_betano_nba_odds(target_date: date | None = None) -> list[dict]:
    """
    Fetch today's (or target_date's) NBA Betano odds.
    Primary: OddsPapi. Fallback: DuckDuckGo search.

    Returns list of game dicts. Each has at minimum:
      home, away, time, ml_home_dec, ml_away_dec, odds_source, odds_estimated
    """
    if target_date is None:
        target_date = date.today()

    api_key = os.getenv("ODDSPAPI_KEY", "")
    if api_key:
        games = _oddspapi_nba_odds(api_key, target_date)
        if games:
            return games
        log.warning("OddsPapi returned no games — falling back to DDG")
    else:
        log.warning("ODDSPAPI_KEY not set — skipping primary, using DDG fallback")

    return _ddg_betano_odds(target_date)


def format_odds_for_prompt(games: list[dict]) -> str:
    """
    Format odds list into compact text for LLM prompts.
    Token-efficient: ~40 chars per game instead of raw JSON.
    """
    if not games:
        return "No odds data available."

    # If fallback raw text, return it directly
    if len(games) == 1 and "raw_search_text" in games[0]:
        return f"[DDG fallback odds]\n{games[0]['raw_search_text'][:3000]}"

    lines = [f"Source: {games[0].get('odds_source', 'unknown')}"]
    for g in games:
        home = g.get("home", "?")
        away = g.get("away", "?")
        ml_h = g.get("ml_home_dec", "?")
        ml_a = g.get("ml_away_dec", "?")
        sp   = g.get("spread", "N/A")
        ou   = g.get("over_under", "N/A")
        est  = " [est]" if g.get("odds_estimated") else ""
        lines.append(
            f"{away} @ {home}{est} | ML: {ml_h}/{ml_a} | Spread: {sp} | O/U: {ou}"
        )
    return "\n".join(lines)
