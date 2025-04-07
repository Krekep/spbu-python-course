import pytest
from project.BlackJack.game import Game
from project.BlackJack.players import Player, Bot
from project.BlackJack.bot_strategy import (
    AccurateStrategy,
    AggressiveStrategy,
    CountingStrategy,
)


@pytest.fixture
def setup_game():
    """Fixture to set up a game instance for testing."""

    game = Game()
    game.add_player(game.create_bot('accurate', 'Bot1'))
    game.add_player(game.create_bot('aggressive', 'Bot2'))
    game.add_player(game.create_bot('counting', 'Counting'))

    return game


@pytest.mark.parametrize(
    "rule_name, new_value, expect_success",
    [
        ("BLACKJACK_PAYOUT", 2.0, True),    # Корректный параметр
        ("MAX_ROUND", 10, True),             # Корректный параметр
        ("non_existent_parameter", 10, False)  # Несуществующий параметр
    ]
)
def test_change_rules(setup_game, rule_name, new_value, expect_success):
    game = setup_game

    if expect_success:
        # Если параметр должен измениться
        game.modify_game_rule(rule_name, new_value, print_res=False)
        assert getattr(game, rule_name) == new_value, f"Rule {rule_name} don't changet on {new_value}."
    else:
        with pytest.raises(ValueError, match=f"Unknown game rule {rule_name}"):
            game.modify_game_rule(rule_name, new_value, print_res=False)


def test_change_bot_strategy(setup_game):
    game = setup_game
    original_strategy = next(p for p in game.players if p.name == "Bot1").strategy
    
    # Успешная смена стратегии
    game.change_bot_strategy("Bot1", 'aggressive', print_res=False)
    bot = next(p for p in game.players if p.name == "Bot1")
    assert isinstance(bot.strategy, AggressiveStrategy)
    assert not isinstance(bot.strategy, type(original_strategy))

    with pytest.raises(ValueError, match=f"Unknown strategy: strategy"):
        game.change_bot_strategy("Bot1", 'strategy', print_res=False)
    
    # Несуществующий бот
    with pytest.raises(ValueError, match=f"The bot was not found: Alex"):
        game.change_bot_strategy('Alex', 'accurate', print_res=False)
      



@pytest.mark.parametrize("rounds_played", [1, 3, 5])
def test_game_state_changes_over_time(setup_game, rounds_played):
    game = setup_game
    for _ in range(rounds_played):
        game.play_round(print_res=False)

    assert (
        game.round_count == rounds_played
    ), f"Expected round to be {rounds_played} but got {game.round_count}"



def test_deal_initial_cards(setup_game):
    game = setup_game
    game.start_round()

    for player in game.players:
        assert len(player.hand) == 2, f"{player.name} did not receive 2 cards."
    assert (
        len(game.dealer.hand) == 1
    ), "Dealer did not receive their visible card."
    assert (
        game.dealer.hide_card is not None
    ), "Dealer did not receive a hidden card."






@pytest.mark.parametrize(
    "player_score, dealer_score, expected_result",
    [
        (22, 18, "lose"),  # Player busts
        (19, 22, "win"),   # Dealer busts
        (20, 19, "win"),   # Player wins
        (18, 20, "lose"),  # Dealer wins
        (20, 20, "push"),  # Tie
        (21, 21, "push"),  # Tie with 21
    ],
)
def test_settle_bets(setup_game, player_score, dealer_score, expected_result):
    game = setup_game
    player = game.players[0]
    
    player.score = player_score
    game.dealer.score = dealer_score
    
    bet_amount = 10
    game.bets[player.name] = bet_amount
    
    initial_chips = player.chips
    
    game.settle_bets(print_res=False)
    
    if expected_result == "win":
        assert player.chips == initial_chips + bet_amount, "Player should win their bet"
    elif expected_result == "lose":
        assert player.chips == initial_chips - bet_amount, "Player should lose their bet"
    elif expected_result == "push":
        assert player.chips == initial_chips, "Player should get their bet back on a tie"



def test_game_state_progress(setup_game):
    game = setup_game
    game.modify_game_rule("BLACKJACK_PAYOUT", 1.0, print_res=False)
    initial_round = game.round_count
    initial_deck_size = game.deck.count

    rounds_to_play = 2
    for _ in range(rounds_to_play):
        game.play_round(print_res=False)

    assert (
        game.round_count == initial_round + rounds_to_play
    ), "Round count did not increment correctly."

    assert (
        game.deck.count > initial_deck_size
    ), "Deck size did not decrease after playing rounds."
