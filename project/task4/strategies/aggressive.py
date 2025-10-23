from .strategy import Strategy
from core.hand import Hand
from core.card import Card


class AggressiveStrategy(Strategy):
    """
    Aggressive strategy: frequently hits, takes more risks.
    """

    def should_hit(self, player_hand: Hand, dealer_up_card: Card) -> bool:
        """
        Hits on most hands, even relatively high values against strong dealer cards.

        Parameters:
            player_hand : Hand (Player's current hand)
            dealer_up_card : Card (Dealer's visible card)

        Returns:
            bool: True if should hit based on aggressive criteria
        """
        if player_hand.value < 17:
            return True
        elif player_hand.value == 17 and dealer_up_card.value >= 7:
            return True
        return player_hand.value < 19
