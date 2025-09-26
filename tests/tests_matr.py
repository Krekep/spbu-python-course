import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "project"))

from matrics import sum_matr, pro_matr, tra_matr


def test_sum_matr():
    a = [[1.0, 2.0], [3.0, 4.0]]
    b = [[5.0, 6.0], [7.0, 8.0]]
    expected = [[6.0, 8.0], [10.0, 12.0]]
    assert sum_matr(a, b) == expected

    c = [[5.0]]
    d = [[3.0]]
    assert sum_matr(c, d) == [[8.0]]

    e = [[-1.0, 2.0], [3.0, -4.0]]
    f = [[5.0, -6.0], [-7.0, 8.0]]
    expected = [[4.0, -4.0], [-4.0, 4.0]]
    assert sum_matr(e, f) == expected


def test_pro_matr():
    a = [[1.0, 2.0], [3.0, 4.0]]
    b = [[2.0, 0.0], [1.0, 3.0]]
    expected = [[4.0, 6.0], [10.0, 12.0]]
    assert pro_matr(a, b) == expected

    c = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    d = [[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]]
    expected = [[58.0, 64.0], [139.0, 154.0]]
    assert pro_matr(c, d) == expected

    e = [[1.0, 2.0]]
    f = [[1.0], [2.0], [3.0]]
    assert pro_matr(e, f) is None


def test_tra_matr():
    a = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
    expected = [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]
    assert tra_matr(a) == expected

    b = [[1.0, 2.0, 3.0]]
    expected = [[1.0], [2.0], [3.0]]
    assert tra_matr(b) == expected

    c = [[1.0, 2.0], [3.0, 4.0]]
    expected = [[1.0, 3.0], [2.0, 4.0]]
    assert tra_matr(c) == expected

    d = [[1.0], [2.0], [3.0]]
    expected = [[1.0, 2.0, 3.0]]
    assert tra_matr(d) == expected
