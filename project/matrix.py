from typing import List

# Matrix operations


def matrix_addition(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Add two matrices.

    Args:
        A (List[List[float]]): The first matrix.
        B (List[List[float]]): The second matrix.

    Returns:
        List[List[float]]: The resulting matrix from the addition.

    Raises:
        ValueError: If the input matrices have different dimensions.
    """
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Error: matrices of different dimensions.")

    result_m = [[0.0] * len(A[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            result_m[i][j] = A[i][j] + B[i][j]

    return result_m


def matrix_multiplication(
    A: List[List[float]], B: List[List[float]]
) -> List[List[float]]:
    """
    Multiply two matrices.

    Args:
        A (List[List[float]]): The first matrix.
        B (List[List[float]]): The second matrix.

    Returns:
        List[List[float]]: The resulting matrix from the multiplication.

    Raises:
        ValueError: If the number of columns in A does not match the number of rows in B.

    Examples:
        >>> matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
    """
    if len(A[0]) != len(B):
        raise ValueError(
            "Error: number of rows of first matrix and number of columns of second matrix are different."
        )

    result_m = [[0.0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result_m[i][j] += A[i][k] * B[k][j]

    return result_m


def matrix_transpose(A: List[List[float]]) -> List[List[float]]:
    """
    Transpose a matrix.

    Args:
        A (List[List[float]]): The matrix to transpose.

    Returns:
        List[List[float]]: The transposed matrix.
    """
    result_m = [[0.0] * len(A) for _ in range(len(A[0]))]

    for i in range(len(A[0])):
        for j in range(len(A)):
            result_m[i][j] = A[j][i]

    return result_m
