from .player import Player
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from strategies.strategy import Strategy
    from core.card import Card

import random


class Bot(Player):
    """
    AI player that makes decisions based on assigned strategy.
    """

    def __init__(self, name: str, strategy: "Strategy", chips: int = 1000) -> None:
        """
        Initializes a bot player with strategy.

        Parameters:
            name : str (Bot's name)
            strategy : Strategy (Decision-making strategy)
            chips : int (Starting chip amount, default 1000)
        """
        super().__init__(name, chips)
        self.strategy = strategy

    def make_decision(self, dealer_up_card: "Card") -> str:
        """
        Makes decision based on strategy and current game state.

        Parameters:
            dealer_up_card : Card (Dealer's visible card)

        Returns:
            str: "hit" or "stand" based on strategy decision
        """
        decision = self.strategy.should_hit(self.hand, dealer_up_card)

        if decision and not self.is_standing:
            return "hit"
        else:
            self.is_standing = True
            return "stand"

    def make_bet(self) -> bool:
        """
        Places bet based on bot's betting strategy and chip count.

        Returns:
            bool: True if bet was placed successfully
        """
        # Разные стратегии ставок для разнообразия
        if "Консервативный" in self.name:
            # Консервативно: 5-10% от баланса
            min_bet = max(10, self.chips // 20)
            max_bet = max(20, self.chips // 10)
        elif "Агрессивный" in self.name:
            # Агрессивно: 15-25% от баланса
            min_bet = max(20, self.chips // 7)
            max_bet = max(50, self.chips // 4)
        else:
            # Стандартно: 10-20% от баланса
            min_bet = max(15, self.chips // 10)
            max_bet = max(30, self.chips // 5)

        bet_amount = random.randint(min_bet, max_bet)
        bet_amount = min(bet_amount, self.chips)  # Не больше чем есть

        success = self.place_bet(bet_amount)
        if success:
            print(f"🤖 {self.name} ставит {bet_amount} фишек")
        return success
