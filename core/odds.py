"""
core/odds.py
NBA odds fetcher — 2-tier fallback strategy.

Tier 1: The-Odds-API (best available EU bookmaker) — requires THE_ODDS_API_KEY
Tier 2: No odds — Scout produces report but 0 picks
"""

import os
import logging
import requests
from datetime import date, timezone

log = logging.getLogger(__name__)

THEODDS_BASE    = "https://api.the-odds-api.com/v4"

# Preferred EU bookmakers in priority order
EU_BOOKMAKERS   = ["onexbet", "unibet", "unibet_fr", "williamhill", "pinnacle", "betfair_ex_eu", "marathonbet", "betsson"]
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


# ── TIER 1: The-Odds-API (best available EU bookmaker) ────────────────────────
US_BOOKMAKERS = ["draftkings", "fanduel", "betmgm", "caesars"]

def _theodds_nba_odds(api_key: str) -> list[dict]:
    """
    Fetch NBA odds from The-Odds-API.
    EU bookmakers are primary (preferred for odds values).
    US bookmakers fill any missing markets (spread/O/U) and cover games EU skips entirely.
    Both fetches are always made; bookmakers are merged per game before normalization.
    Free tier: 500 requests/month. Each call uses ~1 request (2 calls per run).
    """
    url = f"{THEODDS_BASE}/sports/{NBA_SPORT_KEY}/odds"

    def _fetch_raw(regions: str, bookmakers: list) -> list[dict]:
        params = {
            "apiKey":     api_key,
            "regions":    regions,
            "markets":    "h2h,spreads,totals",
            "oddsFormat": "decimal",
            "bookmakers": ",".join(bookmakers),
        }
        try:
            resp = requests.get(url, params=params, timeout=15)
            resp.raise_for_status()
            games = resp.json()
            remaining = resp.headers.get("x-requests-remaining", "?")
            log.info(f"The-Odds-API ({regions}): {len(games)} NBA games | requests remaining: {remaining}")
            for g in games:
                present = sorted({b["key"] for b in g.get("bookmakers", [])})
                log.debug(f"  {g.get('away_team','?')} @ {g.get('home_team','?')}: bookmakers present = {present}")
            return [g for g in games if g]
        except Exception as e:
            log.warning(f"The-Odds-API ({regions}) error: {e}")
            return []

    eu_raw = _fetch_raw("eu", EU_BOOKMAKERS)
    us_raw = _fetch_raw("us", US_BOOKMAKERS)

    # Merge bookmakers per game: EU first (priority for ML odds values),
    # US appended so per-market fallback can fill spread/O/U if EU lacks them.
    game_map: dict[frozenset, dict] = {}
    for g in eu_raw + us_raw:
        key = frozenset([g.get("home_team", "").lower(), g.get("away_team", "").lower()])
        if key not in game_map:
            merged = dict(g)
            merged["bookmakers"] = list(g.get("bookmakers", []))
            game_map[key] = merged
        else:
            existing_keys = {b["key"] for b in game_map[key]["bookmakers"]}
            for bm in g.get("bookmakers", []):
                if bm["key"] not in existing_keys:
                    game_map[key]["bookmakers"].append(bm)

    return [_normalise_theodds(g) for g in game_map.values()]


