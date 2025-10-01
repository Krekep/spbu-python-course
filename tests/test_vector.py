from math import acos, sqrt

import pytest

from project.vector import Vector


def test_vector_len_iter_index():
    v = Vector([1, 2, 3])
    assert len(v) == 3
    assert list(iter(v)) == [1.0, 2.0, 3.0]
    assert v[1] == 2.0


def test_vector_add_sub():
    v = Vector([1, 2, 3])
    w = Vector([4, 5, 6])
    assert list(v + w) == [5.0, 7.0, 9.0]
    assert list(w - v) == [3.0, 3.0, 3.0]


def test_vector_scalar_mul():
    v = Vector([1, -2, 3])
    assert list(v * 2) == [2.0, -4.0, 6.0]
    assert list(0.5 * v) == [0.5, -1.0, 1.5]


def test_vector_dot_and_norm():
    v = Vector([1, 2, 3])
    w = Vector([4, -5, 6])
    assert v @ w == 1 * 4 + 2 * -5 + 3 * 6
    assert abs(v) == sqrt(1 + 4 + 9)


def test_vector_angle():
    v = Vector([1, 0])
    w = Vector([0, 1])
    assert pytest.approx(v.angle_with(w)) == acos(0.0)


def test_zero_vector_angle_error():
    v = Vector([0, 0])
    with pytest.raises(ValueError):
        _ = v.angle_with(Vector([1, 0]))


def test_size_mismatch():
    v = Vector([1, 2])
    w = Vector([1, 2, 3])
    with pytest.raises(ValueError):
        _ = v + w
    with pytest.raises(ValueError):
        _ = v @ w
