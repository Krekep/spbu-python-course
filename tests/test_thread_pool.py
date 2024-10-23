import pytest
from project.thread_pool import ThreadPool
import time
import threading
from typing import List


def test_thread_pool_executes_tasks() -> None:
    """
    Tests the execution of tasks in the thread pool.
    Ensures that all 5 tasks are executed successfully and their results are collected.

    :raises AssertionError: If the number of executed tasks does not match the expected count (5).
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
    Tests that the correct number of threads is created in the pool.
    Ensures that the active thread count increases by the number of threads created in the pool.

    :raises AssertionError: If the number of active threads does not match the expected count.
    """
    initial_active_count = threading.active_count()
    pool = ThreadPool(num_threads=3)

    assert threading.active_count() == initial_active_count + 3

    pool.dispose()


def test_thread_pool_no_tasks_after_dispose() -> None:
    """
    Tests that no new tasks can be added after the thread pool is disposed.

    :raises RuntimeError: If a task is added to the pool after it is disposed.
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
    Tests that the task added to the thread pool must be a callable object.

    :raises ValueError: If the task added to the pool is not callable.
    """
    pool = ThreadPool(num_threads=2)

    with pytest.raises(ValueError, match="Task must be a callable object"):
        pool.enqueue(46)

    pool.dispose()


def test_task_with_exception() -> None:
    """
    Tests that tasks continue to be executed even if one of the tasks raises an exception.
    Ensures that other tasks proceed even after an exception is raised in one of them.

    :raises AssertionError: If subsequent tasks are not executed after an exception occurs.
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
    Tests concurrent execution of tasks in the thread pool.
    Ensures that all tasks are executed and their results are collected in order.

    :raises AssertionError: If the number of executed tasks or their results does not match the expected order.
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
