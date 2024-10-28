from .card import Card
from typing import List


class Bot:
    """
    Represents a bot in the blackjack game with different strategies.

    Attributes:
        cards_on_hand (List[Card]): A list of card instances representing the bot's hand.
        strategy (str): The strategy the bot will follow.
    """

    def __init__(self, strategy: str) -> None:
        """
        Initializes a new bot with an empty hand and a specified strategy.

        Args:
            strategy (str): The strategy the bot will follow.
        """
        self.cards_on_hand: List[Card] = []
        self.strategy = strategy

    def add_card(self, card: Card) -> None:
        """
        Adds a card to the bot.

        Args:
            card (Card): The card to be added to the bot.
        """
        self.cards_on_hand.append(card)

    def calculate_score(self) -> int:
        """
        Calculates the total score of the bot.

        Returns:
            int: The total score of the bot.
        """
        score = 0
        aces = 0

        for card in self.cards_on_hand:
            score += Card.VALUES[card.value]
            if card.value == "A":
                aces += 1

        while score > 21 and aces:
            score -= 10
            aces -= 1

        return score

    def clear_hand(self) -> None:
        """
        Clears the bot's hand for a new round.
        """
        self.cards_on_hand.clear()

    def show_hand(self) -> None:
        """
        Displays the current cards of the bot.
        """
        hand_representation = ", ".join(
            f"{card.value} of {card.suit}" for card in self.cards_on_hand
        )
        print(f"Cards: {hand_representation} | Score: {self.calculate_score()}")

    def decide_action(self, dealer_card: Card) -> str:
        """
        Decides the action for the bot based on its strategy.

        Args:
            dealer_card (Card): The card showing the dealer's hand.

        Returns:
            str: The action decided by the bot ("hit" or "stand").
        """
        score = self.calculate_score()

        if self.strategy == "Cautious":
            return "stand" if score >= 17 else "hit"
        elif self.strategy == "Risky":
            return "hit"
        elif self.strategy == "Thoughtful":
            if score < 17 or (score == 17 and dealer_card.value in ["10", "A"]):
                return "hit"
            return "stand"
        return "stand"
