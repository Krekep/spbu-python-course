import math
import pytest
from project.vector_operations import (
    scalar_product,
    vector_length,
    angle_between_vectors,
)


def test_dot_product():
    v1 = [2, 3, 4]
    v2 = [5, 6, 7]
    assert scalar_product(v1, v2) == 56


def test_vector_length():
    v = [6, 8]
    assert math.isclose(vector_length(v), 10.0)


def test_angle_between_vectors():
    v1 = [1, 1]
    v2 = [-1, 1]
    angle = angle_between_vectors(v1, v2)
    assert math.isclose(angle, math.pi / 2)


def test_angle_between_zero_vector():
    v1 = [0, 0]
    v2 = [1, 1]
    with pytest.raises(ValueError):
        angle_between_vectors(v1, v2)


def test_vector_different_lengths():
    v1 = [1, 2]
    v2 = [3, 4, 5]
    with pytest.raises(ValueError):
        scalar_product(v1, v2)


def test_empty_vector():
    v1 = []
    v2 = [1, 2, 3]
    with pytest.raises(ValueError):
        scalar_product(v1, v2)


def test_invalid_data():
    v1 = [1, 2, "a"]
    v2 = [3, 4, 5]
    with pytest.raises(TypeError):
        scalar_product(v1, v2)


def test_empty_vector_length():
    v = []
    with pytest.raises(ValueError):
        vector_length(v)


def test_invalid_data_vector_length():
    v = [1, "a", 3]
    with pytest.raises(TypeError):
        vector_length(v)
