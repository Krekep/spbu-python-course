"""
Tests for roulette game
"""

import pytest
from project.task4.roulette import (
    Player,
    Bet,
    ConservativeStrategy,
    RiskStrategy,
    MegaRiskStrategy,
    MathematicalStrategy,
    RouletteGame,
    RouletteWheel,
)


class TestPlayer:
    """Test Player"""

    def test_player_creation_valid(self):
        """Test creating player with valid parameters"""
        strategy = ConservativeStrategy()
        player = Player(1000, 25, strategy, "TestPlayer")
        assert player._name == "TestPlayer"
        assert player.balance == 1000
        assert player._age == 25
        assert player.strategy == strategy
        assert player.current_bets == []

    def test_player_underage_raises_error(self):
        """Test player creation with underage raises ValueError"""
        strategy = ConservativeStrategy()
        with pytest.raises(ValueError, match="Player must be over 18 years old"):
            Player(1000, 17, strategy)

    def test_player_default_name(self):
        """Test player creation with default name"""
        strategy = ConservativeStrategy()
        player = Player(1000, 20, strategy)
        assert player._name == "Unknown"

    def test_player_balance_can_be_zero(self):
        """Test player creation with zero balance"""
        strategy = ConservativeStrategy()
        player = Player(0, 20, strategy)
        assert player.balance == 0


class TestBet:
    """Test Bet class validation and creation"""

    def test_valid_number_bet(self):
        """Test creating valid number bet"""
        bet = Bet("number", 17, 100)
        assert bet.type_bet == "number"
        assert bet.bet_value == 17
        assert bet.sum_bet == 100

    def test_valid_color_bet_red(self):
        """Test creating valid red color bet"""
        bet = Bet("color", "red", 50)
        assert bet.type_bet == "color"
        assert bet.bet_value == "red"

    def test_valid_color_bet_black(self):
        """Test creating valid black color bet"""
        bet = Bet("color", "black", 50)
        assert bet.type_bet == "color"
        assert bet.bet_value == "black"

    def test_valid_even_odd_bet(self):
        """Test creating valid even/odd bets"""
        bet_even = Bet("even_odd", "even", 50)
        bet_odd = Bet("even_odd", "odd", 50)
        assert bet_even.bet_value == "even"
        assert bet_odd.bet_value == "odd"

    def test_valid_dozen_bets(self):
        """Test creating valid dozen bets"""
        for dozen in ["1st", "2nd", "3rd"]:
            bet = Bet("dozen", dozen, 50)
            assert bet.bet_value == dozen

    def test_valid_column_bets(self):
        """Test creating valid column bets"""
        for column in [1, 2, 3]:
            bet = Bet("column", column, 50)
            assert bet.bet_value == column

    def test_valid_half_bets(self):
        """Test creating valid half bets"""
        for half in ["1-18", "19-36"]:
            bet = Bet("half", half, 50)
            assert bet.bet_value == half

    def test_invalid_bet_type_raises_error(self):
        """Test invalid bet type raises ValueError"""
        with pytest.raises(ValueError, match="Invalid bet type"):
            Bet("invalid_type", 10, 100)

    def test_invalid_number_raises_error(self):
        """Test invalid number raises ValueError"""
        with pytest.raises(ValueError, match="Number must be 0-36"):
            Bet("number", 37, 100)
        with pytest.raises(ValueError, match="Number must be 0-36"):
            Bet("number", -1, 100)

    def test_invalid_color_raises_error(self):
        """Test invalid color raises ValueError"""
        with pytest.raises(ValueError, match="Color must be 'red' or 'black'"):
            Bet("color", "green", 100)

    def test_invalid_even_odd_raises_error(self):
        """Test invalid even/odd raises ValueError"""
        with pytest.raises(ValueError, match="Even/Odd must be 'even' or 'odd'"):
            Bet("even_odd", "invalid", 100)

    def test_invalid_dozen_raises_error(self):
        """Test invalid dozen raises ValueError"""
        with pytest.raises(ValueError, match="Dozen must be '1st', '2nd' or '3rd'"):
            Bet("dozen", "4th", 100)

    def test_invalid_column_raises_error(self):
        """Test invalid column raises ValueError"""
        with pytest.raises(ValueError, match="Column must be 1, 2 or 3"):
            Bet("column", 4, 100)
        with pytest.raises(ValueError, match="Column must be 1, 2 or 3"):
            Bet("column", 0, 100)

    def test_invalid_half_raises_error(self):
        """Test invalid half raises ValueError"""
        with pytest.raises(ValueError, match="Half must be '1-18' or '19-36'"):
            Bet("half", "20-36", 100)


