from functools import reduce
from typing import Iterable, Callable, Any, Optional, Dict, Set, List, Literal


def dataGen(n: int) -> Iterable[int]:
    """Input data generator"""
    for i in range(n):
        yield i


def to_collect(
    data: Iterable,
    key: Optional[Callable[..., Any]] = None,
    *,
    flag: Literal["l", "s", "d"]
) -> List | Set | Dict:
    """Collects results into a list"""
    if flag == "l":
        return list(data)
    if flag == "s":
        return set(data)
    if flag == "d":
        if key is None:
            return dict(enumerate(data))
        return {key(i): i for i in data}


def filter_triad(num: Iterable) -> Iterable:
    """Custom function to filter numbers divisible by 3"""
    for n in num:
        if n % 3 == 0:
            yield n


def cube(num: Iterable) -> Iterable:
    """User-defined cube function"""
    for n in num:
        yield n**3


def pipeline(data: Iterable, *operations: Callable) -> Iterable:
    """
    A general-purpose pipeline that applies operations sequentially
    """
    result = data
    for operation in operations:
        result = operation(result)
    return result
