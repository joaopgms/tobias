"""
core/validators.py
Hard enforcement of required fields on bet and draft pick objects.
A missing field is always a hard error — never silently skip.
"""

BET_REQUIRED = [
    "id", "match", "time", "pick", "odds", "stake", "potential_return",
    "reasoning", "confidence", "anchor_players",
    "result", "returned", "pnl", "settled_at",
]

DRAFT_REQUIRED = [
    "id", "match", "time", "pick", "odds", "stake", "potential_return",
    "confidence", "reasoning", "anchor_players", "drafted_at",
]


class ValidationError(Exception):
    pass


def validate_bet(bet: dict, context: str = "") -> None:
    missing = [f for f in BET_REQUIRED if f not in bet]
    if missing:
        raise ValidationError(
            f"Bet {bet.get('id', '?')} missing fields {missing} [{context}]"
        )


def validate_draft(pick: dict, context: str = "") -> None:
    missing = [f for f in DRAFT_REQUIRED if f not in pick]
    if missing:
        raise ValidationError(
            f"Draft {pick.get('id', '?')} missing fields {missing} [{context}]"
        )


def validate_all_bets(bets: list[dict], context: str = "") -> None:
    for bet in bets:
        validate_bet(bet, context)


def validate_all_drafts(picks: list[dict], context: str = "") -> None:
    for pick in picks:
        validate_draft(pick, context)


def make_empty_bet(bet_id: str) -> dict:
    """Returns a bet object with all required fields set to safe defaults."""
    return {
        "id": bet_id, "match": "", "time": "", "pick": "", "odds": 0.0,
        "stake": 0.0, "potential_return": 0.0, "reasoning": "",
        "confidence": 0, "anchor_players": [],
        "result": None, "returned": None, "pnl": None, "settled_at": None,
    }
