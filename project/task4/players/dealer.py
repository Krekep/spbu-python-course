from .player import Player
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.card import Card


class Dealer(Player):
    """
    Dealer player that follows fixed Blackjack rules.
    """

    def __init__(self) -> None:
        """
        Initializes dealer with no chips (house always has funds).
        """
        super().__init__("Dealer", 0)

    def make_decision(self, dealer_up_card: "Card") -> str:
        """
        Dealer always follows fixed rules: hit on soft 17 or less.

        Parameters:
            dealer_up_card : Card (Not used by dealer)

        Returns:
            str: "hit" or "stand" based on dealer rules
        """
        if self.should_hit():
            return "hit"
        else:
            self.is_standing = True
            return "stand"

    def should_hit(self) -> bool:
        """
        Determines if dealer should hit based on Blackjack rules.

        Returns:
            bool: True if dealer should hit, False to stand
        """
        return self.hand.value < 17 or (self.hand.value == 17 and self.hand.aces > 0)

    def make_bet(self) -> bool:
        """
        Dealer doesn't place bets (house role).

        Returns:
            bool: Always True (dealer never fails to "bet")
        """
        return True

    def reveal_hand(self) -> str:
        """
        Returns formatted string showing dealer's full hand.

        Returns:
            str: Dealer's hand description with total value
        """
        return f"Карты дилера: {self.hand} (Сумма: {self.hand.value})"
