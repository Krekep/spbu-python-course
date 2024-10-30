import random
from typing import Optional
from project.game.players import Bot, Bet, Croupier


class AggressiveStrategy(Bot):
    """
    The AggressiveStrategy class represents a bot that uses an aggressive betting strategy in the roulette game.
    This strategy involves betting on a specific number.

    Methods:
        place_bet() -> Optional[Bet]: Places a bet on a specific number.
        play(croupier: Croupier) -> None: Simulates the bot playing a round of roulette using the aggressive strategy.
    """

    def place_bet(self) -> Optional[Bet]:
        """
        Places a bet on a specific number.

        Returns:
            Optional[Bet]: The bet placed by the bot, or None if the bot has insufficient balance.
        """
        if self.balance <= 0:
            return None
        choice = random.randint(0, 36)
        amount = min(self.balance, 10)
        return Bet(amount, "number", choice)

    def play(self, croupier: Croupier) -> None:
        """
        Simulates the bot playing a round of roulette using the aggressive strategy.

        Args:
            croupier (Croupier): The croupier handling the roulette wheel.
        """
        bet = self.place_bet()
        if bet:
            print(f"{self.name} bets {bet.amount} on the number {bet.choice}")
            winning_number, _ = croupier.spin_wheel()
            if winning_number == bet.choice:
                print(f"{self.name} won on the number {winning_number}!")
                self.update_balance(bet.amount * 36)
            else:
                print(f"{self.name} lost. Result: {winning_number}")
                self.update_balance(-bet.amount)


class BasicStrategy(Bot):
    """
    The BasicStrategy class represents a bot that uses a basic betting strategy in the roulette game.
    This strategy involves betting on a color (red or black).

    Methods:
        place_bet() -> Optional[Bet]: Places a bet on a color.
        play(croupier: Croupier) -> None: Simulates the bot playing a round of roulette using the basic strategy.
    """

    def place_bet(self) -> Optional[Bet]:
        """
        Places a bet on a color.

        Returns:
            Optional[Bet]: The bet placed by the bot, or None if the bot has insufficient balance.
        """
        if self.balance <= 0:
            return None
        choice = random.choice(["red", "black"])
        amount = min(self.balance, 10)
        return Bet(amount, "color", choice)

    def play(self, croupier: Croupier) -> None:
        """
        Simulates the bot playing a round of roulette using the basic strategy.

        Args:
            croupier (Croupier): The croupier handling the roulette wheel.
        """
        bet = self.place_bet()
        if bet:
            print(f"{self.name} bets {bet.amount} on the color {bet.choice}")
            _, winning_color = croupier.spin_wheel()
            if winning_color == bet.choice:
                print(f"{self.name} won! Colour: {winning_color}")
                self.update_balance(bet.amount * 2)
            else:
                print(f"{self.name} lost. Colour: {winning_color}")
                self.update_balance(-bet.amount)


class OptimalStrategy(Bot):
    """
    The OptimalStrategy class represents a bot that uses an optimal betting strategy in the roulette game.
    This strategy involves betting on a dozen (1-12, 13-24, 25-36).

    Methods:
        place_bet() -> Optional[Bet]: Places a bet on a dozen.
        play(croupier: Croupier) -> None: Simulates the bot playing a round of roulette using the optimal strategy.
    """

    def place_bet(self) -> Optional[Bet]:
        """
        Places a bet on a dozen.

        Returns:
            Optional[Bet]: The bet placed by the bot, or None if the bot has insufficient balance.
        """
        if self.balance <= 0:
            return None
        choice = random.choice([1, 2, 3])  # 1 - 1-12, 2 - 13-24, 3 - 25-36
        amount = min(self.balance, 10)
        return Bet(amount, "dozen", choice)

    def play(self, croupier: Croupier) -> None:
        """
        Simulates the bot playing a round of roulette using the optimal strategy.

        Args:
            croupier (Croupier): The croupier handling the roulette wheel.
        """
        bet = self.place_bet()
        if bet:
            print(f"{self.name} bets {bet.amount} on the dozen {bet.choice}")
            winning_number, _ = croupier.spin_wheel()
            if (
                (bet.choice == 1 and 1 <= winning_number <= 12)
                or (bet.choice == 2 and 13 <= winning_number <= 24)
                or (bet.choice == 3 and 25 <= winning_number <= 36)
            ):
                print(f"{self.name} won on the number {winning_number}")
                self.update_balance(bet.amount * 3)
            else:
                print(f"{self.name} lost. Result: {winning_number}")
                self.update_balance(-bet.amount)
