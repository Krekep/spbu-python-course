import math
from typing import List


def scalar_product(v1: List[float], v2: List[float]) -> float:
    if len(v1) != len(v2):
        raise ValueError("Векторы должны быть одинаковой длины.")
    if not v1 or not v2:
        raise ValueError("Векторы не могут быть пустыми.")
    if not all(isinstance(x, (int, float)) for x in v1):
        raise TypeError("Все элементы вектора v1 должны быть числами.")
    if not all(isinstance(x, (int, float)) for x in v2):
        raise TypeError("Все элементы вектора v2 должны быть числами.")

    return sum(x * y for x, y in zip(v1, v2))


def vector_length(v: List[float]) -> float:
    if not v:
        raise ValueError("Вектор не должен быть пустым.")
    if not all(isinstance(x, (int, float)) for x in v):
        raise TypeError("Все элементы вектора должны быть числами.")

    return math.sqrt(sum(x**2 for x in v))


def angle_between_vectors(v1: List[float], v2: List[float]) -> float:
    prod = scalar_product(v1, v2)
    len_v1 = vector_length(v1)
    len_v2 = vector_length(v2)
    if len_v1 == 0 or len_v2 == 0:
        raise ValueError("Длина вектора не может быть нулевой.")
    return math.acos(prod / (len_v1 * len_v2))
