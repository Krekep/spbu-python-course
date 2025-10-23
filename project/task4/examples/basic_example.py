"""
Базовый пример работы игры Blackjack.
Демонстрирует изменение состояния игры в каждом раунде.
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.game import Game
from strategies.conservative import ConservativeStrategy
from strategies.aggressive import AggressiveStrategy
from strategies.basic import BasicStrategy

def run_basic_example():
    """Запуск базового примера с подробным выводом каждого раунда"""
    print("=" * 80)
    print("БАЗОВЫЙ ПРИМЕР BLACKJACK - ИЗМЕНЕНИЕ СОСТОЯНИЯ ПО РАУНДАМ")
    print("=" * 80)
    
    # Создаем игру с меньшим количеством раундов для наглядности
    game = Game(num_decks=2, max_rounds=3)
    
    # Добавляем ботов с разными стратегиями
    game.add_bot("Консерватор", ConservativeStrategy(), 500)
    game.add_bot("Агрессор", AggressiveStrategy(), 500)
    game.add_bot("Тактик", BasicStrategy(), 500)
    
    # Запускаем игру
    game.start_game()
    
    # Игровой цикл
    for round_num in range(game.max_rounds):
        if not game.is_game_active:
            break
            
        print(f"\n{'='*80}")
        print(f"РАУНД {round_num + 1} - НАЧАЛО")
        print(f"{'='*80}")
        
        # Играем раунд
        game.play_round()
        
        # Получаем состояние после раунда
        game_state = game.get_game_state()
        
        # Выводим детальную информацию о состоянии
        print(f"\n📊 СОСТОЯНИЕ ПОСЛЕ РАУНДА {round_num + 1}:")
        print(f"   Номер раунда: {game_state['round']}")
        print(f"   Активных игроков: {game_state['active_players']}")
        print(f"   Карт в колоде: {game_state['deck_cards']}")
        
        print(f"\n🎩 ДИЛЕР:")
        print(f"   Карты: {game_state['dealer']['hand']}")
        print(f"   Сумма очков: {game_state['dealer']['hand_value']}")
        print(f"   Перебор: {'Да' if game_state['dealer']['busted'] else 'Нет'}")
        
        print(f"\n👥 ИГРОКИ:")
        for player in game_state['players']:
            print(f"   {player['name']} ({player['type']}):")
            print(f"     Фишки: {player['chips']} ({'+' if player['chips'] > 500 else '-'}{player['chips'] - 500})")
            print(f"     Карты: {player['hand']}")
            print(f"     Сумма очков: {player['hand_value']}")
            print(f"     Перебор: {'Да' if player['busted'] else 'Нет'}")
            print(f"     Текущая ставка: {player['bet']}")
        
        print(f"\n📈 ИЗМЕНЕНИЯ ПО СРАВНЕНИЮ С НАЧАЛОМ РАУНДА:")
        if round_num == 0:
            print("   Начальное состояние")
        else:
            # Сравниваем с предыдущим состоянием (упрощенно)
            prev_state = game.round_history[round_num - 1]['final_state']
            for current_player in game_state['players']:
                prev_player = next((p for p in prev_state['players'] if p['name'] == current_player['name']), None)
                if prev_player:
                    change = current_player['chips'] - prev_player['chips']
                    if change != 0:
                        print(f"   {current_player['name']}: {change:+} фишек")
    
    # Финальный анализ
    print(f"\n{'='*80}")
    print("ФИНАЛЬНЫЙ АНАЛИЗ ИГРЫ")
    print(f"{'='*80}")
    
    final_state = game.get_game_state()
    
    print(f"\n📊 ОБЩАЯ СТАТИСТИКА:")
    print(f"   Сыграно раундов: {final_state['round']}")
    print(f"   Осталось карт в колоде: {final_state['deck_cards']}")
    print(f"   Активных игроков: {final_state['active_players']}")
    
    print(f"\n🏆 РЕЗУЛЬТАТЫ:")
    sorted_players = sorted(final_state['players'], key=lambda x: x['chips'], reverse=True)
    for i, player in enumerate(sorted_players, 1):
        profit = player['chips'] - 500  # Начальный баланс был 500
        profit_percent = (profit / 500) * 100
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
        print(f"   {medal} {player['name']}: {player['chips']} фишек ({profit:+} фишек, {profit_percent:+.1f}%)")
    
    print(f"\n📈 ЭФФЕКТИВНОСТЬ СТРАТЕГИЙ:")
    for player in sorted_players:
        if "Консерватор" in player['name']:
            print("   Консервативная стратегия: Меньший риск, стабильные результаты")
        elif "Агрессор" in player['name']:
            print("   Агрессивная стратегия: Высокий риск, потенциал больших выигрышей/потерь")
        elif "Тактик" in player['name']:
            print("   Тактическая стратегия: Баланс риска и математической оптимальности")

if __name__ == "__main__":
    run_basic_example()