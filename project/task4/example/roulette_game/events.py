from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class BettingEvent:
    """Event emitted when player makes a bet"""

    player_name: str
    bet_type: Any
    bet_value: Any
    amount: int
    player_balance: int


@dataclass
class GameResultEvent:
    """Event emitted after each round with results"""

    round_number: int
    winning_number: int
    winning_color: Any
    player_results: Dict[str, int]
