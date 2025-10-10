from functools import reduce
from typing import Any, Callable, Iterable, Iterator, List


def data_generator(start: int = 0, end: int = 10) -> Iterator[int]:
    """Generator that yields numbers from start to end-1."""
    for i in range(start, end):
        yield i


def pipeline(source: Iterable, *operations: Callable) -> Iterator:
    """
    Takes a data source and sequence of operations,
    applies them sequentially, returning a lazy generator.
    Operations are applied in the order they are provided.
    """
    stream = source
    for operation in operations:
        stream = operation(stream)
    return stream


def map_operation(func: Callable) -> Callable[[Iterable], Iterator]:
    """Map operation - applies function to each element."""

    def _inner(stream: Iterable) -> Iterator:
        for item in stream:
            yield func(item)

    return _inner


def filter_operation(predicate: Callable) -> Callable[[Iterable], Iterator]:
    """Filter operation - filters elements based on condition."""

    def _inner(stream: Iterable) -> Iterator:
        for item in stream:
            if predicate(item):
                yield item

    return _inner


def zip_operation(*others: Iterable) -> Callable[[Iterable], Iterator]:
    """Zip operation - combines with other iterables."""

    def _inner(stream: Iterable) -> Iterator:
        return zip(stream, *others)

    return _inner


def reduce_operation(
    func: Callable, initializer: Any = None
) -> Callable[[Iterable], Any]:
    """
    Reduce operation - reduces sequence to single value.
    Terminal operation - should be used at the end of pipeline.
    """

    def _inner(stream: Iterable) -> Any:
        if initializer is not None:
            return reduce(func, stream, initializer)
        return reduce(func, stream)

    return _inner


def take_operation(n: int) -> Callable[[Iterable], Iterator]:
    """Takes first n elements from the stream."""

    def _inner(stream: Iterable) -> Iterator:
        for i, item in enumerate(stream):
            if i < n:
                yield item
            else:
                break

    return _inner


def skip_operation(n: int) -> Callable[[Iterable], Iterator]:
    """Skips first n elements."""

    def _inner(stream: Iterable) -> Iterator:
        for i, item in enumerate(stream):
            if i >= n:
                yield item

    return _inner


def enumerate_operation(start: int = 0) -> Callable[[Iterable], Iterator]:
    """Adds index to each element."""

    def _inner(stream: Iterable) -> Iterator:
        for i, item in enumerate(stream, start):
            yield (i, item)

    return _inner


def custom_operation(func: Callable) -> Callable[[Iterable], Iterator]:
    """Wrapper for custom stream processing functions."""

    def _inner(stream: Iterable) -> Iterator:
        yield from func(stream)

    return _inner


def collect(stream: Iterable, collection_type: type = list) -> Any:
    """Collects lazy generator results into specified collection."""
    return collection_type(stream)


def collect_to_list(stream: Iterable) -> List:
    """Collects results into list."""
    return list(stream)


def count(stream: Iterable) -> int:
    """Counts number of elements in the stream."""
    return sum(1 for _ in stream)
