import threading
from typing import Callable, List


class ThreadPool:

    """
    The ThreadPool class manages a pool of threads to execute tasks concurrently.

    Attributes:

        num_threads (int):
            Number of threads in the thread pool.
        tasks (list):
            List of tasks to be executed by the threads.
        threads (list):
            List of thread objects.
        lock (threading.Lock):
            Mutex lock for thread synchronization.
        condition (threading.Condition):
            Condition variable for thread synchronization.
        stop (bool):
            Flag to signal threads to stop.
    Methods:

        init(self, num_threads):
            Constructor method to initialize the ThreadPool with a specified number of threads.
        worker(self):
            Worker method for individual threads to execute tasks from the task queue.
        enqueue(self, task):
            Add a task to the task queue.
        dispose(self):
            Stop the thread pool and wait for all threads to finish.

    """

    def __init__(self, num_threads: int) -> None:

        """
        Initializes the ThreadPool with a specified number of threads.

        Args:
            num_threads (int): The number of threads to create in the pool.
        """

        self.num_threads: int = num_threads
        self.tasks: List[Callable | None] = []
        self.threads: List[threading.Thread] = []
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.stop = False

        for _ in range(num_threads):

            thread = threading.Thread(target=self.worker)
            thread.start()
            self.threads.append(thread)

    def worker(self) -> None:

        """
        Initializes the ThreadPool with a specified number of threads.

        Args:
            num_threads (int): The number of threads to create in the pool.
        """

        while True:
            with self.condition:
                while not self.tasks:
                    self.condition.wait()

                task = self.tasks.pop(0)

            if task is None:
                break

            task()

    def enqueue(self, task: Callable) -> None:

        """
        Adds a task to the task queue.

        Args:
            task (callable): The task to be executed.
        """

        with self.condition:
            self.tasks.append(task)
            self.condition.notify()

    def dispose(self) -> None:

        """
        Stops the thread pool and waits for all threads to finish.
        """

        with self.condition:

            self.stop = True
            for _ in range(self.num_threads):
                self.tasks.append(None)
            self.condition.notify_all()

        for thread in self.threads:
            thread.join()
