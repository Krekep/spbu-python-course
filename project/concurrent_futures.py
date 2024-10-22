import itertools
import concurrent.futures
import math


def pair_cosine(pair):
    """Вычисляет косинус суммы двух чисел в паре."""
    return math.cos(pair[0] + pair[1])


def cartesian_product_cosine_sum(numbers):
    """Вычисляет сумму косинусов полного декартового произведения множества."""
    if not numbers:
        return 0

    pairs = list(itertools.product(numbers, repeat=2))

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(pair_cosine, pairs))

    total_sum = sum(results)
    return total_sum
