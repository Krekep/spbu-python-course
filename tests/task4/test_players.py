import pytest
from unittest.mock import Mock, patch
from project.task4.core.card import Card
from project.task4.players.player import Player
from project.task4.players.bot import Bot
from project.task4.players.human import HumanPlayer
from project.task4.players.dealer import Dealer
from project.task4.strategies.aggressive import AggressiveStrategy
from project.task4.strategies.conservative import ConservativeStrategy


@pytest.mark.unit
class TestPlayer:
    """Тесты для базового класса Player"""

    @pytest.mark.unit
    def test_player_creation(self, sample_player):
        """Тест создания игрока"""
        assert sample_player.name == "TestPlayer"
        assert sample_player.chips == 1000
        assert sample_player.bet == 0
        assert not sample_player.is_standing
        assert not sample_player.has_busted

    def test_place_bet_success(self, sample_player):
        """Тест успешной ставки"""
        success = sample_player.place_bet(100)

        assert success == True
        assert sample_player.bet == 100
        assert sample_player.chips == 900

    def test_place_bet_insufficient_chips(self, sample_player):
        """Тест ставки с недостаточным количеством фишек"""
        success = sample_player.place_bet(1500)

        assert success == False
        assert sample_player.bet == 0
        assert sample_player.chips == 1000

    def test_place_bet_zero(self, sample_player):
        """Тест нулевой ставки"""
        success = sample_player.place_bet(0)

        assert success == False
        assert sample_player.bet == 0
        assert sample_player.chips == 1000

    def test_place_bet_negative(self, sample_player):
        """Тест отрицательной ставки"""
        success = sample_player.place_bet(-100)

        assert success == False
        assert sample_player.bet == 0
        assert sample_player.chips == 1000

    def test_win_bet(self, sample_player):
        """Тест выигрыша ставки"""
        sample_player.place_bet(100)
        sample_player.win_bet()

        # Начальные фишки: 1000, ставка: 100, осталось: 900
        # Выигрыш: 100 * 2 = 200, итого: 900 + 200 = 1100
        assert sample_player.chips == 1100

    def test_lose_bet(self, sample_player):
        """Тест проигрыша ставки"""
        sample_player.place_bet(100)
        sample_player.lose_bet()

        assert sample_player.chips == 900
        assert sample_player.bet == 0

    def test_push_bet(self, sample_player):
        """Тест возврата ставки (ничья)"""
        sample_player.place_bet(100)
        sample_player.push()

        assert sample_player.chips == 1000
        assert sample_player.bet == 0

    def test_blackjack_win(self, sample_player):
        """Тест выигрыша блэкджеком"""
        sample_player.place_bet(100)
        sample_player.blackjack_win()

        assert sample_player.chips == 1000 + 150  # 1000 - 100 + 250 = 1150
        assert sample_player.bet == 0

    def test_reset_hand(self, sample_player):
        """Тест сброса состояния руки"""
        sample_player.is_standing = True
        sample_player.has_busted = True
        sample_player.hand.add_card(Card("Hearts", "10", 10))

        sample_player.reset_hand()

        assert not sample_player.is_standing
        assert not sample_player.has_busted
        assert len(sample_player.hand.cards) == 0
        assert sample_player.hand.value == 0

    def test_player_string_representation(self, sample_player):
        """Тест строкового представления игрока"""
        assert str(sample_player) == "TestPlayer (Фишки: 1000)"


class TestBot:
    """Тесты для класса Bot"""

    def test_bot_creation(self, sample_bot):
        """Тест создания бота"""
        assert sample_bot.name == "TestBot"
        assert sample_bot.chips == 1000
        assert isinstance(sample_bot.strategy, ConservativeStrategy)

    def test_bot_make_decision_hit(self, sample_bot):
        """Тест решения бота взять карту"""
        # Создаем руку с низким значением
        sample_bot.hand.add_card(Card("Hearts", "5", 5))
        sample_bot.hand.add_card(Card("Diamonds", "3", 3))

        dealer_card = Card("Spades", "10", 10)
        decision = sample_bot.make_decision(dealer_card)

        assert decision in ["hit", "stand"]

    def test_bot_make_decision_stand(self, sample_bot):
        """Тест решения бота остановиться"""
        # Создаем руку с высоким значением
        sample_bot.hand.add_card(Card("Hearts", "10", 10))
        sample_bot.hand.add_card(Card("Diamonds", "9", 9))

        dealer_card = Card("Spades", "5", 5)
        decision = sample_bot.make_decision(dealer_card)

        assert decision == "stand"

    def test_bot_place_bet(self, sample_bot):
        """Тест ставки бота"""
        success = sample_bot.make_bet()  # ЗАМЕНИТЬ place_bet() на make_bet()
        assert success == True
        assert sample_bot.bet > 0
        assert sample_bot.bet <= sample_bot.chips

    def test_bot_different_strategies_betting(self):
        """Тест ставок ботов с разными стратегиями"""
        conservative_bot = Bot("ConsBot", ConservativeStrategy(), 1000)
        aggressive_bot = Bot("AggrBot", AggressiveStrategy(), 1000)

        conservative_bot.make_bet()
        aggressive_bot.make_bet()

        # Проверяем, что оба сделали ставки
        assert conservative_bot.bet > 0
        assert aggressive_bot.bet > 0

        # Проверяем, что ставки различаются (из-за разных стратегий)
        # Но не обязательно, что агрессивный всегда ставит больше из-за случайности
        assert conservative_bot.bet != aggressive_bot.bet

        # Проверяем разумные пределы ставок
        assert conservative_bot.bet <= 1000
        assert aggressive_bot.bet <= 1000

    def test_bot_standing_after_stand_decision(self, sample_bot):
        """Тест, что бот останавливается после решения stand"""
        sample_bot.hand.add_card(Card("Hearts", "10", 10))
        sample_bot.hand.add_card(Card("Diamonds", "9", 9))

        dealer_card = Card("Spades", "5", 5)
        sample_bot.make_decision(dealer_card)

        assert sample_bot.is_standing == True


