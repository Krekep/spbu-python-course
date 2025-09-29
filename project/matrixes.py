from typing import List


def matrix_addition(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """Add two matrices element-wise.

    Args:
        A (list of list of float): First matrix.
        B (list of list of float): Second matrix.

    Raises:
        ValueError: If the matrices have different sizes.

    Returns:
        list of list of float: The resulting matrix after addition.
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("The matrices must be the same size.")
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def matrix_multiplication(
    A: List[List[float]], B: List[List[float]]
) -> List[List[float]]:
    """Multiply two matrices using the standard matrix multiplication.

    Args:
        A (list of list of float): First matrix (m x n).
        B (list of list of float): Second matrix (n x p).

    Raises:
        ValueError: If the number of columns of A does not equal the number of rows of B.

    Returns:
        list of list of float: The resulting matrix (m x p).
    """
    if len(A[0]) != len(B):
        raise ValueError(
            "The number of columns of A should be equal to the number of rows of B"
        )

    result: List[List[float]] = []
    for i in range(len(A)):
        row: List[float] = []
        for j in range(len(B[0])):
            element: float = 0
            for k in range(len(B)):
                element += A[i][k] * B[k][j]
            row.append(element)
        result.append(row)
    return result


def matrix_transpose(A: List[List[float]]) -> List[List[float]]:
    """Transpose a matrix (swap rows and columns).

    Args:
        A (list of list of float): Input matrix (m x n).

    Returns:
        list of list of float: Transposed matrix (n x m).
    """
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
