import random
from .card import Card


class Deck:
    """
    Represents a deck of cards for a blackjack game.

    Attributes:
        cards (list[Card]): A list of card instances representing the deck.
    """

    def __init__(self) -> None:
        """
        Initializes a new deck of cards, creating 52 standard cards.
        """
        self.cards: list[Card] = []
        self._create_deck()

    def _create_deck(self) -> None:
        """
        Creates a standard deck of 52 cards.
        """
        for suit in Card.SUITS:
            for value in Card.VALUES.keys():
                self.cards.append(Card(suit, value))

    def shuffle(self) -> None:
        """
        Shuffles the deck of cards in place.
        """
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """
        Deals a single card from the deck.

        Returns:
            Card: The card that was dealt.

        Raises:
            IndexError: If there are no cards left to deal.
        """
        if not self.cards:
            raise IndexError("No cards left in the deck to deal")
        return self.cards.pop()
