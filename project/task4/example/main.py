from project.task4.roulette import (
    Player,
    ConservativeStrategy,
    RiskStrategy,
    MegaRiskStrategy,
    MathematicalStrategy,
    RouletteGame,
)


def main():
    print("=-=-= DEMO GAME 1=-=-=\n")

    bot1 = Player(10000000, 18, ConservativeStrategy(), "Kolya_228_pro_gamer")
    bot2 = Player(10000000, 30, RiskStrategy(), "Mellstroy")
    bot3 = Player(10000000, 28, MegaRiskStrategy(), "Ivan_Zolo")
    bot4 = Player(10000000, 32, MathematicalStrategy(), "Drakula")

    print("Players:")
    print(f"  {bot1._name} (баланс: {bot1.balance})")
    print(f"  {bot2._name} (баланс: {bot2.balance})")
    print(f"  {bot3._name} (баланс: {bot3.balance})")
    print(f"  {bot4._name} (баланс: {bot4.balance})")

    game = RouletteGame([bot1, bot2, bot3, bot4], max_rounds=10)

    print("\n=-=-= START =-=-=\n")

    round_count = 0
    while game.play_round():
        round_count += 1

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
