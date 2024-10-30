from project.game.strategy import AggressiveStrategy, BasicStrategy, OptimalStrategy
from project.game.roulette import RouletteGame


def example_game():
    """
    Runs an example roulette game with three bots using different strategies.

    """
    bots = [
        AggressiveStrategy(name="bot_1", balance=100),
        BasicStrategy(name="bot_2", balance=100),
        OptimalStrategy(name="bot_3, balance = 100"),
    ]
    game = RouletteGame(bots, max_steps=10)
    game.run_game()


if __name__ == "__main__":
    """
    The entry point of the script.

    """
    example_game()
