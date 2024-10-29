import random
from typing import Optional, Any
from project.game.players import Bot, Bet, Croupier


class AggressiveStrategy(Bot):
    def place_bet(self) -> Optional[Bet]:
        if self.balance <= 0:
            return None
        choice = random.randint(0, 36)
        amount = min(self.balance, 10)
        return Bet(amount, "number", choice)

    def play(self, croupier: Croupier) -> None:
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
    def place_bet(self) -> Optional[Bet]:
        if self.balance <= 0:
            return None
        choice = random.choice(["red", "black"])
        amount = min(self.balance, 10)
        return Bet(amount, "color", choice)

    def play(self, croupier: Croupier) -> None:
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
    def place_bet(self) -> Optional[Bet]:
        if self.balance <= 0:
            return None
        choice = random.choice([1, 2, 3])  # 1 - 1-12, 2 - 13-24, 3 - 25-36
        amount = min(self.balance, 10)
        return Bet(amount, "dozen", choice)

    def play(self, croupier: Croupier) -> None:
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
