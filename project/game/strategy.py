import random
from typing import Optional
from project.game.bot import Bot, Bet


class AggressiveStrategy(Bot):
    def place_bet(self) -> Optional[Bet]:
        if self.balance <= 0:
            return None
        # Ставим на случайное число от 0 до 36
        choice = random.randint(0, 36)
        amount = min(self.balance, 10)
        return Bet(amount, "number", choice)

    def play(self):
        bet = self.place_bet()
        if bet:
            print(f"{self.name} ставит {bet.amount} на номер {bet.choice}")
            winning_number = random.randint(0, 36)  # Имитируем результат рулетки
            if winning_number == bet.choice:
                print(f"{self.name} выиграл на номере {winning_number}!")
                self.update_balance(bet.amount * 36)
            else:
                print(f"{self.name} проиграл. Результат: {winning_number}")
                self.update_balance(-bet.amount)


class BasicStrategy(Bot):
    def place_bet(self) -> Optional[Bet]:
        if self.balance <= 0:
            return None
        # Ставим на красное или черное
        choice = random.choice(["red", "black"])
        amount = min(self.balance, 10)
        return Bet(amount, "color", choice)

    def play(self):
        bet = self.place_bet()
        if bet:
            print(f"{self.name} ставит {bet.amount} на {bet.choice}")
            winning_color = random.choice(["red", "black"])
            if winning_color == bet.choice:
                print(f"{self.name} выиграл! Цвет: {winning_color}")
                self.update_balance(bet.amount * 2)
            else:
                print(f"{self.name} проиграл. Цвет: {winning_color}")
                self.update_balance(-bet.amount)


class OptimalStrategy(Bot):
    def place_bet(self) -> Optional[Bet]:
        if self.balance <= 0:
            return None
        # Ставим на дюжину
        choice = random.choice([1, 2, 3])  # 1 - 1-12, 2 - 13-24, 3 - 25-36
        amount = min(self.balance, 10)
        return Bet(amount, "dozen", choice)

    def play(self):
        bet = self.place_bet()
        if bet:
            print(f"{self.name} ставит {bet.amount} на дюжину {bet.choice}")
            winning_number = random.randint(0, 36)
            if (
                (bet.choice == 1 and 1 <= winning_number <= 12)
                or (bet.choice == 2 and 13 <= winning_number <= 24)
                or (bet.choice == 3 and 25 <= winning_number <= 36)
            ):
                print(f"{self.name} выиграл! Номер: {winning_number}")
                self.update_balance(bet.amount * 3)
            else:
                print(f"{self.name} проиграл. Номер: {winning_number}")
                self.update_balance(-bet.amount)
