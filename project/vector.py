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


def Scalar(v1: List[float], v2: List[float]) -> float:
    """
    Calculate scalar product of two vectors

    Parameters:
        v1 (List[float]): First vector
        v2 (List[float]): Second vector

    Returns:
        float: Scalar product of vectors v1 and v2
    """
    return sum(v1[i] * v2[i] for i in range(len(v1)))


def Lenth(v: List[float]) -> float:
    """
    Calculate length of a vector

    Parameters:
        v (List[float]): Input vector

    Returns:
        float: Length of vector v
    """
    return sqrt(sum(x**2 for x in v))


def Angle(v1: List[float], v2: List[float]) -> float:
    """
    Calculate angle between two vectors

    Parameters:
        v1 (List[float]): First vector
        v2 (List[float]): Second vector

    Returns:
        float: Angle between vectors in radians
    """
    return acos(Scalar(v1, v2) / (Lenth(v1) * Lenth(v2)))
