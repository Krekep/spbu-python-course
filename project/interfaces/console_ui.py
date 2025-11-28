import os
import time
from datetime import datetime


class ConsoleUI:
    def __init__(self):
        self.view_width = 5
        self.view_height = 5
        self._last_draw_time = 0
        self._min_draw_interval = 0.4
        self._last_state = None

    @staticmethod
    def clear_console():
        os.system('cls')

    def draw(self, world_state):
        current_time = time.time()

        if current_time - self._last_draw_time < self._min_draw_interval:
            return

        if self._last_state == world_state:
            return

        self._last_state = world_state
        self._last_draw_time = current_time

        self.clear_console()

        world = world_state['world']
        player = world_state['player']
        cursor_x, cursor_y = world_state['cursor']

        output_lines = list()

        output_lines.append("Поле:")
        start_x = max(0, cursor_x - self.view_width // 2)
        start_y = max(0, cursor_y - self.view_height // 2)
        end_x = min(world.width, start_x + self.view_width)
        end_y = min(world.height, start_y + self.view_height)

        for y in range(start_y, end_y):
            row = []
            for x in range(start_x, end_x):
                field_cell = world.get_field(x, y)
                cell = field_cell.cell
                if x == cursor_x and y == cursor_y:
                    row.append("{#}")
                elif cell:
                    row.append(cell.get_display_char())
                else:
                    row.append("[ ]")
            output_lines.append(" ".join(row))

        current_field = world.get_field(cursor_x, cursor_y)
        output_lines.append(f"\nКурсор: ({cursor_x}, {cursor_y})")

        if world_state['show_temp']:
            output_lines.append(f"Температура: {current_field.temperature:.1f}")

        if world_state['show_nutrients']:
            output_lines.append(f"Питательные вещества: {current_field.nutrients:.1f}")

        current_cell = current_field.cell
        if current_cell:
            output_lines.append(f"Клетка: здоровье={current_cell.current_health:.1f}")
            output_lines.append(f"Ген: голод={current_cell.gene.hunger:.1f}, тепло={current_cell.gene.max_heat:.1f}")

        print(f"\nИнвентарь [{len(player.inventory)}]:")
        print("№  Здоровье  Голод  Тепло  Холод  Мутация  Еда")
        print("─" * 50)

        for i, cell in enumerate(player.inventory):
            marker = "▶" if i == player.selected_cell_index else " "
            gene = cell.gene

            print(f"{marker}{i:2} {cell.current_health:7.1f}  {gene.hunger:5.1f}  {gene.max_heat:5.1f}  "
                  f"{gene.max_cold:5.1f}  {gene.mutation_rate:7.1f}  {cell.stomach:4.1f}")

        status = "ПАУЗА" if world_state['is_paused'] else "ЗАПУЩЕНО"
        output_lines.append(f"\nСтатус: {status}")
        save_files = [f for f in os.listdir('.') if f.startswith('world_save_') and f.endswith('.pkl')]
        if save_files:
            latest_save = max(save_files)
            file_time = os.path.getctime(latest_save)
            time_str = datetime.fromtimestamp(file_time).strftime("%d.%m %H:%M")
            print(f"💾 Последнее сохранение: {time_str}")

        print(f"\nУправление:")
        print(f"  Стрелки/WASD - движение  P - пауза  Пробел - клетка")
        print(f"  T/N - температура/питательные вещества  Enter - выбор клетки")
        print(f"  F5 - сохранить  F9 - загрузить  F1 - список сохранений")

        print("\n".join(output_lines))
