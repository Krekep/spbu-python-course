from typing import List, Optional


def get_row_matrix(matrix: Optional[List[List[int]]]) -> int:
    """Возвращает количество строк в матрице."""
    if matrix is None or not matrix:
        raise ValueError("Матрица пуста или None")
    return len(matrix)


def get_cols_matrix(matrix: Optional[List[List[int]]]) -> int:
    """Возвращает количество столбцов в матрице."""
    rows = get_row_matrix(matrix)
    return len(matrix[0]) if rows > 0 else 0


def sum_matrix(A: Optional[List[List[int]]], B: Optional[List[List[int]]]) -> List[List[int]]:
    """Сложение двух матриц."""
    row_a = get_row_matrix(A)
    cols_a = get_cols_matrix(A)

    row_b = get_row_matrix(B)
    cols_b = get_cols_matrix(B)

    if row_a != row_b or cols_a != cols_b:
        raise ValueError("Размеры матриц не совпадают")

    result = [[A[i][j] + B[i][j] for j in range(cols_a)] for i in range(row_a)]
    return result


def product_matrix(A: Optional[List[List[int]]], B: Optional[List[List[int]]]) -> List[List[int]]:
    """Умножение двух матриц."""
    row_a = get_row_matrix(A)
    cols_a = get_cols_matrix(A)

    row_b = get_row_matrix(B)
    cols_b = get_cols_matrix(B)

    if cols_a != row_b:
        raise ValueError("Число столбцов первой матрицы должно быть равно числу строк второй матрицы")

    result = [[0 for _ in range(cols_b)] for _ in range(row_a)]

    for i in range(row_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += A[i][k] * B[k][j]

    return result


def transpose_matrix(matrix: Optional[List[List[int]]]) -> List[List[int]]:
    """Транспонирование матрицы."""
    rows = get_row_matrix(matrix)
    cols = get_cols_matrix(matrix)

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result
