import pytest
import math
from project.vector_operations import scalar_product, length_vec, cos_AB

def test_scalar_product():
    len_a = 5
    len_b = 10
    angle = math.cos(math.radians(30))  # угол 30 градусов
    expected = abs(len_a) * abs(len_b) * angle
    assert scalar_product(len_a, len_b, angle) == pytest.approx(expected)

def test_length_vec():
    A = (0, 0, 0)
    B = (3, 4, 0)
    expected = 5  # длина вектора должна быть 5 (теорема Пифагора)
    assert length_vec(A, B) == pytest.approx(expected)

def test_length_vec_same_point():
    A = (1, 2, 3)
    B = (1, 2, 3)
    expected = 0  # длина вектора между одинаковыми точками должна быть 0
    assert length_vec(A, B) == pytest.approx(expected)

def test_cos_AB():
    A = (1, 0, 0)
    B = (0, 1, 0)
    expected = 0  # косинус угла между перпендикулярными векторами должен быть 0
    assert cos_AB(A, B) == pytest.approx(expected)

def test_cos_AB_same_direction():
    A = (1, 0, 0)
    B = (2, 0, 0)
    expected = 1  # косинус угла между сонаправленными векторами должен быть 1
    assert cos_AB(A, B) == pytest.approx(expected)

def test_cos_AB_opposite_direction():
    A = (1, 0, 0)
    B = (-1, 0, 0)
    expected = -1  # косинус угла между противоположными векторами должен быть -1
    assert cos_AB(A, B) == pytest.approx(expected)
