import pytest
from typing import Generator, List, Tuple
from functools import reduce


@pytest.fixture
def sample_numbers():
    """Fixture providing sample numbers for testing"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def sample_strings():
    """Fixture providing sample strings for testing"""
    return ["apple", "banana", "cherry", "date", "elderberry"]


@pytest.fixture
def empty_list():
    """Fixture providing empty list for edge case testing"""
    return []


def square(x):
    """Square a number"""
    return x * x


def is_even(x):
    """Check if number is even"""
    return x % 2 == 0


def is_long_word(word, min_length=5):
    """Check if word length exceeds minimum length"""
    return len(word) > min_length


def add_exclamation(word):
    """Add exclamation mark to word"""
    return word + "!"


def custom_reducer(acc, x):
    """Custom reducer function for testing"""
    return acc + x


class TestGeneratorData:
    """Test cases for generator_data function"""

    def test_generator_data_with_numbers(self, sample_numbers):
        """Test generator with numeric data"""
        gen = generator_data(sample_numbers)
        result = list(gen)
        assert result == sample_numbers
        assert isinstance(gen, Generator)

    def test_generator_data_with_strings(self, sample_strings):
        """Test generator with string data"""
        gen = generator_data(sample_strings)
        result = list(gen)
        assert result == sample_strings

    def test_generator_data_empty(self, empty_list):
        """Test generator with empty input"""
        gen = generator_data(empty_list)
        result = list(gen)
        assert result == []


class TestPipeline:
    """Test cases for pipeline function with different operations"""

    @pytest.mark.parametrize(
        "input_data,expected",
        [
            ([1, 2, 3, 4], [1, 4, 9, 16]),
            ([0, 5, 10], [0, 25, 100]),
        ],
    )
    def test_pipeline_map(self, input_data, expected):
        """Test pipeline with map operation using parametrized inputs"""
        gen = generator_data(input_data)
        result_gen = pipeline(gen, lambda data: map(square, data))
        result = collect(result_gen)
        assert result == expected

    @pytest.mark.parametrize(
        "input_data,expected",
        [
            ([1, 2, 3, 4, 5, 6], [2, 4, 6]),
            ([1, 3, 5], []),
        ],
    )
    def test_pipeline_filter(self, input_data, expected):
        """Test pipeline with filter operation"""
        gen = generator_data(input_data)
        result_gen = pipeline(gen, lambda data: filter(is_even, data))
        result = collect(result_gen)
        assert result == expected

    def test_pipeline_multiple_operations(self, sample_numbers):
        """Test pipeline with multiple chained operations"""
        gen = generator_data(sample_numbers)
        result_gen = pipeline(
            gen, lambda data: filter(is_even, data), lambda data: map(square, data)
        )
        result = collect(result_gen)
        assert result == [4, 16, 36, 64, 100]

    def test_pipeline_with_strings(self, sample_strings):
        """Test pipeline operations with string data"""
        gen = generator_data(sample_strings)
        result_gen = pipeline(
            gen,
            lambda data: filter(lambda x: is_long_word(x, 4), data),
            lambda data: map(add_exclamation, data),
        )
        result = collect(result_gen)
        expected = ["apple!", "banana!", "cherry!", "elderberry!"]
        assert result == expected

    def test_pipeline_zip_operation(self):
        """Test pipeline with zip operation"""
        numbers = [1, 2, 3]
        letters = ["a", "b", "c"]
        gen1 = generator_data(numbers)
        gen2 = generator_data(letters)

        result_gen = pipeline(gen1, lambda data: zip(data, letters))
        result = collect(result_gen)
        assert result == [(1, "a"), (2, "b"), (3, "c")]

    def test_pipeline_empty_sequence(self, empty_list):
        """Test pipeline with empty input sequence"""
        gen = generator_data(empty_list)
        result_gen = pipeline(
            gen, lambda data: map(square, data), lambda data: filter(is_even, data)
        )
        result = collect(result_gen)
        assert result == []


class TestCollect:
    """Test cases for collect aggregator function"""

    @pytest.mark.parametrize(
        "output_type,expected_type",
        [
            (list, list),
            (tuple, tuple),
            (set, set),
        ],
    )
    def test_collect_different_types(self, sample_numbers, output_type, expected_type):
        """Test collect with different output types using parametrized tests"""
        gen = generator_data(sample_numbers)
        result = collect(gen, output_type)
        assert isinstance(result, expected_type)
        if output_type != set:
            assert result == output_type(sample_numbers)

    def test_collect_default_list(self, sample_numbers):
        """Test collect with default list output"""
        gen = generator_data(sample_numbers)
        result = collect(gen)
        assert isinstance(result, list)
        assert result == sample_numbers


class TestIntegration:
    """Integration tests for complete data processing workflow"""

    def test_complete_workflow(self):
        """Test complete workflow: generation → transformations → collection"""
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        gen = generator_data(data)
        processed = pipeline(
            gen,
            lambda data: filter(lambda x: x % 2 == 0, data),
            lambda data: map(lambda x: x * 2, data),
            lambda data: filter(lambda x: x > 5, data),
        )
        result = collect(processed)

        assert result == [8, 12, 16, 20]

    def test_complex_string_processing(self):
        """Test complex string processing workflow"""
        words = ["hello", "world", "python", "test", "programming"]

        gen = generator_data(words)
        processed = pipeline(
            gen,
            lambda data: filter(lambda x: len(x) > 4, data),
            lambda data: map(str.upper, data),
            lambda data: map(lambda x: x + "!", data),
        )
        result = collect(processed)

        expected = ["HELLO!", "WORLD!", "PYTHON!", "PROGRAMMING!"]
        assert result == expected


class TestLazyEvaluation:
    """Tests to verify lazy evaluation behavior"""

    def test_lazy_evaluation(self):
        """Test that computations are truly lazy (executed only when needed)"""
        call_count = 0

        def counting_square(x):
            """Square function that counts how many times it's called"""
            nonlocal call_count
            call_count += 1
            return x * x

        data = [1, 2, 3, 4, 5]
        gen = generator_data(data)
        squared_gen = pipeline(gen, lambda data: map(counting_square, data))

        assert call_count == 0

        result = collect(squared_gen)
        assert call_count == 5
        assert result == [1, 4, 9, 16, 25]

    def test_lazy_with_break_early(self):
        """Test that lazy evaluation allows breaking early from processing"""
        processed_items = []

        def track_processing(x):
            """Track which items get processed"""
            processed_items.append(x)
            return x * 2

        data = [1, 2, 3, 4, 5]
        gen = generator_data(data)
        processed_gen = pipeline(gen, lambda data: map(track_processing, data))

        result = []
        for i, item in enumerate(processed_gen):
            result.append(item)
            if i == 2:
                break

        assert processed_items == [1, 2, 3]
        assert result == [2, 4, 6]
