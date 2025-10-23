import random
from typing import List
from .card import Card


class Deck:
    """
    Represents a deck of playing cards, can contain multiple standard decks.
    """

    def __init__(self, num_decks: int = 1) -> None:
        """
        Initializes a deck with specified number of standard decks.

        Parameters:
            num_decks : int (Number of standard 52-card decks to include, default 1)
        """
        self.suits = ["Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦"]
        self.ranks = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11,
        }
        self.cards: List[Card] = []
        self.num_decks = num_decks
        self._build_deck()

    def _build_deck(self) -> None:
        """
        Builds the deck by creating all card combinations for each deck.
        """
        self.cards = []
        for _ in range(self.num_decks):
            for suit in self.suits:
                for rank, value in self.ranks.items():
                    self.cards.append(Card(suit, rank, value))

    def shuffle(self) -> None:
        """
        Shuffles the deck randomly using Fisher-Yates algorithm.
        """
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """
        Deals one card from the top of the deck.

        Returns:
            Card: The top card from the deck

        Note:
            If deck is empty, automatically rebuilds and shuffles a new deck
        """
        if len(self.cards) == 0:
            self._build_deck()
            self.shuffle()
        return self.cards.pop()

    def __len__(self) -> int:
        """
        Returns the number of cards remaining in the deck.

        Returns:
            int: Number of cards in the deck
        """
        return len(self.cards)

    def reset_round_count(self) -> None:
        """
        Resets round counter (for subclasses that track rounds).
        """
        pass
