import threading
from typing import Callable, List


class ThreadPool:
    def __init__(self, num_threads: int):
        """Инициализирует пул потоков с заданным числом потоков."""
        self.num_threads: int = num_threads
        self.tasks: List[Callable] = []
        self.tasks_lock: threading.Lock = threading.Lock()
        self.task_available: threading.Condition = threading.Condition(self.tasks_lock)
        self.stopped: threading.Event = threading.Event()
        self.threads: List[threading.Thread] = []
        self._initialize_threads()

    def _initialize_threads(self) -> None:
        """Создает и запускает потоки для выполнения задач."""
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self._worker, daemon=True)
            self.threads.append(thread)
            thread.start()

    def _worker(self) -> None:
        """Рабочий метод, который выполняет задачи из пула."""
        while not self.stopped.is_set():
            with self.task_available:
                while not self.tasks and not self.stopped.is_set():
                    self.task_available.wait()
                if self.stopped.is_set():
                    break
                task = self.tasks.pop(0)

            try:
                task()
            except Exception as e:
                print(f"Exception in task: {e}")

    def enqueue(self, task: Callable) -> None:
        """
        Добавляет задачу в пул для выполнения.
        Вызывает RuntimeError: если пул уже завершен.
        Вызывает ValueError: если задача не является вызываемым объектом.
        """
        if self.stopped.is_set():
            raise RuntimeError("Cannot add tasks after the pool is disposed.")
        if not callable(task):
            raise ValueError("Task must be a callable object (function).")
        with self.task_available:
            self.tasks.append(task)
            self.task_available.notify()

    def dispose(self) -> None:
        """Завершает работу пула и ожидает завершения всех потоков."""
        self.stopped.set()
        with self.task_available:
            self.task_available.notify_all()
        for thread in self.threads:
            thread.join()
