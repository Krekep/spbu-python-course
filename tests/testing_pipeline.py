import pytest
from functools import reduce
from typing import Callable, Iterable, Dict, Iterator, Tuple, List, Set
from project.pipeline import dataGen, filter_triad, cube, pipeline, to_collect


@pytest.fixture
def small_dataset() -> Iterator[int]:
    """Fixture providing a small dataset generator."""
    return dataGen(10)


@pytest.fixture
def my_operations() -> Dict[str, Callable[[Iterable], Iterable]]:
    """Fixture providing custom operations for testing."""
    return {"filter_triad": filter_triad, "cube": cube}


@pytest.fixture
def numb_3() -> Iterator[int]:
    """Fixture providing numbers divisible by 3."""
    return iter([0, 3, 6, 9, 12])


class TestDataGen:
    """Test cases for the data generator component."""

    def test_correct_gen(self, small_dataset: Iterator[int]) -> None:
        """Test that data generator produces correct sequence."""
        result: List[int] = to_collect(small_dataset, flag="l")
        assert result == [0, 1, 2, 3, 4]

    def test_lazy(self) -> None:
        """Test lazy evaluation of data generator."""
        gen: Iterator[int] = dataGen(1000)
        trio: List[int] = [next(gen) for _ in range(3)]
        assert trio == [0, 1, 2]
        assert next(gen) == 3


class TestPipeline:
    """Test cases for the pipeline function."""

    def test_basic_flow(
        self,
        small_dataset: Iterator[int],
        my_operations: Dict[str, Callable[[Iterable], Iterable]],
    ) -> None:
        """Test basic pipeline flow with custom operations."""
        result: Iterable = pipeline(
            small_dataset, my_operations["filter_triad"], my_operations["cube"]
        )
        final: List[int] = to_collect(result, flag="l")
        assert final == [0, 27]


class TestFuncSupport:
    """Test cases for built-in function support."""

    def test_map(
        self,
        small_dataset: Iterator[int],
        classic_operations: Dict[str, Callable[[Iterable], Iterable]],
    ) -> None:
        """Test pipeline support for map function."""
        result: Iterable = pipeline(small_dataset, map)
        final: List[int] = to_collect(result, flag="l")
        assert final == [0, 2, 4, 6, 8]

    def test_filter(
        self,
        small_dataset: Iterator[int],
        classic_operations: Dict[str, Callable[[Iterable], Iterable]],
    ) -> None:
        """Test pipeline support for filter function."""
        result: Iterable = pipeline(small_dataset, filter)
        final: List[int] = to_collect(result, flag="l")
        assert final == [0, 2, 4]

    def test_zip(
        self,
        small_dataset: Iterator[int],
        classic_operations: Dict[str, Callable[[Iterable], Iterable]],
    ) -> None:
        """Test pipeline support for zip function."""
        result: Iterable = pipeline(small_dataset, zip)
        final: List[Tuple[int, int]] = to_collect(result, flag="l")
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
        final: List[int] = to_collect(result, flag="l")
        assert final == [0, 3]

    def test_cube_function(self) -> None:
        """Test custom cube function."""
        data: Iterator[int] = iter([1, 2, 3])
        result: Iterable = cube(data)
        final: List[int] = to_collect(result, flag="l")
        assert final == [1, 8, 27]


class TestAggregatorFunctions:
    def test_to_collect(self) -> None:
        """Test all collection modes in one test."""
        data = [1, 2, 3, 4]

        # Test list flag
        result_list = to_collect(data, flag="l")
        assert result_list == [1, 2, 3, 4]
        assert isinstance(result_list, list)

        # Test set flag
        result_set = to_collect(data, flag="s")
        assert result_set == {1, 2, 3, 4}
        assert isinstance(result_set, set)

        # Test dict flag without key
        result_dict_default = to_collect(data, flag="d")
        assert result_dict_default == {0: 1, 1: 2, 2: 3, 3: 4}
        assert isinstance(result_dict_default, dict)

        # Test dict flag with key
        result_dict_with_key = to_collect(data, key=lambda x: f"key_{x}", flag="d")
        assert result_dict_with_key == {"key_1": 1, "key_2": 2, "key_3": 3, "key_4": 4}
        assert isinstance(result_dict_with_key, dict)