class TestHumanPlayer:
    """Тесты для класса HumanPlayer"""

    def test_human_player_creation(self, sample_human):
        """Тест создания человеческого игрока"""
        assert sample_human.name == "TestHuman"
        assert sample_human.chips == 1000

    @patch("builtins.input", return_value="h")
    def test_human_make_decision_hit(self, mock_input, sample_human):
        """Тест решения человека взять карту"""
        dealer_card = Card("Spades", "10", 10)
        decision = sample_human.make_decision(dealer_card)

        assert decision == "hit"

    @patch("builtins.input", return_value="s")
    def test_human_make_decision_stand(self, mock_input, sample_human):
        """Тест решения человека остановиться"""
        dealer_card = Card("Spades", "10", 10)
        decision = sample_human.make_decision(dealer_card)

        assert decision == "stand"

    @patch("builtins.input", return_value="d")
    def test_human_make_decision_double(self, mock_input, sample_human):
        """Тест решения человека удвоить ставку"""
        sample_human.place_bet(100)
        dealer_card = Card("Spades", "5", 5)
        decision = sample_human.make_decision(dealer_card)

        assert decision == "double"
        assert sample_human.bet == 200

    @patch(
        "builtins.input", side_effect=["x", "h"]
    )  # Сначала неверный ввод, потом верный
    def test_human_invalid_then_valid_input(self, mock_input, sample_human):
        """Тест неверного ввода с последующим верным"""
        dealer_card = Card("Spades", "10", 10)
        decision = sample_human.make_decision(dealer_card)

        assert decision == "hit"
        assert mock_input.call_count == 2

    @patch("builtins.input", return_value="100")
    def test_human_make_bet(self, mock_input, sample_human):
        """Тест ставки человеческого игрока"""
        success = sample_human.make_bet()

        assert success == True
        assert sample_human.bet == 100
        assert sample_human.chips == 900

    @patch(
        "builtins.input", side_effect=["-50", "100"]
    )  # Сначала отрицательная, потом верная
    def test_human_invalid_then_valid_bet(self, mock_input, sample_human):
        """Тест неверной ставки с последующей верной"""
        success = sample_human.make_bet()

        assert success == True
        assert sample_human.bet == 100

    @patch(
        "builtins.input", side_effect=["not_a_number", "150"]
    )  # Сначала не число, потом верное
    def test_human_non_numeric_bet(self, mock_input, sample_human):
        """Тест нечисловой ставки с последующей верной"""
        success = sample_human.make_bet()

        assert success == True
        assert sample_human.bet == 150


class TestDealer:
    """Тесты для класса Dealer"""

    def test_dealer_creation(self, sample_dealer):
        """Тест создания дилера"""
        assert sample_dealer.name == "Dealer"
        assert sample_dealer.chips == 0

    def test_dealer_should_hit_below_17(self, sample_dealer):
        """Тест, что дилер берет карту при значении ниже 17"""
        sample_dealer.hand.add_card(Card("Hearts", "10", 10))
        sample_dealer.hand.add_card(Card("Diamonds", "6", 6))

        assert sample_dealer.should_hit() == True

    def test_dealer_should_stand_at_17(self, sample_dealer):
        """Тест, что дилер останавливается при значении 17"""
        sample_dealer.hand.add_card(Card("Hearts", "10", 10))
        sample_dealer.hand.add_card(Card("Diamonds", "7", 7))

        assert sample_dealer.should_hit() == False

    def test_dealer_should_stand_above_17(self, sample_dealer):
        """Тест, что дилер останавливается при значении выше 17"""
        sample_dealer.hand.add_card(Card("Hearts", "10", 10))
        sample_dealer.hand.add_card(Card("Diamonds", "8", 8))

        assert sample_dealer.should_hit() == False

    def test_dealer_make_decision(self, sample_dealer):
        """Тест решения дилера"""
        # Дилер всегда следует правилам
        sample_dealer.hand.add_card(Card("Hearts", "10", 10))
        sample_dealer.hand.add_card(Card("Diamonds", "6", 6))

        dealer_card = Card("Spades", "5", 5)  # Не используется дилером
        decision = sample_dealer.make_decision(dealer_card)

        assert decision == "hit"

    def test_dealer_soft_17_hit(self, sample_dealer):
        """Тест, что дилер берет карту на мягком 17"""
        # Мягкое 17: A + 6
        sample_dealer.hand.add_card(Card("Hearts", "A", 11))
        sample_dealer.hand.add_card(Card("Diamonds", "6", 6))

        assert sample_dealer.should_hit() == True

    def test_dealer_reveal_hand(self, sample_dealer):
        """Тест метода раскрытия руки дилера"""
        sample_dealer.hand.add_card(Card("Hearts", "10", 10))
        sample_dealer.hand.add_card(Card("Diamonds", "7", 7))

        reveal_text = sample_dealer.reveal_hand()
        expected_text = (
            f"Карты дилера: {sample_dealer.hand} (Сумма: {sample_dealer.hand.value})"
        )

        assert reveal_text == expected_text
