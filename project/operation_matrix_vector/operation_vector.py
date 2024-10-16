from math import sqrt, acos
from typing import List


def scalar(v1: List[float], v2: List[float]) -> float:
    """
    Calculate the scalar product (dot product) of two vectors.

    Parameters:
    ----------
    v1 : List[float]
        The first input vector.
    v2 : List[float]
        The second input vector.

    Returns:
    -------
    float
        The scalar product of the vectors.

    Raises:
    ------
    ValueError
        If the lengths of the vectors are not equal.
    """

    if len(v1) != len(v2):
        raise ValueError("!Vectors have different lengths!")

    scalar = 0.0
    for i in range(len(v1)):
        scalar += v1[i] * v2[i]

    return scalar


def length(v: List[float]) -> float:
    """
    Calculate the length (magnitude) of a vector.

    Parameters:
    ----------
    v : List[float]
        The vector.

    Returns:
    -------
    float
        The length of the vector.
    """

    result = 0.0
    for i in range(len(v)):
        result += (v[i]) ** 2

    return sqrt(result)


def angle(v1: List[float], v2: List[float]) -> float:
    """
    Calculate the angle between two vectors.

    Parameters:
    ----------
    v1 : List[float]
        The first vector.
    v2 : List[float]
        The second vector.

    Returns:
    -------
    float
        The angle between the vectors in radians.
    """

    return acos(scalar(v1, v2) / (length(v1) * length(v2)))
