"""
Vector Operations Module

This module provides basic vector operations including:
- Scalar (dot) product calculation
- Vector length calculation
- Angle between vectors calculation

All functions work with vectors represented as lists of floats.
"""

from math import sqrt, acos
from typing import List, Optional


def Scalar(v1: List[float], v2: List[float]) -> Optional[float]:
    """
    Calculate scalar product of two vectors

    Parameters:
        v1 (List[float]): First vector
        v2 (List[float]): Second vector

    Returns:
        Optional[float]: Scalar product of vectors v1 and v2
    """
    if len(v1) != len(v2):
        return None

    if not v1 or not v2:
        return None

    return sum(v1[i] * v2[i] for i in range(len(v1)))


def Lenth(v: List[float]) -> float:
    """
    Calculate length of a vector

    Parameters:
        v (List[float]): Input vector

    Returns:
        float: Length of vector v
    """
    if not v:
        return 0.0

    return sqrt(sum(x**2 for x in v))


def Angle(v1: List[float], v2: List[float]) -> Optional[float]:
    """
    Calculate angle between two vectors

    Parameters:
        v1 (List[float]): First vector
        v2 (List[float]): Second vector

    Returns:
        Optional[float]: Angle between vectors in radians
    """

    if len(v1) != len(v2):
        return None

    scalar_product = Scalar(v1, v2)
    if scalar_product is None:
        return None

    length_v1 = Lenth(v1)
    length_v2 = Lenth(v2)

    if length_v1 == 0 or length_v2 == 0:
        return None

    denominator = length_v1 * length_v2
    if denominator == 0:
        return None

    cos_angle = scalar_product / denominator
    if cos_angle < -1 or cos_angle > 1:
        return None

    return acos(cos_angle)
