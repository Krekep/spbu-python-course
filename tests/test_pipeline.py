import pytest
from functools import reduce
from typing import Callable, Iterable, Dict, Iterator, Tuple, List, Set, Any
from project.pipeline import dataGen, randomiser, ran_stri, pipeline, to_collect


@pytest.fixture
def small_dataset() -> Iterator[int]:
    return dataGen(5)


@pytest.fixture
def my_operations() -> Dict[str, Any]:
    return {"randomiser": randomiser, "ran_stri": ran_stri}


@pytest.fixture
def numb_3() -> Iterator[int]:
    return dataGen(5)


class TestDataGen:
    def test_correct_gen(self, small_dataset: Iterator[int]) -> None:
        result = to_collect(small_dataset, flag="l")
        assert result == [0, 1, 2, 3, 4]

    def test_lazy(self) -> None:
        gen = dataGen(1000)
        trio = [next(gen) for _ in range(3)]
        assert trio == [0, 1, 2]
        assert next(gen) == 3


class TestPipeline:
    def test_basic_flow(
        self, small_dataset: Iterator[int], my_operations: Dict[str, Any]
    ) -> None:
        result = pipeline(small_dataset, lambda x: my_operations["randomiser"](5))
        final = to_collect(result, flag="l")
        assert len(final) == 5
        assert all(1 <= x <= 50 for x in final)


class TestFuncSupport:
    def test_map(self, small_dataset: Iterator[int]) -> None:
        result = pipeline(small_dataset, lambda x: (y * 2 for y in x))
        final = to_collect(result, flag="l")
        assert final == [0, 2, 4, 6, 8]

    def test_filter(self, small_dataset: Iterator[int]) -> None:
        result = pipeline(small_dataset, lambda x: (y for y in x if y % 2 == 0))
        final = to_collect(result, flag="l")
        assert final == [0, 2, 4]

    def test_zip(self) -> None:
        data = [0, 1, 2, 3, 4]
        result = pipeline(iter(data), lambda x: zip(x, (y + 10 for y in data)))
        final = to_collect(result, flag="l")
        assert final == [(0, 10), (1, 11), (2, 12), (3, 13), (4, 14)]

    def test_reduce(self) -> None:
        random_data = randomiser(5)
        result = reduce(lambda x, y: x + y, random_data)
        assert isinstance(result, int)
        assert 5 <= result <= 250


class TestCustomSupport:
    def test_randomiser(self) -> None:
        result = randomiser(5)
        final = to_collect(result, flag="l")
        assert len(final) == 5
        assert all(1 <= x <= 50 for x in final)

    def test_ran_stri_function(self) -> None:
        result = ran_stri(3)
        final = to_collect(result, flag="l")
        assert len(final) == 3
        for string in final:
            assert 1 <= len(string) <= 5
            assert all(char in "qwertyuiopasdfghjklzxcvbnm" for char in string)


class TestAggregatorFunctions:
    def test_to_collect(self) -> None:
        data = [1, 2, 3, 4]
        result_list = to_collect(data, flag="l")
        assert result_list == [1, 2, 3, 4]

        result_set = to_collect(data, flag="s")
        assert result_set == {1, 2, 3, 4}

        result_dict_default = to_collect(data, flag="d")
        assert result_dict_default == {0: 1, 1: 2, 2: 3, 3: 4}

        result_dict_with_key = to_collect(data, key=lambda x: f"key_{x}", flag="d")
        assert result_dict_with_key == {"key_1": 1, "key_2": 2, "key_3": 3, "key_4": 4}
