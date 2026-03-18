"""
core/nba_injuries.py
Official NBA Injury Report fetcher.

Source: https://official.nba.com/nba-injury-report-2025-26-season/
PDFs: https://ak-static.cms.nba.com/referee/injury/Injury-Report_YYYY-MM-DD_HH_MMam/pm.pdf
Updated every 15 minutes throughout game day.

PDF column layout (x positions, approximate):
  x~24:  Game Date
  x~121: Game Time
  x~201: Matchup
  x~265: Team Name
  x~426: Player Name  (Last, First format)
  x~587: Status
  x~667: Reason
"""

import io
import logging
import requests
from datetime import datetime, timezone, timedelta

log = logging.getLogger(__name__)

PDF_BASE = "https://ak-static.cms.nba.com/referee/injury/Injury-Report_{date}_{time}.pdf"

TIME_SLOTS = [
    "06_00PM","05_45PM","05_30PM","05_15PM","05_00PM",
    "04_45PM","04_30PM","04_15PM","04_00PM","03_45PM",
    "03_30PM","03_15PM","03_00PM","02_45PM","02_30PM",
    "02_15PM","02_00PM","01_45PM","01_30PM","01_15PM",
    "01_00PM","12_45PM","12_30PM","12_15PM","12_00PM",
    "11_45AM","11_30AM","11_15AM","11_00AM",
    "10_45AM","10_30AM","10_15AM","10_00AM",
]

# Column x-position boundaries
COL_TEAM   = (240, 420)   # team name column
COL_PLAYER = (420, 570)   # player name column
COL_STATUS = (570, 650)   # status column
COL_REASON = (650, 900)   # reason column


def _try_pdf_url(date_str: str, time_slot: str) -> bytes | None:
    url = PDF_BASE.format(date=date_str, time=time_slot)
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code == 200 and "pdf" in resp.headers.get("content-type", ""):
            return resp.content
    except Exception:
        pass
    return None


def _words_in_col(words: list, x_min: float, x_max: float) -> list:
    """Return words whose x0 falls within the column range."""
    return [w for w in words if x_min <= w["x0"] < x_max]


def _parse_injury_pdf(pdf_bytes: bytes) -> dict:
    """
    Parse NBA official injury PDF using column-position-aware word extraction.
    Groups words by y-position (row), then assigns each word to a column by x-position.
    """
    try:
        import pdfplumber
    except ImportError:
        log.warning("pdfplumber not installed — pip install pdfplumber")
        return {}

    injuries = {}
    current_team = None

    try:
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
            for page in pdf.pages:
                words = page.extract_words(x_tolerance=1, y_tolerance=3,
                                           keep_blank_chars=True)
                if not words:
                    continue

                # Group words by y-position (same row)
                rows = {}
                for w in words:
                    y = round(w["top"])
                    rows.setdefault(y, []).append(w)

                # Track multi-line reason (some reasons wrap to next line)
                last_player = None
                last_team = None

                for y in sorted(rows.keys()):
                    row_words = rows[y]

                    team_words   = _words_in_col(row_words, *COL_TEAM)
                    player_words = _words_in_col(row_words, *COL_PLAYER)
                    status_words = _words_in_col(row_words, *COL_STATUS)
                    reason_words = _words_in_col(row_words, *COL_REASON)

                    team_text   = " ".join(w["text"] for w in team_words).strip()
                    player_text = " ".join(w["text"] for w in player_words).strip()
                    status_text = " ".join(w["text"] for w in status_words).strip()
                    reason_text = " ".join(w["text"] for w in reason_words).strip()

                    # Update current team if team column has content
                    if team_text and team_text not in ("Team", "NOT YET SUBMITTED"):
                        current_team = team_text

                    # Skip header rows
                    if status_text in ("Current Status", "Status") or player_text == "Player Name":
                        continue

                    # If we have a player + status in this row — it's a data row
                    if player_text and status_text and current_team:
                        # Skip "NOT YET SUBMITTED" rows
                        if "not yet" in player_text.lower() or "not yet" in status_text.lower():
                            continue

                        # Normalise "Last, First" → "First Last"
                        if "," in player_text:
                            parts = player_text.split(",", 1)
                            player_name = f"{parts[1].strip()} {parts[0].strip()}"
                        else:
                            player_name = player_text

                        if current_team not in injuries:
                            injuries[current_team] = []

                        entry = {
                            "name":   player_name,
                            "status": status_text,
                            "reason": reason_text,
                            "pos":    "",
                        }
                        injuries[current_team].append(entry)
                        last_player = entry
                        last_team = current_team

                    elif reason_text and not player_text and not status_text and last_player:
                        # Continuation row — append to last player's reason
                        last_player["reason"] = (last_player["reason"] + " " + reason_text).strip()

    except Exception as e:
        log.error(f"NBA injuries: PDF parse error: {e}")

    # Clean up reason bleed from multi-line PDF rows
    for team, players in injuries.items():
        for p in players:
            reason = p["reason"]
            for marker in ["Injury/Illness - ", "NOT YET SUBMITTED",
                           "G League - Two-Way G League", "G League - On Assignment G League"]:
                idx = reason.find(marker, 5)
                if idx > 0:
                    reason = reason[:idx].strip()
            p["reason"] = reason

    # Remove junk team entries (header artifacts)
    injuries = {k: v for k, v in injuries.items()
                if k not in ("Injury Report:", "Team") and len(v) > 0}

    return injuries


