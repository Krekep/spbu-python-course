import pytest
import sys
import os

# Добавляем пути для импортов с учетом структуры проекта
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))  # spbu-python-course/
task4_dir = os.path.join(project_root, "project", "task4")

sys.path.insert(0, task4_dir)

from project.task4.core.card import Card
from project.task4.core.deck import Deck
from project.task4.core.hand import Hand
from project.task4.core.game import Game
from project.task4.players.player import Player
from project.task4.players.bot import Bot
from project.task4.players.human import HumanPlayer
from project.task4.players.dealer import Dealer
from project.task4.strategies.conservative import ConservativeStrategy
from project.task4.strategies.aggressive import AggressiveStrategy
from project.task4.strategies.basic import BasicStrategy

# Регистрируем пользовательские маркеры
def pytest_configure(config):
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )

@pytest.fixture
def sample_card():
    """Фикстура для создания тестовой карты"""
    return Card("Hearts", "A", 11)

@pytest.fixture
def sample_deck():
    """Фикстура для создания тестовой колоды"""
    return Deck(1)

@pytest.fixture
def sample_hand():
    """Фикстура для создания тестовой руки"""
    return Hand()

@pytest.fixture
def sample_player():
    """Фикстура для создания тестового игрока"""
    return Bot("TestPlayer", ConservativeStrategy(), 1000)

@pytest.fixture
def sample_bot():
    """Фикстура для создания тестового бота"""
    return Bot("TestBot", ConservativeStrategy(), 1000)

@pytest.fixture
def sample_human():
    """Фикстура для создания тестового человеческого игрока"""
    return HumanPlayer("TestHuman", 1000)

@pytest.fixture
def sample_dealer():
    """Фикстура для создания тестового дилера"""
    return Dealer()

@pytest.fixture
def sample_game():
    """Фикстура для создания тестовой игры"""
    game = Game(num_decks=1, max_rounds=5)
    game.add_bot("TestBot1", ConservativeStrategy(), 500)
    game.add_bot("TestBot2", AggressiveStrategy(), 500)
    return game

@pytest.fixture
def strategies():
    """Фикстура для создания всех стратегий"""
    return {
        'conservative': ConservativeStrategy(),
        'aggressive': AggressiveStrategy(),
        'basic': BasicStrategy()
    }

@pytest.fixture
def blackjack_hand():
    """Фикстура для создания руки с блэкджеком"""
    hand = Hand()
    hand.add_card(Card("Spades", "A", 11))
    hand.add_card(Card("Spades", "K", 10))
    return hand

@pytest.fixture
def busted_hand():
    """Фикстура для создания руки с перебором"""
    hand = Hand()
    hand.add_card(Card("Hearts", "10", 10))
    hand.add_card(Card("Diamonds", "9", 9))
    hand.add_card(Card("Clubs", "5", 5))
    return hand

@pytest.fixture
def soft_hand():
    """Фикстура для создания мягкой руки (с тузом)"""
    hand = Hand()
    hand.add_card(Card("Hearts", "A", 11))
    hand.add_card(Card("Diamonds", "6", 6))
    return hand