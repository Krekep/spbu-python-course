import pytest

from project.task1.matrices import matrix_sum, matrix_mult, matrix_transpose


def matrix_sum_test():
    """Test of calculating the sum of the matrices"""
    assert matrix_sum([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[6, 8], [10, 12]]


def matrix_sum_error():
    """Test of calculating the sum of the matrices with different lengths"""
    with pytest.raises(ValueError):
        matrix_sum([[1, 2]], [[1, 2, 3]])


def matrix_mult_test():
    """Test of calculating the matrix multiplication"""
    assert matrix_mult([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]


def matrix_mult_test_error():
    """Test of calculating the matrix multiplication if the number of columns in the first matrix must match the number of rows in the second matrix"""
    with pytest.raises(ValueError):
        matrix_mult([[1, 2]], [[3]])


def matrix_transpose_test():
    """Test of calculating the matrix transposition"""
    assert matrix_transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
