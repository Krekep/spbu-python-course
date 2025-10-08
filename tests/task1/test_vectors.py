import pytest

from project.task1.vectors import scalar_mult, vector_length, angle_vectors


def test_scalar_mult():
    """Test of calculating the scalar product"""
    assert scalar_mult([1, 2, 3], [4, 5, 7]) == 35
    assert scalar_mult([1, 2, 3], [0, 0, 0]) == 0
    assert scalar_mult([1, -2], [-1, 2]) == -5


def test_scalar_mult_error():
    """Test the scalar product of different lengths"""
    with pytest.raises(ValueError):
        scalar_mult([1, 2, 3], [1, 2])


def test_vector_length():
    """Test of calculating the length of a vector"""
    assert vector_length([3, 4]) == 5
    assert vector_length([0, 0]) == 0
    assert vector_length([-3, -4]) == 5


def test_angle_vectors():
    """Test of calculating the angle between vectors"""
    assert angle_vectors([1, 0], [0, 1]) == 90


def test_angle_vectors_error():
    """Test of calculating the angle between vectors with zero length"""
    with pytest.raises(ValueError):
        angle_vectors([0, 0], [1, 2])
    with pytest.raises(ValueError):
        angle_vectors([0, 0], [0, 0])
