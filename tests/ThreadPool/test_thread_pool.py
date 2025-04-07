import pytest
import project.ThreadPool.thread_pool as tp
import time
import threading

def example_task_1(x, results):
    time.sleep(1) 
    results.append(x)

def example_task_2(x, results):
    time.sleep(x) 
    results.append(x)



def test_num_threads_and_disposal():
    pool = tp.ThreadPool(3)

    assert threading.active_count() == 4, f"Expected 4 active threads, but got {threading.active_count()}"

    results = []
    
    for i in range(3):
        pool.enqueue(example_task_1, i, results)

    time.sleep(0.5)  
    assert len(results) == 0, "Threads should not be done yet"

    pool.dispose()

    assert len(results) == 3, "Not all tasks finished after dispose"





def concurrency_test():
    pool = tp.ThreadPool(3)
    results = []

    start_time = time.time()
    for i in range(3):
        pool.enqueue(example_task_2, i+1, results)

    pool.dispose()

    end_time = time.time()

    assert end_time - start_time < 4, "Tasks were not executed in parallel (execution took too long)"
    


def test_enqueue_and_execute():
    pool = tp.ThreadPool(3)
    results = []

    start_time = time.time()

    for i in range(6):
        pool.enqueue(example_task_1, i, results)

    pool.dispose()

    end_time = time.time()

    assert sorted(results) == [
        0,
        1,
        2,
        3,
        4,
        5,
    ], "Tasks did not execute in the expected order"
    assert (
        end_time - start_time < 3
    ), "Tasks were not executed in parallel (execution took too long)"
