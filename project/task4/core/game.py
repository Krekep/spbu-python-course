from typing import List, Dict, Any, TYPE_CHECKING
from .deck import Deck

if TYPE_CHECKING:
    from players.player import Player
    from players.bot import Bot
    from players.human import HumanPlayer

from players.dealer import Dealer

class Game:
    """
    Main game controller for Blackjack, manages rounds, players and game flow.
    """
    
    def __init__(self, num_decks: int = 6, max_rounds: int = 100) -> None:
        """
        Initializes a new Blackjack game.

        Parameters:
            num_decks : int (Number of decks to use, default 6)
            max_rounds : int (Maximum number of rounds to play, default 100)
        """
        self.deck = Deck(num_decks)
        self.dealer = Dealer()
        self.players: List['Player'] = []
        self.current_round = 0
        self.max_rounds = max_rounds
        self.is_game_active = False
        self.round_history: List[Dict[str, Any]] = []
        self.num_decks = num_decks
    
    def add_player(self, player: 'Player') -> None:
        """
        Adds a player to the game.

        Parameters:
            player : Player (Player instance to add to the game)
        """
        self.players.append(player)
    
    def add_bot(self, name: str, strategy: Any, chips: int = 1000) -> None:
        """
        Creates and adds a bot player to the game.

        Parameters:
            name : str (Name of the bot player)
            strategy : Any (Strategy object for bot decision making)
            chips : int (Starting chip count, default 1000)
        """
        from players.bot import Bot
        bot = Bot(name, strategy, chips)
        self.add_player(bot)
    
    def add_human_player(self, name: str, chips: int = 1000) -> None:
        """
        Creates and adds a human player to the game.

        Parameters:
            name : str (Name of the human player)
            chips : int (Starting chip count, default 1000)
        """
        from players.human import HumanPlayer
        human = HumanPlayer(name, chips)
        self.add_player(human)
    
    def start_game(self) -> None:
        """
        Starts the game by shuffling deck and initializing game state.
        """
        self.deck.shuffle()
        self.is_game_active = True
        self.current_round = 0
        
        print("♠♣♥♦ НАЧАЛО ИГРЫ В BLACKJACK ♠♣♥♦")
        print(f"Игроки: {[player.name for player in self.players]}")
        print(f"Максимум раундов: {self.max_rounds}")
        print("-" * 50)
    
    def _reset_round(self) -> None:
        """
        Resets all player and dealer hands for a new round.
        """
        self.dealer.reset_hand()
        for player in self.players:
            player.reset_hand()
    
    def _place_bets(self, round_info: Dict[str, Any]) -> None:
        """
        Handles the betting phase where all players place their bets.

        Parameters:
            round_info : Dict[str, Any] (Dictionary to store betting information)
        """
        print("\n--- Ставки ---")
        bets_list: List[str] = []
        
        for player in self.players:
            if player.chips <= 0:
                print(f"💀 {player.name} пропускает раунд (нет фишек)")
                continue
                
            from players.human import HumanPlayer
            if isinstance(player, HumanPlayer):
                player.make_bet()
                bets_list.append(f"--- Ставка {player.name} ---")
                bets_list.append(f"Доступно фишек: {player.chips + player.bet}")
                bets_list.append(f"Ставка {player.bet} принята!")
            else:
                player.make_bet()
                bets_list.append(f"🤖 {player.name} ставит {player.bet} фишек")
        
        round_info["bets"] = bets_list

    def _deal_initial_cards(self, round_info: Dict[str, Any]) -> None:
        """
        Deals initial two cards to all players and dealer.

        Parameters:
            round_info : Dict[str, Any] (Dictionary to store card dealing information)
        """
        card_dealing_list: List[str] = []
        dealer_turn_dict: Dict[str, Any] = {}
        
        for player in self.players:
            if player.bet > 0:
                card = self.deck.deal_card()
                player.hand.add_card(card)
                card_dealing_list.append(f"🃏 {player.name} получает {card}")
        
        card = self.deck.deal_card()
        self.dealer.hand.add_card(card)
        dealer_turn_dict["up_card"] = str(card)
        card_dealing_list.append(f"🃏 Дилер получает {card}")
        
        for player in self.players:
            if player.bet > 0:
                card = self.deck.deal_card()
                player.hand.add_card(card)
                card_dealing_list.append(f"🃏 {player.name} получает {card}")
        
        card = self.deck.deal_card()
        self.dealer.hand.add_card(card)
        card_dealing_list.append("🃏 Дилер получает карту рубашкой вверх")
        
        round_info["card_dealing"] = card_dealing_list
        round_info["dealer_turn"] = dealer_turn_dict
    
    def _check_dealer_blackjack(self, round_info: Dict[str, Any]) -> bool:
        """
        Checks if dealer has blackjack and handles immediate round end.

        Parameters:
            round_info : Dict[str, Any] (Dictionary to store round results)

        Returns:
            bool: True if dealer has blackjack, False otherwise
        """
        if self.dealer.hand.is_blackjack():
            print("\n💥 У дилера BLACKJACK!")
            
            blackjack_info = [
                "💥 У дилера BLACKJACK!",
                f"📊 Итог дилера: {self.dealer.hand} (Сумма: {self.dealer.hand.value})"
            ]
            
            print(f"Карты дилера: {self.dealer.hand} (Сумма: {self.dealer.hand.value})")
            
            results_list: List[str] = []
            results_list.extend(blackjack_info)
            
            for player in self.players:
                if player.bet > 0:
                    player_result = f"\n📊 {player.name}: {player.hand} (Сумма: {player.hand.value})"
                    print(player_result)
                    results_list.append(player_result)
                    
                    if player.hand.is_blackjack():
                        player.push()
                        result_msg = f"  🤝 Ничья с дилером (BLACKJACK)! Возврат ставки: {player.bet}"
                        print(result_msg)
                        results_list.append(result_msg)
                    else:
                        player.lose_bet()
                        result_msg = "  💥 Проигрыш! У дилера BLACKJACK"
                        print(result_msg)
                        results_list.append(result_msg)
            
            round_info["results"] = results_list
            round_info["dealer_blackjack"] = True
            round_info["dealer_turn"] = {
                "actions": ["💥 У дилера BLACKJACK!", f"📋 Карты дилера: {self.dealer.hand} (Сумма: {self.dealer.hand.value})"]
            }
            
            return True
        return False
    
    def _play_players_turns(self, round_info: Dict[str, Any]) -> None:
        """
        Processes all player turns in round-robin fashion.

        Parameters:
            round_info : Dict[str, Any] (Dictionary to store player turn information)
        """
        dealer_up_card = self.dealer.hand.cards[0]
        
        print("\n--- Ходы игроков ---")
        print(f"📋 Открытая карта дилера: {dealer_up_card}")
        
        active_players = [p for p in self.players if p.bet > 0 and not p.has_busted and not p.is_standing]
        round_number = 0
        
        player_turns_list: List[Dict[str, Any]] = []
        
        while active_players:
            round_number += 1
            print(f"\n♠ Круг {round_number} ♠")
            
            for player in active_players[:]:
                if player.has_busted or player.is_standing:
                    active_players.remove(player)
                    continue
                
                player_turn_actions: List[str] = []
                
                from players.human import HumanPlayer
                if isinstance(player, HumanPlayer):
                    decision = player.make_decision(dealer_up_card)
                    
                    if decision == "hit":
                        card = self.deck.deal_card()
                        player.hand.add_card(card)
                        player_turn_actions.append(f"🃏 {player.name} получает {card} (Сумма: {player.hand.value})")
                        
                        if player.hand.is_busted():
                            player.has_busted = True
                            player_turn_actions.append(f"💥 {player.name} ПЕРЕБРАЛ! ({player.hand.value})")
                            print(f"💥 {player.name} ПЕРЕБРАЛ!")
                    
                    elif decision == "double":
                        player.is_standing = True
                        player_turn_actions.append(f"💰 {player.name} удваивает ставку до {player.bet} и завершает ход")
                    
                    else:
                        player.is_standing = True
                        player_turn_actions.append(f"✅ {player.name} останавливается")
                
                else:
                    decision = player.make_decision(dealer_up_card)
                    
                    if decision == "hit":
                        card = self.deck.deal_card()
                        player.hand.add_card(card)
                        player_turn_actions.append(f"🤖 {player.name} берет карту")
                        player_turn_actions.append(f"🃏 {player.name} получает {card} (Сумма: {player.hand.value})")
                        
                        if player.hand.is_busted():
                            player.has_busted = True
                            player_turn_actions.append(f"💥 {player.name} ПЕРЕБРАЛ! ({player.hand.value})")
                            print(f"💥 {player.name} ПЕРЕБРАЛ!")
                        else:
                            print(f"🤖 {player.name} берет карту")
                    
                    else:
                        player.is_standing = True
                        player_turn_actions.append(f"✅ {player.name} останавливается")
                        player_turn_actions.append(f"✅ {player.name} останавливается на {player.hand.value}")
                        print(f"✅ {player.name} останавливается")
                
                player_turns_list.append({
                    "header": f"♠ Круг {round_number} ♠",
                    "actions": player_turn_actions
                })
                
                active_players.remove(player)
            
            active_players = [p for p in self.players if p.bet > 0 and not p.has_busted and not p.is_standing]
        
        round_info["player_turns"] = player_turns_list
    
    def _play_dealer_turn(self, round_info: Dict[str, Any]) -> None:
        """
        Processes dealer's turn according to Blackjack rules.

        Parameters:
            round_info : Dict[str, Any] (Dictionary to store dealer turn information)
        """
        print("\n--- Ход дилера ---")
        
        dealer_actions: List[str] = []
        print(f"📋 Карты дилера: {self.dealer.hand} (Сумма: {self.dealer.hand.value})")
        dealer_actions.append(f"📋 Карты дилера: {self.dealer.hand} (Сумма: {self.dealer.hand.value})")
        
        while self.dealer.should_hit():
            card = self.deck.deal_card()
            self.dealer.hand.add_card(card)
            dealer_actions.append(f"🃏 Дилер берет {card}. Теперь: {self.dealer.hand.value}")
            print(f"🃏 Дилер берет {card}. Теперь: {self.dealer.hand.value}")
        
        dealer_actions.append(f"✅ Дилер останавливается на {self.dealer.hand.value}")
        print(f"✅ Дилер останавливается на {self.dealer.hand.value}")
        
        round_info["dealer_turn"]["actions"] = dealer_actions
    
    def _determine_winners(self, round_info: Dict[str, Any]) -> None:
        """
        Determines winners and calculates payouts for all players.

        Parameters:
            round_info : Dict[str, Any] (Dictionary to store round results)
        """
        dealer_value = self.dealer.hand.value
        dealer_busted = self.dealer.hand.is_busted()
        
        print("\n--- Результаты раунда ---")
        print(f"📊 Итог дилера: {self.dealer.hand} (Сумма: {dealer_value})")
        
        results_list: List[str] = []
        results_list.append(f"📊 Итог дилера: {self.dealer.hand} (Сумма: {dealer_value})")
        
        for player in self.players:
            if player.bet == 0:
                continue
                
            player_result = f"\n📊 {player.name}: {player.hand} (Сумма: {player.hand.value})"
            print(player_result)
            results_list.append(player_result)
            
            if player.hand.is_blackjack():
                player.blackjack_win()
                win_msg = f"  🎉 BLACKJACK! Выигрыш: {int(player.bet * 1.5)}"
                print(win_msg)
                results_list.append(win_msg)
            
            elif player.has_busted:
                player.lose_bet()
                bust_msg = f"  💥 Перебор! Проигрыш: {player.bet}"
                print(bust_msg)
                results_list.append(bust_msg)
            
            elif dealer_busted:
                player.win_bet()
                win_msg = f"  🎉 Дилер перебрал! Выигрыш: {player.bet * 2}"
                print(win_msg)
                results_list.append(win_msg)
            
            elif player.hand.value > dealer_value:
                player.win_bet()
                win_msg = f"  🎉 Победа! {player.hand.value} > {dealer_value}. Выигрыш: {player.bet * 2}"
                print(win_msg)
                results_list.append(win_msg)
            
            elif player.hand.value == dealer_value:
                player.push()
                push_msg = f"  🤝 Ничья! Возврат ставки: {player.bet}"
                print(push_msg)
                results_list.append(push_msg)
            
            else:
                player.lose_bet()
                lose_msg = f"  😞 Проигрыш! {player.hand.value} < {dealer_value}"
                print(lose_msg)
                results_list.append(lose_msg)
        
        round_info["results"] = results_list
    
    def _check_game_status(self) -> None:
        """
        Checks if game should continue or end based on round limit or player bankruptcies.
        """
        active_players = [p for p in self.players if p.chips > 0]
        if not active_players:
            print("\n💀 Все игроки обанкротились! Игра окончена.")
            self.is_game_active = False
        elif self.current_round >= self.max_rounds:
            print(f"\n🏁 Достигнут лимит в {self.max_rounds} раундов!")
            self.is_game_active = False
    
    def get_game_state(self) -> Dict[str, Any]:
        """
        Returns current state of the game for display or saving.

        Returns:
            Dict[str, Any]: Dictionary containing game state information
        """
        from players.human import HumanPlayer
        
        return {
            "round": self.current_round,
            "max_rounds": self.max_rounds,
            "active_players": len([p for p in self.players if p.chips > 0]),
            "deck_cards": len(self.deck),
            "players": [
                {
                    "name": p.name,
                    "chips": p.chips,
                    "hand": str(p.hand),
                    "hand_value": p.hand.value,
                    "bet": p.bet,
                    "busted": p.has_busted,
                    "type": "Human" if isinstance(p, HumanPlayer) else "Bot"
                } for p in self.players
            ],
            "dealer": {
                "hand": str(self.dealer.hand),
                "hand_value": self.dealer.hand.value,
                "busted": self.dealer.hand.is_busted()
            }
        }
    
    def play_round(self) -> Dict[str, Any]:
        """
        Plays one complete round of Blackjack.

        Returns:
            Dict[str, Any]: Detailed information about the played round
        """
        if not self.is_game_active or self.current_round >= self.max_rounds:
            return {"game_over": True}
        
        self.current_round += 1
        round_info = {
            "round": self.current_round,
            "bets": [],
            "card_dealing": [],
            "player_turns": [],
            "dealer_turn": {},
            "results": [],
            "final_state": {}
        }
        
        print(f"\n{'='*60}")
        print(f"🎰 РАУНД {self.current_round}")
        print(f"{'='*60}")
        
        self._reset_round()
        self._place_bets(round_info)
        self._deal_initial_cards(round_info)
        
        if self._check_dealer_blackjack(round_info):
            round_info["final_state"] = self.get_game_state()
            self._save_round_to_history(round_info)
            return round_info
        
        self._play_players_turns(round_info)
        self._play_dealer_turn(round_info)
        self._determine_winners(round_info)
        round_info["final_state"] = self.get_game_state()
        self._save_round_to_history(round_info)
        self._check_game_status()
        
        return round_info
    
    def _save_round_to_history(self, round_info: Dict[str, Any]) -> None:
        """
        Saves round information to game history.

        Parameters:
            round_info : Dict[str, Any] (Round information to save)
        """
        self.round_history.append(round_info.copy())
    
    def show_round_report(self, round_number: int) -> None:
        """
        Displays detailed report for a specific round.

        Parameters:
            round_number : int (Round number to display report for)
        """
        if round_number < 1 or round_number > len(self.round_history):
            print("❌ Неверный номер раунда")
            return
        
        round_info = self.round_history[round_number - 1]
        
        print(f"\n{'='*60}")
        print(f"🎰 РАУНД {round_number} (ОТЧЕТ)")
        print(f"{'='*60}")
        
        print("\n--- Ставки ---")
        for bet_info in round_info["bets"]:
            print(bet_info)
        
        print("\n--- Раздача карт ---")
        for card_info in round_info["card_dealing"]:
            print(card_info)
        
        if round_info.get("dealer_blackjack"):
            print("\n--- Ход дилера ---")
            for action in round_info["dealer_turn"]["actions"]:
                print(action)
        else:
            if round_info["player_turns"]:
                print("\n--- Ходы игроков ---")
                print(f"📋 Открытая карта дилера: {round_info['dealer_turn'].get('up_card', '')}")
                
                for turn_info in round_info["player_turns"]:
                    print(f"\n{turn_info['header']}")
                    for action in turn_info["actions"]:
                        print(action)
            
            print("\n--- Ход дилера ---")
            for action in round_info["dealer_turn"]["actions"]:
                print(action)
        
        print("\n--- Результаты раунда ---")
        for result in round_info["results"]:
            print(result)
        
        state = round_info["final_state"]
        print(f"\n📊 Текущее состояние:")
        print(f"Раунд: {state['round']}/{state['max_rounds']}")
        print(f"Карт в колоде: {state['deck_cards']}")
        
        print(f"\n💰 Фишки игроков:")
        for player in state["players"]:
            status = "💀 БАНКРОТ" if player["chips"] == 0 else f"🏆 {player['chips']}"
            print(f"  {player['name']} ({player['type']}): {status}")
        
        print("=" * 60)

    def set_deck(self, deck: 'Deck') -> None:
        """
        Sets a custom deck for testing or demonstration purposes.

        Parameters:
            deck : Deck (Custom deck to use instead of standard deck)
        """
        self.deck = deck