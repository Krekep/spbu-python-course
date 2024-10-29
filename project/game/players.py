import random
from typing import Optional


class Croupier:
    def spin_wheel(self) -> tuple[int, str]:
        winning_number = random.randint(0, 36)
        winning_color = self.get_color(winning_number)
        return winning_number, winning_color

    @staticmethod
    def get_color(number: int) -> str:
        if number == 0:
            return "green"
        elif number % 2 == 0:
            return (
                "red"
                if number
                in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
                else "black"
            )
        else:
            return (
                "black"
                if number
                in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
                else "red"
            )


class Bet:
    def __init__(self, amount: int, bet_type: str, choice: int | str) -> None:
        self.amount = amount
        self.bet_type = bet_type
        self.choice = choice


class Bot:
    def __init__(self, name: str, balance: int) -> None:
        self.name = name
        self.balance = balance

    def place_bet(self) -> Optional[Bet]:
        raise NotImplementedError("!this method should be overridden by subclasses!")

    def update_balance(self, amount: int) -> None:

        self.balance += amount

    def play(self, croupier: Croupier) -> None:
        raise NotImplementedError("!this method should be overridden by subclasses!")
