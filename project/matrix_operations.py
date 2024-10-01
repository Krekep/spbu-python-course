from typing import List, Optional


def get_row_matrix(matrix: Optional[List[List[int]]]) -> int:
    """Возвращает количество строк в матрице."""
    if matrix is None or not matrix:
        raise ValueError("Матрица пуста или None")
    return len(matrix)


def get_cols_matrix(matrix: Optional[List[List[int]]]) -> int:
    """Возвращает количество столбцов в матрице."""
    if matrix is None or not matrix:
        raise ValueError("Матрица пуста или None")
    rows = get_row_matrix(matrix)
    return len(matrix[0]) if rows > 0 else 0


def sum_matrix(
    a: Optional[List[List[int]]], b: Optional[List[List[int]]]
) -> List[List[int]]:
    """Сложение двух матриц."""
    if a is None or b is None:
        raise ValueError("Одна из матриц пуста или None")

    row_a = get_row_matrix(a)
    cols_a = get_cols_matrix(a)

    row_b = get_row_matrix(b)
    cols_b = get_cols_matrix(b)

    if row_a != row_b or cols_a != cols_b:
        raise ValueError("Размеры матриц не совпадают")

    result = [[a[i][j] + b[i][j] for j in range(cols_a)] for i in range(row_a)]
    return result


def product_matrix(
    a: Optional[List[List[int]]], b: Optional[List[List[int]]]
) -> List[List[int]]:
    """Умножение двух матриц."""
    if a is None or b is None:
        raise ValueError("Одна из матриц пуста или None")

    row_a = get_row_matrix(a)
    cols_a = get_cols_matrix(a)

    row_b = get_row_matrix(b)
    cols_b = get_cols_matrix(b)

    if cols_a != row_b:
        raise ValueError(
            "Число столбцов первой матрицы должно быть равно числу строк второй матрицы"
        )

    result = [[0 for _ in range(cols_b)] for _ in range(row_a)]

    for i in range(row_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result


def transponir_matrix(matrix: Optional[List[List[int]]]) -> List[List[int]]:
    """Транспонирование матрицы."""
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return (
            []
        )  # Возвращаем пустую матрицу, если входная матрица пуста или пустой список

    rows = len(matrix)  # Количество строк
    cols = len(matrix[0])  # Количество столбцов

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result
