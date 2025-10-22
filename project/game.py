from random import randint
from typing import Tuple, List, Optional, Dict

class Ruller:
    ''' for genereting roulette '''
    def __init__(self, color_cur: Optional[str] = None, number_cur: Optional[int] = None) -> None:
        self.numbers: List[int] = list(range(0, 37))
        self.number_cur: Optional[int] = number_cur
        self.color_cur: Optional[str] = color_cur

    def ruller_spin(self) -> Tuple[int, str]:
        ''' spin roulette '''
        self.number_cur = randint(0, 36)
        self.color_cur = self.ruller_color(self.number_cur)
        return self.number_cur, self.color_cur

    def ruller_color(self, numb: int) -> str:
        ''' gettig color'''
        if numb == 0:
            return 'green'
        elif numb % 2 == 0:
            return 'red'
        else:
            return 'black'

    def get_result(self) -> Tuple[Optional[int], Optional[str]]:
        return self.number_cur, self.color_cur

class Bots:
    ''' for genereting players '''
    def __init__(self, number1_b: Optional[int] = None, number2_b: Optional[int] = None) -> None:
        self.diapason: List[int] = []
        self.color_b: Optional[str] = None
        self.indicator: int = randint(1, 3)
        self.ifwin: bool = False
        self.number1_b: int = number1_b if number1_b is not None else randint(0, 36)
        self.number2_b: int = number2_b if number2_b is not None else randint(0, 36)

    def choice(self) -> Tuple[str, List[int]]:
        self.number1_b = randint(0, 30)
        self.number2_b = randint(self.number1_b + 1, 36)
      
        self.diapason = []
        ''' feel the range according to the numbers choicen by bots '''
        if self.number2_b != 0:
            for number in range(self.number1_b, self.number2_b + 1):
                self.diapason.append(number)
        else:
            self.diapason.append(self.number1_b)
        self.color_b = self.color_choice()
        return self.color_b, self.diapason

    def color_choice(self) -> str:
        ''' find the len of range to choose color '''
        temp_diapason: List[int] = []
        if self.number2_b != 0:
            for number in range(self.number1_b, self.number2_b + 1):
                temp_diapason.append(number)
        else:
            temp_diapason.append(self.number1_b)

        color_indicator: int
        if len(temp_diapason) == 1:
            color_indicator = randint(1, 2)
        else:
            color_indicator = randint(1, 3)

        if color_indicator == 1:
            return 'red'
        elif color_indicator == 2:
            return 'black'
        else:
            return 'green'

    def get_choice(self) -> List[int]:
        return self.diapason

class Bet777:
    ''' class for bets '''
    def __init__(self, money: int = 1000, xbet: int = 100) -> None:
        self.money: int = money
        self.xbet: int = xbet

    def capital(self, money: int) -> None:
        self.money = money

    def bet(self, xbet: int) -> None:
        self.xbet = xbet

    def get_choice(self) -> Tuple[int, int]:
        return self.money, self.xbet

class Strategies:
    @staticmethod
    def choose_strategy(curva_bet: int, ifwin: bool, money: int, indicator: Optional[int] = None) -> int:
        actual_indicator = randint(1, 3)
        '''We choose one of the possible strategies'''
        if actual_indicator == 1:
            result_bet: int = Strategies.dalamber(curva_bet, ifwin, money) 
        elif actual_indicator == 2:
            result_bet = Strategies.martingeil(curva_bet, ifwin, money)
        else:
            result_bet = Strategies.all_capital(curva_bet, ifwin, money)
        return result_bet

    @staticmethod
    def dalamber(curva_bet: int, ifwin: bool, money: Optional[int] = None) -> int:
        ''' Dalamber strategy '''
        if ifwin:
            return max(0, curva_bet - 100)
        else:
            return curva_bet + 100

    @staticmethod
    def martingeil(curva_bet: int, ifwin: bool, money: Optional[int] = None) -> int:
        '''Martengeil strategy'''
        if not ifwin:
            return curva_bet * 2
        else:
            return curva_bet

    @staticmethod
    def all_capital(curva_bet: int, ifwin: bool, money: int) -> int:
        ''' strategy all or nothing'''
        if ifwin:
            return max(0, money - curva_bet)
        else:
            return money

