from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.hand import Hand
    from core.card import Card


class Strategy(ABC):
    """
    Abstract base class for Blackjack decision strategies.
    """

    @abstractmethod
    def should_hit(self, player_hand: "Hand", dealer_up_card: "Card") -> bool:
        """
        Determines whether player should hit based on strategy.

        Parameters:
            player_hand : Hand (Player's current hand)
            dealer_up_card : Card (Dealer's visible card)

        Returns:
            bool: True if player should hit, False to stand
        """
        pass

    def __str__(self) -> str:
        """
        Returns strategy class name as string representation.

        Returns:
            str: Name of the strategy class
        """
        return self.__class__.__name__
