from typing import Generator, Iterable, Any, Callable, Sequence
from functools import reduce


def generator_data(data: Iterable[Any]) -> Generator:
    """Generator for generating data

    Parameters:
        data (Iterable): any iterable object

    Returns:
        Generator
    """
    for i in data:
        yield i


def pipeline(data: Generator, *operations: Callable) -> Generator:
    """A pipeline function that applies the passed operations to the input sequence in sequence

    Parameters:
        data (Generator): any iterable object
        *operations (Callable): operations for a data

    Returns:
        data: result
    """
    for oper in operations:
        data = oper(data)
    return data


def collect(gener: Iterable[Any], out: Callable = list) -> Sequence:
    """An aggregator function that collects the pipeline result into a collection

    Parameters:
        gener (Iterable): generator
        out (Callable): object of sequence

    Returns:
        Sequence: collection
    """
    return out(gener)
