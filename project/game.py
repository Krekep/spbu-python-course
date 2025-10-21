from random import randint

class Ruller:
    ''' for genereting roulette '''
    def __init__(self, color_cur = None, number_cur = None):
        self.numbers = list(range(0, 37))

    def ruller_spin(self):
        ''' spin roulette '''
        self.number_cur = randint(0, 37)
        self.color_cur = self.ruller_color(self.number_cur)
        return self.number_cur, self.color_cur

    def ruller_color(self, numb):
        ''' gettig color'''
        if numb%2 == 0 and numb != 0:
            return 'red'
        elif numb%2 != 0:
            return 'black'
        else:
            return 'green'

    def get_result(self, number_cur, color_cur):
        return self.number_cur, self.color_cur

class Bots:
    ''' for genereting players '''
    def __init__(self, number1_b=None, number2_b=None):
        self.diapason = []
        self.color_b = None
        self.indicator = randint(1, 3)
        self.ifwin = False

    def choice(self):
        self.number1_b = randint(0, 30)
        self.number2_b = randint(self.number1_b + 1, 36)
      
        self.diapason = []
        ''' feel the range according to the numbers choicen by bots '''
        if self.number2_b and self.number2_b != 0:
            for number in range(self.number1_b, self.number2_b + 1):
                self.diapason.append(number)
        else:
            self.diapason.append(self.number1_b)
        self.color_b = self.color_choice()
        return self.color_b, self.diapason

    def color_choice(self):
        ''' find the len of range to choose color '''
        temp_diapason = []
        if self.number2_b and self.number2_b != 0:
            for number in range(self.number1_b, self.number2_b + 1):
                temp_diapason.append(number)
        else:
            temp_diapason.append(self.number1_b)

        if len(temp_diapason) == 1:
            indicator = randint(1, 2)
        else:
            indicator = randint(1, 3)

        if indicator == 1:
            return 'red'
        elif indicator == 2:
            return 'black'
        else:
            return 'green'

    def get_choice(self):
        return self.diapason

    def show_guys(self):
        print(f'Diapason: {self.diapason}, Color: {self.color_b}')

class Bet777:
    ''' class for bets '''
    def __init__(self, money=1000, xbet=100):
        self.money = money
        self.xbet = xbet

    def capital(self, money):
        self.money = money

    def bet(self, xbet):
        self.xbet = xbet

    def get_choice(self):
        return self.money, self.xbet

class Strategies:
    @staticmethod
    def choose_strategy(curva_bet, ifwin, money=None, indicator=None):
        indicator = randint(1, 3)
        '''We choose one of the possible strategies'''
        if indicator == 1:
            xbet = Strategies.dalamber(curva_bet, ifwin, money)
        elif indicator == 2:
            xbet = Strategies.martingeil(curva_bet, ifwin, money)
        else:
            xbet = Strategies.all_capital(curva_bet, ifwin, money)
        return xbet

    @staticmethod
    def dalamber(curva_bet, ifwin, money=None):
        ''' Dalamber strategy '''
        if ifwin:
            if (curva_bet - 100)> 0: return (curva_bet - 100)
            else: return curva_bet
        else:
            return curva_bet + 100

    @staticmethod
    def martingeil(curva_bet, ifwin, money=None):
        '''Martengeil strategy'''
        if not ifwin:
            return curva_bet * 2
        else:
            return curva_bet

    @staticmethod
    def all_capital(curva_bet, ifwin, money=None):
        ''' strategy all or nothing'''
        if money is None:
            return curva_bet

        if ifwin:
            return max(0, money - curva_bet)
        else:
            return money

