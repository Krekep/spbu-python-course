from itertools import product
import random


class Card:
    def __init__(self, name: str, suit: str) -> None:
        self.name = name
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.name}{self.suit}"


class Deck:
    def __init__(self) -> None:
        self.count = 0
        self.cards = [Card(card[0], card[1]) for card in product(
                ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"],
                ["♥", "♦", "♣", "♠"]
            )]

    def shuffle(self) -> None:
        random.shuffle(self.cards)
        self.count = 0

    def get_card(self) -> "Card":
        self.count += 1
        return self.cards[self.count - 1]
    