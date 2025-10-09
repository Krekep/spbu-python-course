import pytest
from functools import reduce
from typing import Callable, Iterable, Dict, Iterator


@pytest.fixture
def small_dataset() -> Iterator[int]:
    """Fixture providing a small dataset generator."""
    return dataGen(5)


@pytest.fixture
def zero_dataset() -> Iterator[int]:
    """Fixture providing an empty dataset generator."""
    return dataGen(0)


@pytest.fixture
def my_operations() -> Dict[str, Callable[[Iterable], Iterable]]:
    """Fixture providing custom operations for testing."""
    return {
        'filter_triad': filter_triad,
        'cube': cube
    }


@pytest.fixture
def numb_3() -> Iterator[int]:
    """Fixture providing numbers divisible by 3."""
    return iter([0, 3, 6, 9, 12])


@pytest.fixture
def classic_operations() -> Dict[str, Callable[[Iterable], Iterable]]:
    """Fixture providing built-in style operations for testing."""
    return {
        'd_map': lambda x: map(lambda y: y * 2, x),
        'z_filter': lambda x: filter(lambda y: y % 2 == 0, x),
        'add_zip': lambda x: zip(x, map(lambda y: y + 10, x))
    }


class TestDataGen:
    """Test cases for the data generator component."""

    def test_correct_gen(self, small_dataset: Iterator[int]) -> None:
        """Test that data generator produces correct sequence."""
        result: list[int] = list(small_dataset)
        assert result == [0, 1, 2, 3, 4]

    def test_lazy(self) -> None:
        """Test lazy evaluation of data generator."""
        gen: Iterator[int] = dataGen(1000)
        trio: list[int] = [next(gen) for _ in range(3)]
        assert trio == [0, 1, 2]
        assert next(gen) == 3


class TestPipeline:
    """Test cases for the pipeline function."""
    
    def test_basic_flow(self, small_dataset: Iterator[int], 
                        my_operations: Dict[str, Callable[[Iterable], Iterable]]) -> None:
        """Test basic pipeline flow with custom operations."""
        result: Iterable = pipeline(
            small_dataset,
            my_operations['filter_triad'],
            my_operations['cube']
        )
        final: list[int] = to_list(result)
        assert final == [0, 27]


class TestFuncSupport:
    """Test cases for built-in function support."""
    
    def test_map(self, small_dataset: Iterator[int],
                 classic_operations: Dict[str, Callable[[Iterable], Iterable]]) -> None:
        """Test pipeline support for map function."""
        result: Iterable = pipeline(small_dataset, classic_operations['d_map'])
        final: list[int] = to_list(result)
        assert final == [0, 2, 4, 6, 8]

    def test_filter(self, small_dataset: Iterator[int],
                    classic_operations: Dict[str, Callable[[Iterable], Iterable]]) -> None:
        """Test pipeline support for filter function."""
        result: Iterable = pipeline(small_dataset, classic_operations['z_filter'])
        final: list[int] = to_list(result)
        assert final == [0, 2, 4]

    def test_zip(self, small_dataset: Iterator[int],
                 classic_operations: Dict[str, Callable[[Iterable], Iterable]]) -> None:
        """Test pipeline support for zip function."""
        result: Iterable = pipeline(small_dataset, classic_operations['add_zip'])
        final: list[tuple[int, int]] = to_list(result)
        assert final == [(0, 10), (1, 11), (2, 12), (3, 13), (4, 14)]

    def test_reduce(self, numb_3: Iterator[int]) -> None:
        """Test integration with reduce function."""
        data: Iterable = pipeline(numb_3, cube)
        result: int = reduce(lambda x, y: x + y, data)
        assert result == 0 + 27 + 216 + 729 + 1728


class TestCustomSupport:
    """Test cases for custom function support."""
    
    def test_filter_triad(self, small_dataset: Iterator[int]) -> None:
        """Test custom filter_triad function."""
        result: Iterable = filter_triad(small_dataset)
        final: list[int] = to_list(result)
        assert final == [0, 3]

    def test_cube_function(self) -> None:
        """Test custom cube function."""
        data: Iterator[int] = iter([1, 2, 3])
        result: Iterable = cube(data)
        final: list[int] = to_list(result)
        assert final == [1, 8, 27]


class TestAggregatorFunctions:
    """Test cases for aggregator functions."""
    
    def test_to_list(self, small_dataset: Iterator[int]) -> None:
        """Test to_list aggregator function."""
        result: list[int] = to_list(small_dataset)
        assert result == [0, 1, 2, 3, 4]
        assert isinstance(result, list)

    def test_to_set(self) -> None:
        """Test to_set aggregator function with duplicate handling."""
        def data_duplicates() -> Iterator[int]:
            """Generator yielding duplicate values for testing."""
            yield 1
            yield 2
            yield 1
            yield 3

        result: set[int] = to_set(data_duplicates())
        assert result == {1, 2, 3}
        assert isinstance(result, set)

    def test_to_dict(self, small_dataset: Iterator[int]) -> None:
        """Test to_dict aggregator function."""
        result: dict[int, int] = to_dict(small_dataset)
        expected: dict[int, int] = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
        assert result == expected
        assert isinstance(result, dict)
