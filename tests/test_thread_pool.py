import pytest
from project.thread_pool import ThreadPool
import time
import threading
from typing import List


def test_thread_pool_executes_tasks() -> None:
    """
    Тестирует выполнение задач в пуле потоков.
    Проверяет, что все 5 задач были выполнены.
    """
    results: List[int] = []
    completed_tasks = threading.Event()

    def sample_task() -> None:
        results.append(1)
        if len(results) == 5:
            completed_tasks.set()

    pool = ThreadPool(num_threads=2)

    for _ in range(5):
        pool.enqueue(sample_task)

    completed_tasks.wait()
    pool.dispose()

    assert len(results) == 5


def test_thread_pool_correct_number_of_threads() -> None:
    """
    Тестирует, что в пуле потоков создается правильное количество потоков.
    """
    pool = ThreadPool(num_threads=3)

    assert len(pool.threads) == 3

    pool.dispose()


def test_thread_pool_no_tasks_after_dispose() -> None:
    """
    Проверяет, что нельзя добавлять задачи после завершения пула.
    """
    results: List[int] = []

    def sample_task() -> None:
        results.append(1)

    pool = ThreadPool(num_threads=2)

    pool.enqueue(sample_task)

    pool.dispose()

    with pytest.raises(
        RuntimeError, match="Cannot add tasks after the pool is disposed."
    ):
        pool.enqueue(sample_task)


def test_task_must_be_callable() -> None:
    """
    Проверяет, что задача должна быть вызываемым объектом.
    """
    pool = ThreadPool(num_threads=2)

    with pytest.raises(ValueError, match="Task must be a callable object"):
        pool.enqueue(46)

    pool.dispose()


def test_task_with_exception() -> None:
    """
    Проверяет, что при возникновении исключения в задаче,
    остальные задачи продолжают выполняться.
    """
    results: List[int] = []
    completed_tasks = threading.Event()

    def task_with_exception() -> None:
        raise ValueError("Test Exception")

    def normal_task() -> None:
        results.append(1)
        if len(results) == 1:
            completed_tasks.set()

    pool = ThreadPool(num_threads=2)

    pool.enqueue(task_with_exception)
    pool.enqueue(normal_task)

    completed_tasks.wait()
    pool.dispose()

    assert len(results) == 1


def test_thread_pool_concurrent_tasks() -> None:
    """
    Тестирует выполнение нескольких задач одновременно.
    Проверяет, что все задачи были выполнены.
    """
    results: List[int] = []
    completed_tasks = threading.Event()

    def sample_task(x: int) -> None:
        time.sleep(0.5)
        results.append(x)
        if len(results) == 5:
            completed_tasks.set()

    pool = ThreadPool(num_threads=3)

    for i in range(5):
        pool.enqueue(lambda i=i: sample_task(i))

    completed_tasks.wait()
    pool.dispose()

    assert sorted(results) == [0, 1, 2, 3, 4]
