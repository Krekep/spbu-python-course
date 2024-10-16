from typing import List


def add(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Add two matrices.

    Parameters:
    ----------
    A : List[List[float]]
        The first matrix.
    B : List[List[float]]
        The second matrix.

    Returns:
    -------
    List[List[float]]
        The resulting matrix after addition.

    Raises:
    ------
    ValueError
        If the matrices have different dimensions.
    """

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("!Matrices have different dimensions!")

    res = [[0.0] * len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            res[i][j] = A[i][j] + B[i][j]
    return res


def mul(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiply two matrices.

    Parameters:
    ----------
    A : List[List[float]]
        The first matrix.
    B : List[List[float]]
        The second matrix.

    Returns:
    -------
    List[List[float]]
        The resulting matrix after multiplication.

    Raises:
    ------
    ValueError
        If the number of columns in the first matrix does not match the number of rows in the second matrix.
    """

    if len(A[0]) != len(B):
        raise ValueError("!Matrices cannot be multiplied!")

    res = [[0.0] * len(B[0]) for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]

    return res


def transpose(A: List[List[float]]) -> List[List[float]]:
    """
    Transpose a matrix.

    Parameters:
    ----------
    A : List[List[float]]
        The matrix to be transposed.

    Returns:
    -------
    List[List[float]]
        The transposed matrix.
    """

    res = [[0.0] * len(A) for i in range(len(A[0]))]

    for i in range(len(A[0])):
        for j in range(len(A)):
            res[i][j] = A[j][i]

    return res
