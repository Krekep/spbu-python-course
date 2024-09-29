import pytest
from project.matrix_operations import (
    get_row_matrix,
    get_cols_matrix,
    sum_matrix,
    product_matrix,
    transponir_matrix,
)

def test_get_row_matrix():
    matrix = [[1, 2, 3], [4, 5, 6]]
    assert get_row_matrix(matrix) == 2  # Количество строк

def test_get_cols_matrix():
    matrix = [[1, 2, 3], [4, 5, 6]]
    assert get_cols_matrix(matrix) == 3  # Количество столбцов

def test_sum_matrix():
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert sum_matrix(m1, m2) == expected

def test_sum_matrix_invalid_size():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[7, 8], [9, 10]]
    assert sum_matrix(m1, m2) == -1  # Несовместимые размеры матриц

def test_sum_matrix_empty_matrix():
    m1 = []
    m2 = [[1, 2], [3, 4]]
    assert sum_matrix(m1, m2) == -1  # Пустая матрица

def test_product_matrix():
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert product_matrix(m1, m2) == expected

def test_product_matrix_invalid_size():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[7, 8], [9, 10]]
    assert product_matrix(m1, m2) == -1  # Несовместимые размеры для умножения

def test_product_matrix_empty_matrix():
    m1 = []
    m2 = [[1, 2], [3, 4]]
    assert product_matrix(m1, m2) == -1  # Пустая матрица

def test_transponir_matrix():
    matrix = [[1, 2], [3, 4], [5, 6]]
    expected = [[1, 3, 5], [2, 4, 6]]
    assert transponir_matrix(matrix) == expected

def test_transponir_matrix_empty_matrix():
    matrix = []
    expected = []
    assert transponir_matrix(matrix) == expected  # Транспонирование пустой матрицы
