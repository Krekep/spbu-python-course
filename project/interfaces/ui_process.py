from multiprocessing import Queue
import time


def ui_process(world_state_queue: Queue):
    from .console_ui import ConsoleUI

    ui = ConsoleUI()
    last_world_state = None

    while True:
        try:
            world_state = world_state_queue.get_nowait()
            last_world_state = world_state
        except Exception as _:
            pass

        if last_world_state is not None:
            ui.draw(last_world_state)

        time.sleep(0.05)
