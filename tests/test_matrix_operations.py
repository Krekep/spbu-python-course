import pytest
from project.matrix_operations import (
    get_row_matrix,
    get_cols_matrix,
    sum_matrix,
    product_matrix,
    transponir_matrix,
)


def test_get_row_matrix():
    """
    Tests the function get_row_matrix to ensure it returns the correct number of rows.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test will pass if the number of rows returned by get_row_matrix is correct.
    """
    matrix = [[1, 2, 3], [4, 5, 6]]
    assert get_row_matrix(matrix) == 2  # Number of rows


def test_get_cols_matrix():
    """
    Tests the function get_cols_matrix to ensure it returns the correct number of columns.
    
    Parameters
    ----------
    None

    Returns
    -------
    None
        The test will pass if the number of columns returned by get_cols_matrix is correct.
    """
    matrix = [[1, 2, 3], [4, 5, 6]]
    assert get_cols_matrix(matrix) == 3  # Number of columns


def test_sum_matrix():
    """
    Tests the sum_matrix function to ensure correct matrix addition.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test will pass if the sum of two matrices is correctly computed.
    """
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert sum_matrix(a, b) == expected


def test_sum_matrix_invalid_size():
    """
    Tests sum_matrix for invalid sizes.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test will pass if a ValueError is raised when the matrix sizes do not match.
    """
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10]]
    with pytest.raises(ValueError, match="Matrix sizes do not match"):
        sum_matrix(a, b)


def test_sum_matrix_empty_matrix():
    """
    Tests sum_matrix with an empty matrix.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test will pass if a ValueError is raised for an empty matrix.
    """
    a = []
    b = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Matrix is empty or None"):
        sum_matrix(a, b)


def test_product_matrix():
    """
    Tests the product_matrix function for matrix multiplication.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test will pass if the product of two matrices is correctly computed.
    """
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    expected = [[19, 22], [43, 50]]
    assert product_matrix(a, b) == expected


def test_product_matrix_invalid_size():
    """
    Tests product_matrix for invalid matrix dimensions.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test will pass if a ValueError is raised when matrix dimensions are invalid for multiplication.
    """
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[7, 8], [9, 10]]
    with pytest.raises(
        ValueError,
        match="The number of columns in the first matrix must equal the number of rows in the second matrix",
    ):
        product_matrix(a, b)


def test_product_matrix_empty_matrix():
    """
    Tests product_matrix with an empty matrix.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test will pass if a ValueError is raised for an empty matrix.
    """
    a = []
    b = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Matrix is empty or None"):
        product_matrix(a, b)


def test_transponir_matrix():
    """
    Tests the transponir_matrix function for matrix transposition.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test will pass if the matrix is correctly transposed.
    """
    matrix = [[1, 2], [3, 4], [5, 6]]
    expected = [[1, 3, 5], [2, 4, 6]]
    assert transponir_matrix(matrix) == expected


def test_transponir_matrix_empty_matrix():
    """
    Tests transponir_matrix with an empty matrix.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test will pass if the transposition of an empty matrix returns an empty matrix.
    """
    matrix = []
    expected = []
    assert transponir_matrix(matrix) == expected  # Transposing an empty matrix
