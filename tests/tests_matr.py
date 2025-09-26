import numpy as np
import random
from matrics import sum_matr, tra_matr, pro_matr


def test_sum():
    n = random.randint(1, 40)
    m = random.randint(1, 40)
    matr1 = np.random.randint(100, size=(n, m))
    matr2 = np.random.randint(100, size=(n, m))
    assert np.array_equal(np.array(sum_matr(matr1, matr2)), matr1 + matr2)


def test_pro():
    n = random.randint(1, 40)
    m = random.randint(1, 40)
    matr1 = np.random.randint(100, size=(n, m))
    matr2 = np.random.randint(100, size=(m, n))
    assert np.allclose(np.array(pro_matr(matr1, matr2)), np.dot(matr1, matr2))


def test_tra():
    n = random.randint(1, 40)
    m = random.randint(1, 40)
    matr1 = np.random.randint(100, size=(n, m))
    assert np.array_equal(np.array(tra_matr(matr1)), np.transpose(matr1))
