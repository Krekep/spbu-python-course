import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "project"))

from matrics import sum_matr, pro_matr, tra_matr


def test_sum_matr():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert sum_matr(a, b) == expected

    c = [[5]]
    d = [[3]]
    assert sum_matr(c, d) == [[8]]

    e = [[-1, 2], [3, -4]]
    f = [[5, -6], [-7, 8]]
    expected = [[4, -4], [-4, 4]]
    assert sum_matr(e, f) == expected


def test_pro_matr():
    a = [[1, 2], [3, 4]]
    b = [[2, 0], [1, 3]]
    expected = [[4, 6], [10, 12]]
    assert pro_matr(a, b) == expected

    c = [[1, 2, 3], [4, 5, 6]]
    d = [[7, 8], [9, 10], [11, 12]]
    expected = [[58, 64], [139, 154]]
    assert pro_matr(c, d) == expected

    e = [[1, 2]]
    f = [[1], [2], [3]]
    assert pro_matr(e, f) is None


def test_tra_matr():
    a = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert tra_matr(a) == expected

    b = [[1, 2, 3]]
    expected = [[1], [2], [3]]
    assert tra_matr(b) == expected

    c = [[1, 2], [3, 4]]
    expected = [[1, 3], [2, 4]]
    assert tra_matr(c) == expected

    d = [[1], [2], [3]]
    expected = [[1, 2, 3]]
    assert tra_matr(d) == expected
