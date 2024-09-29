Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from typing import List, Optional
... 
... 
... def get_row_matrix(matrix: Optional[List[List[int]]]) -> int:
...     """Возвращает количество строк в матрице."""
...     if matrix is None or not matrix:
...         raise ValueError("Матрица пуста или None")
...     return len(matrix)
... 
... 
... def get_cols_matrix(matrix: Optional[List[List[int]]]) -> int:
...     """Возвращает количество столбцов в матрице."""
...     rows = get_row_matrix(matrix)
...     return len(matrix[0]) if rows > 0 else 0
... 
... 
... def sum_matrix(A: Optional[List[List[int]]], B: Optional[List[List[int]]]) -> List[List[int]]:
...     """Сложение двух матриц."""
...     row_a = get_row_matrix(A)
...     cols_a = get_cols_matrix(A)
... 
...     row_b = get_row_matrix(B)
...     cols_b = get_cols_matrix(B)
... 
...     if row_a != row_b or cols_a != cols_b:
...         raise ValueError("Размеры матриц не совпадают")
... 
...     result = [[A[i][j] + B[i][j] for j in range(cols_a)] for i in range(row_a)]
...     return result
... 
... 
... def product_matrix(A: Optional[List[List[int]]], B: Optional[List[List[int]]]) -> List[List[int]]:
...     """Умножение двух матриц."""
...     row_a = get_row_matrix(A)
...     cols_a = get_cols_matrix(A)

    row_b = get_row_matrix(B)
    cols_b = get_cols_matrix(B)

    if cols_a != row_b:
        raise ValueError("Количество столбцов первой матрицы должно равняться количеству строк второй")

    result = [[sum(A[i][k] * B[k][j] for k in range(cols_a)) for j in range(cols_b)] for i in range(row_a)]
    return result


def transpose_matrix(matrix: Optional[List[List[int]]]) -> List[List[int]]:
    """Транспонирование матрицы."""
    row = get_row_matrix(matrix)
    cols = get_cols_matrix(matrix)

    result = [[matrix[j][i] for j in range(row)] for i in range(cols)]
