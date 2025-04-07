import random
from typing import List, Dict, Optional
from abc import ABCMeta, abstractmethod
from project.BlackJack.players import Player, Bot, Dealer
import project.BlackJack.deck
import project.BlackJack.bot_strategy



class GameMeta(ABCMeta):
    """A metaclass for dynamically changing the rules of the game and bot strategies"""
    
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        
        cls.MAX_PLAYERS = 6  
        cls.BLACKJACK_PAYOUT = 1.5  
        cls.DEALER_STAND_SCORE = 17  
        cls.MAX_ROUND = 5
        cls.STOP_CARD = 32
        
        # Регистрируем доступные стратегии ботов
        cls.strategies = {
            'accurate': project.BlackJack.bot_strategy.AccurateStrategy(),
            'aggressive': project.BlackJack.bot_strategy.AggressiveStrategy(),
            'counting': project.BlackJack.bot_strategy.CountingStrategy()
        }


class Game(metaclass=GameMeta):
    def __init__(self):
        self.deck = project.BlackJack.deck.Deck()
        self.players: List[Player] = []
        self.counting_players: List[Bot] = []
        self.dealer = Dealer()
        self.bets: Dict[str, int] = {}
        self.game_over = False
        self.round_count = 0
        

    def add_player(self, player: Player) -> None:
        """Add a player to the game"""
        if len(self.players) >= self.MAX_PLAYERS:
            raise ValueError(f"Maximum number of players: {self.MAX_PLAYERS}")
        self.players.append(player)
        if isinstance(player, Bot) and isinstance(player.strategy, project.BlackJack.bot_strategy.CountingStrategy):
            self.counting_players.append(player)



    def create_bot(self, strategy_name: str, bot_name: str, chips: int = 1000) -> Bot:
        strategy = self.strategies.get(strategy_name.lower())
        if strategy:
            return Bot(strategy, bot_name, chips)
        else:
            raise ValueError(f"Unknown strategy: {strategy_name}")

        
    def shuffle(self) -> None:
        self.deck.shuffle()
        for c_player in self.counting_players:
            c_player.strategy.count = 0

    def start_round(self) -> None:
        """Start a new round (deal the cards)"""
        if self.deck.count >= self.STOP_CARD:
            self.shuffle()
        
        for player in self.players:
            player.hand = []
            player.score = 0
        self.dealer.hand = []
        self.dealer.score = 0
        
        for _ in range(2):
            for player in self.players:
                card = self.deck.get_card()
                player.get_card(card)
                player.calculate_score()
                self.counting(card)
                
            card = self.deck.get_card()
            if _ == 1:
                self.dealer.hide_card = card
            else:
                self.dealer.get_card(card)
                self.counting(card)

            self.dealer.calculate_score()
            
        self.game_over = False
        



    def place_bets(self) -> None:
        """Accept bets from all players"""
        self.bets = {}
        for player in self.players:
            bet = random.randint(10, min(100, player.chips))
            bet_amount = player.place_bet(bet)
            self.bets[player.name] = bet_amount
    

    
    def play_turn(self, player: Player) -> None:
        """Process the current player's turn"""
        if self.game_over:
            return
        
        if isinstance(player, Bot):
            while player.decide_hit(): 
                self.hit(player)
                self.print_table()
        
        

    
    def hit(self, player: Player) -> None:
        """Give the player an extra card"""
        card = self.deck.get_card()
        player.get_card(card)
        player.calculate_score()
        
        self.counting(card)
    
    def play_dealer_turn(self) -> None:
        """Dealer's move according to the rules of the game"""
        if self.dealer.hide_card:
            self.dealer.hand.append(self.dealer.hide_card)
            self.counting(self.dealer.hide_card)
            self.dealer.hide_card = None
            self.dealer.calculate_score()
            self.print_table()
        
        while self.dealer.score < self.DEALER_STAND_SCORE and self.dealer.score <= 21:
            card = self.deck.get_card()
            self.dealer.get_card(card)
            self.counting(card)
            self.dealer.calculate_score()
            self.print_table()
        

        if self.MAX_ROUND == self.round_count:
            self.game_over = True
    
    def settle_bets(self, print_res: bool = True) -> None:
        """Determine the winners and distribute the chips"""
        dealer_score = self.dealer.score
        
        if print_res:
            print(f"Dealer: {dealer_score}")


        for player in self.players:
            bet = self.bets.get(player.name, 0)
        
            if player.score > 21:
                player.settle_bet(-bet)
                if print_res:
                    print(f"{player.name}: {player.score} lost {bet} (overage). Chips number: {player.chips}")
                continue
                
            if dealer_score > 21:
                winnings = bet
                player.settle_bet(winnings)
                if print_res:
                    print(f"{player.name}: {player.score} win {winnings} (dealer is overage). Chips number: {player.chips}")
                continue
                
            if (len(player.hand) == 2 and player.score == 21 and 
                not (len(self.dealer.hand) == 2 and dealer_score == 21)):
                winnings = int(bet * self.BLACKJACK_PAYOUT)
                player.settle_bet(winnings)
                if print_res:
                    print(f"{player.name}: {player.score} win {winnings} (Black Jack). Chips number: {player.chips}")
                continue
                
            if player.score > dealer_score:
                winnings = bet 
                player.settle_bet(winnings)
                if print_res:
                    print(f"{player.name}: {player.score} win {winnings}. Chips number: {player.chips}")
            elif player.score == dealer_score:
                player.settle_bet(0) 
                if print_res:
                    print(f"{player.name}: {player.score} (draw). Chips number: {player.chips}")
            else:
                player.settle_bet(-bet)
                if print_res:
                    print(f"{player.name}: {player.score} lost {bet}. Chips number: {player.chips}")
    

    def print_table(self) -> None:
        for player in self.players:
            hand_str = " ".join(str(card) for card in player.hand)
            print(player.name + ": " + hand_str + "\n")
        
        hand_str = " ".join(str(card) for card in self.dealer.hand)
        print("Dealer: " + hand_str)
        print("____________")
        


    def counting(self, card: project.BlackJack.deck.Card) -> None:
        for c_player in self.counting_players:
                    c_player.strategy.update_count(card)



    def change_bot_strategy(self, bot_name: str, strategy_name: str, print_res: bool = True) -> None:
        """Change the strategy of the bot during the game"""
        for player in self.players:
            if player.name == bot_name and isinstance(player, Bot):
                strategy = self.strategies.get(strategy_name.lower())
                if strategy:
                    player.strategy = strategy
                    if print_res:
                        print(f"Strategy {bot_name} changed to {strategy_name}")
                else:
                    raise ValueError(f"Unknown strategy: {strategy_name}")
                return
        raise ValueError(f"The bot was not found: {bot_name}")



    def modify_game_rule(self, rule_name: str, value, print_res: bool = True) -> None:
        """Change the rules of the game dynamically"""
        if hasattr(self, rule_name):
            setattr(self, rule_name, value)
            if print_res:
                print(f"Rule {rule_name} changed to {value}")
        else:
            raise ValueError(f"Unknown game rule {rule_name}")
        
    

    def play_round(self, print_res: bool = True):
        self.round_count += 1
        if print_res:
            print(f"\nRound {self.round_count}")
            print("________________________")
        self.place_bets()
        self.start_round()
        if print_res:
            self.print_table()


        for player in self.players:
            self.play_turn(player)

        self.play_dealer_turn()
        self.settle_bets()
    


    def play(self, print_res: bool = True) -> None:
        self.shuffle()
        while not self.game_over:
            self.play_round(print_res)

        
    

