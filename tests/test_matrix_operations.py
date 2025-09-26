"""
Test module for matrix operations.
Contains unit tests for matrix functions: addition, multiplication, transposition.
"""

import sys
import os

# Add project directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "project"))

from matrics import sum_matr, pro_matr, tra_matr


def test_sum_matr():
    """
    Test matrix addition with various cases.

    Test cases:
    - Basic 2x2 matrices
    - 1x1 matrices
    - Matrices with negative numbers
    """
    # Test basic 2x2 matrices
    a = [[1.0, 2.0], [3.0, 4.0]]
    b = [[5.0, 6.0], [7.0, 8.0]]
    expected = [[6.0, 8.0], [10.0, 12.0]]
    assert sum_matr(a, b) == expected

    # Test 1x1 matrices
    c = [[5.0]]
    d = [[3.0]]
    assert sum_matr(c, d) == [[8.0]]

    # Test matrices with negative numbers
    e = [[-1.0, 2.0], [3.0, -4.0]]
    f = [[5.0, -6.0], [-7.0, 8.0]]
    expected = [[4.0, -4.0], [-4.0, 4.0]]
    assert sum_matr(e, f) == expected


def test_pro_matr():
    """
    Test matrix multiplication with various cases.

    Test cases:
    - Square matrices multiplication
    - Rectangular matrices multiplication
    - Incompatible matrices (should return None)
    """
    # Test square matrices multiplication
    a = [[1.0, 2.0], [3.0, 4.0]]
    b = [[2.0, 0.0], [1.0, 3.0]]
    expected = [[4.0, 6.0], [10.0, 12.0]]
    assert pro_matr(a, b) == expected

    # Test rectangular matrices multiplication
    c = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    d = [[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]]
    expected = [[58.0, 64.0], [139.0, 154.0]]
    assert pro_matr(c, d) == expected

    # Test incompatible matrices
    e = [[1.0, 2.0]]  # 1x2
    f = [[1.0], [2.0], [3.0]]  # 3x1
    assert pro_matr(e, f) is None


def test_tra_matr():
    """
    Test matrix transposition with various cases.

    Test cases:
    - Rectangular matrix transposition
    - Row vector transposition
    - Square matrix transposition
    - Column vector transposition
    """
    # Test rectangular matrix transposition
    a = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    expected = [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]
    assert tra_matr(a) == expected

    # Test row vector transposition
    b = [[1.0, 2.0, 3.0]]
    expected = [[1.0], [2.0], [3.0]]
    assert tra_matr(b) == expected

    # Test square matrix transposition
    c = [[1.0, 2.0], [3.0, 4.0]]
    expected = [[1.0, 3.0], [2.0, 4.0]]
    assert tra_matr(c) == expected

    # Test column vector transposition
    d = [[1.0], [2.0], [3.0]]
    expected = [[1.0, 2.0, 3.0]]
    assert tra_matr(d) == expected
