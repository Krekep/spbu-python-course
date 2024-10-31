from .card import Card
from .hand import Hand
from .deck import Deck


class Bot:
    """
    Represents a bot in the blackjack game with different strategies and betting capability.

    Attributes:
        hand (Hand): The bot's hand of cards.
        balance (float): The bot's current balance.
    """

    def __init__(self, initial_balance: float = 100.0) -> None:
        """
        Initializes a new bot with an empty hand and initial balance.

        Args:
            initial_balance (float): Starting balance for the bot.
        """
        self.hand = Hand()
        self.balance = initial_balance
        self.current_bet = 0.0

    def place_bet(self) -> None:
        """Sets a default bet amount for each round."""
        self.current_bet = min(10.0, self.balance)

    def decide_action(self, dealer_card: Card, deck: Deck) -> None:
        """
        Decides the action for the bot based on its strategy.

        Args:
            dealer_card (Card): The dealer's visible card.
            deck (Deck): The game deck to draw cards from.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")

    def reset_hand(self) -> None:
        """Clears the bot's hand for a new round."""
        self.hand.clear()

    def hit(self, deck: Deck) -> None:
        """
        Draws a card from the game deck and adds it to the bot's hand.

        Args:
            deck (Deck): The game deck to draw a card from.
        """
        card = deck.deal_card()
        self.hand.add_card(card)

    def win_bet(self, blackjack: bool = False) -> None:
        """
        Updates the balance based on the result of the round.

        Args:
            blackjack (bool): True if the bot won with a blackjack, applying a higher payout.
        """
        payout = 1.5 if blackjack else 1.0
        self.balance += self.current_bet * payout

    def lose_bet(self) -> None:
        """Subtracts the current bet from the balance if the bot loses."""
        self.balance -= self.current_bet


class CautiousBot(Bot):
    """A bot with a cautious strategy."""

    def decide_action(self, dealer_card: Card, deck: Deck) -> None:
        score = self.hand.calculate_score()
        while score < 17:
            self.hit(deck)
            score = self.hand.calculate_score()


class ThoughtfulBot(Bot):
    """A bot with a thoughtful strategy, considering dealer's visible card."""

    def decide_action(self, dealer_card: Card, deck: Deck) -> None:
        score = self.hand.calculate_score()
        if score < 17 or (score == 17 and dealer_card.value in ["10", "A"]):
            self.hit(deck)


class StrategicBot(Bot):
    """
    A bot with a dynamic strategy that adjusts based on previous round outcomes.

    This bot will increase its bet after a win and reduce it after a loss, trying to maximize
    its balance over the game.
    """

    def decide_action(self, dealer_card: Card, deck: Deck) -> None:
        score = self.hand.calculate_score()
        while score < 18:
            self.hit(deck)
            score = self.hand.calculate_score()

    def place_bet(self) -> None:
        """Adjusts the bet based on previous round's result to manage risk."""
        if self.current_bet > 0 and self.balance > 50:
            self.current_bet = min(self.current_bet * 1.1, self.balance)
        if self.current_bet > 0 and self.balance < 50:
            self.current_bet = max(self.current_bet * 0.8, 10)
        if self.current_bet == 0:
            self.current_bet = min(10.0, self.balance)
