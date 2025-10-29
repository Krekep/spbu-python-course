"""
Demo game 2
"""

from random import randint

from project.task4.example.roulette_game.game import RouletteGame
from project.task4.example.roulette_game.players import Player
from project.task4.example.roulette_game.strategies import (
    ConservativeStrategy,
    RiskStrategy,
    MathematicalStrategy,
)


def main():
    """Main function demonstrating roulette game with the same balance

    Creates 4 bots with different strategies (without MegaRiskStrategy)
    """
    print("=-=-= DEMO GAME 1=-=-=\n")

    # Create bots
    bot1 = Player(
        randint(0, 100000000), 99, ConservativeStrategy(), "Kolya_228_pro_gamer"
    )
    bot2 = Player(randint(0, 100000000), 26, RiskStrategy(), "Mellstroy")
    bot3 = Player(randint(0, 100000000), 457, MathematicalStrategy(), "Drakula")

    # Display initial player information
    print("Players:")
    print(f"  {bot1._name} (balance: {bot1.balance})")
    print(f"  {bot2._name} (balance: {bot2.balance})")
    print(f"  {bot3._name} (balance: {bot3.balance})")

    # Initialize the game with 10 rounds or less
    game = RouletteGame([bot1, bot2, bot3], max_rounds=10)

    # Play rounds until game ends
    print("\n=-=-= START =-=-=\n")

    round_count = 0
    while game.play_round():
        round_count += 1
        game.show_game_state()

    print(f"\n=-=-= Game over after {round_count} rounds =-=-=")
    print("Final balance:")
    for player in game.players:
        status = "Dropped out" if player.balance <= 0 else "In game"
        print(f"  {player._name}: {player.balance} ({status})")

    active_players = [p for p in game.players if p.balance > 0]
    if active_players:
        winner = max(active_players, key=lambda p: p.balance)
        print(f"\n Winner: {winner._name} with balance {winner.balance}!")
    else:
        print("\n All players were dropped out!")


if __name__ == "__main__":
    main()
