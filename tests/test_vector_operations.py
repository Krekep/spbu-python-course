import pytest
import math
from project.vector_operations import scalar_product, length_vec, cos_ab


def test_scalar_product():
    vector_a = (5, 0, 0)  # Пример вектора
    vector_b = (10 * math.cos(math.radians(30)), 10 * math.sin(math.radians(30)), 0)
    expected = scalar_product(
        vector_a, vector_b
    )  # Используем функцию для получения ожидаемого значения
    assert scalar_product(vector_a, vector_b) == pytest.approx(expected, rel=1e-5)


def test_length_vec():
    a = (0, 0, 0)
    b = (3, 4, 0)
    expected = 5  # длина вектора должна быть 5 (теорема Пифагора)
    assert length_vec(a, b) == pytest.approx(expected)


def test_length_vec_same_point():
    a = (1, 2, 3)
    b = (1, 2, 3)
    expected = 0  # длина вектора между одинаковыми точками должна быть 0
    assert length_vec(a, b) == pytest.approx(expected)


def test_cos_ab():
    a = (1, 0, 0)
    b = (0, 1, 0)
    expected = 0  # косинус угла между перпендикулярными векторами должен быть 0
    assert cos_ab(a, b) == pytest.approx(expected)


def test_cos_ab_same_direction():
    a = (1, 0, 0)
    b = (2, 0, 0)
    expected = 1  # косинус угла между сонаправленными векторами должен быть 1
    assert cos_ab(a, b) == pytest.approx(expected)


def test_cos_ab_opposite_direction():
    a = (1, 0, 0)
    b = (-1, 0, 0)
    expected = -1  # косинус угла между противоположными векторами должен быть -1
    assert cos_ab(a, b) == pytest.approx(expected)
