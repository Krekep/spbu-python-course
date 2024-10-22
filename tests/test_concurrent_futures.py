import pytest
import time
import math
import itertools
from project.concurrent_futures import cartesian_product_cosine_sum, pair_cosine


@pytest.mark.parametrize(
    "numbers, expected_sum",
    [
        ([1, 2], math.cos(2) + math.cos(3) + math.cos(3) + math.cos(4)),
        ([1, 0], math.cos(2) + math.cos(1) + math.cos(1) + math.cos(0)),
        ([1, -1], math.cos(2) + math.cos(0) + math.cos(0) + math.cos(-2)),
        (
            [2, 4, 3],
            math.cos(4)
            + math.cos(6)
            + math.cos(5)
            + math.cos(6)
            + math.cos(8)
            + math.cos(7)
            + math.cos(5)
            + math.cos(7)
            + math.cos(6),
        ),
        ([0], math.cos(0)),
        ([], 0),
    ],
)
def test_cartesian_product_cosine_sum(numbers, expected_sum):
    """Тестирует корректность суммы косинусов."""
    assert cartesian_product_cosine_sum(numbers) == expected_sum


def test_comparison():
    """Сравнивает производительность многопроцессного и однопоточного подходов."""
    numbers = list(range(100))

    start_time = time.time()

    if not numbers:
        single_thread_sum = 0
    else:
        pairs = list(itertools.product(numbers, repeat=2))
        results = [pair_cosine(pair) for pair in pairs]
        single_thread_sum = sum(results)

    single_thread_time = time.time() - start_time

    start_time = time.time()
    cartesian_product_cosine_sum(numbers)
    multi_thread_time = time.time() - start_time

    print(f"Single-threaded time: {single_thread_time:.4f}s")
    print(f"Multi-threaded time: {multi_thread_time:.4f}s")