class TestConservativeStrategy:
    """Test ConservativeStrategy betting behavior"""

    def test_strategy_alternates_colors(self):
        """Test strategy alternates between red and black"""
        strategy = ConservativeStrategy()
        player = Player(1000, 25, strategy)

        bet1 = strategy.make_bet(player)
        first_color = bet1.bet_value

        bet2 = strategy.make_bet(player)
        second_color = bet2.bet_value

        assert first_color != second_color
        assert first_color in ["red", "black"]
        assert second_color in ["red", "black"]

    def test_bet_amount_is_10_percent(self):
        """Test bet amount is 10% of balance"""
        strategy = ConservativeStrategy()
        player = Player(1000, 25, strategy)

        bet = strategy.make_bet(player)
        assert bet.sum_bet == 100

    def test_minimum_bet_is_1(self):
        """Test minimum bet is 1 even with low balance"""
        strategy = ConservativeStrategy()
        player = Player(5, 25, strategy)

        bet = strategy.make_bet(player)
        assert bet.sum_bet == 1

    def test_bet_type_is_always_color(self):
        """Test strategy always bets on color"""
        strategy = ConservativeStrategy()
        player = Player(1000, 25, strategy)

        for _ in range(10):
            bet = strategy.make_bet(player)
            assert bet.type_bet == "color"


class TestRiskStrategy:
    """Test RiskStrategy random number betting"""

    def test_bet_type_is_always_number(self):
        """Test strategy always bets on numbers"""
        strategy = RiskStrategy()
        player = Player(1000, 25, strategy)

        bet = strategy.make_bet(player)
        assert bet.type_bet == "number"

    def test_number_is_within_range(self):
        """Test random numbers are within 0-36 range"""
        strategy = RiskStrategy()
        player = Player(1000, 25, strategy)

        for _ in range(100):
            bet = strategy.make_bet(player)
            assert 0 <= bet.bet_value <= 36

    def test_bet_amount_is_10_percent(self):
        """Test bet amount is 10% of balance"""
        strategy = RiskStrategy()
        player = Player(1000, 25, strategy)

        bet = strategy.make_bet(player)
        assert bet.sum_bet == 100


class TestMegaRiskStrategy:
    """Test MegaRiskStrategy"""

    def test_always_bets_on_zero(self):
        """Test strategy always bets on number zero"""
        strategy = MegaRiskStrategy()
        player = Player(1000, 25, strategy)

        for _ in range(10):
            bet = strategy.make_bet(player)
            assert bet.type_bet == "number"
            assert bet.bet_value == 0

    def test_bet_amount_is_50_percent(self):
        """Test bet amount is 50% of balance"""
        strategy = MegaRiskStrategy()
        player = Player(1000, 25, strategy)

        bet = strategy.make_bet(player)
        assert bet.sum_bet == 500


class TestMathematicalStrategy:
    """Test MathematicalStrategy Martingale system"""

    def test_initial_bet_is_small(self):
        """Test initial bet amount is small"""
        strategy = MathematicalStrategy()
        player = Player(1000, 25, strategy)

        bet = strategy.make_bet(player)
        assert bet.sum_bet == 1

    def test_doubles_after_loss(self):
        """Test bet doubles after a loss"""
        strategy = MathematicalStrategy()
        player = Player(1000, 25, strategy)

        bet1 = strategy.make_bet(player)
        assert bet1.sum_bet == 1

        strategy.update_result(False)

        bet2 = strategy.make_bet(player)
        assert bet2.sum_bet == 2

    def test_resets_after_win(self):
        """Test bet resets to 1 after a win"""
        strategy = MathematicalStrategy()
        player = Player(1000, 25, strategy)

        strategy.make_bet(player)
        strategy.update_result(False)

        strategy.make_bet(player)

        strategy.update_result(True)

        bet = strategy.make_bet(player)
        assert bet.sum_bet == 1

    def test_alternates_colors(self):
        """Test strategy alternates between red and black"""
        strategy = MathematicalStrategy()
        player = Player(1000, 25, strategy)

        bet1 = strategy.make_bet(player)
        first_color = bet1.bet_value

        bet2 = strategy.make_bet(player)
        second_color = bet2.bet_value

        assert first_color != second_color
        assert bet1.type_bet == "color"
        assert bet2.type_bet == "color"


class TestRouletteWheel:
    """Test RouletteWheel spinning and result calculation"""

    def test_wheel_creation(self):
        """Test wheel initializes with correct numbers"""
        wheel = RouletteWheel()
        assert len(wheel.red_numbers) == 18
        assert len(wheel.black_numbers) == 18
        assert 0 not in wheel.red_numbers
        assert 0 not in wheel.black_numbers

    def test_spin_returns_valid_structure(self):
        """Test spin returns dictionary with all required keys"""
        wheel = RouletteWheel()
        result = wheel.spin()

        assert "number" in result
        assert "color" in result
        assert "is_even" in result
        assert "range" in result

    def test_spin_number_range(self):
        """Test spin numbers are within valid range"""
        wheel = RouletteWheel()

        for _ in range(100):
            result = wheel.spin()
            assert 0 <= result["number"] <= 36

    def test_color_determination_red(self):
        """Test red numbers return correct"""
        wheel = RouletteWheel()

        for number in wheel.red_numbers:
            assert wheel._get_color(number) == "red"

    def test_color_determination_black(self):
        """Test black numbers return correct"""
        wheel = RouletteWheel()

        for number in wheel.black_numbers:
            assert wheel._get_color(number) == "black"

    def test_color_determination_zero(self):
        """Test zero returns"""
        wheel = RouletteWheel()
        assert wheel._get_color(0) == "green"

    def test_even_determination(self):
        """Test even number detection"""
        wheel = RouletteWheel()

        assert wheel._is_even(2) is True
        assert wheel._is_even(3) is False
        assert wheel._is_even(0) is False

    def test_range_determination(self):
        """Test number range"""
        wheel = RouletteWheel()

        assert wheel._get_range(0) == "zero"
        assert wheel._get_range(1) == "1-18"
        assert wheel._get_range(18) == "1-18"
        assert wheel._get_range(19) == "19-36"
        assert wheel._get_range(36) == "19-36"


