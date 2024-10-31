from .card import Card
from typing import List


class Hand:
    """
    Represents a hand of cards for a player or dealer in a blackjack game.

    Attributes:
        cards (List[Card]): A list of card instances representing the hand.
    """

    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Adds a card to the hand.

        Args:
            card (Card): The card to be added.
        """
        self.cards.append(card)

    def add_initial_cards(self, cards: List[Card]) -> None:
        """
        Adds an initial set of cards to the hand.

        Args:
            cards (List[Card]): A list of cards to add.
        """
        self.cards.extend(cards)

    def calculate_score(self) -> int:
        """
        Calculates the total score of the hand.

        Returns:
            int: The total score of the hand.
        """
        score = 0
        aces = 0

        for card in self.cards:
            score += card.points
            if card.value == "A":
                aces += 1

        while score > 21 and aces:
            score -= 10
            aces -= 1

        return score

    def clear(self) -> None:
        """
        Clears the hand for a new round.
        """
        self.cards.clear()

    def show(self) -> None:
        """
        Displays the current cards in the hand.
        """
        hand_representation = ", ".join(
            f"{card.value} of {card.suit}" for card in self.cards
        )
        print(f"Cards: {hand_representation} | Score: {self.calculate_score()}")
