from project.game.strategy import AggressiveStrategy, BasicStrategy, OptimalStrategy
from project.game.roulette import RouletteGame

if __name__ == "__main__":
    bots = [
        AggressiveStrategy("AggressiveBot"),
        BasicStrategy("BasicBot"),
        OptimalStrategy("OptimalBot"),
    ]
    game = RouletteGame(bots, max_steps=10)
    game.run_game()
