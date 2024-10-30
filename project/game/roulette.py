from typing import List
from project.game.players import Bot
from project.game.table import RouletteTable


class RouletteGame:
    """
    The RouletteGame class manages the overall roulette game, including multiple bots and game rounds.

    Attributes:
        bots (List[Bot]): A list of bots participating in the game.
        step (int): The current step or round of the game.
        max_steps (int): The maximum number of steps or rounds for the game.

    Methods:
        __init__(bots: List[Bot], max_steps: int = 10) -> None: Initializes the roulette game with the given bots and maximum steps.
        is_game_over() -> bool: Checks if the game is over.
        display_game_state() -> None: Displays the current state of the game.
        find_winner() -> List[Bot]: Finds the winner(s) of the game.
        run_game() -> None: Runs the roulette game until it is over.
    """

    def __init__(self, bots: List[Bot], max_steps: int = 10) -> None:
        """
        Initializes the roulette game with the given bots and maximum steps.

        Args:
            bots (List[Bot]): A list of bots participating in the game.
            max_steps (int): The maximum number of steps or rounds for the game. Default is 10.
        """
        self.bots = bots
        self.step = 0
        self.max_steps = max_steps

    def is_game_over(self) -> bool:
        """
        Checks if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        if self.step >= self.max_steps:
            return True
        for bot in self.bots:
            if bot.balance <= 0:
                return True
        return False

    def display_game_state(self) -> None:
        """
        Displays the current state of the game.
        """
        print(f"Step {self.step}:")
        for bot in self.bots:
            print(f"{bot.name}: Balance = {bot.balance}")
        print()

    def find_winner(self) -> List[Bot]:
        """
        Finds the winner(s) of the game.

        Returns:
            List[Bot]: A list of bots with the highest balance.
        """
        max_balance = max(bot.balance for bot in self.bots)
        return [bot for bot in self.bots if bot.balance == max_balance]

    def run_game(self) -> None:
        """
        Runs the roulette game until it is over.
        """
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
