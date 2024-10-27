import itertools
import concurrent.futures
import math


def heavy_computation(pair):
    """Performs a heavy computation on a pair of numbers."""
    return math.sqrt(math.cos(pair[0]) * math.sin(pair[1]) + 1)


def cartesian_product_heavy_sum(numbers):
    """Calculates the sum of heavy computations over the cartesian product of a set."""
    if not numbers:
        return 0

    pairs = list(itertools.product(numbers, repeat=2))

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(heavy_computation, pairs))

    total_sum = sum(results)
    return total_sum
