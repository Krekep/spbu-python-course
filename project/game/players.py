import random
from typing import Optional


class Croupier:
    """
    The Croupier class simulates the actions of a roulette croupier, including spinning the wheel
    and determining the winning number and color.

    Methods:
        spin_wheel(): Spins the roulette wheel and returns the winning number and color.
        get_color(number: int): Determines the color of the given roulette number.
    """

    def spin_wheel(self) -> tuple[int, str]:
        """
        Spins the roulette wheel and returns a tuple containing the winning number and its corresponding color.

        Returns:
            tuple[int, str]: A tuple containing the winning number and its color.
        """
        winning_number = random.randint(0, 36)
        winning_color = self.get_color(winning_number)
        return winning_number, winning_color

    @staticmethod
    def get_color(number: int) -> str:
        """
        Determines the color of the given roulette number.

        Args:
            number (int): The roulette number.

        Returns:
            str: The color of the number ('green', 'red', or 'black').
        """
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
    """
    The Bet class represents a bet made by a player, including the amount, type, and choice of the bet.

    Attributes:
        amount (int): The amount of the bet.
        bet_type (str): The type of the bet (e.g., 'number', 'color').
        choice (int | str): The choice of the bet (e.g., a specific number or color).

    Methods:
        __init__(amount: int, bet_type: str, choice: int | str): Initializes a new bet.
    """

    def __init__(self, amount: int, bet_type: str, choice: int | str) -> None:
        """
        Initializes a new bet.

        Args:
            amount (int): The amount of the bet.
            bet_type (str): The type of the bet (e.g., 'number', 'color').
            choice (int | str): The choice of the bet (e.g., a specific number or color).
        """
        self.amount = amount
        self.bet_type = bet_type
        self.choice = choice


class Bot:
    """
    The Bot class represents an automated player in the roulette game.

    Attributes:
        name (str): The name of the bot.
        balance (int): The initial balance of the bot.

    Methods:
        __init__(name: str, balance: int): Initializes a new bot.
        place_bet() -> Optional[Bet]: Places a bet. This method should be overridden by subclasses.
        update_balance(amount: int): Updates the bot's balance by a given amount.
        play(croupier: Croupier): Simulates the bot playing a round of roulette. This method should be overridden by subclasses.
    """

    def __init__(self, name: str, balance: int) -> None:
        """
        Initializes a new bot.

        Args:
            name (str): The name of the bot.
            balance (int): The initial balance of the bot.
        """
        self.name = name
        self.balance = balance

    def place_bet(self) -> Optional[Bet]:
        """
        Places a bet. This method should be overridden by subclasses to implement specific betting strategies.

        Returns:
            Optional[Bet]: The bet placed by the bot, or None if no bet is placed.

        Raises:
            NotImplementedError: If the method is not overridden by a subclass.
        """
        raise NotImplementedError("!this method should be overridden by subclasses!")

    def update_balance(self, amount: int) -> None:
        """
        Updates the bot's balance by a given amount.

        Args:
            amount (int): The amount to add to the bot's balance.
        """

        self.balance += amount

    def play(self, croupier: Croupier) -> None:
        """
        Simulates the bot playing a round of roulette. This method should be overridden by subclasses to implement
        specific playing strategies.

        Args:
            croupier (Croupier): The croupier handling the roulette wheel.

        Raises:
            NotImplementedError: If the method is not overridden by a subclass.
        """
        raise NotImplementedError("!this method should be overridden by subclasses!")
