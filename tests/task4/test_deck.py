import pytest
from project.task4.core.deck import Deck
from project.task4.core.card import Card


@pytest.mark.unit
class TestDeck:
    """Тесты для класса Deck"""

    @pytest.mark.unit
    def test_deck_creation(self, sample_deck):
        """Тест создания колоды"""
        assert len(sample_deck.cards) == 52
        assert sample_deck.num_decks == 1

    def test_deck_multiple_decks(self):
        """Тест создания колоды из нескольких дек"""
        deck = Deck(2)
        assert len(deck.cards) == 104

    def test_deck_shuffle(self, sample_deck):
        """Тест перемешивания колоды"""
        original_order = sample_deck.cards.copy()
        sample_deck.shuffle()
        shuffled_order = sample_deck.cards

        # Проверяем, что порядок изменился (может иногда падать из-за случайности)
        assert original_order != shuffled_order
        assert len(original_order) == len(shuffled_order)

    def test_deal_card(self, sample_deck):
        """Тест раздачи карты"""
        initial_count = len(sample_deck.cards)
        card = sample_deck.deal_card()

        assert isinstance(card, Card)
        assert len(sample_deck.cards) == initial_count - 1
        assert card not in sample_deck.cards

    def test_deal_card_from_empty_deck(self):
        """Тест раздачи карты из пустой колоды"""
        deck = Deck(1)
        # Раздаем все карты
        for _ in range(52):
            deck.deal_card()

        # Колода должна автоматически перестроиться и перемешаться
        card = deck.deal_card()
        assert isinstance(card, Card)
        assert len(deck.cards) == 51

    def test_deck_rebuild_after_empty(self):
        """Тест перестроения колоды после опустошения"""
        deck = Deck(1)
        initial_cards = deck.cards.copy()

        # Раздаем все карты
        dealt_cards = []
        for _ in range(52):
            dealt_cards.append(deck.deal_card())

        # Колода пуста
        assert len(deck.cards) == 0

        # Следующая раздача должна перестроить колоду
        new_card = deck.deal_card()
        assert len(deck.cards) == 51
        # Проверяем, что новая карта имеет корректный тип
        assert isinstance(new_card, Card)

    def test_deck_contains_all_cards(self):
        """Тест, что колода содержит все необходимые карты"""
        deck = Deck(1)
        suits = ["Spades ♠", "Clubs ♣", "Hearts ♥", "Diamonds ♦"]
        ranks = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 10,
            "Q": 10,
            "K": 10,
            "A": 11,
        }

        # Проверяем количество карт
        expected_count = len(suits) * len(ranks)
        assert len(deck.cards) == expected_count

        # Проверяем, что все комбинации присутствуют
        card_combinations = set()
        for card in deck.cards:
            card_combinations.add((card.suit, card.rank, card.value))

        expected_combinations = set()
        for suit in suits:
            for rank, value in ranks.items():
                expected_combinations.add((suit, rank, value))

        assert card_combinations == expected_combinations

    def test_deck_len_method(self, sample_deck):
        """Тест метода __len__"""
        assert len(sample_deck) == 52

        sample_deck.deal_card()
        assert len(sample_deck) == 51

    @pytest.mark.parametrize(
        "num_decks,expected_cards",
        [
            (1, 52),
            (2, 104),
            (4, 208),
            (6, 312),
        ],
    )
    def test_different_deck_sizes(self, num_decks, expected_cards):
        """Параметризованный тест разных размеров колод"""
        deck = Deck(num_decks)
        assert len(deck.cards) == expected_cards
