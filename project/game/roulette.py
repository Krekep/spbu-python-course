from typing import List
from project.game.bot import Bot


class RouletteGame:
    def __init__(self, bots: List[Bot], max_steps: int = 10) -> None:

        self.bots = bots
        self.step = 0
        self.max_steps = max_steps

    def play_round(self) -> None:
        for bot in self.bots:
            bot.play()
        self.step += 1

    def run_game(self) -> None:
        while not self.is_game_over():
            self.play_round()
            self.display_game_state()
        self.display_winner()

    def is_game_over(self) -> bool:
        if self.step >= self.max_steps:
            return True
        for bot in self.bots:
            if bot.balance <= 0:
                return True
        return False

    def display_game_state(self) -> None:
        print(f"Step {self.step}:")
        for bot in self.bots:
            print(f"{bot.name}: Balance = {bot.balance}")
        print()

    def display_winner(self) -> None:
        winner = max(self.bots, key=lambda bot: bot.balance)
        print(f"Winner is {winner.name} with balance {winner.balance}")
