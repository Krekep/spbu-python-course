import math
from typing import List, Optional


def scalar_product(a: Optional[List[float]], b: Optional[List[float]]) -> float:
    """
    Calculates the scalar product of two vectors of arbitrary dimension.

    Parameters
    ----------
    a : Optional[List[float]]
        The first vector represented as a list of floats.
    b : Optional[List[float]]
        The second vector represented as a list of floats.

    Returns
    -------
    float
        The scalar product of vectors `a` and `b`.

    Raises
    ------
    ValueError
        If one of the vectors is None, empty, or if the vectors are not of the same dimension.
    """
    if a is None or b is None:
        raise ValueError("One of the vectors is empty or None")
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension")

    # Scalar product of two vectors
    return sum(a[i] * b[i] for i in range(len(a)))


def length_vec(a: Optional[List[float]], b: Optional[List[float]]) -> float:
    """
    Calculates the length of the vector between two points `a` and `b` in arbitrary dimensions.

    Parameters
    ----------
    a : Optional[List[float]]
        The first point represented as a list of floats.
    b : Optional[List[float]]
        The second point represented as a list of floats.

    Returns
    -------
    float
        The length of the vector between points `a` and `b`.

    Raises
    ------
    ValueError
        If one of the points is None, empty, or if the points are not of the same dimension.
    """
    if a is None or b is None:
        raise ValueError("One of the points is empty or None")
    if len(a) != len(b):
        raise ValueError("Points must have the same dimension")

    return math.sqrt(sum((b[i] - a[i]) ** 2 for i in range(len(a))))


def cos_ab(a: Optional[List[float]], b: Optional[List[float]]) -> float:
    """
    Calculates the cosine of the angle between vectors `a` and `b` in arbitrary dimensions.

    Parameters
    ----------
    a : Optional[List[float]]
        The first vector represented as a list of floats.
    b : Optional[List[float]]
        The second vector represented as a list of floats.

    Returns
    -------
    float
        The cosine of the angle between vectors `a` and `b`.

    Raises
    ------
    ValueError
        If one of the vectors is None, empty, if the vectors have different dimensions, or if one of the vectors has zero length.
    """
    if a is None or b is None:
        raise ValueError("One of the vectors is empty or None")
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension")

    dot_product = scalar_product(a, b)
    magnitude_a = math.sqrt(sum(coord**2 for coord in a))
    magnitude_b = math.sqrt(sum(coord**2 for coord in b))

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError(
            "The length of one of the vectors is zero, cannot compute the cosine of the angle"
        )

    return dot_product / (magnitude_a * magnitude_b)
