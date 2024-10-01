from typing import List, Optional


def get_row_matrix(matrix: Optional[List[List[int]]]) -> int:
    """
    Returns the number of rows in the matrix.

    Parameters
    ----------
    matrix : Optional[List[List[int]]]
        A matrix represented as a list of lists of integers. It can be None or an empty list.

    Returns
    -------
    int
        The number of rows in the matrix.

    Raises
    ------
    ValueError
        If the matrix is None or empty.
    """
    if matrix is None or not matrix:
        raise ValueError("Matrix is empty or None")
    return len(matrix)


def get_cols_matrix(matrix: Optional[List[List[int]]]) -> int:
    """
    Returns the number of columns in the matrix.

    Parameters
    ----------
    matrix : Optional[List[List[int]]]
        A matrix represented as a list of lists of integers. It can be None or an empty list.

    Returns
    -------
    int
        The number of columns in the matrix.

    Raises
    ------
    ValueError
        If the matrix is None or empty.
    """
    if matrix is None or not matrix:
        raise ValueError("Matrix is empty or None")
    rows = get_row_matrix(matrix)
    return len(matrix[0]) if rows > 0 else 0


def sum_matrix(
    a: Optional[List[List[int]]], b: Optional[List[List[int]]]
) -> List[List[int]]:
    """
    Adds two matrices.

    Parameters
    ----------
    a : Optional[List[List[int]]]
        The first matrix represented as a list of lists of integers.
    b : Optional[List[List[int]]]
        The second matrix represented as a list of lists of integers.

    Returns
    -------
    List[List[int]]
        The resulting matrix from the addition of matrices `a` and `b`.

    Raises
    ------
    ValueError
        If either matrix is None, or if the dimensions of the two matrices do not match.
    """
    if a is None or b is None:
        raise ValueError("One of the matrices is None or empty")

    row_a = get_row_matrix(a)
    cols_a = get_cols_matrix(a)

    row_b = get_row_matrix(b)
    cols_b = get_cols_matrix(b)

    if row_a != row_b or cols_a != cols_b:
        raise ValueError("Matrix sizes do not match")

    result = [[a[i][j] + b[i][j] for j in range(cols_a)] for i in range(row_a)]
    return result


def product_matrix(
    a: Optional[List[List[int]]], b: Optional[List[List[int]]]
) -> List[List[int]]:
    """
    Multiplies two matrices.

    Parameters
    ----------
    a : Optional[List[List[int]]]
        The first matrix represented as a list of lists of integers.
    b : Optional[List[List[int]]]
        The second matrix represented as a list of lists of integers.

    Returns
    -------
    List[List[int]]
        The resulting matrix from the multiplication of matrices `a` and `b`.

    Raises
    ------
    ValueError
        If either matrix is None, or if the number of columns in matrix `a` does not match
        the number of rows in matrix `b`.
    """
    if a is None or b is None:
        raise ValueError("One of the matrices is None or empty")

    row_a = get_row_matrix(a)
    cols_a = get_cols_matrix(a)

    row_b = get_row_matrix(b)
    cols_b = get_cols_matrix(b)

    if cols_a != row_b:
        raise ValueError(
            "The number of columns in the first matrix must equal the number of rows in the second matrix"
        )

    result = [[0 for _ in range(cols_b)] for _ in range(row_a)]

    for i in range(row_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result


def transponir_matrix(matrix: Optional[List[List[int]]]) -> List[List[int]]:
    """
    Transposes a matrix (switches rows and columns).

    Parameters
    ----------
    matrix : Optional[List[List[int]]]
        A matrix represented as a list of lists of integers. It can be None or an empty list.

    Returns
    -------
    List[List[int]]
        The transposed matrix.

    Raises
    ------
    ValueError
        If the matrix is None or empty.
    """
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        return []  # Returns an empty matrix if the input is None or empty

    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result
