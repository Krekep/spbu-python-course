import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from project.matrix_operations import (
    matrix_addition,
    matrix_multiplication,
    transpose_matrix,
)


def test_matrix_addition():
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    expected_result = [[6.0, 8.0], [10.0, 12.0]]
    assert matrix_addition(m1, m2) == expected_result


def test_matrix_multiplication():
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    expected_result = [[19.0, 22.0], [43.0, 50.0]]
    assert matrix_multiplication(m1, m2) == expected_result


def test_transpose_matrix():
    m = [[1, 2], [3, 4]]
    expected_result = [[1.0, 3.0], [2.0, 4.0]]
    assert transpose_matrix(m) == expected_result
