from core.game import Game
from strategies.conservative import ConservativeStrategy
from strategies.aggressive import AggressiveStrategy
from strategies.basic import BasicStrategy


def main():
    print("♠♣♥♦ ДОБРО ПОЖАЛОВАТЬ В BLACKJACK! ♠♣♥♦")

    # Создание игры
    game = Game(num_decks=6, max_rounds=20)

    # Добавление реального игрока
    player_name = input("Введите ваше имя: ").strip() or "Игрок"
    game.add_human_player(player_name, 1000)

    # Добавление ботов с разными стратегиями
    game.add_bot("Консервативный Бот", ConservativeStrategy(), 1000)
    game.add_bot("Агрессивный Бот", AggressiveStrategy(), 1000)
    game.add_bot("Тактический Бот", BasicStrategy(), 1000)

    # Запуск игры
    game.start_game()

    # Игровой цикл
    while game.is_game_active:
        input("\nНажмите Enter для начала раунда...")
        game.play_round()

        # Вывод текущего состояния
        state = game.get_game_state()
        print(f"\n📊 Текущее состояние:")
        print(f"Раунд: {state['round']}/{state['max_rounds']}")
        print(f"Карт в колоде: {state['deck_cards']}")

        print(f"\n💰 Фишки игроков:")
        for player in state["players"]:
            status = "💀 БАНКРОТ" if player["chips"] == 0 else f"🏆 {player['chips']}"
            print(f"  {player['name']} ({player['type']}): {status}")

        print("=" * 60)

        # Запрос на показ отчета
        if game.current_round > 0:
            show_report = (
                input(f"\n📋 Посмотреть отчет по РАУНД {game.current_round}? (y/n): ")
                .lower()
                .strip()
            )
            if show_report == "y":
                game.show_round_report(game.current_round)

    # Финальные результаты
    print("\n🎰 ФИНАЛЬНЫЕ РЕЗУЛЬТАТЫ 🎰")
    final_state = game.get_game_state()

    # Сортировка игроков по количеству фишек
    sorted_players = sorted(
        final_state["players"], key=lambda x: x["chips"], reverse=True
    )

    for i, player in enumerate(sorted_players, 1):
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
        print(f"{medal} {player['name']}: {player['chips']} фишек")

    if sorted_players and sorted_players[0]["chips"] > 0:
        print(
            f"\n🏆 ПОБЕДИТЕЛЬ: {sorted_players[0]['name']} с {sorted_players[0]['chips']} фишками!"
        )
    else:
        print(f"\n💀 Все игроки обанкротились! Победителя нет.")


if __name__ == "__main__":
    main()
