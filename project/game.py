from .deck import Deck
from .dealer import Dealer
from .bot import Bot, CautiousBot, StrategicBot, ThoughtfulBot
from typing import List, Dict
from decimal import Decimal


class Game:
    """
    Represents a Blackjack game involving a dealer and multiple bots.

    Attributes:
        _deck (Deck): The deck of cards used in the game.
        _dealer (Dealer): The dealer in the game.
        _bots (List[Bot]): A list of bots playing the game.
        _round_active (bool): Indicates if a round is currently active.
        _total_rounds (int): Total number of rounds to be played.
        _current_round (int): The current round number.
        _results (dict): Dictionary to track the results of each bot.
        _last_winners (List[str]): List of winners from the last round.
    """

    def __init__(self, total_rounds: int = 5) -> None:
        """
        Initializes a new game of Blackjack with a dealer and three bots, each with a unique strategy.

        Args:
            total_rounds (int): The total number of rounds to be played.
        """
        self._deck = Deck()
        self._dealer = Dealer()
        self._bots: List[Bot] = [CautiousBot(), StrategicBot(), ThoughtfulBot()]
        self._round_active = False
        self._total_rounds = total_rounds
        self._current_round = 0
        self._results = {f"Bot {i + 1}": 0 for i in range(3)}
        self._last_winners: List[str] = []

    def start_game(self) -> None:
        """Starts the game by shuffling the deck and preparing the first round."""
        while self._current_round < self._total_rounds:
            print(f"\nStarting round {self._current_round + 1}...")
            self.play_round()
        self.display_final_results()
        print("\nEnd of the game!")

    def play_round(self) -> None:
        """Plays a single round of Blackjack."""
        self._current_round += 1
        self._round_active = True
        self._deck = Deck()
        self._deck.shuffle()

        print("\nEach player places a bet.")
        for i, bot in enumerate(self._bots):
            bot.place_bet()
            print(
                f"Bot {i + 1} places a bet of {bot._current_bet.quantize(Decimal('0.01'))}"
            )

        self._dealer.draw_initial_cards(self._deck)
        dealer_blackjack = self._dealer.hand.calculate_score() == 21
        print(f"\nDealer's initial cards:")
        self._dealer.hand.show()
        if dealer_blackjack:
            print("Dealer has a blackjack!")

        print("\nEach player is dealt two cards.")
        for i, bot in enumerate(self._bots):
            bot.hand.add_card(self._deck.deal_card())
            bot.hand.add_card(self._deck.deal_card())
            print(f"Bot {i + 1} initial cards:")
            bot.hand.show()

        print("\nBots start taking turns...")
        for i, bot in enumerate(self._bots):
            bot_blackjack = bot.hand.calculate_score() == 21
            if bot_blackjack:
                print(f"Bot {i + 1} has a blackjack!")
                bot.win_bet(blackjack=True)
                self._last_winners.append(f"Bot {i + 1}")
            if dealer_blackjack:
                if bot_blackjack:
                    print(f"Bot {i + 1} ties with the dealer (both have blackjack).")
                else:
                    bot.lose_bet()
                    print(f"Bot {i + 1} loses to dealer's blackjack.")
            elif not dealer_blackjack and not bot_blackjack:
                print(f"Bot {i + 1}:")
                bot.decide_action(self._dealer.hand.cards[0], self._deck)
                bot.hand.show()
                score = bot.hand.calculate_score()
                if score > 21:
                    print(f"Bot {i + 1} busts!")
                else:
                    print(f"Bot {i + 1} stands with score: {score}")

        if not dealer_blackjack:
            print("\nDealer's turn:")
            self._dealer.play_turn(self._deck)
            self._dealer.hand.show()
            dealer_score = self._dealer.hand.calculate_score()
            print(f"Dealer's final score: {dealer_score}\n")

            for i, bot in enumerate(self._bots):
                bot_score = bot.hand.calculate_score()
                if bot_score > 21:
                    bot.lose_bet()
                elif dealer_score > 21 or bot_score > dealer_score:
                    bot.win_bet()
                    print(f"Bot {i + 1} wins against the dealer!")
                    self._results[f"Bot {i + 1}"] += 1
                    self._last_winners.append(f"Bot {i + 1}")
                elif bot_score == dealer_score:
                    print(f"Bot {i + 1} ties with the dealer!")
                else:
                    bot.lose_bet()
                    print(f"Bot {i + 1} loses to the dealer!")

        self.display_round_results()
        self.reset_game()

    def display_round_results(self) -> None:
        """Displays the results of the current round, including each bot's balance."""
        print("\nRound Results:")
        for i, bot in enumerate(self._bots):
            print(
                f"Bot {i + 1} balance: {bot._balance.quantize(Decimal('0.01'))}, bet: {bot._current_bet.quantize(Decimal('0.01'))}"
            )

    def reset_game(self) -> None:
        """Resets the game state for a new round."""
        self._dealer.hand.clear()
        for bot in self._bots:
            bot.hand.clear()
        self._round_active = False

    def display_final_results(self) -> None:
        """Displays the final results of the game after all rounds."""
        print("\nFinal Results:")
        for bot_name, wins in self._results.items():
            print(f"{bot_name}: {wins} wins")
        max_wins = max(self._results.values())
        winners = [
            bot_name for bot_name, wins in self._results.items() if wins == max_wins
        ]
        if len(winners) > 1:
            print(f"\nIt's a tie between: {', '.join(winners)} with {max_wins} wins!")
        else:
            print(f"\nThe winner is: {winners[0]} with {max_wins} wins!")

    def get_current_round(self) -> int:
        """Returns the current round number."""
        return self._current_round

    def get_last_winners(self) -> List[str]:
        """Returns the winners of the last round."""
        return self._last_winners

    def get_results(self) -> Dict[str, int]:
        """Returns the current results of the game."""
        return self._results
