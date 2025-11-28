from multiprocessing import Queue
import concurrent.futures
import time
from models import World
from models import Player
from .simulation import Simulation
# from models import CellActions


def simulation_process(input_queue: Queue, world_state_queue: Queue):
    world = World()
    player = Player()
    simulation = Simulation(world, player)

    last_ui_update = 0
    ui_update_interval = 0.1

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        while True:
            current_time = time.time()

            simulation.process_input(input_queue)

            if not simulation.is_paused:
                cells_to_update = [cell for cell in world.cells
                                   if cell.is_alive and cell.x is not None and cell.y is not None]

                if cells_to_update:
                    batch_size = max(1, len(cells_to_update) // 4)
                    futures = []

                    for i in range(0, len(cells_to_update), batch_size):
                        batch = cells_to_update[i:i + batch_size]
                        future = executor.submit(update_cell_batch, batch)
                        futures.append(future)

                    for future in concurrent.futures.as_completed(futures):
                        try:
                            future.result()
                        except Exception as e:
                            print(f"Ошибка обновления клетки: {e}")

            if current_time - last_ui_update >= ui_update_interval:
                world_state = {
                    'world': world,
                    'player': player,
                    'cursor': (simulation.cursor_x, simulation.cursor_y),
                    'is_paused': simulation.is_paused,
                    'show_temp': simulation.show_temperature,
                    'show_nutrients': simulation.show_nutrients
                }

                while not world_state_queue.empty():
                    try:
                        world_state_queue.get_nowait()
                    except Exception as e:
                        print(f"Ошибка: {e}")
                        break

                world_state_queue.put(world_state)
                last_ui_update = current_time

            time.sleep(0.05)


def update_cell_batch(cell_batch):
    for cell in cell_batch:
        try:
            from models import CellActions
            gen = CellActions.action_generator(cell)
            cell.handle_action(next(gen))
        except Exception as e:
            print(f"Ошибка обновления клетки: {e}")
