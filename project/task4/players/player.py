from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.hand import Hand
    from core.card import Card


class Player(ABC):
    """
    Abstract base class representing a Blackjack player.
    """

    def __init__(self, name: str, chips: int = 1000) -> None:
        """
        Initializes a player with name and starting chips.

        Parameters:
            name : str (Player's name)
            chips : int (Starting chip amount, default 1000)
        """
        from core.hand import Hand

        self.name = name
        self.hand = Hand()
        self.chips = chips
        self.bet = 0
        self.is_standing = False
        self.has_busted = False

    def place_bet(self, amount: int) -> bool:
        """
        Places a bet from player's chips.

        Parameters:
            amount : int (Amount to bet)

        Returns:
            bool: True if bet was successful, False if insufficient chips
        """
        if 0 < amount <= self.chips:
            self.bet = amount
            self.chips -= amount
            return True
        return False

    @abstractmethod
    def make_bet(self) -> bool:
        """
        Abstract method for placing a bet (implemented in subclasses).

        Returns:
            bool: True if bet was placed successfully
        """
        pass

    @abstractmethod
    def make_decision(self, dealer_up_card: "Card") -> str:
        """
        Abstract method for making game decisions (hit, stand, double).

        Parameters:
            dealer_up_card : Card (Dealer's visible card)

        Returns:
            str: Decision as "hit", "stand", or "double"
        """
        pass

    def win_bet(self) -> None:
        """
        Awards win payout (2:1) to player and resets bet.
        """
        self.chips += self.bet * 2
        self.bet = 0

    def lose_bet(self) -> None:
        """
        Processes lost bet by resetting bet to zero.
        """
        self.bet = 0

    def push(self) -> None:
        """
        Returns bet to player in case of tie.
        """
        self.chips += self.bet
        self.bet = 0

    def blackjack_win(self) -> None:
        """
        Awards blackjack payout (3:2) to player and resets bet.
        """
        self.chips += int(self.bet * 2.5)
        self.bet = 0

    def reset_hand(self) -> None:
        """
        Resets player's hand and game state for new round.
        """
        self.hand.clear()
        self.is_standing = False
        self.has_busted = False

    def __str__(self) -> str:
        """
        Returns string representation of player.

        Returns:
            str: Player name and chip count
        """
        return f"{self.name} (Фишки: {self.chips})"
