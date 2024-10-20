import pytest
from project.thread_pool import ThreadPool
import time


def test_thread_pool_executes_tasks():
    results = []

    def sample_task():
        results.append(1)

    pool = ThreadPool(num_threads=2)

    for _ in range(5):
        pool.enqueue(sample_task)

    pool.tasks.join()

    assert len(results) == 5

    pool.dispose()


def test_thread_pool_correct_number_of_threads():
    pool = ThreadPool(num_threads=3)

    assert len(pool.threads) == 3

    pool.dispose()


def test_thread_pool_no_tasks_after_dispose():
    results = []

    def sample_task():
        results.append(1)

    pool = ThreadPool(num_threads=2)

    pool.enqueue(sample_task)

    pool.dispose()

    with pytest.raises(
        RuntimeError, match="Cannot add tasks after the pool is disposed."
    ):
        pool.enqueue(sample_task)


def test_task_must_be_callable():
    pool = ThreadPool(num_threads=2)

    with pytest.raises(ValueError, match="Task must be a callable object"):
        pool.enqueue(46)

    pool.dispose()


def test_task_with_exception():
    results = []

    def task_with_exception():
        raise ValueError("Test Exception")

    def normal_task():
        results.append(1)

    pool = ThreadPool(num_threads=2)

    pool.enqueue(task_with_exception)
    pool.enqueue(normal_task)

    pool.tasks.join()

    assert len(results) == 1

    pool.dispose()


def test_thread_pool_concurrent_tasks():
    results = []

    def sample_task(x):
        time.sleep(0.5)
        results.append(x)

    pool = ThreadPool(num_threads=3)

    for i in range(5):
        pool.enqueue(lambda i=i: sample_task(i))

    pool.tasks.join()

    assert sorted(results) == [0, 1, 2, 3, 4]

    pool.dispose()
