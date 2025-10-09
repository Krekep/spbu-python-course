import pytest

from project.task1.vectors import scalar_mult, vector_length, angle_vectors


def scalar_mult_test():
    """Test of calculating the scalar product"""
    assert scalar_mult([1, 2, 3], [4, 5, 7]) == 32
    assert scalar_mult([1, 2, 3], [0, 0, 0]) == 0
    assert scalar_mult([1, -2], [-1, 2]) == -5


def scalar_mult_test_error():
    """Test the scalar product of different lengths"""
    with pytest.raises(ValueError):
        scalar_mult([1, 2, 3], [1, 2])


def vector_length_test():
    """Test of calculating the length of a vector"""
    assert vector_length([3, 4]) == 5
    assert vector_length([0, 0]) == 0
    assert vector_length([-3, -4]) == 5


def angle_vectors_test():
    """Test of calculating the angle between vectors"""
    assert angle_vectors([1, 0], [0, 0]) == 90


def angle_vectors_test_error():
    """Test of calculating the angle between vectors with zero length"""
    with pytest.raises(ValueError):
        angle_vectors([0, 0], [1, 2])
    with pytest.raises(ValueError):
        angle_vectors([0, 0], [0, 0])
