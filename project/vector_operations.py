import math


def coordinates_vectors(v1: list[float], v2: list[float]) -> float:
    """
    Calculates the dot product of two vectors.

    Args:
        v1 (list[float]): The first vector.
        v2 (list[float]): The second vector.

    Returns:
        float: The dot product of the two vectors.
    """
    result = 0.0
    for x, y in zip(v1, v2):
        result += x * y
    return result


def vector_length(v: list[float]) -> float:
    """
    Calculates the length (magnitude) of a vector.

    Args:
        v (list[float]): The vector.

    Returns:
        float: The length of the vector.
    """
    result = 0.0
    for x in v:
        result += x**2
    return math.sqrt(result)


def angle_between_vectors(v1: list[float], v2: list[float]) -> float:
    """
    Calculates the angle between two vectors in radians.

    Args:
        v1 (list[float]): The first vector.
        v2 (list[float]]): The second vector.

    Returns:
        float: The angle between the two vectors in radians.
    """
    coordinates = coordinates_vectors(v1, v2)
    len_v1 = vector_length(v1)
    len_v2 = vector_length(v2)
    if len_v1 * len_v2 == 0:
        raise ValueError("One of the vectors has zero length")
    result = math.acos(coordinates / (len_v1 * len_v2))
    return result
