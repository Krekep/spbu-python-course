import math
from typing import List


def vector_length(vec: List[float]) -> float:
    """Calculate the length (magnitude) of a vector.

    Args:
        vec (list of float): A list of numerical values representing the vector.

    Returns:
        float: The Euclidean length of the vector.
    """
    return sum(x**2 for x in vec) ** 0.5


def scalar_product(vec1: List[float], vec2: List[float]) -> float:
    """Calculate the scalar (dot) product of two vectors.

    Args:
        vec1 (list of float): First vector.
        vec2 (list of float): Second vector.

    Raises:
        ValueError: If the vectors have different lengths.

    Returns:
        float: The scalar product of vec1 and vec2.
    """
    if len(vec1) != len(vec2):
        raise ValueError("Vectors of different lengths")

    return sum(x * y for x, y in zip(vec1, vec2))


def angle_vectors(vec1: List[float], vec2: List[float]) -> float:
    """Calculate the angle in radians between two vectors.

    Args:
        vec1 (list of float): First vector.
        vec2 (list of float): Second vector.

    Raises:
        ValueError: If either vector has zero length.

    Returns:
        float: The angle between vec1 and vec2 in radians.
    """
    dot = scalar_product(vec1, vec2)
    length_vec1 = vector_length(vec1)
    length_vec2 = vector_length(vec2)

    if length_vec1 == 0 or length_vec2 == 0:
        raise ValueError("The length of the vectors cannot be zero")

    cos_angle = dot / (length_vec1 * length_vec2)
    cos_angle = max(-1.0, min(1.0, cos_angle))

    return math.acos(cos_angle)
