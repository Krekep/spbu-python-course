import pytest
import time
import math
import itertools
from project.concurrent_futures import cartesian_product_heavy_sum, heavy_computation


@pytest.mark.parametrize(
    "numbers, expected_sum",
    [
        (
            [1, 0],
            math.sqrt(math.cos(1) * math.sin(0) + 1)
            + math.sqrt(math.cos(0) * math.sin(1) + 1)
            + math.sqrt(math.cos(1) * math.sin(1) + 1)
            + math.sqrt(math.cos(0) * math.sin(0) + 1),
        ),
        (
            [1, -1],
            math.sqrt(math.cos(1) * math.sin(-1) + 1)
            + math.sqrt(math.cos(-1) * math.sin(1) + 1)
            + math.sqrt(math.cos(1) * math.sin(1) + 1)
            + math.sqrt(math.cos(-1) * math.sin(-1) + 1),
        ),
        ([0], math.sqrt(math.cos(0) * math.sin(0) + 1)),
        ([], 0),
    ],
)
def test_cartesian_product_heavy_sum(numbers, expected_sum):
    """
    Tests the correctness of the heavy computation sum.

    :param numbers: A list of numbers to be used for calculating the cartesian product.
    :param expected_sum: The expected sum of heavy computations for the given numbers.
    """
    assert cartesian_product_heavy_sum(numbers) == expected_sum


def test_comparison():
    """
    Compares the performance of multi-threaded and single-threaded approaches.
    This test measures the execution time for calculating the sum of heavy computations using both approaches.
    """
    numbers = list(range(100))

    start_time = time.time()
    pairs = list(itertools.product(numbers, repeat=2))
    single_thread_sum = sum(heavy_computation(pair) for pair in pairs)
    single_thread_time = time.time() - start_time

    start_time = time.time()
    cartesian_product_heavy_sum(numbers)
    multi_thread_time = time.time() - start_time

    # print(f"Single-threaded time: {single_thread_time:.4f}s")
    # print(f"Multi-threaded time: {multi_thread_time:.4f}s")

    # assert multi_thread_time < single_thread_time, "Multi-threaded approach should be faster than single-threaded."
    assert single_thread_sum == cartesian_product_heavy_sum(
        numbers
    ), "Results should match for single-threaded and multi-threaded approaches."
