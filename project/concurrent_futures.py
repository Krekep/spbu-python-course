import concurrent.futures
import itertools


def pair_sum(pair):
    return sum(pair)


def cartesian_product_sum(numbers):
    if not numbers:
        return 0

    pairs = list(itertools.product(numbers, repeat=2))

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(pair_sum, pairs))

    total_sum = sum(results)
    return total_sum
