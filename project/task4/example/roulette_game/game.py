from typing import List, Dict, Any

from project.task4.example.roulette_game.bets import Bet
from project.task4.example.roulette_game.enums import BetType, EvenOdd, Dozen
from project.task4.example.roulette_game.wheel import RouletteWheel


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

    def __init__(self, players: List, max_rounds: int = 20):
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

        active_players_bets: Dict = {}
        bankrupt_players: List = []

        for player in self.players:
            if player.balance > 0:
                player_bet = player.strategy.make_bet(player)
                if player_bet.sum_bet > player.balance:
                    player_bet.sum_bet = player.balance
                player.balance -= player_bet.sum_bet
                player.current_bets.append(player_bet)
                active_players_bets[player] = player_bet
                bet_value_str = (
                    player_bet.bet_value.value
                    if hasattr(player_bet.bet_value, "value")
                    else str(player_bet.bet_value)
                )
                print(
                    f"{player._name} puts {player_bet.sum_bet} on {player_bet.type_bet.value} {bet_value_str}"
                )
            else:
                print(f"{player._name} dropped out")
                bankrupt_players.append(player)

            if not active_players_bets:
                print("No active players remaining!")
                return False

            winning_result = self.wheel.spin()
        print(f"Came up: {winning_result['number']} ({winning_result['color'].value})")

        for player, bet in active_players_bets.items():
            winnings = self._calculate_winnings(bet, winning_result)
            player.balance += winnings
            if winnings > 0:
                print(f"{player._name} won {winnings}!")
            player.current_bets = []

            if hasattr(player.strategy, "update_result"):
                player.strategy.update_result(winnings > 0)

        all_bets_info: Dict = {**active_players_bets}
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
        winning_color = winning_result["color"]

        if bet.type_bet == BetType.NUMBER:
            return bet.sum_bet * 35 if bet.bet_value == winning_number else 0
        elif bet.type_bet == BetType.COLOR:
            return bet.sum_bet * 2 if bet.bet_value == winning_color else 0
        elif bet.type_bet == BetType.EVEN_ODD:
            actual_result = EvenOdd.EVEN if winning_result["is_even"] else EvenOdd.ODD
            return bet.sum_bet * 2 if bet.bet_value == actual_result else 0
        elif bet.type_bet == BetType.DOZEN:
            if bet.bet_value == Dozen.FIRST and 1 <= winning_number <= 12:
                return bet.sum_bet * 3
            elif bet.bet_value == Dozen.SECOND and 13 <= winning_number <= 24:
                return bet.sum_bet * 3
            elif bet.bet_value == Dozen.THIRD and 25 <= winning_number <= 36:
                return bet.sum_bet * 3
            else:
                return 0
        elif bet.type_bet == BetType.COLUMN:
            if bet.bet_value == 1 and winning_number % 3 == 1 and winning_number != 0:
                return bet.sum_bet * 3
            elif bet.bet_value == 2 and winning_number % 3 == 2 and winning_number != 0:
                return bet.sum_bet * 3
            elif bet.bet_value == 3 and winning_number % 3 == 0 and winning_number != 0:
                return bet.sum_bet * 3
            else:
                return 0
        elif bet.type_bet == BetType.HALF:
            return (
                bet.sum_bet * 2 if bet.bet_value.value == winning_result["range"] else 0
            )
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
        return all(player.balance <= 0 for player in self.players)
