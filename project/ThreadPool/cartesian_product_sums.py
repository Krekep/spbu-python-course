from typing import List, Generator, Tuple
import itertools
from concurrent.futures import ProcessPoolExecutor

def cartesian_product_gen(sets: List[List[int]]) -> Generator[Tuple[int, ...], None, None]:
    """
    Генератор декартова произведения (всех возможных комбинаций) для списка множеств целых чисел.

    Args:
    sets (List[List[int]]): Список списков целых чисел, для которых вычисляется декартово произведение.

    Returns:
    Generator[Tuple[int, ...], None, None]: Генератор, возвращающий кортежи с комбинациями элементов входных множеств.

    Raises:
    Нет исключений.
    """
    for combination in itertools.product(*sets):
        yield combination


def cartesian_product_sum(thread_num: int, sets: List[List[int]]) -> int:
    """
    Вычисляет сумму всех элементов декартова произведения с использованием многопоточной обработки.

    Args:
    thread_num (int): Количество потоков для параллельных вычислений.
    sets (List[List[int]]): Список списков целых чисел для обработки.

    Returns:
    int: Сумма всех элементов всех комбинаций декартова произведения.

    Raises:
    Нет.
    """
    gen = cartesian_product_gen(sets)
    total_sum = 0
    with ProcessPoolExecutor(max_workers=thread_num) as executor:
        futures = executor.map(sum, gen)
        total_sum = sum(futures)
    return total_sum
