import threading
import time
import pytest
from project.thread_pool.thread_pool import ThreadPool


def sample_task(x):

    """
    A sample task function that simulates a task by sleeping for 1 second and printing a completion message.

    """

    time.sleep(1)
    print(f"The task {x} is completed")


def test_enqueue():

    """
    Test the enqueue method of the ThreadPool class.

    This test creates a ThreadPool with 3 threads, enqueues 4 tasks, and checks if all tasks are executed.
    """

    num_threads = 3
    pool = ThreadPool(num_threads)

    tasks_executed = []

    def ex_task(x):
        tasks_executed.append(x)

    for i in range(4):
        pool.enqueue(lambda i=i: ex_task(i))

    time.sleep(1)
    pool.dispose()

    assert (
        len(tasks_executed) == 4
    ), f"!expected 4 tasks completed, got {len(tasks_executed)}!"


def test_dispose():

    """
    Test the dispose method of the ThreadPool class.

    This test creates a ThreadPool with 5 threads, enqueues a sample task, disposes the pool,
    and checks if all threads are completed.
    """
    num_threads = 5
    pool = ThreadPool(num_threads)

    pool.enqueue(sample_task)
    pool.dispose()
    pool.enqueue(sample_task)

    for thread in pool.threads:
        assert not thread.is_alive(), "!not all threads are completed!"


def test_thread_pool():

    """
    Test the initialization of the ThreadPool class.

    This test creates a ThreadPool with 6 threads and checks if the correct number of threads are created.
    """

    pool = ThreadPool(6)

    assert len(pool.threads) == 6, f"!expected 6 threads, found {len(pool.threads)}!"

    pool.dispose()


def test_active_thread():

    """
    Test the active thread count after creating a ThreadPool.

    This test creates a ThreadPool with 7 threads, waits for a short period, and checks if the correct number
    of active threads are present.
    """

    active_threads = threading.active_count()
    pool = ThreadPool(7)

    time.sleep(0.5)

    new_active_threads = threading.active_count()
    res_active_threads = new_active_threads - active_threads
    pool.dispose()

    assert (
        res_active_threads == 7
    ), f"!expected 7 active threads, found {res_active_threads}!"


def test_add_tasks_to_thread_pool_after_n_tasks_finished():

    n = 8
    tasks_executed = []

    def ex_task(x):
        tasks_executed.append(x)

    pool = ThreadPool(n)

    for i in range(n):
        pool.enqueue(lambda i=i: ex_task(i))

    time.sleep(1)

    assert (
        len(tasks_executed) == 8
    ), f"!expected 8 tasks completed, got {len(tasks_executed)}!"

    for i in range(n, n * 2):
        pool.enqueue(lambda i=i: ex_task(i))

    time.sleep(1)

    assert (
        len(tasks_executed) == 16
    ), f"!expected 16 tasks completed, got {len(tasks_executed)}!"

    pool.dispose()
