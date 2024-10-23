import threading
from typing import Callable, List


class ThreadPool:
    """
    The pool creates a specified number of threads that wait for tasks to be added to the task queue.
    When a task is added, one of the threads retrieves and executes it.

    :param num_threads: The number of threads to create in the pool. This dictates how many tasks
                        can be executed simultaneously.
    """

    def __init__(self, num_threads: int):
        """
        Initializes the thread pool with the specified number of threads.

        :param num_threads: The number of threads to create in the pool.
        """
        self.num_threads: int = num_threads
        self.tasks: List[Callable] = []
        self.tasks_lock: threading.Lock = threading.Lock()
        self.task_available: threading.Condition = threading.Condition(self.tasks_lock)
        self.stopped: threading.Event = threading.Event()
        self.threads: List[threading.Thread] = []
        self._initialize_threads()

    def _initialize_threads(self) -> None:
        """
        Creates and starts threads that will execute tasks from the pool.
        The threads are set as daemon threads, meaning they will automatically exit
        when the main program exits.
        """
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self._worker, daemon=True)
            self.threads.append(thread)
            thread.start()

    def _worker(self) -> None:
        """
        The worker method that runs in each thread.
        It continuously waits for new tasks and executes them until the pool is disposed.
        """
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
        Adds a new task to the pool's task queue to be executed by the threads.

        :param task: A callable object (function) to be executed by one of the threads.
        :raises RuntimeError: If the pool has been disposed and new tasks are not allowed.
        :raises ValueError: If the task is not callable.
        """
        if self.stopped.is_set():
            raise RuntimeError("Cannot add tasks after the pool is disposed.")
        if not callable(task):
            raise ValueError("Task must be a callable object (function).")
        with self.task_available:
            self.tasks.append(task)
            self.task_available.notify()

    def dispose(self) -> None:
        """
        Terminates the thread pool, notifying all threads to finish their
        current tasks and stop. Blocks until all threads have completed their tasks.
        """
        self.stopped.set()
        with self.task_available:
            self.task_available.notify_all()
        for thread in self.threads:
            thread.join()
