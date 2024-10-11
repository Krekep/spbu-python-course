import pytest
from project.matrix_operations import (
    matrix_addition,
    matrix_multiplication,
    transpose_matrix,
)


def test_matrix_addition():
    m1 = [[5, 8], [12, 7]]
    m2 = [[3, 4], [6, 9]]
    expected = [[8, 12], [18, 16]]
    assert matrix_addition(m1, m2) == expected


def test_matrix_addition_invalid_sizes():
    m1 = [[5, 8, 2], [7, 6, 1]]
    m2 = [[3, 4], [6, 9]]
    with pytest.raises(ValueError):
        matrix_addition(m1, m2)


def test_matrix_addition_empty_matrix():
    m1 = []
    m2 = [[1, 2], [3, 4]]
    with pytest.raises(ValueError):
        matrix_addition(m1, m2)


def test_matrix_multiplication():
    m1 = [[2, 5], [7, 4]]
    m2 = [[6, 1], [9, 3]]
    expected = [[57, 17], [78, 19]]
    assert matrix_multiplication(m1, m2) == expected


def test_matrix_multiplication_invalid_sizes():
    m1 = [[5, 8, 2], [7, 6, 1]]
    m2 = [[3, 4], [6, 9]]
    with pytest.raises(ValueError):
        matrix_multiplication(m1, m2)


def test_matrix_multiplication_empty_matrix():
    m1 = []
    m2 = [[1, 2], [3, 4]]
    with pytest.raises(ValueError):
        matrix_multiplication(m1, m2)


def test_transpose_matrix():
    m = [[8, 4, 3], [5, 7, 9]]
    expected = [[8, 5], [4, 7], [3, 9]]
    assert transpose_matrix(m) == expected


def test_transpose_matrix_invalid():
    m = []
    with pytest.raises(ValueError):
        transpose_matrix(m)
