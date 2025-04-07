from abc import ABC, abstractmethod
import project.BlackJack.deck


class Strategy(ABC):
    """
    Base class for different playing strategies.
    """
    @abstractmethod
    def decide_hit(self, score: int) -> bool:
        pass


class AccurateStrategy(Strategy):
    """
    Strategy where the player hits if the hand value is less than 14.
    """
    def decide_hit(self, score: int) -> bool:
        return score < 14


class AggressiveStrategy(Strategy):
    """
    Strategy where the player hits if the hand value is less than 17.
    """
    def decide_hit(self, score: int) -> bool:
        return score < 17


class CountingStrategy(Strategy):
    """
    Strategy that uses card counting to decide whether to hit.

    Attributes:
        count (int): The count value that tracks the advantage in the deck.
    """
    def __init__(self) -> None:
        self.count: int = 0

    def update_count(self, card: project.BlackJack.deck.Card) -> None:
        """
        Updates the count based on the card dealt.

        Args:
            card (Card): The card to update the count with.
        """
        if card.name in ["2", "3", "4", "5", "6"]:
            self.count += 1
        elif card.name in ["10", "J", "Q", "K", "A"]:
            self.count -= 1

    def decide_hit(self, score: int) -> bool:
        if self.count > 2:
            return score < 19
        elif self.count < -2:
            return score < 16
        else:
            return score < 17
        
    