def fetch_official_nba_injuries(target_date: datetime | None = None) -> dict:
    """
    Fetch the most recent NBA official injury report PDF for the given date.
    Returns dict: {team_name: [{name, status, reason, pos}, ...]}
    Returns {} if unavailable — caller should fall back to ESPN.
    """
    if target_date is None:
        target_date = datetime.now(timezone.utc)

    # NBA reports use ET (UTC-4 in March/April)
    et_time = target_date + timedelta(hours=-4)
    date_str = et_time.strftime("%Y-%m-%d")

    log.info(f"NBA injuries: fetching official report for {date_str} ET")

    for slot in TIME_SLOTS:
        pdf_bytes = _try_pdf_url(date_str, slot)
        if not pdf_bytes:
            continue
        result = _parse_injury_pdf(pdf_bytes)
        if result:
            total = sum(len(v) for v in result.values())
            log.info(f"NBA injuries: {total} players across {len(result)} teams (slot {slot})")
            return result
        log.warning(f"NBA injuries: slot {slot} fetched but 0 players parsed — trying next")

    log.warning("NBA injuries: no data from any slot — ESPN fallback will be used")
    return {}


def format_injuries_for_prompt(injuries: dict, tonight_teams: list | None = None) -> str:
    """
    Format official injuries into compact prompt text.
    If tonight_teams is provided, only show injuries for teams playing tonight.
    This prevents hallucination where Scout reasons about players not in tonight's games.
    """
    if not injuries:
        return "No injury reports available from NBA official source."

    NOTABLE = {"out", "doubtful", "questionable", "game time decision"}

    # Filter to tonight's teams only if provided
    if tonight_teams:
        # Normalise for matching — injuries dict may use full names
        tonight_lower = [t.lower() for t in tonight_teams]
        injuries = {
            team: players for team, players in injuries.items()
            if any(t in team.lower() or team.lower() in t for t in tonight_lower)
        }

    if not injuries:
        return "No injury reports for tonight\'s teams."

    lines = [f"Source: NBA Official Injury Report ({len(injuries)} teams playing tonight)"]

    for team, players in injuries.items():
        notable = [p for p in players if p["status"].lower() in NOTABLE]
        if notable:
            parts = []
            for p in notable[:6]:
                r = f" ({p['reason']})" if p.get("reason") else ""
                parts.append(f"{p['name']} {p['status']}{r}")
            lines.append(f"{team}: {', '.join(parts)}")

    return "\n".join(lines) if len(lines) > 1 else "No notable injuries reported."
