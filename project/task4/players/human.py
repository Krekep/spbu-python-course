from .player import Player
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.card import Card

class HumanPlayer(Player):
    """
    Human player that makes decisions through user input.
    """
    
    def __init__(self, name: str, chips: int = 1000) -> None:
        """
        Initializes a human player.

        Parameters:
            name : str (Player's name)
            chips : int (Starting chip amount, default 1000)
        """
        super().__init__(name, chips)
    
    def make_decision(self, dealer_up_card: 'Card') -> str:
        """
        Gets decision from user input with validation.

        Parameters:
            dealer_up_card : Card (Dealer's visible card)

        Returns:
            str: User's decision as "hit", "stand", or "double"
        """
        print(f"\n--- Ход {self.name} ---")
        print(f"Ваши карты: {self.hand} (Сумма: {self.hand.value})")
        print(f"Карта дилера: {dealer_up_card}")
        print(f"Ваши фишки: {self.chips}, Ставка: {self.bet}")
        
        while True:
            choice = input("Выберите действие - Взять карту (h), Остановиться (s), Удвоить (d): ").lower().strip()
            
            if choice in ['h', 'hit', 'взять', 'х']:
                return "hit"
            elif choice in ['s', 'stand', 'стоп', 'остановиться', 'с']:
                print(f"✅ {self.name} останавливается")
                return "stand"
            elif choice in ['d', 'double', 'удвоить', 'д']:
                if self.chips >= self.bet:
                    self.chips -= self.bet
                    self.bet *= 2
                    print(f"💰 {self.name} удваивает ставку до {self.bet} и завершает ход")
                    return "double"
                else:
                    print("Недостаточно фишек для удвоения!")
            else:
                print("Неверный ввод. Попробуйте снова.")
        
    def make_bet(self) -> bool:
        """
        Gets bet amount from user input with validation.

        Returns:
            bool: True if bet was placed successfully
        """
        print(f"\n--- Ставка {self.name} ---")
        print(f"Доступно фишек: {self.chips}")
        
        while True:
            try:
                bet_input = input("Введите размер ставки: ")
                bet_amount = int(bet_input)
                
                if bet_amount <= 0:
                    print("Ставка должна быть положительной!")
                elif bet_amount > self.chips:
                    print(f"Недостаточно фишек! Доступно: {self.chips}")
                    max_bet = input(f"Сделать максимальную ставку ({self.chips})? (y/n): ").lower().strip()
                    if max_bet == 'y':
                        bet_amount = self.chips
                        success = self.place_bet(bet_amount)
                        if success:
                            print(f"Ставка {bet_amount} принята!")
                            return True
                    else:
                        continue
                else:
                    success = self.place_bet(bet_amount)
                    if success:
                        print(f"Ставка {bet_amount} принята!")
                        return True
                    else:
                        print("Ошибка при размещении ставки!")
                    
            except ValueError:
                print("Пожалуйста, введите число!")