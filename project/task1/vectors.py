import math
from typing import List

"""
List of modules:
 * scalar product
 * vector length
 * angle between vectors
"""


def scalar_mult(v1: List[float], v2: List[float]) -> float:
    """
    Calculating the scalar product

    Parameters:
        v1 (List[float]): First vector
        v2 (List[float]): Second vector

    Returns:
        float: Scalar product

    Raises:
        ValueError: If the vectors have different lengths
    """
    if len(v1) != len(v2):
        raise ValueError("The vectors must be of the same length!")
    else:
        return sum(v1[x] * v2[x] for x in range(len(v1)))


def vector_length(vector: List[float]) -> float:
    """
    Calculating the length of a vector

    Parameters:
        vector (List[float]): Vector

    Returns:
        float: Length of a vector
    """
    return (sum((vector[x]) ** 2 for x in range(len(vector)))) ** 0.5


def angle_vectors(v1: List[float], v2: List[float]) -> float:
    """
    Calculating the angle between vectors

    Parameters:
        v1 (List[float]): First vector
        v2 (List[float]): Second vector

    Returns:
        float: The angle between two vectors in degrees

    Raises:
        ValueError: If the vector has zero length
    """
    if len(v1) == 0 or len(v2) == 0:
        raise ValueError("Vectors must be non-zero!")
    else:
        return (
            180
            * math.acos(scalar_mult(v1, v2) / (vector_length(v1) * vector_length(v2)))
        ) / math.pi