class Game:
    def __init__(self):
        '''create bots with initial money and bets'''
        self.bot1 = Bots()
        self.bot2 = Bots()
        self.bet1 = Bet777()  
        self.bet2 = Bet777()
        self.roulette = Ruller()

        '''Initializing game parameters'''
        self.flag = 0
        self.indicator = randint(1, 3)
        self.ifwin = False
        self.gain = 0

        '''Making initial bot selections'''
        self.bot1.choice()
        self.bot2.choice()
        print("~ Начало игры ~")

    def full_money(self):
        return self.bet1.xbet + self.bet2.xbet

    def apply_strategy_to_bot(self, bot_number):
        ''' choose strategy '''
        if bot_number == 1:
            bot_bet = self.bet1
            bot = self.bot1
        else:
            bot_bet = self.bet2
            bot = self.bot2

        new_bet = Strategies.choose_strategy(
            curva_bet = bot_bet.xbet,
            ifwin = bot.ifwin,
            money = bot_bet.money,
            indicator = bot.indicator
        )
        bot_bet.bet(new_bet)
        return new_bet

    def play_round(self, bot_number):
        ''' start 1 raund for choicen bot '''
        print(f"Ход для Бота{bot_number} ---")

        new_bet = self.apply_strategy_to_bot(bot_number)
        print(f"Бот{bot_number} сделал ставку: {new_bet}")

        if bot_number == 1:
            bot_choice = self.bot1.choice()
        else:
            bot_choice = self.bot2.choice()
        print(f"Бот{bot_number} выбрал: {bot_choice}")

        roulette_result = self.roulette.ruller_spin()
        print(f"Рулетка выпала: число {roulette_result[0]}, цвет {roulette_result[1]}")

        self.check_win(bot_number, roulette_result)

    def check_win(self, bot_number, roulette_result):
        ''' checking if bot win'''
        strategies = {1: "Даламбер", 2: "Мартингейл", 3: "Все в игру"}
        if bot_number == 1:
            bot = self.bot1
            bot_bet = self.bet1
        else:
            bot = self.bot2
            bot_bet = self.bet2
    
        bot_choice = bot.get_choice()
    
        if len(bot_choice) == 1:
            if bot.color_b == roulette_result[1] and (roulette_result[0] in bot_choice):
                self.gain = self.full_money()
                self.ifwin = True
                print(f'  Поплное попадание!')
                print(f" - была выбрана стратегия {strategies[bot.indicator]}, капитал теперь {bot_bet.money}\n")
            else:
                self.gain = 0
                self.ifwin = False
                print(f'  Было близко...')
                print(f" - была выбрана стратегия {strategies[bot.indicator]}, капитал теперь {bot_bet.money + self.gain - bot_bet.xbet}\n")       
        else:
            if (roulette_result[0] in bot_choice) and (roulette_result[1] == bot.color_b):
                self.gain = self.full_money()*0.75
                self.ifwin = True
                print(f'  Попал в диапазон и угадал с цветом')
                print(f" - была выбрана стратегия {strategies[bot.indicator]}, капитал теперь {bot_bet.money + self.gain - bot_bet.xbet}\n")
            elif (roulette_result[0] in bot_choice) and (roulette_result[1] != bot.color_b):
                self.gain = self.full_money() * 0.5
                self.ifwin = False
                print(f'  Попал в диапазон, но цвет мимо')
                print(f" - была выбрана стратегия {strategies[bot.indicator]}, капитал теперь {bot_bet.money + self.gain - bot_bet.xbet}\n")
            else:
                self.gain = 0
                self.ifwin = False
                print(f'  Ни одного попадания!')
                print(f" - была выбрана стратегия {strategies[bot.indicator]}, капитал теперь {bot_bet.money + self.gain - bot_bet.xbet}\n")

        bot_bet.money += self.gain - bot_bet.xbet

    def play_game(self, max_rounds=30):
        '''game start'''
        print(f"Начальные деньги: Бот1 - ${self.bet1.money}, Бот2 - ${self.bet2.money}")

        round_count = 0
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

    def declare_winner(self):
        ''' to find the winner'''
        print(" ~ игра окончена ~ ")
        if self.bet1.money > self.bet2.money:
            print(f"Победил: Бот1 с ${self.bet1.money}!")
        elif self.bet2.money > self.bet1.money:
            print(f"Победил:) Бот2 с ${self.bet2.money}!")
        else:
            print(f"Ничья :( Оба бота имеют обанкротились")
