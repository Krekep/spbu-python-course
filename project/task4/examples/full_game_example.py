"""
Пример полной игры Blackjack с генерацией отчета после каждого раунда.
Демонстрирует полный цикл игры с сохранением всех состояний.
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.game import Game
from strategies.conservative import ConservativeStrategy
from strategies.aggressive import AggressiveStrategy
from strategies.basic import BasicStrategy


def run_full_game_example():
    """Полная игра с генерацией отчетов"""
    print("=" * 80)
    print("ПОЛНАЯ ИГРА BLACKJACK С ОТЧЕТАМИ")
    print("=" * 80)

    # Создаем игру
    game = Game(num_decks=2, max_rounds=5)

    # Добавляем ботов
    game.add_bot("Консерватор", ConservativeStrategy(), 800)
    game.add_bot("Агрессор", AggressiveStrategy(), 800)
    game.add_bot("Тактик", BasicStrategy(), 800)

    game.start_game()

    # Игровой цикл с автоматическим созданием отчетов
    for round_num in range(game.max_rounds):
        if not game.is_game_active:
            break

        print(f"\n{'='*80}")
        print(f"🎰 РАУНД {round_num + 1}")
        print(f"{'='*80}")

        # Играем раунд
        game.play_round()

        # Автоматически генерируем отчет
        print(f"\n📋 АВТОМАТИЧЕСКИЙ ОТЧЕТ ПО РАУНДУ {round_num + 1}")
        print("-" * 50)
        game.show_round_report(round_num + 1)

        # Краткая статистика изменений
        if round_num > 0:
            print(f"\n📈 ИЗМЕНЕНИЯ ПОСЛЕ РАУНДА {round_num + 1}:")
            current_state = game.get_game_state()
            previous_state = game.round_history[round_num - 1]["final_state"]

            for current_player in current_state["players"]:
                previous_player = next(
                    (
                        p
                        for p in previous_state["players"]
                        if p["name"] == current_player["name"]
                    ),
                    None,
                )
                if previous_player:
                    change = current_player["chips"] - previous_player["chips"]
                    if change != 0:
                        trend = "📈" if change > 0 else "📉" if change < 0 else "➡️"
                        print(f"   {trend} {current_player['name']}: {change:+} фишек")

    # Финальный отчет
    print(f"\n{'='*80}")
    print("ФИНАЛЬНЫЙ ОТЧЕТ ПО ВСЕЙ ИГРЕ")
    print(f"{'='*80}")

    final_state = game.get_game_state()

    print(f"\n📊 ИТОГОВАЯ СТАТИСТИКА:")
    print(f"   Сыграно раундов: {final_state['round']}")
    print(f"   Начальный баланс каждого игрока: 800 фишек")
    print(f"   Осталось карт в колоде: {final_state['deck_cards']}")

    print(f"\n🏆 ФИНАЛЬНЫЕ РЕЗУЛЬТАТЫ:")
    sorted_players = sorted(
        final_state["players"], key=lambda x: x["chips"], reverse=True
    )
    for i, player in enumerate(sorted_players, 1):
        profit = player["chips"] - 800
        profit_percent = (profit / 800) * 100
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
        performance = (
            "Отлично"
            if profit_percent > 20
            else "Хорошо"
            if profit_percent > 0
            else "Плохо"
        )
        print(
            f"   {medal} {player['name']}: {player['chips']} фишек ({profit:+}, {profit_percent:+.1f}%) - {performance}"
        )

    # Анализ игры
    print(f"\n📝 АНАЛИЗ ИГРЫ:")
    total_rounds = final_state["round"]
    for i in range(1, total_rounds + 1):
        round_info = game.round_history[i - 1]
        print(f"\n   Раунд {i}:")

        # Находим победителей раунда
        winners = []
        for player in round_info["final_state"]["players"]:
            if player["chips"] > (player["chips"] - player.get("profit", 0)):
                winners.append(player["name"])

        if winners:
            print(f"     Победители: {', '.join(winners)}")
        else:
            print(f"     Победителей нет")

        # Статистика раунда
        active_players = len(
            [p for p in round_info["final_state"]["players"] if p["chips"] > 0]
        )
        print(f"     Активных игроков: {active_players}")


if __name__ == "__main__":
    run_full_game_example()
