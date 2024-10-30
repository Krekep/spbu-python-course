from typing import List
from project.game.players import Bot
from project.game.table import RouletteTable


class RouletteGame:
    def __init__(self, bots: List[Bot], max_steps: int = 10) -> None:

        self.bots = bots
        self.step = 0
        self.max_steps = max_steps

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

    def find_winner(self) -> List[Bot]:
        max_balance = max(bot.balance for bot in self.bots)
        return [bot for bot in self.bots if bot.balance == max_balance]

    def run_game(self) -> None:
        while not self.is_game_over():
            print(f"Round {self.step + 1}:")
            for bot in self.bots:
                if bot.balance > 0:
                    table = RouletteTable()
                    table.play_game(bot)
            self.step += 1
            self.display_game_state()
        winners = self.find_winner()
        if winners:
            winner_names = ", ".join(winner.name for winner in winners)
            print(f"Winner(s): {winner_names} with balance: {winners[0].balance}")
        else:
            print("All the players have lost!")
