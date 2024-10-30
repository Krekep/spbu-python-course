import pytest
from project.game.strategy import AggressiveStrategy, BasicStrategy, OptimalStrategy
from project.game.roulette import RouletteGame
from project.game.players import Bot, Bet, Croupier
from project.game.table import RouletteTable


@pytest.fixture
def setup_game() -> RouletteGame:
    bots = [
        AggressiveStrategy(name="bot_1", balance=100),
        BasicStrategy(name="bot_2", balance=100),
        OptimalStrategy(name="bot_3", balance=100),
    ]
    game = RouletteGame(bots, max_steps=10)
    return game


def test_spin_wheel():
    croupier = Croupier()
    number, color = croupier.spin_wheel()
    assert number in range(0, 37), f"!spin result: {number}!"
    assert color in ["red", "black", "green", f"!spin result:({color})!"]


def test_play_game_steps(setup_game, capsys):
    initial_balances = [bot.balance for bot in setup_game.bots]
    for step in range(1, setup_game.max_steps + 1):
        print(f"Step {step}:")
        for bot in setup_game.bots:
            if bot.balance > 0:
                table = RouletteTable()
                table.play_game(bot)
        setup_game.step += 1
        setup_game.display_game_state()
    final_balances = [bot.balance for bot in setup_game.bots]
    captured = capsys.readouterr()
    assert initial_balances != final_balances
    assert "Step 1:" in captured.out
    assert "Step 10:" in captured.out


def test_bet_placement(setup_game):
    setup_game.run_game()
    print("Final Balances after betting:")
    for bot in setup_game.bots:
        print(f"{bot.name}: {bot.balance}")
    assert any(bot.balance <= 100 for bot in setup_game.bots)


def test_bots_place_bets_correctly(setup_game):
    game = setup_game
    bets = [bot.place_bet() for bot in game.bots]
    assert all(bet is not None for bet in bets), f"!bets placed: {bets}!"


def test_game_rounds_increase(setup_game):
    initial_rounds = setup_game.step
    setup_game.run_game()
    assert (
        setup_game.step > initial_rounds
    ), f"!rounds played: {initial_rounds} -> {setup_game.step}!"


def test_bots_balance_update(setup_game):
    setup_game.run_game()
    print("Balances after game:")
    for bot in setup_game.bots:
        print(f"{bot.name}: {bot.balance}")
    assert all(bot.balance >= 0 for bot in setup_game.bots)


def test_roulette_game_is_game_over(setup_game):
    assert not setup_game.is_game_over()
    for bot in setup_game.bots:
        bot.balance = 0
    assert setup_game.is_game_over(), "!rouletteGame is_game_over method test passed!"


def test_state_changes_over_time(setup_game):
    game = setup_game
    initial_steps = game.step
    initial_balances = [bot.balance for bot in game.bots]

    game.run_game()

    print(f"Initial Steps: {initial_steps}, Final Steps: {game.step}")
    assert game.step > initial_steps

    final_balances = [bot.balance for bot in game.bots]
    print(f"Initial Balances: {initial_balances}, Final Balances: {final_balances}")
    assert any(
        final != initial for final, initial in zip(final_balances, initial_balances)
    )


def test_method_influence_on_game_state(setup_game):
    initial_balances = [bot.balance for bot in setup_game.bots]
    for bot in setup_game.bots:
        croupier = Croupier()
        bot.play(croupier)
    final_balances = [bot.balance for bot in setup_game.bots]
    assert initial_balances != final_balances
