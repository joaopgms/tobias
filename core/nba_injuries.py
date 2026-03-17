"""
core/nba_injuries.py
Official NBA Injury Report fetcher.

Source: https://official.nba.com/nba-injury-report-2025-26-season/
PDFs published at: https://ak-static.cms.nba.com/referee/injury/Injury-Report_YYYY-MM-DD_HH_MMAM/PM.pdf

Teams are legally required to report by:
  - 5pm local time day before (non-B2B games)
  - 1pm local time on game day
  - Updated continuously throughout the day

PDF columns: Game Date | Game Time | Matchup | Team | Player Name | Current Status | Reason
"""

import io
import logging
import requests
from datetime import datetime, timezone, timedelta

log = logging.getLogger(__name__)

PDF_BASE = "https://ak-static.cms.nba.com/referee/injury/Injury-Report_{date}_{time}.pdf"
INDEX_URL = "https://official.nba.com/nba-injury-report-2025-26-season/"

# Time slots published throughout the day (ET)
# We'll try the most recent ones before Scout's 14:00 UTC run
TIME_SLOTS = [
    "06_00PM", "05_45PM", "05_30PM", "05_15PM", "05_00PM",
    "04_45PM", "04_30PM", "04_15PM", "04_00PM", "03_45PM",
    "03_30PM", "03_15PM", "03_00PM", "02_45PM", "02_30PM",
    "02_15PM", "02_00PM", "01_45PM", "01_30PM", "01_15PM",
    "01_00PM", "12_45PM", "12_30PM", "12_15PM", "12_00PM",
    "11_45AM", "11_30AM", "11_15AM", "11_00AM",
    "10_45AM", "10_30AM", "10_15AM", "10_00AM",
]


def _try_pdf_url(date_str: str, time_slot: str) -> bytes | None:
    """Try to fetch a specific PDF. Returns bytes or None."""
    url = PDF_BASE.format(date=date_str, time=time_slot)
    try:
        resp = requests.get(url, timeout=10,
                            headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code == 200 and resp.headers.get("content-type","").startswith("application/pdf"):
            log.info(f"NBA injuries: fetched {url}")
            return resp.content
    except Exception:
        pass
    return None


def _parse_injury_pdf(pdf_bytes: bytes) -> dict:
    """
    Parse the NBA official injury PDF into a dict keyed by team name.
    Returns: {team_name: [{name, status, reason, game_time, matchup}, ...]}
    """
    try:
        import pdfplumber
    except ImportError:
        log.warning("pdfplumber not installed — run: pip install pdfplumber")
        return {}

    injuries = {}
    try:
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if not table:
                    continue
                # Find header row
                headers = [str(h).strip().lower() if h else "" for h in table[0]]
                # Expected: game date, game time, matchup, team, player name, current status, reason
                # Map column indices
                col = {}
                for i, h in enumerate(headers):
                    if "team" in h and "matchup" not in h:  col["team"] = i
                    elif "player" in h:                      col["player"] = i
                    elif "status" in h:                      col["status"] = i
                    elif "reason" in h:                      col["reason"] = i
                    elif "matchup" in h:                     col["matchup"] = i
                    elif "game time" in h or "time" in h:    col["time"] = i

                if "team" not in col or "player" not in col or "status" not in col:
                    log.warning(f"NBA injuries: unexpected PDF columns: {headers}")
                    continue

                for row in table[1:]:
                    if not row or not any(row):
                        continue
                    team   = str(row[col["team"]] or "").strip()
                    player = str(row[col["player"]] or "").strip()
                    status = str(row[col["status"]] or "").strip()
                    reason = str(row.get(col.get("reason", -1), "") or "").strip()

                    if not team or not player or not status:
                        continue
                    # Skip "NOT YET SUBMITTED" rows
                    if "not yet" in status.lower() or "submitted" in status.lower():
                        continue

                    if team not in injuries:
                        injuries[team] = []
                    injuries[team].append({
                        "name":   player,
                        "status": status,
                        "reason": reason,
                        "pos":    "",  # not in NBA official report
                    })

    except Exception as e:
        log.error(f"NBA injuries: PDF parse error: {e}")

    return injuries


def fetch_official_nba_injuries(target_date: datetime | None = None) -> dict:
    """
    Fetch the most recent NBA official injury report PDF for the given date.
    Falls back to ESPN if PDF unavailable.

    Returns dict: {team_name: [{name, status, reason, pos}, ...]}
    """
    if target_date is None:
        target_date = datetime.now(timezone.utc)

    # NBA reports use ET — convert UTC to ET (UTC-4 in March)
    et_offset = timedelta(hours=-4)
    et_time = target_date + et_offset
    date_str = et_time.strftime("%Y-%m-%d")

    log.info(f"NBA injuries: fetching official report for {date_str} (ET)")

    # Try time slots from most recent downward
    # Build list of slots up to current ET time
    current_et_hour = et_time.hour
    current_et_min  = et_time.minute

    for slot in TIME_SLOTS:
        pdf_bytes = _try_pdf_url(date_str, slot)
        if pdf_bytes:
            injuries = _parse_injury_pdf(pdf_bytes)
            if injuries:
                log.info(f"NBA injuries: {sum(len(v) for v in injuries.values())} players across {len(injuries)} teams")
                return injuries
            else:
                log.warning(f"NBA injuries: PDF fetched but no data parsed from slot {slot}")

    log.warning("NBA injuries: no official PDF available — returning empty")
    return {}


def format_injuries_for_prompt(injuries: dict, max_teams: int = 30) -> str:
    """Format official injuries into compact text for LLM prompt."""
    if not injuries:
        return "No injury reports available from NBA official source."

    lines = [f"Source: NBA Official Injury Report ({sum(len(v) for v in injuries.values())} players, {len(injuries)} teams)"]
    priority_statuses = {"Out", "Doubtful", "Questionable", "Game Time Decision", "GTD"}

    for team, players in list(injuries.items())[:max_teams]:
        notable = [p for p in players if any(s.lower() in p["status"].lower()
                   for s in ["out", "doubtful", "questionable", "game time", "gtd"])]
        if notable:
            parts = []
            for p in notable[:5]:
                r = f" ({p['reason']})" if p.get('reason') else ""
                parts.append(f"{p['name']} {p['status']}{r}")
            lines.append(f"{team}: {', '.join(parts)}")

    return "\n".join(lines)
