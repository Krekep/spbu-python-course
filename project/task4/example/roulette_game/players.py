from typing import List, Optional

from project.task4.example.roulette_game.bets import Bet


class Player:
    """Class representing a player in the roulette game.

    Parameters:
        balance (int): Player balance
        age (int): Player age (must be 18 or older)
        strategy (Strategy): Strategy object
        name (str): Player name, default "Unknown"

    Raises:
        ValueError: If age is less than 18

    Attributes:
        _name (str): Player name
        balance (int): Current player balance
        _age (int): Player age
        strategy (Strategy): Betting strategy
        current_bets (List[Bet]): List of current active bets
    """

    def __init__(self, balance: int, age: int, strategy, name: str = "Unknown"):
        if age < 18:
            raise ValueError("Player must be over 18 years old")
        self._name = name
        self.balance = balance
        self._age = age
        self.strategy = strategy
        self.current_bets: List[Bet] = []
        self._game_history: List[dict] = []

    def make_bet(self) -> Optional[Bet]:
        """Player makes a bet using their strategy"""
        if self.balance <= 0:
            return None

        bet = self.strategy.make_bet(self.balance, self._game_history)

        if bet.sum_bet > self.balance:
            bet.sum_bet = self.balance

        self.balance -= bet.sum_bet
        self.current_bets.append(bet)
        return bet

    def process_result(self, won: bool, winnings: int) -> None:
        """Process the result of a bet"""
        self.balance += winnings
        self.current_bets.clear()
        self.strategy.update_result(won)

    def update_game_history(self, game_history: List[dict]) -> None:
        """Update player's copy of game history"""
        self._game_history = game_history.copy()

    @property
    def is_active(self) -> bool:
        """Check if player can still play"""
        return self.balance > 0

    @property
    def name(self) -> str:
        """Get player name"""
        return self._name
