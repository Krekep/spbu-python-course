import pytest
import math
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from project.vector_operation import dot_product, vector_length, angle_between_vectors


def test_dot_product():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert dot_product([0, 0, 0], [1, 2, 3]) == 0
    assert dot_product([-1, -2], [1, 2]) == -5


def test_vector_length():
    assert vector_length([3, 4]) == 5
    assert vector_length([0, 0]) == 0
    assert vector_length([1, 2, 2]) == 3


def test_angle_between_vectors():
    assert angle_between_vectors([1, 0], [0, 1]) == pytest.approx(
        math.pi / 2
    )  # Прямой угол
    assert angle_between_vectors([1, 0], [1, 0]) == 0  # Нулевой угол
    with pytest.raises(ValueError):
        angle_between_vectors([0, 0], [1, 1])  # Нулевой вектор
