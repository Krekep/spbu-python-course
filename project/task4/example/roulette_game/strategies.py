from abc import ABC, abstractmethod
from random import randint

from project.task4.example.roulette_game.bets import Bet
from project.task4.example.roulette_game.enums import BetType, Color
from project.task4.example.roulette_game.players import BetType, Color


class Strategy(ABC):
    """Abstract base class for betting strategies

    All strategy classes must implement the make_bet method
    """

    def __init__(self):
        self._last_result: bool = True

    @abstractmethod
    def make_bet(self, player_balance: int, game_history: list) -> Bet:
        """Creates a strategy logic.

        Parameters:
            player (Player): Player object containing current game state

        Returns:
            Bet: Bet object with type, value and amount
        """
        pass

    def update_result(self, won: bool) -> None:
        """Update strategy with result of last bet"""
        self._last_result = won

    def last_result(self) -> bool:
        """Get result of last bet"""
        return self._last_result


class ConservativeStrategy(Strategy):
    """Conservative betting strategy

    This strategy alternates between red and black colors and bets 10% of balance.

    Attributes:
        last_color (str): Last color bet
    """

    def __init__(self):
        super().__init__()
        self.last_color = Color.BLACK

    def make_bet(self, player_balance: int, game_history: list) -> Bet:
        """Makes a conservative bet

        Parameters:
            player (Player): Player object with current balance

        Returns:
            Bet: Color bet
        """
        color = Color.RED if self.last_color == Color.BLACK else Color.BLACK
        self.last_color = color
        amount = max(1, int(player_balance * 0.1))
        return Bet(BetType.COLOR, color, amount)


class RiskStrategy(Strategy):
    """Risky betting strategy

    This strategy selects random numbers (0-36) and bets 10% of balance.
    """

    def make_bet(self, player_balance: int, game_history: list) -> Bet:
        """Makes a risky bet

        Parameters:
            player (Player): Player object with current balance

        Returns:
            Bet: Number bet
        """
        number = randint(0, 36)
        amount = max(1, int(player_balance * 0.1))
        return Bet(BetType.NUMBER, number, amount)


class MegaRiskStrategy(Strategy):
    """Very risky strategy

    This strategy always bets on number zero with 50% of current balance.
    """

    def make_bet(self, player_balance: int, game_history: list) -> Bet:
        """Makes a very risky bet on number zero.

        Parameters:
            player (Player): Player object with current balance

        Returns:
            Bet: Number bet
        """
        amount = max(1, int(player_balance * 0.5))
        return Bet(BetType.NUMBER, 0, amount)


class MathematicalStrategy(Strategy):
    """Mathematical strategy Martingale

    This strategy doubles the bet after losses and resets after wins.
    Bets on alternating colors.

    Attributes:
        last_bet_amount (int): Amount of last bet
        last_color (str): Last color bet
        consecutive_losses (int): Number of consecutive losses
    """

    def __init__(self):
        super().__init__()
        self.last_bet_amount = 1
        self.last_color = Color.RED
        self.consecutive_losses = 0
        self._previous_bet_amount = 1

    def make_bet(self, player_balance: int, game_history: list) -> Bet:
        """Makes bet using Martingale

        Parameters:
            player (Player): Player object with current balance

        Returns:
            Bet: Color bet
        """
        self.last_color = Color.BLACK if self.last_color == Color.RED else Color.RED

        new_bet_amount = 1 * (2**self.consecutive_losses)
        new_bet_amount = min(new_bet_amount, player_balance)
        if new_bet_amount == 0 and player_balance > 0:
            new_bet_amount = 1

        self.last_bet_amount = new_bet_amount
        return Bet(BetType.COLOR, self.last_color, new_bet_amount)

    def update_result(self, won: bool) -> None:
        """Updates strategy with result of last bet.

        Parameters:
            won (bool): True if last bet won, else False
        """
        super().update_result(won)
        if won:
            self.consecutive_losses = 0
        else:
            self.consecutive_losses += 1

    @property
    def previous_bet_amount(self) -> int:
        return self.last_bet_amount
