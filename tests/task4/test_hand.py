import pytest
from project.task4.core.hand import Hand
from project.task4.core.card import Card


@pytest.mark.unit
class TestHand:
    """Тесты для класса Hand"""

    @pytest.mark.unit
    def test_hand_creation(self, sample_hand):
        """Тест создания руки"""
        assert len(sample_hand.cards) == 0
        assert sample_hand.value == 0
        assert sample_hand.aces == 0

    def test_add_card(self, sample_hand):
        """Тест добавления карты в руку"""
        card = Card("Hearts", "7", 7)
        sample_hand.add_card(card)

        assert len(sample_hand.cards) == 1
        assert sample_hand.cards[0] == card
        assert sample_hand.value == 7

    def test_add_multiple_cards(self, sample_hand):
        """Тест добавления нескольких карт"""
        cards = [Card("Hearts", "5", 5), Card("Diamonds", "8", 8)]

        for card in cards:
            sample_hand.add_card(card)

        assert len(sample_hand.cards) == 2
        assert sample_hand.value == 13

    def test_hand_clear(self, sample_hand):
        """Тест очистки руки"""
        sample_hand.add_card(Card("Hearts", "10", 10))
        sample_hand.add_card(Card("Diamonds", "J", 10))

        sample_hand.clear()

        assert len(sample_hand.cards) == 0
        assert sample_hand.value == 0
        assert sample_hand.aces == 0

    def test_blackjack_detection(self, blackjack_hand):
        """Тест обнаружения блэкджека"""
        assert blackjack_hand.is_blackjack() == True

    def test_non_blackjack_hand(self, sample_hand):
        """Тест, что обычная рука не определяется как блэкджек"""
        sample_hand.add_card(Card("Hearts", "10", 10))
        sample_hand.add_card(Card("Diamonds", "7", 7))

        assert sample_hand.is_blackjack() == False

    def test_three_card_blackjack_detection(self):
        """Тест, что три карты не могут быть блэкджеком"""
        hand = Hand()
        hand.add_card(Card("Hearts", "A", 11))
        hand.add_card(Card("Diamonds", "5", 5))
        hand.add_card(Card("Clubs", "5", 5))

        assert hand.is_blackjack() == False

    def test_bust_detection(self, busted_hand):
        """Тест обнаружения перебора"""
        assert busted_hand.is_busted() == True

    def test_non_bust_hand(self, sample_hand):
        """Тест, что рука без перебора правильно определяется"""
        sample_hand.add_card(Card("Hearts", "10", 10))
        sample_hand.add_card(Card("Diamonds", "7", 7))

        assert sample_hand.is_busted() == False

    def test_ace_adjustment_soft_hand(self, soft_hand):
        """Тест корректировки туза в мягкой руке"""
        # Мягкая рука: A(11) + 6 = 17
        assert soft_hand.value == 17

        # Добавляем карту, вызывающую перебор
        soft_hand.add_card(Card("Clubs", "10", 10))
        # Рука должна скорректироваться: A(1) + 6 + 10 = 17
        assert soft_hand.value == 17
        assert soft_hand.aces == 0  # Все тузы скорректированы

    def test_multiple_aces_adjustment(self):
        """Тест корректировки нескольких тузов"""
        hand = Hand()
        hand.add_card(Card("Hearts", "A", 11))
        hand.add_card(Card("Diamonds", "A", 11))
        hand.add_card(Card("Clubs", "9", 9))

        # A(11) + A(11) + 9 = 31 -> перебор
        # Корректировка: A(1) + A(11) + 9 = 21
        assert hand.value == 21
        assert hand.aces == 1  # Один туз остался как 11

    def test_hand_string_representation(self, sample_hand):
        """Тест строкового представления руки"""
        sample_hand.add_card(Card("Hearts", "10", 10))
        sample_hand.add_card(Card("Diamonds", "J", 10))

        expected = "10 of Hearts, J of Diamonds"
        assert str(sample_hand) == expected

    def test_empty_hand_string(self, sample_hand):
        """Тест строкового представления пустой руки"""
        assert str(sample_hand) == ""

    @pytest.mark.parametrize(
        "cards,expected_value,expected_blackjack,expected_busted",
        [
            ([("A", 11), ("K", 10)], 21, True, False),  # Блэкджек
            ([("10", 10), ("9", 9), ("3", 3)], 22, False, True),  # Перебор
            ([("A", 11), ("5", 5), ("A", 11)], 17, False, False),  # Два туза
            ([("7", 7), ("8", 8)], 15, False, False),  # Обычная рука
            ([("A", 11), ("A", 11), ("A", 11), ("8", 8)], 21, False, False),  # Три туза
        ],
    )
    def test_various_hand_scenarios(
        self, cards, expected_value, expected_blackjack, expected_busted
    ):
        """Параметризованный тест различных сценариев руки"""
        hand = Hand()
        for rank, value in cards:
            hand.add_card(Card("Hearts", rank, value))

        assert hand.value == expected_value
        assert hand.is_blackjack() == expected_blackjack
        assert hand.is_busted() == expected_busted
