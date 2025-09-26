import numpy as np
import random
from vector import Scalar, Lenth, Angle


def test_lenth():
    n = random.randint(1, 10)
    x = np.random.random(n)
    assert np.array_equal(np.array(Lenth(x)), np.linalg.norm(x))


def test_scalar():
    n = random.randint(1, 10)
    x = np.random.random(n)
    y = np.random.random(n)
    assert np.array_equal(np.array(Scalar(x, y)), np.dot(x, y))
