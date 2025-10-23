import pytest
from unittest.mock import Mock, patch
from project.task4.core.game import Game
from project.task4.core.card import Card
from project.task4.strategies.conservative import ConservativeStrategy


@pytest.mark.unit
class TestGame:
    """Тесты для класса Game"""

    @pytest.mark.unit
    def test_game_creation(self, sample_game):
        """Тест создания игры"""
        assert sample_game.num_decks == 1
        assert sample_game.max_rounds == 5
        assert len(sample_game.players) == 2
        assert sample_game.current_round == 0
        assert not sample_game.is_game_active

    def test_add_player(self, sample_game):
        """Тест добавления игрока"""
        initial_count = len(sample_game.players)
        sample_game.add_bot("NewBot", ConservativeStrategy(), 500)

        assert len(sample_game.players) == initial_count + 1
        assert sample_game.players[-1].name == "NewBot"

    def test_add_human_player(self, sample_game):
        """Тест добавления человеческого игрока"""
        sample_game.add_human_player("HumanPlayer", 1000)

        human_players = [p for p in sample_game.players if p.name == "HumanPlayer"]
        assert len(human_players) == 1
        assert human_players[0].chips == 1000

    def test_start_game(self, sample_game):
        """Тест начала игры"""
        sample_game.start_game()

        assert sample_game.is_game_active == True
        assert len(sample_game.deck.cards) > 0

    def test_reset_round(self, sample_game):
        """Тест сброса состояния раунда"""
        # Сначала устанавливаем некоторые состояния
        sample_game.players[0].is_standing = True
        sample_game.players[0].has_busted = True
        sample_game.players[0].hand.add_card(Card("Hearts", "10", 10))

        sample_game.dealer.is_standing = True
        sample_game.dealer.hand.add_card(Card("Diamonds", "10", 10))

        sample_game._reset_round()

        # Проверяем сброс состояний
        for player in sample_game.players:
            assert not player.is_standing
            assert not player.has_busted
            assert len(player.hand.cards) == 0

        assert not sample_game.dealer.is_standing
        assert len(sample_game.dealer.hand.cards) == 0

    def test_place_bets(self, sample_game):
        """Тест процесса ставок"""
        sample_game.start_game()
        round_info = {"bets": []}

        sample_game._place_bets(round_info)

        # Проверяем, что все игроки сделали ставки
        for player in sample_game.players:
            assert player.bet > 0
            assert player.bet <= player.chips

        # Проверяем, что информация о ставках записана
        assert len(round_info["bets"]) > 0

    def test_deal_initial_cards(self, sample_game):
        """Тест начальной раздачи карт"""
        sample_game.start_game()
        round_info = {"card_dealing": []}

        sample_game._place_bets(round_info)
        sample_game._deal_initial_cards(round_info)

        # Проверяем, что у всех игроков по 2 карты
        for player in sample_game.players:
            if player.bet > 0:
                assert len(player.hand.cards) == 2

        # Проверяем, что у дилера 2 карты
        assert len(sample_game.dealer.hand.cards) == 2

        # Проверяем, что информация о раздаче записана
        assert len(round_info["card_dealing"]) > 0

    def test_dealer_blackjack_detection_true(self, sample_game):
        """Тест обнаружения блэкджека у дилера"""
        sample_game.start_game()
        round_info = {"results": []}

        # Создаем блэкджек у дилера
        sample_game.dealer.hand.add_card(Card("Spades", "A", 11))
        sample_game.dealer.hand.add_card(Card("Spades", "K", 10))

        result = sample_game._check_dealer_blackjack(round_info)

        assert result == True
        assert len(round_info["results"]) > 0

    def test_dealer_blackjack_detection_false(self, sample_game):
        """Тест, что обычная рука дилера не определяется как блэкджек"""
        sample_game.start_game()
        round_info = {"results": []}

        # Создаем обычную руку у дилера
        sample_game.dealer.hand.add_card(Card("Spades", "10", 10))
        sample_game.dealer.hand.add_card(Card("Spades", "7", 7))

        result = sample_game._check_dealer_blackjack(round_info)

        assert result == False

    def test_determine_winners_dealer_busted(self, sample_game):
        """Тест определения победителей при переборе дилера"""
        sample_game.start_game()
        round_info = {"results": []}

        # Игроки делают ставки
        for player in sample_game.players:
            player.place_bet(100)  # Ставка 100, остается 400 фишек

        # Дилер перебирает
        sample_game.dealer.hand.add_card(Card("Spades", "10", 10))
        sample_game.dealer.hand.add_card(Card("Hearts", "10", 10))
        sample_game.dealer.hand.add_card(Card("Diamonds", "5", 5))

        sample_game._determine_winners(round_info)

        # Все игроки должны выиграть: 400 + 200 = 600
        for player in sample_game.players:
            assert player.chips == 600  # 500 - 100 + 200 = 600

    def test_determine_winners_player_blackjack(self, sample_game):
        """Тест определения победителей при блэкджеке игрока"""
        sample_game.start_game()
        round_info = {"results": []}

        # Игрок делает ставку и получает блэкджек
        player = sample_game.players[0]
        player.place_bet(100)
        player.hand.add_card(Card("Spades", "A", 11))
        player.hand.add_card(Card("Spades", "K", 10))

        # Дилер получает обычную руку
        sample_game.dealer.hand.add_card(Card("Hearts", "10", 10))
        sample_game.dealer.hand.add_card(Card("Diamonds", "7", 7))

        sample_game._determine_winners(round_info)

        # Игрок с блэкджеком должен получить 3:2
        assert player.chips == 500 + 150  # 500 - 100 + 250 = 650

    def test_determine_winners_push(self, sample_game):
        """Тест определения ничьей"""
        sample_game.start_game()
        round_info = {"results": []}

        # Игрок делает ставку
        player = sample_game.players[0]
        initial_chips = player.chips
        player.place_bet(100)

        # Игрок и дилер имеют одинаковое значение
        player.hand.add_card(Card("Spades", "10", 10))
        player.hand.add_card(Card("Spades", "7", 7))

        sample_game.dealer.hand.add_card(Card("Hearts", "10", 10))
        sample_game.dealer.hand.add_card(Card("Diamonds", "7", 7))

        sample_game._determine_winners(round_info)

        # При ничье игрок получает ставку обратно
        assert player.chips == initial_chips

    def test_get_game_state(self, sample_game):
        """Тест получения состояния игры"""
        sample_game.start_game()
        state = sample_game.get_game_state()

        assert "round" in state
        assert "max_rounds" in state
        assert "active_players" in state
        assert "deck_cards" in state
        assert "players" in state
        assert "dealer" in state

        assert len(state["players"]) == len(sample_game.players)
        assert "name" in state["players"][0]
        assert "chips" in state["players"][0]
        assert "hand" in state["players"][0]
        assert "hand_value" in state["players"][0]

    def test_check_game_status_continue(self, sample_game):
        """Тест проверки статуса игры (продолжение)"""
        sample_game.start_game()
        sample_game.current_round = 3

        sample_game._check_game_status()

        assert sample_game.is_game_active == True

    def test_check_game_status_max_rounds(self, sample_game):
        """Тест проверки статуса игры (достигнут лимит раундов)"""
        sample_game.start_game()
        sample_game.current_round = sample_game.max_rounds

        sample_game._check_game_status()

        assert sample_game.is_game_active == False

    def test_check_game_status_no_active_players(self, sample_game):
        """Тест проверки статуса игры (нет активных игроков)"""
        sample_game.start_game()

        # У всех игроков заканчиваются фишки
        for player in sample_game.players:
            player.chips = 0

        sample_game._check_game_status()

        assert sample_game.is_game_active == False
