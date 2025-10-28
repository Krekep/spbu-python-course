import math
from typing import List, Union


def scalar(a: List[float], b: List[float]) -> float:
    """
    Calculate the scalar product (dot product) of two vectors.

    Args:
        a: First vector (list of numbers)
        b: Second vector (list of numbers)

    Returns:
        Scalar product of the vectors

    Raises:
        ValueError: If vectors have different dimensions
    """
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension")
    result = 0.0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


def normal(a: List[float]) -> float:
    """
    Calculate the length (norm) of a vector.

    Args:
        a: Input vector (list of numbers)

    Returns:
        Length of the vector
    """
    return math.sqrt(sum(x * x for x in a))


def angle(a: List[float], b: List[float]) -> float:
    """
    Calculate the angle between two vectors in degrees.

    Args:
        a: First vector (list of numbers)
        b: Second vector (list of numbers)

    Returns:
        Angle between vectors in degrees

    Raises:
        ValueError: If one of the vectors is zero
    """
    norm_a = normal(a)
    norm_b = normal(b)
    if norm_a == 0 or norm_b == 0:
        raise ValueError("Cannot use zero vector")
    cos_angle = scalar(a, b) / (norm_a * norm_b)
    rad_angle = math.acos(cos_angle)
    angle_deg = math.degrees(rad_angle)
    return angle_deg


def trans(M: List[List[float]]) -> List[List[float]]:
    """
    Transpose a matrix.

    Args:
        M: Input matrix (list of lists of numbers)

    Returns:
        Transposed matrix
    """
    rows = len(M)
    cols = len(M[0])
    transposed_matrix = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(M[j][i])
        transposed_matrix.append(new_row)
    return transposed_matrix


def multiplication(M: List[List[float]], N: List[List[float]]) -> List[List[float]]:
    """
    Multiply two matrices.

    Args:
        M: First matrix (list of lists of numbers)
        N: Second matrix (list of lists of numbers)

    Returns:
        Result of matrix multiplication

    Raises:
        ValueError: If matrices have incompatible dimensions
    """
    if len(M[0]) != len(N):
        raise ValueError("Incompatible matrix dimensions")
    rows_m = len(M)
    cols_m = len(M[0])
    cols_n = len(N[0])
    result = []
    for i in range(rows_m):
        new_row = []
        for j in range(cols_n):
            sum_val = 0.0
            for k in range(cols_m):
                sum_val += M[i][k] * N[k][j]
            new_row.append(sum_val)
        result.append(new_row)
    return result


def summa(M: List[List[float]], N: List[List[float]]) -> List[List[float]]:
    """
    Add two matrices.

    Args:
        M: First matrix (list of lists of numbers)
        N: Second matrix (list of lists of numbers)

    Returns:
        Sum of matrices

    Raises:
        ValueError: If matrices have different dimensions
    """
    if len(M) != len(N) or len(M[0]) != len(N[0]):
        raise ValueError("Matrices must have the same dimensions")
    rows = len(M)
    cols = len(M[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(M[i][j] + N[i][j])
        result.append(new_row)
    return result


ALGEBRA_OPERATIONS: List[str] = [
    "scalar",
    "normal",
    "angle",
    "trans",
    "multiplication",
    "summa",
]
