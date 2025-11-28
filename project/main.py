import multiprocessing
from multiprocessing import Queue
from interfaces import keyboard_process
from interfaces import ui_process
from core import simulation_process


def main():
    input_queue = Queue()
    world_state_queue = Queue()

    # Создаем процессы
    processes = [
        multiprocessing.Process(target=keyboard_process, args=(input_queue,), name="KeyboardProcess"),
        multiprocessing.Process(target=ui_process, args=(world_state_queue,), name="UIProcess"),
        multiprocessing.Process(target=simulation_process, args=(input_queue, world_state_queue),
                                name="SimulationProcess")
    ]

    # Запускаем процессы
    for process in processes:
        process.start()
        print(f"🚀 Запущен процесс: {process.name}")

    # Ждем завершения
    try:
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        print("\n🛑 Остановка процессов...")
        for process in processes:
            process.terminate()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
