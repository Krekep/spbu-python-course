import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "project"))

import math
from vector import Scalar, Lenth, Angle


def test_scalar():
    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    expected = 1 * 4 + 2 * 5 + 3 * 6  # 32
    assert Scalar(v1, v2) == expected

    v3 = [0, 0, 0]
    v4 = [1, 2, 3]
    assert Scalar(v3, v4) == 0

    v5 = [-1, 2, -3]
    v6 = [4, -5, 6]
    expected = (-1) * 4 + 2 * (-5) + (-3) * 6
    assert Scalar(v5, v6) == expected


def test_lenth():
    v1 = [3, 4]
    expected = 5.0
    assert Lenth(v1) == expected

    v2 = [1, 0, 0]
    assert Lenth(v2) == 1.0

    v3 = [5]
    assert Lenth(v3) == 5.0

    v4 = [0, 0, 0, 0]
    assert Lenth(v4) == 0.0


def test_angle():
    v1 = [1, 0]
    v2 = [0, 1]
    expected = math.pi / 2
    assert abs(Angle(v1, v2) - expected) < 0.0001

    v3 = [1, 2]
    v4 = [2, 4]
    assert Angle(v3, v4) == 0.0

    v5 = [1, 0]
    v6 = [-1, 0]
    expected = math.pi
    assert abs(Angle(v5, v6) - expected) < 0.0001
