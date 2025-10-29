from typing import Any

from project.task4.example.roulette_game.enums import (
    BetType,
    Color,
    EvenOdd,
    Dozen,
    Half,
)


class Bet:
    """Class a bet in roulette.

    Parameters:
        bet_type (str): Type of bet ('number', 'color', 'even_odd', 'dozen', 'column', 'half')
        bet_value (Any): Value of the bet
        amount (int): Amount of the bet

    Raises:
        ValueError: If bet type or value is invalid

    Attributes:
        bet_type (str): Type of bet
        bet_value (Any): Bet value
        amount (int): Bet amount
    """

    def __init__(self, type_bet: BetType, bet_value: Any, sum_bet: int):
        self.type_bet = type_bet
        self.bet_value = bet_value
        self.sum_bet = sum_bet
        self._validate_bet()

    def _validate_bet(self) -> None:
        """Validates bet type and value"""
        if not isinstance(self.type_bet, BetType):
            raise ValueError(f"Invalid bet type: {self.type_bet}")

        if self.type_bet == BetType.NUMBER and self.bet_value not in range(37):
            raise ValueError("Number must be 0-36")
        elif self.type_bet == BetType.COLOR and not isinstance(self.bet_value, Color):
            raise ValueError("Color must be Color.RED or Color.BLACK")
        elif self.type_bet == BetType.EVEN_ODD and not isinstance(
            self.bet_value, EvenOdd
        ):
            raise ValueError("Even/Odd must be EvenOdd.EVEN or EvenOdd.ODD")
        elif self.type_bet == BetType.DOZEN and not isinstance(self.bet_value, Dozen):
            raise ValueError("Dozen must be Dozen.FIRST, Dozen.SECOND or Dozen.THIRD")
        elif self.type_bet == BetType.COLUMN and self.bet_value not in [1, 2, 3]:
            raise ValueError("Column must be 1, 2 or 3")
        elif self.type_bet == BetType.HALF and not isinstance(self.bet_value, Half):
            raise ValueError("Half must be Half.FIRST_18 or Half.LAST_18")
