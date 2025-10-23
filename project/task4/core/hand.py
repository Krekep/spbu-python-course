from typing import List
from .card import Card


class Hand:
    """
    Represents a player's hand of cards in Blackjack.
    """

    def __init__(self) -> None:
        """
        Initializes an empty hand.
        """
        self.cards: List[Card] = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card) -> None:
        """
        Adds a card to the hand and recalculates total value.

        Parameters:
            card : Card (Card to add to the hand)
        """
        self.cards.append(card)
        self.value += card.value

        if card.rank == "A":
            self.aces += 1
        self._adjust_for_ace()

    def _adjust_for_ace(self) -> None:
        """
        Adjusts ace values from 11 to 1 if hand would otherwise bust.
        """
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def clear(self) -> None:
        """
        Clears all cards from the hand and resets values.
        """
        self.cards.clear()
        self.value = 0
        self.aces = 0

    def is_blackjack(self) -> bool:
        """
        Checks if hand is a blackjack (Ace + 10-value card).

        Returns:
            bool: True if hand is blackjack, False otherwise
        """
        return len(self.cards) == 2 and self.value == 21

    def is_busted(self) -> bool:
        """
        Checks if hand value exceeds 21 (bust).

        Returns:
            bool: True if hand value > 21, False otherwise
        """
        return self.value > 21

    def __str__(self) -> str:
        """
        Returns string representation of the hand.

        Returns:
            str: Comma-separated list of cards in the hand
        """
        return ", ".join(str(card) for card in self.cards)
