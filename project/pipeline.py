from functools import reduce
from random import randint
from typing import (
    Iterable,
    Callable,
    Any,
    Optional,
    Dict,
    Set,
    List,
    Literal,
    Union,
    Iterator,
)


def dataGen(n: int) -> Iterator[int]:
    """Input data generator"""
    for i in range(n):
        yield i


def to_collect(
    data: Iterable,
    key: Optional[Callable[..., Any]] = None,
    *,
    flag: Literal["l", "s", "d"]
) -> Union[List, Set, Dict]:
    """Collects results into a list, set or dict"""
    if flag == "l":
        return list(data)
    if flag == "s":
        return set(data)
    if flag == "d":
        if key is None:
            return dict(enumerate(data))
        return {key(i): i for i in data}


def randomiser(num: int) -> Iterator[int]:
    """
    Generate a sequence of random integers.
    Args:
        num: Number of random integers to generate
    Yields:
        Random integers in the range 1-50
    """
    for _ in range(num):
        yield randint(1, 50)


def ran_stri(stri: int) -> Iterator[str]:
    """
    Generate random strings composed of lowercase English letters.
    Args:
        stri: Number of random strings to generate
    Yields:
        Random strings of length 1-5 characters
    """
    base: str = "qwertyuiopasdfghjklzxcvbnm"
    for _ in range(stri):
        leni: int = randint(1, 5)
        rand_str: str = "".join(base[randint(0, 25)] for _ in range(leni))
        yield rand_str


def pipeline(data: Iterable, *operations: Callable) -> Iterable:
    """
    A general-purpose pipeline that applies operations sequentially
    """
    result = data
    for operation in operations:
        result = operation(result)
    return result
