from functools import reduce
from typing import Callable, Iterable, Any, List


def dataGen(n: int) -> Iterable[int]:
    """Input data generator"""
    for i in range(n):
        yield i

def to_list(data: Iterable) -> List:
    """Collects results into a list"""
    return list(data)

def to_dict(data: Iterable, key: Callable = None) -> dict:
    """Collects results into a dictionary"""
    if key is None:
        return dict(enumerate(data))
    return {key(i): i for i in data}

def to_set(data: Iterable) -> set:
    """Collects results into a set"""
    return set(data)

def filter_triad(num: Iterable) -> Iterable:
    """Custom function to filter numbers divisible by 3"""
    for n in num:
        if n % 3 == 0:
            yield n

def cube(num: Iterable) -> Iterable:
    """User-defined cube function"""
    for n in num:
        yield n ** 3

def pipeline(data: Iterable, *operations: Callable) -> Iterable:
    """
    A general-purpose pipeline that applies operations sequentially
    """
    result = data
    for operation in operations:
        result = operation(result)
    return result
  
