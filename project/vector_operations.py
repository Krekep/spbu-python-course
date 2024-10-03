from math import acos

def  vector_multiply(v1: list[float], v2: list[float]) -> float:
    """
    Dot prodaction of two vectors

    Args:
    v1: list[float] - first vector
    v2: list[float] - second vector

    Return:
    float - dot prodaction
    """
    if len(v1) == len(v2):
        v_res: int = 0
        for i in range(len(v1)):
            v_res += v1[i] * v2[i]
        return v_res
    else:
        raise ValueError("Different vectors' dimensions")
    
def vector_length(v: list[float]) -> float:
    """
    Calculate length of vector

    Args:
    v: list[float] - vector

    Return:
    float - length of vector
    """
    return (vector_multiply(v, v)) ** 0.5

def vector_angle(v1: list[float], v2: list[float]) -> float:
    """
    Calculate angle between two vectors

    Args:
    v1:list[float] - first vector
    v2:list[float] - second vector

    Return:
    float - angle in radians
    """
    return acos(vector_multiply(v1, v2) / (vector_length(v1) * (vector_length(v2))))