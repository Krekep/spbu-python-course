import threading


class ThreadPool:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.tasks = []
        self.threads = []
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self._shutdown = False

        for _ in range(self.num_threads):
            thread = threading.Thread(target=self._worker)
            thread.daemon = True
            thread.start()
            self.threads.append(thread)

    def _worker(self):
        while True:
            with self.condition:
                while not self.tasks and not self._shutdown:
                    self.condition.wait()
                if self._shutdown and not self.tasks:
                    break
                task = self.tasks.pop(0)
            task()

    def enqueue(self, task):
        with self.condition:
            if not self._shutdown:
                self.tasks.append(task)
                self.condition.notify()

    def dispose(self):
        with self.condition:
            self._shutdown = True
            self.condition.notify_all()

        for thread in self.threads:
            thread.join()