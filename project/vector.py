from math import sqrt, acos


def Scalar(v1: List[float], v2: List[float]) -> float:
    return sum(v1[i] * v2[i] for i in range(len(v1)))


def Lenth(v: List[float]) -> float:
    return sqrt(sum(x**2 for x in v))


def Angle(v1: List[float], v2: List[float]) -> float:
    return acos(Scalar(v1, v2) / (Lenth(v1) * Lenth(v2)))
