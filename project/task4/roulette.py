from abc import ABC, abstractmethod
from random import randint
from typing import List, Dict, Any, Optional

"""
Roulette game implementation with bots and various strategies.
"""


class Player:
    """Class representing a player in the roulette game.

    Parameters:
        balance (int): Player balance
        age (int): Player age (must be 18 or older)
        strategy (Strategy): Strategy object
        name (str): Player name, default "Unknown"

    Raises:
        ValueError: If age is less than 18

    Attributes:
        _name (str): Player name
        balance (int): Current player balance
        _age (int): Player age
        strategy (Strategy): Betting strategy
        current_bets (List[Bet]): List of current active bets
    """

    def __init__(
        self, balance: int, age: int, strategy: "Strategy", name: str = "Unknown"
    ):
        if age < 18:
            raise ValueError("Player must be over 18 years old")
        self._name = name
        self.balance = balance
        self._age = age
        self.strategy = strategy
        self.current_bets: List["Bet"] = []


class Bet:
    """Class a bet in roulette.

    Parameters:
        bet_type (str): Type of bet ('number', 'color', 'even_odd', 'dozen', 'column', 'half')
        bet_value (Any): Value of the bet
        amount (int): Amount of the bet

    Raises:
        ValueError: If bet type or value is invalid

    Attributes:
        bet_type (str): Type of bet
        bet_value (Any): Bet value
        amount (int): Bet amount
    """

    VALID_TYPES = ["number", "color", "even_odd", "dozen", "column", "half"]

    def __init__(self, type_bet: str, bet_value: Any, sum_bet: int):
        self.type_bet = type_bet
        self.bet_value = bet_value
        self.sum_bet = sum_bet
        self._validate_bet()

    def _validate_bet(self) -> None:
        """Validates bet type and value

        Raises:
            ValueError: If bet parameters are invalid
        """
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
    """Abstract base class for betting strategies

    All strategy classes must implement the make_bet method
    """

    @abstractmethod
    def make_bet(self, player: Player) -> Bet:
        """Creates a strategy logic.

        Parameters:
            player (Player): Player object containing current game state

        Returns:
            Bet: Bet object with type, value and amount
        """
        pass


class ConservativeStrategy(Strategy):
    """Conservative betting strategy

    This strategy alternates between red and black colors and bets 10% of balance.

    Attributes:
        last_color (str): Last color bet
    """

    def __init__(self):
        self.last_color = "black"

    def make_bet(self, player: Player) -> Bet:
        """Makes a conservative bet

        Parameters:
            player (Player): Player object with current balance

        Returns:
            Bet: Color bet
        """
        color = "red" if self.last_color == "black" else "black"
        self.last_color = color

        amount = max(1, int(player.balance * 0.1))

        return Bet("color", color, amount)


class RiskStrategy(Strategy):
    """Risky betting strategy

    This strategy selects random numbers (0-36) and bets 10% of balance.
    """

    def make_bet(self, player: Player) -> Bet:
        """Makes a risky bet

        Parameters:
            player (Player): Player object with current balance

        Returns:
            Bet: Number bet
        """
        number = randint(0, 36)

        amount = max(1, int(player.balance * 0.1))

        return Bet("number", number, amount)


class MegaRiskStrategy(Strategy):
    """Very risky strategy

    This strategy always bets on number zero with 50% of current balance.
    """

    def make_bet(self, player: Player) -> Bet:
        """Makes a very risky bet on number zero.

        Parameters:
            player (Player): Player object with current balance

        Returns:
            Bet: Number bet
        """
        amount = max(1, int(player.balance * 0.5))
        return Bet("number", 0, amount)


class MathematicalStrategy(Strategy):
    """Mathematical strategy Martingale

    This strategy doubles the bet after losses and resets after wins.
    Bets on alternating colors.

    Attributes:
        last_bet_amount (int): Amount of last bet
        last_color (str): Last color bet
        last_win (bool): Result of last bet
    """

    def __init__(self):
        self.last_bet_amount = 1
        self.last_color = "red"
        self.last_win = True

    def make_bet(self, player: Player) -> Bet:
        """Makes bet using Martingale

        Parameters:
            player (Player): Player object with current balance

        Returns:
            Bet: Color bet
        """
        if not self.last_win:
            self.last_bet_amount *= 2
        else:
            self.last_bet_amount = 1

        self.last_color = "black" if self.last_color == "red" else "red"

        amount = min(self.last_bet_amount, player.balance)
        if amount <= 0:
            amount = 1

        return Bet("color", self.last_color, amount)

    def update_result(self, won: bool) -> None:
        """Updates strategy with result of last bet.

        Parameters:
            won (bool): True if last bet won, else False
        """
        self.last_win = won


