from .strategy import Strategy
from core.hand import Hand
from core.card import Card

class ConservativeStrategy(Strategy):
    """
    Conservative strategy: rarely hits, stands on relatively low values.
    """
    
    def should_hit(self, player_hand: Hand, dealer_up_card: Card) -> bool:
        """
        Hits only when hand value is very low (below 13).

        Parameters:
            player_hand : Hand (Player's current hand)
            dealer_up_card : Card (Dealer's visible card, not used)

        Returns:
            bool: True if hand value < 13, False otherwise
        """
        return player_hand.value < 13