import pytest
import numpy as np
from math import isclose

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from project.task1 import Vector, Matrix

# Vector
def test_vector_initialization():
    vec = Vector([1, 2, 3])
    assert np.array_equal(
        vec.vector, np.array([1, 2, 3])
    ), "Vector initialization failed"


def test_vector_length():
    vec = Vector([1, 2, 3])
    assert len(vec) == 3, "Vector length is incorrect"


def test_vector_getitem():
    vec = Vector([1, 2, 3])
    assert vec[0] == 1, "Vector __getitem__ is incorrect"


def test_vector_dot_product():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    vec1 = Vector(v1)
    vec2 = Vector(v2)
    assert vec1 * vec2 == sum(
        [x * y for x, y in zip(vec1, vec2)]
    ), "Dot product is incorrect"


def test_vector_norm():
    vec = Vector([3, 4])
    assert vec.norm() == 5, "Vector norm calculation is incorrect"


def test_vector_angle():
    vec1 = Vector([1, 0])
    vec2 = Vector([0, 1])
    angle = vec1 ^ vec2
    assert isclose(angle, np.pi / 2), "Angle between vectors is incorrect"


def test_zero_vector_norm():
    vec = Vector([0, 0, 0])
    with pytest.raises(ZeroDivisionError):
        vec ^ vec  # This should raise ZeroDivisionError


# Matrix
def test_matrix_addition():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    result = matrix1 + matrix2
    expected = Matrix([[6, 8], [10, 12]])
    assert np.array_equal(result.matrix, expected.matrix)


def test_matrix_multiplication():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    result = matrix1 @ matrix2
    expected = Matrix([[19, 22], [43, 50]])
    assert np.array_equal(result.matrix, expected.matrix)


def test_matrix_transpose():
    matrix1 = Matrix([[1, 2], [3, 4]])
    result = matrix1.T()
    expected = Matrix([[1, 3], [2, 4]])
    assert np.array_equal(result.matrix, expected.matrix)


def test_identity_multiplication():
    matrix1 = Matrix([[1, 2], [3, 4]])
    identity = Matrix([[1, 0], [0, 1]])
    result = matrix1 @ identity
    assert np.array_equal(result.matrix, matrix1.matrix)


def test_addition_with_zero_matrix():
    matrix1 = Matrix([[1, 2], [3, 4]])
    zero_matrix = Matrix([[0, 0], [0, 0]])
    result = matrix1 + zero_matrix
    assert np.array_equal(result.matrix, matrix1.matrix)