def _normalise_theodds(g: dict) -> dict:
    home = g.get("home_team", "")
    away = g.get("away_team", "")
    start = g.get("commence_time", "")
    ml_home = ml_away = spread = spread_odds_home = spread_odds_away = ou = None
    over_odds = under_odds = None
    bookmaker_used = "unknown"
    bookmakers = g.get("bookmakers", [])
    bm_map = {b["key"]: b for b in bookmakers}

    # Per-market bookmaker selection: for each market type use the highest-priority
    # bookmaker that actually has that market. A single bookmaker may have ML but
    # no totals — this ensures O/U can come from a different source if needed.
    def _markets_for(bm: dict) -> dict:
        return {m["key"]: m for m in bm.get("markets", [])}

    # EU first, then US as fallback for missing markets
    all_bm_priority = [bm_map[k] for k in EU_BOOKMAKERS + US_BOOKMAKERS if k in bm_map]
    if not all_bm_priority and bookmakers:
        all_bm_priority = bookmakers  # last resort: whatever was returned

    for bm in all_bm_priority:
        mkts = _markets_for(bm)
        if ml_home is None and "h2h" in mkts:
            for o in mkts["h2h"].get("outcomes", []):
                if o["name"] == home:   ml_home = o.get("price")
                elif o["name"] == away: ml_away = o.get("price")
            if ml_home is not None:
                bookmaker_used = bm.get("key", bookmaker_used)
        if spread is None and "spreads" in mkts:
            for o in mkts["spreads"].get("outcomes", []):
                if o["name"] == home:
                    spread = o.get("point"); spread_odds_home = o.get("price")
                elif o["name"] == away:
                    spread_odds_away = o.get("price")
        if ou is None and "totals" in mkts:
            for o in mkts["totals"].get("outcomes", []):
                if o["name"] == "Over":
                    ou = o.get("point"); over_odds = o.get("price")
                elif o["name"] == "Under":
                    under_odds = o.get("price")
        if ml_home is not None and spread is not None and ou is not None:
            break  # all markets filled

    log.debug(
        f"  {away} @ {home}: ML={bookmaker_used} spread={'yes' if spread else 'NO'} "
        f"ou={'yes' if ou else 'NO'}"
    )

    return {
        "home": home, "away": away, "time": start,
        "ml_home_dec": ml_home, "ml_away_dec": ml_away,
        "spread": spread, "spread_odds_home": spread_odds_home,
        "spread_odds_away": spread_odds_away, "over_under": ou,
        "odds_source": f"theodds_{bookmaker_used}", "odds_estimated": False,
        "over_odds": over_odds, "under_odds": under_odds,
    }


# ── TIER 2: No odds sentinel ───────────────────────────────────────────────────
NO_ODDS_SENTINEL = [{"odds_source": "no_odds", "odds_estimated": True,
                     "reason": "No odds API available"}]

# Track failure reasons across tiers for diagnostics
_odds_failure_reasons: list[str] = []


# ── Public interface ────────────────────────────────────────────────────────────
def fetch_betano_nba_odds(target_date: date | None = None) -> list[dict]:
    """
    Fetch NBA odds using 2-tier fallback:
      1. The-Odds-API (best EU bookmaker) — if THE_ODDS_API_KEY set
      2. No odds — Scout will analyse games but draft 0 picks
    """
    if target_date is None:
        target_date = date.today()

    # Tier 1: The-Odds-API
    theodds_key = os.getenv("THE_ODDS_API_KEY", "")
    if theodds_key:
        games = _theodds_nba_odds(theodds_key)
        if games:
            log.info(f"Odds source: The-Odds-API ({games[0].get('odds_source','?')})")
            return games
        log.warning("The-Odds-API returned no games — no odds available")
    else:
        log.warning("THE_ODDS_API_KEY not set")

    # Tier 2: No odds
    log.warning("No odds available — Scout will report but draft 0 picks")
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
            "NO LIVE ODDS AVAILABLE — The-Odds-API is unavailable.\n"
            "INSTRUCTION: Produce the full per-game scouting report as normal, "
            "but output draft_picks: [] — do NOT invent or estimate odds. "
            "Note in your scout_report that picks were deferred due to no live odds."
        )

    lines = [f"Source: {games[0].get('odds_source', 'unknown')}"]
    for g in games:
        home = g.get("home", "?"); away = g.get("away", "?")
        ml_h = g.get("ml_home_dec", "?"); ml_a = g.get("ml_away_dec", "?")
        sp   = g.get("spread", "N/A"); ou = g.get("over_under", "N/A")
        sp_h = g.get("spread_odds_home", "?"); sp_a = g.get("spread_odds_away", "?")
        ov   = g.get("over_odds", "?");  un = g.get("under_odds", "?")
        spread_str = f"{sp} ({sp_h}/{sp_a})" if sp and sp != "N/A" else "N/A"
        ou_str     = f"{ou} (O:{ov}/U:{un})" if ou and ou != "N/A" else "N/A"
        lines.append(f"{away} @ {home} | ML: {home}:{ml_h} / {away}:{ml_a} | Spread({home}): {spread_str} | O/U: {ou_str}")
    return "\n".join(lines)