class TestRouletteGame:
    """Test RouletteGame game logic"""

    def test_game_creation(self):
        """Test game initialization with players"""
        players = [
            Player(100, 20, ConservativeStrategy(), "Test1"),
            Player(200, 25, RiskStrategy(), "Test2"),
        ]
        game = RouletteGame(players, max_rounds=5)

        assert game.players == players
        assert game.max_rounds == 5
        assert game.current_round == 0
        assert game.history == []

    def test_is_game_over_max_rounds(self):
        """Test game over when max rounds reached"""
        players = [Player(100, 20, ConservativeStrategy())]
        game = RouletteGame(players, max_rounds=3)
        game.current_round = 3

        assert game.is_game_over() is True

    def test_is_game_over_all_bankrupt(self):
        """Test game over when all players bankrupt"""
        player1 = Player(0, 20, ConservativeStrategy())
        player2 = Player(0, 25, RiskStrategy())
        game = RouletteGame([player1, player2])

        assert game.is_game_over() is True

    def test_is_game_over_continues(self):
        """Test game continues"""
        players = [Player(100, 20, ConservativeStrategy())]
        game = RouletteGame(players, max_rounds=5)
        game.current_round = 2

        assert game.is_game_over() is False

    def test_play_round_returns_false_when_game_over(self):
        """Test play_round returns False when game should end"""
        players = [Player(0, 20, ConservativeStrategy())]
        game = RouletteGame(players)

        assert game.play_round() is False

    def test_show_game_state_method_exists(self):
        """Test show_game_state method"""
        players = [Player(100, 20, ConservativeStrategy())]
        game = RouletteGame(players)

        game.show_game_state()


class TestGameIntegration:
    """Integration tests"""

    def test_single_round_changes_game_state(self):
        """Test that playing a round changes game state"""
        players = [
            Player(200, 20, ConservativeStrategy(), "Test1"),
            Player(200, 25, RiskStrategy(), "Test2"),
        ]
        game = RouletteGame(players, max_rounds=10)

        initial_round = game.current_round
        initial_history_len = len(game.history)

        game.play_round()

        assert game.current_round == initial_round + 1
        assert len(game.history) == initial_history_len + 1

    def test_player_balance_changes_after_bet(self):
        """Test player balance"""
        player = Player(200, 20, ConservativeStrategy(), "Test")
        initial_balance = player.balance

        bet = player.strategy.make_bet(player)
        player.balance -= bet.sum_bet

        assert player.balance == initial_balance - bet.sum_bet

    def test_multiple_strategies_in_same_game(self):
        """Test game works"""
        players = [
            Player(100, 20, ConservativeStrategy(), "Conservative"),
            Player(100, 25, RiskStrategy(), "Risky"),
            Player(100, 30, MegaRiskStrategy(), "MegaRisky"),
            Player(100, 35, MathematicalStrategy(), "Mathematical"),
        ]
        game = RouletteGame(players, max_rounds=2)

        assert game.play_round() is True
        assert game.play_round() is True

    def test_game_history_records_rounds(self):
        """Test game history"""
        players = [Player(100, 20, ConservativeStrategy(), "Test")]
        game = RouletteGame(players, max_rounds=3)

        game.play_round()
        game.play_round()

        assert len(game.history) == 2
        assert game.history[0]["round"] == 1
        assert game.history[1]["round"] == 2
        assert "winning_number" in game.history[0]
        assert "player_balances" in game.history[0]


def test_complete_game_flow():
    """Test complete game flow from start to finish"""
    players = [
        Player(100, 20, ConservativeStrategy(), "Player1"),
        Player(100, 25, RiskStrategy(), "Player2"),
    ]
    game = RouletteGame(players, max_rounds=5)

    rounds_played = 0
    while game.play_round():
        rounds_played += 1
        assert game.current_round == rounds_played
        assert len(game.history) == rounds_played

        for player in players:
            assert player._name in game.history[-1]["player_balances"]

    assert rounds_played <= 5
    assert game.is_game_over() is True
