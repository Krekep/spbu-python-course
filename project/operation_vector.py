from math import sqrt, acos
from typing import List

def scalar(v1: List[float], v2: List[float]) -> float:

    """
    Calculate the scalar product of vectors

    v1 = the first input vector
    v2 = the second input vector

    Return -> the scalar product of the vectors

    ValueError = the lengths of the vectors are not equal
    """

    
    if len(v1) != len(v2):
        raise ValueError("!Vectors have different lengths!")

    scalar = 0.0
    for i in range(len(v1)):
        scalar += v1[i] * v2[i]

    return scalar

def length(v: List[float]) -> float:

    """
    Calculate the length of vector

    v = the vector

    Return -> the length of the vector
    """
   
    result = 0.0
    for i in range(len(v)):
        result += (v[i]) ** 2

    return sqrt(result)

def angle(v1: List[float], v2: List[float]) -> float:

    """
    Calculate the angle between the vectors

    v1 = the first vector
    v2 = the second vector

    Return -> the angle between the vectors
    """
   
    return acos(scalar(v1, v2) / (length(v1) * length(v2)))
