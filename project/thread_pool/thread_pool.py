from threading import Thread
from queue import Queue
from typing import List, Callable, Set
from concurrent.futures import ThreadPoolExecutor
from itertools import product


class ThreadPool:
    """
    A class for managing a pool of threads that can execute tasks concurrently.

    Attributes:
        num_threads : int
            The number of worker threads in the pool.
        tasks : Queue
            A queue that holds tasks (functions) to be executed by the worker threads.
        threads : List[Thread]
            A list of the threads in the pool.
        is_active : bool
            A flag indicating if the thread pool is active and can accept new tasks.

    Methods:
        __init__(num_threads: int) -> None:
            Initializes the ThreadPool with a fixed number of worker threads and starts them.

        worker() -> None:
            A worker thread that processes tasks from the queue. Runs in a loop until the thread pool is disposed.

        enqueue(task: Callable) -> None:
            Adds a new task to the queue to be executed by an available worker thread.

        dispose() -> None:
            Signals all worker threads to finish their current tasks and terminate. Prevents new tasks from being added.
    """

    def __init__(self, num_threads: int) -> None:
        """
        Initializes the ThreadPool with a given number of threads and starts each one.

        Parameters:
        ----------
        num_threads : int
            The number of worker threads to be created and managed by the pool.
        """

        self.num_threads: int = num_threads
        self.tasks: Queue[Callable | None] = Queue()
        self.threads: List[Thread] = []
        self.is_active: bool = True
        for _ in range(num_threads):
            thread = Thread(target=self.worker)
            thread.start()
            self.threads.append(thread)

    def worker(self) -> None:
        """
        Worker method run by each thread.

        Continuously waits for tasks from the queue and executes them. Terminates when
        the thread pool is disposed and the shutdown signal (None) is received.
        """

        while self.is_active:
            task = self.tasks.get()
            if task is None:
                break
            try:
                task()
            finally:
                self.tasks.task_done()

    def enqueue(self, task: Callable) -> None:
        """
        Adds a task to the queue to be executed by a worker thread.

        Parameters:
        ----------
        task : Callable
            A callable function representing the task to be executed.

        Raises:
        -------
        RuntimeError
            If the thread pool is inactive and cannot accept new tasks.
        """

        if not self.is_active:
            raise RuntimeError("ThreadPool is inactive. Cannot enqueue new tasks.")

        self.tasks.put(task)

    def dispose(self) -> None:
        """
        Disposes of the thread pool by signaling all worker threads to finish their tasks and terminate.
        It also prevents new tasks from being added to the pool.
        """
        self.tasks.join()
        self.is_active = False
        for _ in range(self.num_threads):
            self.tasks.put(None)
        for thread in self.threads:
            thread.join()


def parallel_cartesian_sum(sets: List[Set[int]]):
    """
    Computes the sum of the Cartesian product of multiple sets of integers in parallel.

    Arguments:
        sets (list of list of int): A list of sets of integers for which the Cartesian product and sum need to be computed.

    Returns:
        int: The sum of all elements in the Cartesian product of the input sets.
    """
    with ThreadPoolExecutor() as executor:
        cartesian_product = list(product(*sets))
        result = executor.submit(sum, (sum(t) for t in cartesian_product))
        return result.result()
