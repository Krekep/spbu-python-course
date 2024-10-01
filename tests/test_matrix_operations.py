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
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert sum_matrix(a, b) == expected


def test_sum_matrix_invalid_size():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10]]
    with pytest.raises(ValueError, match="Размеры матриц не совпадают"):
        sum_matrix(a, b)


def test_sum_matrix_empty_matrix():
    a = []
    b = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Матрица пуста или None"):
        sum_matrix(a, b)


def test_product_matrix():
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert product_matrix(a, b) == expected


def test_product_matrix_invalid_size():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10]]
    with pytest.raises(
        ValueError,
        match="Число столбцов первой матрицы должно быть равно числу строк второй матрицы",
    ):
        product_matrix(a, b)


def test_product_matrix_empty_matrix():
    a = []
    b = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Матрица пуста или None"):
        product_matrix(a, b)


def test_transponir_matrix():
    matrix = [[1, 2], [3, 4], [5, 6]]
    expected = [[1, 3, 5], [2, 4, 6]]
    assert transponir_matrix(matrix) == expected


def test_transponir_matrix_empty_matrix():
    matrix = []
    expected = []
    assert transponir_matrix(matrix) == expected  # Транспонирование пустой матрицы
