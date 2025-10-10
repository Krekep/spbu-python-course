import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../"))
from project.Task2.generator import *


class TestPipeline:
    """Simplified tests for data processing pipeline."""

    @pytest.fixture
    def sample_data(self):
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    @pytest.fixture
    def empty_data(self):
        return []

    @pytest.mark.parametrize(
        "start,end,expected",
        [
            (0, 5, [0, 1, 2, 3, 4]),
            (1, 4, [1, 2, 3]),
            (-2, 3, [-2, -1, 0, 1, 2]),
        ],
    )
    def test_data_generator(self, start, end, expected):
        """Test data generator with different ranges."""
        result = list(data_generator(start, end))
        assert result == expected

    @pytest.mark.parametrize(
        "func,expected",
        [
            (lambda x: x * 2, [2, 4, 6, 8, 10]),
            (lambda x: x**2, [1, 4, 9, 16, 25]),
            (str, ["1", "2", "3", "4", "5"]),
        ],
    )
    def test_map_operation(self, func, expected):
        """Test map operation with different functions."""
        data = [1, 2, 3, 4, 5]
        mapped = map_operation(func)(data)
        result = list(mapped)
        assert result == expected

    @pytest.mark.parametrize(
        "predicate,expected",
        [
            (lambda x: x % 2 == 0, [2, 4, 6, 8, 10]),
            (lambda x: x > 5, [6, 7, 8, 9, 10]),
            (lambda x: x < 3, [1, 2]),
        ],
    )
    def test_filter_operation(self, sample_data, predicate, expected):
        """Test filter operation with different predicates."""
        filtered = filter_operation(predicate)(sample_data)
        result = list(filtered)
        assert result == expected

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, []),
            (1, [1]),
            (3, [1, 2, 3]),
            (5, [1, 2, 3, 4, 5]),
            (100, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ],
    )
    def test_take_operation(self, sample_data, n, expected):
        """Test take operation with different counts."""
        taken = take_operation(n)(sample_data)
        result = list(taken)
        assert result == expected

    @pytest.mark.parametrize(
        "n,expected",
        [
            (0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            (1, [2, 3, 4, 5, 6, 7, 8, 9, 10]),
            (5, [6, 7, 8, 9, 10]),
            (9, [10]),
            (10, []),
        ],
    )
    def test_skip_operation(self, sample_data, n, expected):
        """Test skip operation with different counts."""
        skipped = skip_operation(n)(sample_data)
        result = list(skipped)
        assert result == expected

    @pytest.mark.parametrize(
        "start,expected",
        [
            (0, [(0, 1), (1, 2), (2, 3)]),
            (1, [(1, 1), (2, 2), (3, 3)]),
            (10, [(10, 1), (11, 2), (12, 3)]),
        ],
    )
    def test_enumerate_operation(self, start, expected):
        """Test enumerate operation with different start values."""
        data = [1, 2, 3]
        enumerated = enumerate_operation(start)(data)
        result = list(enumerated)
        assert result == expected

    @pytest.mark.parametrize(
        "func,initializer,expected",
        [
            (lambda x, y: x + y, None, 55),
            (lambda x, y: x + y, 100, 155),
            (lambda x, y: x * y, None, 3628800),
            (lambda x, y: x if x > y else y, None, 10),
        ],
    )
    def test_reduce_operation(self, sample_data, func, initializer, expected):
        """Test reduce operation with different functions and initializers."""
        if initializer is not None:
            reducer = reduce_operation(func, initializer)
        else:
            reducer = reduce_operation(func)

        result = reducer(sample_data)
        assert result == expected

    @pytest.mark.parametrize(
        "collection_type,expected_type",
        [
            (list, list),
            (tuple, tuple),
            (set, set),
        ],
    )
    def test_collect_different_types(self, sample_data, collection_type, expected_type):
        """Test collect operation with different collection types."""
        stream = filter_operation(lambda x: x % 2 == 0)(sample_data)
        result = collect(stream, collection_type)
        assert isinstance(result, expected_type)

    @pytest.mark.parametrize(
        "data,expected_count",
        [
            ([1, 2, 3, 4, 5], 5),
            ([], 0),
            ([1], 1),
            (range(10), 10),
        ],
    )
    def test_count_operation(self, data, expected_count):
        """Test count operation with different data."""
        result = count(data)
        assert result == expected_count

    def test_zip_operation(self):
        """Test zip operation."""
        data1 = [1, 2, 3]
        data2 = [10, 20, 30]
        zipped = zip_operation(data2)(data1)
        result = list(zipped)
        assert result == [(1, 10), (2, 20), (3, 30)]

    def test_custom_operation(self):
        """Test custom operation."""

        def double_batch(stream):
            for item in stream:
                yield item * 2

        custom_op = custom_operation(double_batch)
        result = list(custom_op([1, 2, 3]))
        assert result == [2, 4, 6]

    def test_pipeline_basic(self, sample_data):
        """Test basic pipeline."""
        result = list(pipeline(sample_data))
        assert result == sample_data

    def test_pipeline_with_operations(self, sample_data):
        """Test pipeline with operations."""
        result = list(
            pipeline(
                sample_data,
                filter_operation(lambda x: x % 2 == 0),
                map_operation(lambda x: x * 3),
                take_operation(3),
            )
        )
        assert result == [6, 12, 18]

    def test_pipeline_complex(self, sample_data):
        """Test complex pipeline."""
        result = list(
            pipeline(
                sample_data,
                filter_operation(lambda x: x > 3),
                skip_operation(2),
                take_operation(3),
                map_operation(str),
                enumerate_operation(1),
            )
        )
        assert result == [(1, "6"), (2, "7"), (3, "8")]

    def test_empty_data(self, empty_data):
        """Test with empty data."""
        result = list(
            pipeline(
                empty_data,
                map_operation(lambda x: x * 2),
                filter_operation(lambda x: x > 0),
                take_operation(5),
            )
        )
        assert result == []

        assert count(empty_data) == 0

    def test_lazy_evaluation(self):
        """Test lazy evaluation."""
        processed_items = []

        def track_processing(x):
            processed_items.append(x)
            return x * 2

        gen = data_generator(1, 1000)
        stream = pipeline(gen, map_operation(track_processing), take_operation(3))

        assert len(processed_items) == 0

        result = list(stream)

        assert len(processed_items) == 3
        assert result == [2, 4, 6]
