import pytest
from project.task4.core.hand import Hand
from project.task4.core.card import Card
from project.task4.strategies.conservative import ConservativeStrategy
from project.task4.strategies.aggressive import AggressiveStrategy
from project.task4.strategies.basic import BasicStrategy

@pytest.mark.unit
class TestConservativeStrategy:
    """Тесты для ConservativeStrategy"""

    @pytest.mark.unit
    
    def test_conservative_hit_low_value(self):
        """Тест консервативной стратегии: взять карту при низком значении"""
        strategy = ConservativeStrategy()
        hand = Hand()
        hand.add_card(Card("Hearts", "5", 5))
        hand.add_card(Card("Diamonds", "4", 4))
        
        dealer_card = Card("Spades", "10", 10)
        
        assert strategy.should_hit(hand, dealer_card) == True
    
    def test_conservative_stand_high_value(self):
        """Тест консервативной стратегии: остановиться при высоком значении"""
        strategy = ConservativeStrategy()
        hand = Hand()
        hand.add_card(Card("Hearts", "10", 10))
        hand.add_card(Card("Diamonds", "8", 8))
        
        dealer_card = Card("Spades", "5", 5)
        
        assert strategy.should_hit(hand, dealer_card) == False
    
    def test_conservative_stand_at_13(self):
        """Тест консервативной стратегии: остановиться на 13"""
        strategy = ConservativeStrategy()
        hand = Hand()
        hand.add_card(Card("Hearts", "10", 10))
        hand.add_card(Card("Diamonds", "3", 3))
        
        dealer_card = Card("Spades", "2", 2)
        
        assert strategy.should_hit(hand, dealer_card) == False

class TestAggressiveStrategy:
    """Тесты для AggressiveStrategy"""
    
    def test_aggressive_hit_low_value(self):
        """Тест агрессивной стратегии: взять карту при низком значении"""
        strategy = AggressiveStrategy()
        hand = Hand()
        hand.add_card(Card("Hearts", "10", 10))
        hand.add_card(Card("Diamonds", "6", 6))
        
        dealer_card = Card("Spades", "10", 10)
        
        assert strategy.should_hit(hand, dealer_card) == True
    
    def test_aggressive_hit_17_against_high_dealer(self):
        """Тест агрессивной стратегии: взять карту на 17 против сильной карты дилера"""
        strategy = AggressiveStrategy()
        hand = Hand()
        hand.add_card(Card("Hearts", "10", 10))
        hand.add_card(Card("Diamonds", "7", 7))
        
        dealer_card = Card("Spades", "10", 10)
        
        assert strategy.should_hit(hand, dealer_card) == True
    
    def test_aggressive_stand_high_value(self):
        """Тест агрессивной стратегии: остановиться при очень высоком значении"""
        strategy = AggressiveStrategy()
        hand = Hand()
        hand.add_card(Card("Hearts", "10", 10))
        hand.add_card(Card("Diamonds", "9", 9))
        
        dealer_card = Card("Spades", "2", 2)
        
        assert strategy.should_hit(hand, dealer_card) == False

class TestBasicStrategy:
    """Тесты для BasicStrategy"""
    
    def test_basic_strategy_hit_low_value(self):
        """Тест базовой стратегии: взять карту при низком значении"""
        strategy = BasicStrategy()
        hand = Hand()
        hand.add_card(Card("Hearts", "5", 5))
        hand.add_card(Card("Diamonds", "4", 4))
        
        dealer_card = Card("Spades", "10", 10)
        
        assert strategy.should_hit(hand, dealer_card) == True
    
    def test_basic_strategy_stand_high_value(self):
        """Тест базовой стратегии: остановиться при высоком значении"""
        strategy = BasicStrategy()
        hand = Hand()
        hand.add_card(Card("Hearts", "10", 10))
        hand.add_card(Card("Diamonds", "8", 8))
        
        dealer_card = Card("Spades", "5", 5)
        
        assert strategy.should_hit(hand, dealer_card) == False
    
    def test_basic_strategy_soft_hand(self):
        """Тест базовой стратегии с мягкой рукой"""
        strategy = BasicStrategy()
        hand = Hand()
        hand.add_card(Card("Hearts", "A", 11))
        hand.add_card(Card("Diamonds", "6", 6))
        
        dealer_card = Card("Spades", "9", 9)
        
        # Мягкая 17 против 9 - взять карту
        assert strategy.should_hit(hand, dealer_card) == True
    
    def test_basic_strategy_hard_12_against_dealer_2(self):
        """Тест базовой стратегии: твердая 12 против дилерской 2"""
        strategy = BasicStrategy()
        hand = Hand()
        hand.add_card(Card("Hearts", "10", 10))
        hand.add_card(Card("Diamonds", "2", 2))
        
        dealer_card = Card("Spades", "2", 2)
        
        # Твердая 12 против 2 - взять карту
        assert strategy.should_hit(hand, dealer_card) == True
    
    def test_basic_strategy_hard_16_against_dealer_10(self):
        """Тест базовой стратегии: твердая 16 против дилерской 10"""
        strategy = BasicStrategy()
        hand = Hand()
        hand.add_card(Card("Hearts", "10", 10))
        hand.add_card(Card("Diamonds", "6", 6))
        
        dealer_card = Card("Spades", "10", 10)
        
        # Твердая 16 против 10 - взять карту
        assert strategy.should_hit(hand, dealer_card) == True
    
    @pytest.mark.parametrize("player_cards,dealer_card,expected_hit", [
        # Твердые руки
        (["10", "6"], "10", True),    # 16 vs 10 - hit
        (["10", "7"], "9", False),    # 17 vs 9 - stand (по базовой стратегии)
        (["10", "8"], "6", False),    # 18 vs 6 - stand
        (["9", "9"], "7", False),     # 18 vs 7 - stand (удвоение не тестируем)
        # Мягкие руки
        (["A", "6"], "9", True),      # Мягкая 17 vs 9 - hit
        (["A", "7"], "9", True),      # Мягкая 18 vs 9 - hit (по базовой стратегии)
        (["A", "8"], "6", False),     # Мягкая 19 vs 6 - stand
    ])
    def test_basic_strategy_various_scenarios(self, player_cards, dealer_card, expected_hit):
        """Параметризованный тест различных сценариев базовой стратегии"""
        strategy = BasicStrategy()
        hand = Hand()
        
        for card_rank in player_cards:
            value = 11 if card_rank == "A" else 10 if card_rank in ["10", "J", "Q", "K"] else int(card_rank)
            hand.add_card(Card("Hearts", card_rank, value))
        
        dealer_value = 11 if dealer_card == "A" else 10 if dealer_card in ["10", "J", "Q", "K"] else int(dealer_card)
        dealer_up_card = Card("Spades", dealer_card, dealer_value)
        
        assert strategy.should_hit(hand, dealer_up_card) == expected_hit