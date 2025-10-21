from abc import ABC, abstractmethod
from random import randint


class Player:
    def __init__(self, balance, age, strategy, name="Unknown"):
        if age < 18:
            raise ValueError("Player must be over 18 years old")
        self._name = name
        self.balance = balance
        self._age = age
        self.strategy = strategy
        self.current_bets = []


class Bet:
    VALID_TYPES = ["number", "color", "even_odd", "dozen", "column", "half"]

    def __init__(self, type_bet, bet_value, sum_bet):
        self.type_bet = type_bet
        self.bet_value = bet_value
        self.sum_bet = sum_bet
        self._validate_bet()

    def _validate_bet(self):
        if self.type_bet not in self.VALID_TYPES:
            raise ValueError(f"Invalid bet type: {self.type_bet}")

        if self.type_bet == "number" and self.bet_value not in range(37):
            raise ValueError("Number must be 0-36")
        elif self.type_bet == "color" and self.bet_value not in ["red", "black"]:
            raise ValueError("Color must be 'red' or 'black'")
        elif self.type_bet == "even_odd" and self.bet_value not in ["even", "odd"]:
            raise ValueError("Even/Odd must be 'even' or 'odd'")
        elif self.type_bet == "dozen" and self.bet_value not in ["1st", "2nd", "3rd"]:
            raise ValueError("Dozen must be '1st', '2nd' or '3rd'")
        elif self.type_bet == "column" and self.bet_value not in [1, 2, 3]:
            raise ValueError("Column must be 1, 2 or 3")
        elif self.type_bet == "half" and self.bet_value not in ["1-18", "19-36"]:
            raise ValueError("Half must be '1-18' or '19-36'")


class Strategy(ABC):
    @abstractmethod
    def make_bet(self, player):
        """Должен возвращать объект Bet"""
        pass


class ConservativeStrategy(Strategy):
    def __init__(self):
        self.last_color = "black"

    def make_bet(self, player):
        color = "red" if self.last_color == "black" else "black"
        self.last_color = color

        amount = max(1, int(player.balance * 0.1))

        return Bet("color", color, amount)


class RiskStrategy(Strategy):
    def make_bet(self, player):
        number = randint(0, 36)

        amount = max(1, int(player.balance * 0.1))

        return Bet("number", number, amount)


class MegaRiskStrategy(Strategy):
    def make_bet(self, player):

        amount = max(1, int(player.balance * 0.5))

        return Bet("number", 0, amount)


class MathematicalStrategy(Strategy):
    def __init__(self):
        self.last_bet_amount = 1
        self.last_color = "red"
        self.last_win = True

    def make_bet(self, player):
        if not self.last_win:
            self.last_bet_amount *= 2
        else:
            self.last_bet_amount = 1

        self.last_color = "black" if self.last_color == "red" else "red"

        amount = min(self.last_bet_amount, player.balance)
        if amount <= 0:
            amount = 1

        return Bet("color", self.last_color, amount)

    def update_result(self, won):
        self.last_win = won


class RouletteWheel:
    def __init__(self):
        self.red_numbers = [
            1,
            3,
            5,
            7,
            9,
            12,
            14,
            16,
            18,
            19,
            21,
            23,
            25,
            27,
            30,
            32,
            34,
            36,
        ]
        self.black_numbers = [
            2,
            4,
            6,
            8,
            10,
            11,
            13,
            15,
            17,
            20,
            22,
            24,
            26,
            28,
            29,
            31,
            33,
            35,
        ]

    def spin(self):
        winning_number = randint(0, 36)
        return {
            "number": winning_number,
            "color": self._get_color(winning_number),
            "is_even": self._is_even(winning_number),
            "range": self._get_range(winning_number),
        }

    def _get_color(self, number):
        if number == 0:
            return "green"

        elif number in self.black_numbers:
            return "black"

        elif number in self.red_numbers:
            return "red"

    def _is_even(self, number):
        return number % 2 == 0 if number != 0 else False

    def _get_range(self, number):
        if number == 0:
            return "zero"
        elif 1 <= number <= 18:
            return "1-18"
        else:
            return "19-36"


class RouletteGame:
    def __init__(self, players, max_rounds=20):
        self.players = players
        self.max_rounds = max_rounds
        self.current_round = 0
        self.wheel = RouletteWheel()
        self.history = []

    def play_round(self):
        if self.is_game_over():
            return False

        self.current_round += 1
        print(f"\n=-=-=-=-=Round {self.current_round}=-=-=-=-=")

        current_bets = {}
        for player in self.players:
            if player.balance > 0:
                bet = player.strategy.make_bet(player)
                if bet.sum_bet > player.balance:
                    bet.sum_bet = player.balance
                player.balance -= bet.sum_bet
                player.current_bets.append(bet)
                current_bets[player] = bet
                print(
                    f"{player._name} puts {bet.sum_bet} on {bet.type_bet} {bet.bet_value}"
                )
            else:
                print(f"{player._name} dropped out")
                current_bets[player] = None

        winning_result = self.wheel.spin()
        print(f"Came up: {winning_result['number']} ({winning_result['color']})")

        for player, bet in current_bets.items():
            if bet is not None:
                winnings = self._calculate_winnings(bet, winning_result)
                player.balance += winnings
                if winnings > 0:
                    print(f"{player._name} won {winnings}!")
                player.current_bets = []

                if hasattr(player.strategy, "update_result"):
                    player.strategy.update_result(winnings > 0)

        round_info = {
            "round": self.current_round,
            "winning_number": winning_result["number"],
            "bets": current_bets,
            "player_balances": {
                player._name: player.balance for player in self.players
            },
        }
        self.history.append(round_info)

        return True

    def _calculate_winnings(self, bet, winning_result):
        winning_number = winning_result["number"]

        if bet.type_bet == "number":
            if bet.bet_value == winning_number:
                return bet.sum_bet * 35
            else:
                return 0

        elif bet.type_bet == "color":
            if bet.bet_value == winning_result["color"]:
                return bet.sum_bet * 2
            else:
                return 0

        elif bet.type_bet == "even_odd":
            actual_result = "even" if winning_result["is_even"] else "odd"
            if bet.bet_value == actual_result:
                return bet.sum_bet * 2
            else:
                return 0

        elif bet.type_bet == "dozen":
            if bet.bet_value == "1st" and 1 <= winning_number <= 12:
                return bet.sum_bet * 3
            elif bet.bet_value == "2nd" and 13 <= winning_number <= 24:
                return bet.sum_bet * 3
            elif bet.bet_value == "3rd" and 25 <= winning_number <= 36:
                return bet.sum_bet * 3
            else:
                return 0

        elif bet.type_bet == "column":
            if bet.bet_value == 1 and winning_number % 3 == 1 and winning_number != 0:
                return bet.sum_bet * 3
            elif bet.bet_value == 2 and winning_number % 3 == 2 and winning_number != 0:
                return bet.sum_bet * 3
            elif bet.bet_value == 3 and winning_number % 3 == 0 and winning_number != 0:
                return bet.sum_bet * 3
            else:
                return 0

        elif bet.type_bet == "half":
            if bet.bet_value == winning_result["range"]:
                return bet.sum_bet * 2
            else:
                return 0

        return 0

    def is_game_over(self):
        if self.current_round >= self.max_rounds:
            return True

        all_bankrupt = all(player.balance <= 0 for player in self.players)
        if all_bankrupt:
            return True

        return False
