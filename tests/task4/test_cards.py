import pytest
from project.task4.core.card import Card


@pytest.mark.unit
class TestCard:
    """Тесты для класса Card"""

    @pytest.mark.unit
    def test_card_creation(self, sample_card):
        """Тест создания карты"""
        assert sample_card.suit == "Hearts"
        assert sample_card.rank == "A"
        assert sample_card.value == 11

    def test_card_string_representation(self):
        """Тест строкового представления карты"""
        card = Card("Spades", "Q", 10)
        assert str(card) == "Q of Spades"

    def test_card_repr_representation(self):
        """Тест repr представления карты"""
        card = Card("Diamonds", "7", 7)
        assert repr(card) == "Card('Diamonds', '7', 7)"

    def test_card_equality(self):
        """Тест сравнения карт"""
        card1 = Card("Hearts", "10", 10)
        card2 = Card("Hearts", "10", 10)
        card3 = Card("Spades", "10", 10)

        assert card1 == card2
        assert card1 != card3

    def test_different_suits_same_rank(self):
        """Тест карт с одинаковым рангом но разными мастями"""
        heart_ace = Card("Hearts", "A", 11)
        spade_ace = Card("Spades", "A", 11)

        assert heart_ace.rank == spade_ace.rank
        assert heart_ace.value == spade_ace.value
        assert heart_ace.suit != spade_ace.suit

    def test_face_cards_value(self):
        """Тест значений карт с картинками"""
        jack = Card("Hearts", "J", 10)
        queen = Card("Hearts", "Q", 10)
        king = Card("Hearts", "K", 10)

        assert jack.value == 10
        assert queen.value == 10
        assert king.value == 10

    def test_ace_card_value(self):
        """Тест значения туза"""
        ace = Card("Hearts", "A", 11)
        assert ace.value == 11

    def test_number_cards_value(self):
        """Тест значений числовых карт"""
        for rank, expected_value in [("2", 2), ("5", 5), ("9", 9)]:
            card = Card("Hearts", rank, expected_value)
            assert card.value == expected_value

    @pytest.mark.parametrize(
        "suit,rank,value,expected_str",
        [
            ("Hearts", "A", 11, "A of Hearts"),
            ("Spades", "10", 10, "10 of Spades"),
            ("Diamonds", "K", 10, "K of Diamonds"),
            ("Clubs", "7", 7, "7 of Clubs"),
        ],
    )
    def test_various_cards_strings(self, suit, rank, value, expected_str):
        """Параметризованный тест строкового представления различных карт"""
        card = Card(suit, rank, value)
        assert str(card) == expected_str
