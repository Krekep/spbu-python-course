from .card import Card
from .hand import Hand
from .deck import Deck
from decimal import Decimal, ROUND_HALF_UP


class Bot:
    """
    Represents a bot in the blackjack game with different strategies and betting capability.

    Attributes:
        hand (Hand): The bot's hand of cards.
        _balance (Decimal): The bot's current balance.
    """

    def __init__(self, initial_balance: Decimal = Decimal("100.00")) -> None:
        """
        Initializes a new bot with an empty hand and initial balance.

        Args:
            initial_balance (float): Starting balance for the bot.
        """
        self.hand = Hand()
        self._balance = initial_balance.quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        self._current_bet = Decimal("0.00")

    def place_bet(self) -> None:
        """Sets a default bet amount for each round."""
        self._current_bet = min(Decimal("10.00"), self._balance)

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
        payout = Decimal("1.5") if blackjack else Decimal("1.0")
        self._balance += (self._current_bet * payout).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )

    def lose_bet(self) -> None:
        """Subtracts the current bet from the balance if the bot loses."""
        self._balance -= self._current_bet.quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )


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
        """Adjusts the bet based on remaining balance to manage risk."""
        if self._current_bet > Decimal("0.00") and self._balance > Decimal("50.00"):
            self._current_bet = min(self._current_bet * Decimal("1.1"), self._balance)
        elif self._current_bet > Decimal("0.00") and self._balance <= Decimal("50.00"):
            self._current_bet = max(
                self._current_bet * Decimal("0.8"), Decimal("10.00")
            )
        elif self._current_bet == Decimal("0.00"):
            self._current_bet = min(Decimal("10.00"), self._balance)
