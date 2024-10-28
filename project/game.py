from .deck import Deck
from .dealer import Dealer
from .bot import Bot
from random import choice
from typing import List, Dict


class Game:
    """
    Represents a Blackjack game involving a dealer and multiple bots.

    Attributes:
        deck (Deck): The deck of cards used in the game.
        dealer (Dealer): The dealer in the game.
        bots (List[Bot]): A list of bots playing the game.
        round_active (bool): Indicates if a round is currently active.
        total_rounds (int): Total number of rounds to be played.
        current_round (int): The current round number.
        results (dict): Dictionary to track the results of each bot.
        last_winners (List[str]): List of winners from the last round.
    """

    def __init__(self, num_bots: int = 3, total_rounds: int = 5) -> None:
        """
        Initializes a new game of Blackjack with a dealer and specified number of bots.

        Args:
            num_bots (int): The number of bots to play the game.
            total_rounds (int): The total number of rounds to be played.
        """
        self.deck = Deck()
        self.dealer = Dealer()
        self.bots: List[Bot] = [
            Bot(strategy=choice(["Cautious", "Risky", "Thoughtful"]))
            for _ in range(num_bots)
        ]
        self.round_active = False
        self.total_rounds = total_rounds
        self.current_round = 0
        self.results = {f"Bot {i + 1}": 0 for i in range(num_bots)}
        self.last_winners: List[str] = []

    def start_game(self) -> None:
        """Starts the game by shuffling the deck and preparing the first round."""
        while self.current_round < self.total_rounds:
            print(f"\nStarting round {self.current_round + 1}...")
            self.play_round()
        self.display_final_results()
        print("\nEnd of the game!")

    def play_round(self) -> None:
        """Plays a single round of Blackjack."""
        self.current_round += 1
        self.round_active = True
        self.deck = Deck()
        self.deck.shuffle()
        self.dealer.draw_initial_cards(self.deck)

        print("\nEach player is dealt two cards.")
        for i, bot in enumerate(self.bots):
            print(f"Bot {i + 1}:")
            bot.add_card(self.deck.deal_card())
            bot.add_card(self.deck.deal_card())
            bot.show_hand()

        print("\nBots start taking turns...")
        for i, bot in enumerate(self.bots):
            print(f"Bot {i + 1}:")
            while True:
                action = bot.decide_action(self.dealer.cards_on_hand[0])
                if action == "hit":
                    bot.add_card(self.deck.deal_card())
                    bot.show_hand()
                    if bot.calculate_score() > 21:
                        print(f"Bot {i + 1} busts!")
                        break
                else:
                    break

        print("\nDealer's turn:")
        self.dealer.play_turn(self.deck)
        self.dealer.show_hand()

        print("\nDetermining the winner of this round...")
        self.determine_winner()

        self.reset_game()

    def determine_winner(self) -> None:
        """Determines the winner of the round based on the scores."""
        dealer_score = self.dealer.calculate_score()
        print(f"Dealer's score: {dealer_score}")
        self.last_winners = []

        for i, bot in enumerate(self.bots):
            bot_score = bot.calculate_score()
            print(f"Bot {i + 1} score: {bot_score}")
            if bot_score > 21:
                print(f"Bot {i + 1} busts!")
            elif dealer_score > 21 or bot_score > dealer_score:
                print(f"Bot {i + 1} wins!")
                self.results[f"Bot {i + 1}"] += 1
                self.last_winners.append(f"Bot {i + 1}")
            elif bot_score == dealer_score:
                print(f"Bot {i + 1} ties with the dealer!")
            else:
                print(f"Bot {i + 1} loses to the dealer!")

    def reset_game(self) -> None:
        """Resets the game state for a new round."""
        self.dealer.clear_hand()
        for bot in self.bots:
            bot.clear_hand()
        self.round_active = False

    def display_final_results(self) -> None:
        """Displays the final results of the game after all rounds."""
        print("\nFinal Results:")
        for bot_name, wins in self.results.items():
            print(f"{bot_name}: {wins} wins")
        max_wins = max(self.results.values())
        winners = [
            bot_name for bot_name, wins in self.results.items() if wins == max_wins
        ]
        if len(winners) > 1:
            print(f"\nIt's a tie between: {', '.join(winners)} with {max_wins} wins!")
        else:
            print(f"\nThe winner is: {winners[0]} with {max_wins} wins!")

    def get_current_round(self) -> int:
        """Returns the current round number."""
        return self.current_round

    def get_last_winners(self) -> List[str]:
        """Returns the winners of the last round."""
        return self.last_winners

    def get_results(self) -> Dict[str, int]:
        """Returns the current results of the game."""
        return self.results
