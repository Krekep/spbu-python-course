import pytest
from project.vector import (
    dot_product,
    vector_length,
    angle,
)


def test_dot_product():
    assert dot_product([2, 5, 1], [3, 4, 2]) == 28.0

    # Test case for zero vector
    assert dot_product([0, 0, 0], [7, 8, 9]) == 0.0

    # Test case with vectors containing negative numbers
    assert dot_product([-3, 1, 2], [6, -4, 5]) == -12.0

    # Test case for mismatched vector sizes
    with pytest.raises(ValueError):
        dot_product([1, 3], [1, 2, 3])


def test_angle():
    # Tests for orthogonal vectors
    assert pytest.approx(angle([1, 0], [0, 3]), 0.1) == 90.0
    assert pytest.approx(angle([0, 1], [1, 0]), 0.1) == 90.0
    assert pytest.approx(angle([0, 6], [6, 0]), 0.1) == 90.0

    # Tests for parallel vectors
    assert pytest.approx(angle([4, 0], [4, 0]), 0.1) == 0.0
    assert pytest.approx(angle([-2, 0], [2, 0]), 0.1) == 180.0


def test_vector_length():
    assert vector_length([8, 15]) == pytest.approx(17.0)
    assert vector_length([0, 4, 0]) == 4.0
    assert vector_length([0, 0, 0]) == 0.0

    # Test case for a vector with negative components
    assert vector_length([-12, -5]) == pytest.approx(13.0)
