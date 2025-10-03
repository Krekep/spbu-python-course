from typing import List

"""
List of modules:
 * Sum of the matrices
 * Matrix multiplication
 * Matrix transposition
"""


def matrix_sum(m1: List[List[float]], m2: List[List[float]]) -> List[List[float]]:
    """
    Calculating the sum of the matrices

    Parameters:
        m1: (List[List[float]]): First matrix
        m2: (List[List[float]]): Second matrix

    Returns:
        List[List[float]]: Sum of the matrices

    Raises:
        ValueError: If the matrices have different lengths
    """
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("The matrices must be of the same length!")
    else:
        return [
            [m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))
        ]


def matrix_mult(m1: List[List[float]], m2: List[List[float]]) -> List[List[float]]:
    """
    Calculating the matrix multiplication

    Parameters:
        m1: (List[List[float]]): First matrix
        m2: (List[List[float]]): Second matrix

    Returns:
        List[List[float]]: Matrix multiplication

    Raises:
        ValueError: If the number of columns in the first matrix must match the number of rows in the second matrix
    """
    if len(m1[0]) != len(m2):
        raise ValueError(
            "The number of columns in the first matrix must match the number of rows in the second matrix!"
        )
    else:
        return [
            [
                sum(m1[i][j] * m2[j][k] for j in range(len(m1[0])))
                for k in range(len(m2[0]))
            ]
            for i in range(len(m1))
        ]


def matrix_transpose(matrix: List[List[float]]) -> List[List[float]]:
    """
    Calculating the matrix transposition

    Parameters:
        matrix: (List[List[float]]): Matrix

    Returns:
        List[List[float]]: Matrix transposition
    """
    return [
        [float(matrix[i][j]) for i in range(len(matrix))] for j in range(len(matrix[0]))
    ]
