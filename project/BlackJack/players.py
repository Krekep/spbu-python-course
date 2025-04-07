from abc import ABC, abstractmethod
import project.BlackJack.deck
import project.BlackJack.bot_strategy
from typing import Optional, List


class Player(ABC):
    def __init__(self, name: str, chips: int = 1000) -> None:
        self.name = name
        self.chips = chips
        self.hand: List[project.BlackJack.deck.Card] = [] 
        self.score = 0

    def get_card(self, card: project.BlackJack.deck.Card) -> None: 
        self.hand.append(card)

    def calculate_score(self) -> None:
        self.score = 0
        ace_flag = False
        if self.hand:
            for card in self.hand:
                match card.name:
                    case "A":
                        self.score += 1
                        ace_flag = True
                    case "K" | "Q" | "J" | "10":
                        self.score += 10
                    case _:
                        self.score += int(card.name)
            if ace_flag and self.score <= 11:
                self.score += 10        

    def place_bet(self, amount: int) -> int:
        amount = min(amount, self.chips)
        return amount

    def settle_bet(self, amount: int) -> None:
        self.chips += amount

    @abstractmethod
    def decide_hit(self) -> bool:
        pass



class Bot(Player):
    def __init__(self, strategy: project.BlackJack.bot_strategy.Strategy, name: str, chips: int = 1000) -> None:
        super().__init__(name, chips)
        self.strategy = strategy

    def decide_hit(self) -> bool:
        return self.strategy.decide_hit(self.score)
    



class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer", 2**63-1)
        self.hide_card: Optional[project.BlackJack.deck.Card] = None
    def decide_hit(self) -> bool:
        raise AttributeError(f"The logic of the dealer's game is defined in the Game class")

    

    

    










    

