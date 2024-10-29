from typing import Optional


class Bet:
    def __init__(self, amount: int, bet_type: str, choice: int | str) -> None:
        self.amount = amount
        self.bet_type = bet_type
        self.choice = choice


class Bot:
    def __init__(self, name: str, balance: int = 100) -> None:
        self.name = name
        self.balance = balance

    def place_bet(self) -> Optional[Bet]:
        raise NotImplementedError("!this method should be overridden by subclasses!")

    def update_balance(self, amount: int) -> None:

        self.balance += amount

    def play(self):
        raise NotImplementedError("!this method should be overridden by subclasses!")
