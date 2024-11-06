from .deck import Deck
from .hand import Hand


class Dealer:
    """
    Represents the dealer in the game.

    hand (Hand): The dealer's hand of cards.
    """

    def __init__(self) -> None:
        """
        Initializes the dealer with an empty hand.
        """
        self.hand = Hand()

    def draw_initial_cards(self, deck: Deck) -> None:
        """
        Draws two initial cards for the dealer from the game deck.

        Args:
            deck (Deck): The game deck to draw cards from.
        """
        initial_cards = [deck.deal_card() for _ in range(2)]
        self.hand.add_initial_cards(initial_cards)

    def hit(self, deck: Deck) -> None:
        """
        Draws a card from the game deck and adds it to the dealer's hand.

        Args:
            deck (Deck): The game deck to draw a card from.
        """
        card = deck.deal_card()
        self.hand.add_card(card)

    def play_turn(self, deck: "Deck") -> None:
        """Plays the dealer's turn according to the game rules."""
        score = self.hand.calculate_score()
        if score == 21:
            print(f"The dealer has blackjack!")
        while score < 17:
            if score >= 17:
                break
            self.hit(deck)
            score = self.hand.calculate_score()

    def reset_hand(self) -> None:
        """
        Clears the dealer's hand for a new round.
        """
        self.hand.clear()