class RouletteWheel:
    """Class representing a roulette wheel.

    Attributes:
        red_numbers (List[int]): List of red numbers
        black_numbers (List[int]): List of black numbers
    """

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

    def spin(self) -> Dict[str, Any]:
        """Spins the roulette wheel

        Returns:
            Dict: Dictionary containing:
                - number (int): Winning number
                - color (str): 'red', 'black', or 'green' for 0
                - is_even (bool): True if even number, False if odd or zero
                - range (str): 'zero', '1-18', or '19-36'
        """
        winning_number = randint(0, 36)
        return {
            "number": winning_number,
            "color": self._get_color(winning_number),
            "is_even": self._is_even(winning_number),
            "range": self._get_range(winning_number),
        }

    def _get_color(self, number: int) -> str:
        """Determines color

        Parameters:
            number (int): Winning number

        Returns:
            str: 'green' for 0, 'red' or 'black' for other numbers
        """

        if number in self.black_numbers:
            return "black"

        elif number in self.red_numbers:
            return "red"

        else:
            return "green"

    def _is_even(self, number: int) -> bool:
        """Checks if number is even.

        Parameters:
            number (int): Number to check

        Returns:
            bool: True if even and not zero, else False
        """
        return number % 2 == 0 if number != 0 else False

    def _get_range(self, number: int) -> str:
        """Determines range

        Parameters:
            number (int): Winning number

        Returns:
            str: 'zero' for 0, '1-18' for numbers 1-18, '19-36' for numbers 19-36
        """
        if number == 0:
            return "zero"
        elif 1 <= number <= 18:
            return "1-18"
        else:
            return "19-36"


class RouletteGame:
    """Main game class

    Parameters:
        players (List[Player]): List of players
        max_rounds (int): Maximum number of rounds, defaults 20

    Attributes:
        players (List[Player]): List of players
        max_rounds (int): Maximum rounds
        current_round (int): Current round number
        wheel (RouletteWheel): Roulette wheel
        history (List[Dict]): History of all rounds
    """

    def __init__(self, players: List[Player], max_rounds: int = 20):
        self.players = players
        self.max_rounds = max_rounds
        self.current_round = 0
        self.wheel = RouletteWheel()
        self.history: List[Dict[str, Any]] = []

    def play_round(self) -> bool:
        """Plays one complete round

        1) Players make bets
        2) Wheel is spun to determine winning number
        3) Winnings are calculated
        4) Game state is updated

        Returns:
            bool: True if game continues, False if game is over
        """
        if self.is_game_over():
            return False

        self.current_round += 1
        print(f"\n=-=-=-=-=Round {self.current_round}=-=-=-=-=")

        active_players_bets: Dict[Player, Bet] = {}
        bankrupt_players: List[Player] = []

        for player in self.players:
            if player.balance > 0:
                player_bet = player.strategy.make_bet(player)
                if player_bet.sum_bet > player.balance:
                    player_bet.sum_bet = player.balance
                player.balance -= player_bet.sum_bet
                player.current_bets.append(player_bet)
                active_players_bets[player] = player_bet
                print(
                    f"{player._name} puts {player_bet.sum_bet} on {player_bet.type_bet} {player_bet.bet_value}"
                )
            else:
                print(f"{player._name} dropped out")
                bankrupt_players.append(player)

        if not active_players_bets:
            print("No active players remaining!")
            return False

        winning_result = self.wheel.spin()
        print(f"Came up: {winning_result['number']} ({winning_result['color']})")

        for player, bet in active_players_bets.items():
            winnings = self._calculate_winnings(bet, winning_result)
            player.balance += winnings
            if winnings > 0:
                print(f"{player._name} won {winnings}!")
            player.current_bets = []

            if hasattr(player.strategy, "update_result"):
                player.strategy.update_result(winnings > 0)

        all_bets_info: Dict[Player, Optional[Bet]] = {**active_players_bets}
        for player in bankrupt_players:
            all_bets_info[player] = None

        round_info = {
            "round": self.current_round,
            "winning_number": winning_result["number"],
            "bets": all_bets_info,
            "player_balances": {
                player._name: player.balance for player in self.players
            },
        }
        self.history.append(round_info)

        return True

    def _calculate_winnings(self, bet: Bet, winning_result: Dict[str, Any]) -> int:
        """Calculates winnings for a bet

        Parameters:
            bet (Bet): Bet to calculate winnings for
            winning_result (Dict): Result from roulette wheel spin

        Returns:
            int: Amount won
        """
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
            return bet.sum_bet * 2 if bet.bet_value == winning_result["range"] else 0

        return 0

    def show_game_state(self) -> None:
        """Displays current state of all players

        Shows each player's name, balance, and status
        """
        print(f"\n--- Game State after Round {self.current_round} ---")
        for player in self.players:
            status = "BANKRUPT" if player.balance <= 0 else f"balance: {player.balance}"
            print(f"  {player._name}: {status}")

    def is_game_over(self) -> bool:
        """Determines if the game should end

        Checks:
        1) Maximum rounds reached
        2) All players are bankrupt

        Returns:
            bool: True if game ends, else False
        """
        if self.current_round >= self.max_rounds:
            return True

        all_bankrupt = all(player.balance <= 0 for player in self.players)
        if all_bankrupt:
            return True

        return False
