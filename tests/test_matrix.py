import pytest
from project.matrix import (
    matrix_addition,
    matrix_multiplication,
    matrix_transpose,
)


def test_matrix_addition():
    A = [[2, 3], [5, 7]]
    B = [[4, 1], [2, 3]]
    assert matrix_addition(A, B) == [[6, 4], [7, 10]]

    # Test case with matrices of different sizes
    with pytest.raises(ValueError):
        matrix_addition([[2]], [[2, 3]])

    # Test case with one zero matrix
    A = [[0, 0], [0, 0]]
    B = [[6, 5], [4, 3]]
    assert matrix_addition(A, B) == [[6, 5], [4, 3]]


def test_matrix_multiplication():
    A = [[2, 3], [5, 7]]
    B = [[1, 4], [2, 6]]
    assert matrix_multiplication(A, B) == [[8, 26], [19, 62]]

    # Test case for incompatible matrix sizes
    with pytest.raises(ValueError):
        matrix_multiplication([[2, 3]], [[1], [2], [3]])

    # Identity matrix multiplication
    A = [[3, 4], [6, 8]]
    E = [[1, 0], [0, 1]]
    assert matrix_multiplication(A, E) == A

    # Test case with zero matrix
    A = [[0, 0], [0, 0]]
    B = [[5, 2], [1, 3]]
    assert matrix_multiplication(A, B) == [[0, 0], [0, 0]]

    # Multiplication of 3x2 and 2x3 matrices
    A = [[1, 2], [3, 1], [4, 5]]
    B = [[2, 3, 4], [1, 0, 2]]
    assert matrix_multiplication(A, B) == [[4, 3, 8], [7, 9, 14], [13, 12, 26]]

    # Test case for multiplying a 1x2 matrix by a 2x1 matrix
    A = [[1, 3]]
    B = [[4], [5]]
    assert matrix_multiplication(A, B) == [[19]]


def test_matrix_transpose():
    A = [[3, 5, 7], [8, 10, 12]]
    assert matrix_transpose(A) == [[3, 8], [5, 10], [7, 12]]

    # Test case for a square matrix
    B = [[2, 4], [6, 8]]
    assert matrix_transpose(B) == [[2, 6], [4, 8]]
