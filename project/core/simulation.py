from models import Cell
from config import INITIAL_CELL_COUNT
from core import Observer
import os
from datetime import datetime
import pickle


class Simulation(Observer):
    def __init__(self, world, player):
        self.world = world
        self.player = player
        self.is_paused = False
        self.cursor_x = world.width // 2
        self.cursor_y = world.height // 2
        self.show_temperature = False
        self.show_nutrients = False

        for _ in range(INITIAL_CELL_COUNT):
            cell = Cell()
            cell.add_observer(self)
            cell.add_observer(self.world)
            self.player.add_cell(cell)

    def save_world(self, filename=None):
        """Сохранить состояние мира в файл"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"world_save_{timestamp}.pkl"

        try:
            save_data = {
                'world_state': self._get_world_state(),
                'player_state': self._get_player_state(),
                'simulation_state': self._get_simulation_state(),
                'timestamp': datetime.now().isoformat()
            }

            with open(filename, 'wb') as f:
                pickle.dump(save_data, f)

            print(f"💾 Мир сохранен в файл: {filename}")
            return True

        except Exception as e:
            print(f"❌ Ошибка сохранения: {e}")
            return False

    def load_world(self, filename):
        try:
            if not os.path.exists(filename):
                print(f"❌ Файл не найден: {filename}")
                return False

            with open(filename, 'rb') as f:
                save_data = pickle.load(f)

            self._restore_world_state(save_data['world_state'])
            self._restore_player_state(save_data['player_state'])
            self._restore_simulation_state(save_data['simulation_state'])

            print(f"📂 Мир загружен из файла: {filename}")
            print(f"🕐 Сохранение от: {save_data['timestamp']}")
            return True

        except Exception as e:
            print(f"❌ Ошибка загрузки: {e}")
            return False

    def _get_world_state(self):
        world_state = {
            'width': self.world.width,
            'height': self.world.height,
            'cells_on_field': []
        }

        for cell in self.world.cells:
            if cell.x is not None and cell.y is not None:
                cell_state = {
                    'x': cell.x,
                    'y': cell.y,
                    'current_health': cell.current_health,
                    'stomach': cell.stomach,
                    'is_alive': cell.is_alive,
                    'gene': {
                        'max_heat': cell.gene.max_heat,
                        'max_cold': cell.gene.max_cold,
                        'max_health': cell.gene.max_health,
                        'hunger': cell.gene.hunger,
                        'mutation_rate': cell.gene.mutation_rate
                    }
                }
                world_state['cells_on_field'].append(cell_state)

        return world_state

    def _get_player_state(self):
        player_state = {
            'inventory': [],
            'selected_cell_index': self.player.selected_cell_index
        }

        for cell in self.player.inventory:
            cell_state = {
                'current_health': cell.current_health,
                'stomach': cell.stomach,
                'is_alive': cell.is_alive,
                'gene': {
                    'max_heat': cell.gene.max_heat,
                    'max_cold': cell.gene.max_cold,
                    'max_health': cell.gene.max_health,
                    'hunger': cell.gene.hunger,
                    'mutation_rate': cell.gene.mutation_rate
                }
            }
            player_state['inventory'].append(cell_state)

        return player_state

    def _get_simulation_state(self):
        return {
            'cursor_x': self.cursor_x,
            'cursor_y': self.cursor_y,
            'is_paused': self.is_paused,
            'show_temperature': self.show_temperature,
            'show_nutrients': self.show_nutrients
        }

    def _restore_world_state(self, world_state):
        self.world.cells.clear()
        for y in range(self.world.height):
            for x in range(self.world.width):
                field_cell = self.world.get_field(x, y)
                field_cell.cell = None

        for cell_state in world_state['cells_on_field']:
            cell = Cell()
            cell._current_health = cell_state['current_health']
            cell._stomach = cell_state['stomach']
            cell.is_alive = cell_state['is_alive']

            gene_state = cell_state['gene']
            cell.gene.max_heat = gene_state['max_heat']
            cell.gene.max_cold = gene_state['max_cold']
            cell.gene.max_health = gene_state['max_health']
            cell.gene.hunger = gene_state['hunger']
            cell.gene.mutation_rate = gene_state['mutation_rate']

            x, y = cell_state['x'], cell_state['y']
            field_cell = self.world.get_field(x, y)
            field_cell.cell = cell
            cell.placement(self.world, x, y)
            self.world.cells.append(cell)

    def _restore_player_state(self, player_state):
        self.player.inventory.clear()
        self.player.selected_cell_index = player_state['selected_cell_index']

        for cell_state in player_state['inventory']:
            cell = Cell()
            cell._current_health = cell_state['current_health']
            cell._stomach = cell_state['stomach']
            cell.is_alive = cell_state['is_alive']

            gene_state = cell_state['gene']
            cell.gene.max_heat = gene_state['max_heat']
            cell.gene.max_cold = gene_state['max_cold']
            cell.gene.max_health = gene_state['max_health']
            cell.gene.hunger = gene_state['hunger']
            cell.gene.mutation_rate = gene_state['mutation_rate']

            self.player.add_cell(cell)

    def _restore_simulation_state(self, simulation_state):
        self.cursor_x = simulation_state['cursor_x']
        self.cursor_y = simulation_state['cursor_y']
        self.is_paused = simulation_state['is_paused']
        self.show_temperature = simulation_state['show_temperature']
        self.show_nutrients = simulation_state['show_nutrients']

    def on_event(self, event):
        if event.event_type == "cell_divided":
            new_cell = event.data['child']
            # parent = event.data['parent']
            new_cell.add_observer(self)
            new_cell.add_observer(self.world)
            self.player.add_cell(new_cell)

    def process_input(self, input_queue):
        processed_commands = set()

        while not input_queue.empty():
            try:
                command = input_queue.get_nowait()

                if command in processed_commands:
                    continue
                processed_commands.add(command)

                if command == 'pause':
                    self.is_paused = not self.is_paused
                    print(f"{'⏸️ Пауза' if self.is_paused else '▶️ Продолжено'}")

                elif command in ['up', 'w']:
                    self.cursor_y = max(0, self.cursor_y - 1)
                elif command in ['down', 's']:
                    self.cursor_y = min(self.world.height - 1, self.cursor_y + 1)
                elif command in ['left', 'a']:
                    self.cursor_x = max(0, self.cursor_x - 1)
                elif command in ['right', 'd']:
                    self.cursor_x = min(self.world.width - 1, self.cursor_x + 1)

                elif command == 'space':
                    self.place_remove_cell()

                elif command == 't':
                    self.show_temperature = not self.show_temperature
                    print(f"{'📊 Показ температуры' if self.show_temperature else '❌ Скрытие температуры'}")

                elif command == 'n':
                    self.show_nutrients = not self.show_nutrients
                    print(
                        f"{'📊 Показ питательных веществ' if self.show_nutrients else '❌ Скрытие питательных веществ'}")

                elif command == 'enter':
                    self.player.next_cell()
                    selected = self.player.get_selected_cell()
                    if selected:
                        print(f"🔍 Выбрана клетка {self.player.selected_cell_index}")

                # НОВЫЕ КОМАНДЫ СОХРАНЕНИЯ/ЗАГРУЗКИ
                elif command == 'save':
                    success = self.save_world()
                    if success:
                        print("✅ Игра успешно сохранена!")
                    else:
                        print("❌ Не удалось сохранить игру")

                elif command == 'load':
                    # Автоматически загружаем последнее сохранение
                    save_files = [f for f in os.listdir('.') if f.startswith('world_save_') and f.endswith('.pkl')]
                    if save_files:
                        latest_save = max(save_files)  # Берем самый новый файл
                        success = self.load_world(latest_save)
                        if success:
                            print("✅ Игра успешно загружена!")
                        else:
                            print("❌ Не удалось загрузить игру")
                    else:
                        print("❌ Нет файлов сохранения")

                elif command == 'list_saves':
                    self._list_save_files()

            except Exception as e:
                print(f'Ошибка!!!: {e}')
                break

    @staticmethod
    def _list_save_files():
        save_files = [f for f in os.listdir('.') if f.startswith('world_save_') and f.endswith('.pkl')]

        if not save_files:
            print("📂 Нет файлов сохранения")
            return

        print("📂 Файлы сохранения:")
        for i, filename in enumerate(sorted(save_files, reverse=True)[:5]):  # Показываем 5 последних
            file_time = os.path.getctime(filename)
            time_str = datetime.fromtimestamp(file_time).strftime("%d.%m %H:%M")
            print(f"  {i + 1}. {filename} ({time_str})")

    def place_remove_cell(self):
        field_cell = self.world.get_field(self.cursor_x, self.cursor_y)
        current_cell = field_cell.cell

        if current_cell:
            field_cell.cell = None
            self.world.cells.remove(current_cell)
            current_cell.x = None
            current_cell.y = None
            self.player.add_cell(current_cell)

            from core.observer import Event
            current_cell.notify_observers(Event(
                event_type="cell_removed",
                data={'x': self.cursor_x, 'y': self.cursor_y},
                source=current_cell
            ))
        else:
            selected = self.player.get_selected_cell()
            field_cell.cell = selected
            self.world.cells.append(selected)
            selected.placement(self.world, self.cursor_x, self.cursor_y)
            self.player.inventory.remove(selected)

            from core.observer import Event
            selected.notify_observers(Event(
                event_type="new_cell_placement",
                data={'x': self.cursor_x, 'y': self.cursor_y},
                source=selected
            ))
