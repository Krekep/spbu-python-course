import math
from typing import List, Optional


def scalar_product(a: Optional[List[float]], b: Optional[List[float]]) -> float:
    """Вычисляет скалярное произведение двух векторов произвольной размерности."""
    if a is None or b is None:
        raise ValueError("Один из векторов пуст или None")
    if len(a) != len(b):
        raise ValueError("Векторы должны быть одной размерности")

    # Скалярное произведение двух векторов
    return sum(a[i] * b[i] for i in range(len(a)))


def length_vec(a: Optional[List[float]], b: Optional[List[float]]) -> float:
    """Вычисляет длину вектора между двумя точками a и b произвольной размерности."""
    if a is None or b is None:
        raise ValueError("Одна из точек пуста или None")
    if len(a) != len(b):
        raise ValueError("Точки должны быть одной размерности")

    return math.sqrt(sum((b[i] - a[i]) ** 2 for i in range(len(a))))


def cos_ab(a: Optional[List[float]], b: Optional[List[float]]) -> float:
    """Вычисляет косинус угла между векторами a и b произвольной размерности."""
    if a is None or b is None:
        raise ValueError("Один из векторов пуст или None")
    if len(a) != len(b):
        raise ValueError("Векторы должны быть одной размерности")

    dot_product = scalar_product(a, b)
    magnitude_a = math.sqrt(sum(coord**2 for coord in a))
    magnitude_b = math.sqrt(sum(coord**2 for coord in b))

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError(
            "Длина одного из векторов равна нулю, невозможно вычислить косинус угла"
        )

    return dot_product / (magnitude_a * magnitude_b)
