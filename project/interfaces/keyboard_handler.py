import keyboard
from multiprocessing import Queue
import time


def keyboard_process(input_queue: Queue):
    key_actions = {
        'p': 'pause',
        'up': 'up', 'w': 'up',
        'down': 'down', 's': 'down',
        'left': 'left', 'a': 'left',
        'right': 'right', 'd': 'right',
        'space': 'space',
        't': 'toggle_temp',
        'n': 'toggle_nutrients',
        'enter': 'select',
        'f5': 'save',
        'f6': 'load',
        'f1': 'list_saves'
    }

    last_key_time = {}
    key_reload = 0.15

    while True:
        current_time = time.time()

        for key, action in key_actions.items():
            if keyboard.is_pressed(key):
                if key not in last_key_time or current_time - last_key_time[key] > key_reload:
                    input_queue.put(action)
                    last_key_time[key] = current_time

        time.sleep(0.02)
