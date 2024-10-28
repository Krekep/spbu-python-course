from .deck import Deck
from .card import Card


class Dealer:
    """
    Represents the dealer in the game.

    Attributes:
        cards_on_hand (list[Card]): The cards held by the dealer.
    """

    def __init__(self) -> None:
        """
        Initializes the dealer with an empty hand.
        """
        self.cards_on_hand: list[Card] = []

    def draw_initial_cards(self, deck: "Deck") -> None:
        """Draws two cards for the dealer from the game deck."""
        for _ in range(2):
            self.hit(deck)

    def hit(self, deck: "Deck") -> None:
        """Draws a card from the game deck and adds it to the dealer's hand."""
        card = deck.deal_card()
        self.cards_on_hand.append(card)

    def calculate_score(self: "Dealer") -> int:
        """
        Calculates the score of the dealer.

        Returns:
            int: The total score of the dealer.
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

    def play_turn(self, deck: "Deck") -> None:
        """Plays the dealer's turn according to the game rules."""
        while self.calculate_score() < 17:
            self.hit(deck)
            if self.calculate_score() == 21:
                break
            if self.calculate_score() > 21:
                print("Dealer busts!")
                break

    def clear_hand(self) -> None:
        """
        Clears the dealer's hand for a new round.
        """
        self.cards_on_hand.clear()

    def show_hand(self) -> None:
        """
        Displays the current cards of the dealer.
        """
        hand_representation = ", ".join(
            f"{card.value} of {card.suit}" for card in self.cards_on_hand
        )
        print(
            f"Dealer's cards: {hand_representation} | Score: {self.calculate_score()}"
        )
