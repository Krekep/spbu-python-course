from typing import List

from project.task4.example.roulette_game.bets import Bet


class Player:
    """Class representing a player in the roulette game.

    Parameters:
        balance (int): Player balance
        age (int): Player age (must be 18 or older)
        strategy (Strategy): Strategy object
        name (str): Player name, default "Unknown"

    Raises:
        ValueError: If age is less than 18

    Attributes:
        _name (str): Player name
        balance (int): Current player balance
        _age (int): Player age
        strategy (Strategy): Betting strategy
        current_bets (List[Bet]): List of current active bets
    """

    def __init__(self, balance: int, age: int, strategy, name: str = "Unknown"):
        if age < 18:
            raise ValueError("Player must be over 18 years old")
        self._name = name
        self.balance = balance
        self._age = age
        self.strategy = strategy
        self.current_bets: List[Bet] = []
