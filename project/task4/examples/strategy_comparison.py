"""
Пример сравнения эффективности разных стратегий игры.
Демонстрирует, как разные стратегии влияют на результаты в долгосрочной перспективе.
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.game import Game
from strategies.conservative import ConservativeStrategy
from strategies.aggressive import AggressiveStrategy
from strategies.basic import BasicStrategy

def run_strategy_comparison():
    """Сравнение эффективности разных стратегий"""
    print("=" * 80)
    print("СРАВНЕНИЕ СТРАТЕГИЙ BLACKJACK")
    print("=" * 80)
    
    # Создаем несколько игр для статистики
    num_games = 5
    strategy_results = {
        "Консервативная": [],
        "Агрессивная": [], 
        "Тактическая": []
    }
    
    for game_num in range(num_games):
        print(f"\n🎮 ИГРА {game_num + 1}/{num_games}")
        print("-" * 40)
        
        game = Game(num_decks=4, max_rounds=10)
        
        # Добавляем ботов с разными стратегиями
        game.add_bot("Консерватор", ConservativeStrategy(), 1000)
        game.add_bot("Агрессор", AggressiveStrategy(), 1000)
        game.add_bot("Тактик", BasicStrategy(), 1000)
        
        game.start_game()
        
        # Играем все раунды
        while game.is_game_active:
            game.play_round()
        
        # Собираем результаты
        final_state = game.get_game_state()
        for player in final_state['players']:
            profit = player['chips'] - 1000
            if "Консерватор" in player['name']:
                strategy_results["Консервативная"].append(profit)
            elif "Агрессор" in player['name']:
                strategy_results["Агрессивная"].append(profit)
            elif "Тактик" in player['name']:
                strategy_results["Тактическая"].append(profit)
            
            print(f"   {player['name']}: {player['chips']} фишек ({profit:+})")
    
    # Анализ результатов
    print(f"\n{'='*80}")
    print("СТАТИСТИЧЕСКИЙ АНАЛИЗ СТРАТЕГИЙ")
    print(f"{'='*80}")
    
    for strategy, results in strategy_results.items():
        avg_profit = sum(results) / len(results)
        win_rate = len([r for r in results if r > 0]) / len(results) * 100
        max_profit = max(results)
        min_profit = min(results)
        
        print(f"\n📊 {strategy} стратегия:")
        print(f"   Средний результат: {avg_profit:+.1f} фишек")
        print(f"   Процент победных игр: {win_rate:.1f}%")
        print(f"   Лучший результат: {max_profit:+} фишек")
        print(f"   Худший результат: {min_profit:+} фишек")
        print(f"   Стабильность: {'Высокая' if max_profit - min_profit < 300 else 'Средняя' if max_profit - min_profit < 600 else 'Низкая'}")
    
    print(f"\n💡 ВЫВОДЫ:")
    print("   • Консервативная стратегия: Меньшая волатильность, стабильные результаты")
    print("   • Агрессивная стратегия: Высокая волатильность, потенциал больших выигрышей/потерь")  
    print("   • Тактическая стратегия: Баланс между риском и стабильностью")
    print("   • В долгосрочной перспективе тактическая стратегия обычно показывает лучшие результаты")

if __name__ == "__main__":
    run_strategy_comparison()