from typing import List


def matrix_addition(m1: List[List[float]], m2: List[List[float]]) -> List[List[float]]:
    if not m1 or not m2:
        raise ValueError("Матрицы не должны быть пустыми.")
    if len(m1) != len(m2) or any(len(row1) != len(row2) for row1, row2 in zip(m1, m2)):
        raise ValueError("Матрицы должны иметь одинаковые размеры для сложения.")
    if any(len(row) != len(m1[0]) for row in m1) or any(
        len(row) != len(m2[0]) for row in m2
    ):
        raise ValueError("Все строки матрицы должны иметь одинаковую длину.")
    return [[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(m1, m2)]


def matrix_multiplication(
    m1: List[List[float]], m2: List[List[float]]
) -> List[List[float]]:
    if any(len(row) != len(m1[0]) for row in m1) or any(
        len(row) != len(m2[0]) for row in m2
    ):
        raise ValueError("Все строки матрицы должны иметь одинаковую длину.")
    if not m1 or not m2 or len(m1[0]) != len(m2):
        raise ValueError(
            "Невозможно выполнить умножение матриц: несоответствие размеров."
        )
    result = []
    for row in m1:
        new_row = []
        for col in zip(*m2):
            new_row.append(sum(x * y for x, y in zip(row, col)))
        result.append(new_row)
    return result


def transpose_matrix(m: List[List[float]]) -> List[List[float]]:
    if not m:
        raise ValueError("Матрица не должна быть пустой.")
    if any(len(row) != len(m[0]) for row in m):
        raise ValueError("Все строки матрицы должны иметь одинаковую длину.")
    return [list(col) for col in zip(*m)]