class Game:
    def __init__(self) -> None:
        '''create bots with initial money and bets'''
        self.bot1: Bots = Bots()
        self.bot2: Bots = Bots()
        self.bet1: Bet777 = Bet777()  
        self.bet2: Bet777 = Bet777()
        self.roulette: Ruller = Ruller()

        '''Initializing game parameters'''
        self.flag: int = 0
        self.indicator: int = randint(1, 3)
        self.ifwin: bool = False
        self.gain: int = 0

        '''Making initial bot selections'''
        self.bot1.choice()
        self.bot2.choice()
        print("~ Начало игры ~")

    def full_money(self) -> int:
        return self.bet1.xbet + self.bet2.xbet

    def apply_strategy_to_bot(self, bot_number: int) -> int:
        ''' choose strategy '''
        if bot_number == 1:
            current_bot_bet: Bet777 = self.bet1
            current_bot: Bots = self.bot1
        else:
            current_bot_bet = self.bet2
            current_bot = self.bot2

        new_bet_value: int = Strategies.choose_strategy(
            curva_bet = current_bot_bet.xbet,
            ifwin = current_bot.ifwin,
            money = current_bot_bet.money,
            indicator = current_bot.indicator
        )
        current_bot_bet.bet(new_bet_value)
        return new_bet_value

    def play_round(self, bot_number: int) -> None:
        ''' start 1 raund for choicen bot '''
        print(f"Ход для Бота{bot_number} ---")

        current_new_bet: int = self.apply_strategy_to_bot(bot_number)
        print(f"Бот{bot_number} сделал ставку: {current_new_bet}")

        if bot_number == 1:
            current_bot_choice: Tuple[str, List[int]] = self.bot1.choice()
        else:
            current_bot_choice = self.bot2.choice()
        print(f"Бот{bot_number} выбрал: {current_bot_choice}")

        roulette_result: Tuple[int, str] = self.roulette.ruller_spin()
        print(f"Рулетка выпала: число {roulette_result[0]}, цвет {roulette_result[1]}")

        self.check_win(bot_number, roulette_result)

    def check_win(self, bot_number: int, roulette_result: Tuple[int, str]) -> None:
        ''' checking if bot win'''
        strategies: Dict[int, str] = {1: "Даламбер", 2: "Мартингейл", 3: "Все в игру"}
        if bot_number == 1:
            current_bot: Bots = self.bot1
            current_bot_bet: Bet777 = self.bet1
        else:
            current_bot = self.bot2
            current_bot_bet = self.bet2
    
        bot_choice: List[int] = current_bot.get_choice()
    
        if len(bot_choice) == 1:
            if current_bot.color_b == roulette_result[1] and (roulette_result[0] in bot_choice):
                self.gain = self.full_money()
                self.ifwin = True
                print(f'  Полное попадание!')
                print(f" - была выбрана стратегия {strategies[current_bot.indicator]}, капитал теперь {current_bot_bet.money}\n")
            else:
                self.gain = 0
                self.ifwin = False
                print(f'  Было близко...')
                print(f" - была выбрана стратегия {strategies[current_bot.indicator]}, капитал теперь {current_bot_bet.money + self.gain - current_bot_bet.xbet}\n")       
        else:
            if (roulette_result[0] in bot_choice) and (roulette_result[1] == current_bot.color_b):
                self.gain = int(self.full_money() * 0.75)
                self.ifwin = True
                print(f'  Попал в диапазон и угадал с цветом')
                print(f" - была выбрана стратегия {strategies[current_bot.indicator]}, капитал теперь {current_bot_bet.money + self.gain - current_bot_bet.xbet}\n")
            elif (roulette_result[0] in bot_choice) and (roulette_result[1] != current_bot.color_b):
                self.gain = int(self.full_money() * 0.5)
                self.ifwin = False
                print(f'  Попал в диапазон, но цвет мимо')
                print(f" - была выбрана стратегия {strategies[current_bot.indicator]}, капитал теперь {current_bot_bet.money + self.gain - current_bot_bet.xbet}\n")
            else:
                self.gain = 0
                self.ifwin = False
                print(f'  Ни одного попадания!')
                print(f" - была выбрана стратегия {strategies[current_bot.indicator]}, капитал теперь {current_bot_bet.money + self.gain - current_bot_bet.xbet}\n")

        current_bot_bet.money += self.gain - current_bot_bet.xbet

    def play_game(self, max_rounds: int = 30) -> None:
        '''game start'''
        print(f"Начальные деньги: Бот1 - ${self.bet1.money}, Бот2 - ${self.bet2.money}")

        round_count: int = 0
        while (self.bet1.money > 0 and self.bet2.money > 0 and round_count < max_rounds):
            self.flag += 1
            round_count += 1
            print(f"Раунд {round_count}:")

            if self.flag % 2 != 0:
                self.play_round(1)
            else:
                self.play_round(2)

            ''' check end'''
            if self.bet1.money <= 0:
                print("Бот1 обанкротился!")
                break
            if self.bet2.money <= 0:
                print("Бот2 обанкротился!")
                break

        self.declare_winner()

    def declare_winner(self) -> None:
        ''' to find the winner'''
        print(" ~ игра окончена ~ ")
        if self.bet1.money > self.bet2.money:
            print(f"Победил: Бот1 с ${self.bet1.money}!")
        elif self.bet2.money > self.bet1.money:
            print(f"Победил:) Бот2 с ${self.bet2.money}!")
        else:
            print(f"Ничья :( Оба бота имеют по ${self.bet1.money}")
