"""
Example of gameplay
"""

from game import Game

def run_example():
    print('Пример игры:')
    game = Game()
    game.play_game(max_rounds = 100) # in this example game will finish only then one of bots lose

if __name__ == "__main__":
    run_example()
