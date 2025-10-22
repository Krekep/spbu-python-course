import pytest
from game import Ruller, Bots, Bet777, Strategies, Game


class TestRuller:
    @pytest.mark.parametrize("number,expected_color", [
        (0, 'green'),
        (2, 'red'),
        (4, 'red'), 
        (1, 'black'),
        (3, 'black'),
        (15, 'black'),
        (10, 'red')
    ])
    def test_ruller_color(self, number, expected_color):
        'to test color'
        r = Ruller()
        assert r.ruller_color(number) == expected_color
    
    def test_ruller_spin(self):
        'to test diapason'
        r = Ruller()
        for _ in range(100):
            number, color = r.ruller_spin()
            assert 0 <= number <= 36
            assert color in ['green', 'red', 'black']
          

class TestBots:
    def test_bots_choice(self):
        'if diapason exist'
        bot = Bots()
        color, diapason = bot.choice()
        assert isinstance(diapason, list)
        assert len(diapason) > 0
        assert color in ['red', 'black', 'green']
    
    def test_get_choice(self):
        'if metod return diapason'
        bot = Bots()
        bot.diapason = [1, 2, 3]
        assert bot.get_choice() == [1, 2, 3]
      

class TestBet777:
    def test_capital_method(self):
        bet = Bet777()
        bet.capital(500)
        assert bet.money == 500
    
    def test_bet_method(self):
        bet = Bet777()
        bet.bet(300)
        assert bet.xbet == 300
      

class TestStrategies:
  
    @pytest.mark.parametrize("curva_bet,ifwin,expected", [
        (200, True, 100),
        (200, False, 300),
        (50, True, 0),
    ])
    def test_dalamber_strategy(self, curva_bet, ifwin, expected):
        result = Strategies.dalamber(curva_bet, ifwin)
        assert result == expected
    
    @pytest.mark.parametrize("curva_bet,ifwin,expected", [
        (100, True, 100),
        (100, False, 200),
    ])
    def test_martingeil_strategy(self, curva_bet, ifwin, expected):
        result = Strategies.martingeil(curva_bet, ifwin)
        assert result == expected
    
    @pytest.mark.parametrize("curva_bet,ifwin,money,expected", [
        (100, True, 1000, 900),
        (100, False, 1000, 1000),
    ])
    def test_all_capital_strategy(self, curva_bet, ifwin, money, expected):
        result = Strategies.all_capital(curva_bet, ifwin, money)
        assert result == expected
    

class TestGame:
    def test_full_money(self):
        game = Game()
        game.bet1.xbet = 150
        game.bet2.xbet = 200
        assert game.full_money() == 350            
