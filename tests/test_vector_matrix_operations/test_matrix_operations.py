import pytest
import numpy as np
from math import isclose

from project.vector_matrix_operations.Matrix import Matrix


def test_matrix_getitem():
    mat = Matrix([[1, 2], [3, 4]])
    assert mat[0, 1] == 2, "Element at position (0, 1) should be 2"
    assert mat[1, 0] == 3, "Element at position (1, 0) should be 3"


def test_matrix_repr():
    mat = Matrix([[1, 2], [3, 4]])
    expected_repr = "Matrix([[1, 2], [3, 4]])"
    assert repr(mat) == expected_repr, f"repr should be {expected_repr}"


def test_matrix_str():
    mat = Matrix([[1, 2], [3, 4]])
    expected_str = "[[1 2]\n [3 4]]"
    assert str(mat) == expected_str, f"str should be {expected_str}"


def test_matrix_addition():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    result = matrix1 + matrix2
    expected = Matrix([[6, 8], [10, 12]])
    assert np.array_equal(result, expected), "Matrix addition is incorrect"


def test_addition_with_zero_matrix():
    matrix1 = Matrix([[1, 2], [3, 4]])
    zero_matrix = Matrix([[0, 0], [0, 0]])
    result = matrix1 + zero_matrix
    assert np.array_equal(result, matrix1)


def test_matrix_addition_shape_mismatch():
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = Matrix([[5, 6, 7], [8, 9, 10]])
    with pytest.raises(ValueError, match="Matrices must be of the same shape"):
        mat1 + mat2


def test_matrix_multiplication():
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    result = matrix1 @ matrix2
    expected = Matrix([[19, 22], [43, 50]])
    assert np.array_equal(result, expected), "Matrix multiplication is incorrect"


def test_identity_multiplication():
    matrix1 = Matrix([[1, 2], [3, 4]])
    identity = Matrix([[1, 0], [0, 1]])
    result = matrix1 @ identity
    assert np.array_equal(
        result, matrix1
    ), "Matrix multiplication with an identity matrix is incorrect"


def test_matrix_multiplication_shape_mismatch():
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = Matrix([[5, 6, 7]])
    with pytest.raises(
        ValueError, match="Matrix shapes are not compatible for multiplication"
    ):
        mat1 @ mat2


def test_matrix_transpose():
    matrix1 = Matrix([[1, 2], [3, 4]])
    result = matrix1.T()
    expected = Matrix([[1, 3], [2, 4]])
    assert np.array_equal(result, expected), "Matrix transposition is incorrect"
