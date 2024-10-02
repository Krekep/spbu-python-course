from math import sqrt, acos
from typing import List

def scalar(v1: List[float], v2: List[float]) -> float:
    
    if len(v1) != len(v2):
        raise ValueError("!Vectors have different lengths!")

    scalar = 0.0
    for i in range(len(v1)):
        scalar += v1[i] * v2[i]

    return scalar

def length(v: List[float]) -> float:
   
    result = 0.0
    for i in range(len(v)):
        result += (v[i]) ** 2

    return sqrt(result)

def angle(v1: List[float], v2: List[float]) -> float:
   
    return acos(scalar(v1, v2) / (length(v1) * length(v2)))
