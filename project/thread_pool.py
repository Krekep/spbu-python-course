import threading
from queue import Queue, Empty


class ThreadPool:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.tasks = Queue()
        self.stopped = threading.Event()
        self.threads = []
        self._initialize_threads()

    def _initialize_threads(self):
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self._worker, daemon=True)
            self.threads.append(thread)
            thread.start()

    def _worker(self):
        while not self.stopped.is_set():
            try:
                task = self.tasks.get(timeout=1)
            except Empty:
                continue
            try:
                task()
            except Exception as e:
                print(f"Exception in task: {e}")
            finally:
                self.tasks.task_done()

    def enqueue(self, task):
        if self.stopped.is_set():
            raise RuntimeError("Cannot add tasks after the pool is disposed.")
        if not callable(task):
            raise ValueError("Task must be a callable object (function).")
        self.tasks.put(task)

    def dispose(self):
        self.stopped.set()
        self.tasks.join()
