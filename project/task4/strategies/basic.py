from .strategy import Strategy
from core.hand import Hand
from core.card import Card


class BasicStrategy(Strategy):
    """
    Basic mathematical strategy based on optimal Blackjack play.
    """

    def should_hit(self, player_hand: Hand, dealer_up_card: Card) -> bool:
        """
        Uses mathematical strategy considering soft/hard hands and dealer's card.

        Parameters:
            player_hand : Hand (Player's current hand)
            dealer_up_card : Card (Dealer's visible card)

        Returns:
            bool: True if mathematically optimal to hit, False to stand
        """
        player_value = player_hand.value
        dealer_value = dealer_up_card.value

        # Мягкие руки (с тузом, который считается как 11)
        if player_hand.aces > 0 and player_value <= 21:
            # Мягкие руки: A,2 - A,9
            if player_value <= 17:
                return True
            elif player_value == 18:
                return dealer_value in [9, 10, 11]  # Берем против 9,10,A
            else:
                return False  # 19+ всегда стоим

        # Твердые руки (без туза или туз считается как 1)
        if player_value <= 11:
            return True  # Всегда берем до 11
        elif player_value == 12:
            return dealer_value in [2, 3, 7, 8, 9, 10, 11]  # Стоим только против 4,5,6
        elif 13 <= player_value <= 16:
            return dealer_value in [7, 8, 9, 10, 11]  # Стоим против 2-6
        else:
            return False  # 17+ всегда стоим
