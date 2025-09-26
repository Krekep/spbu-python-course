from typing import List, Optional


def sum_matr(a: List[List[float]], b: List[List[float]]) -> Optional[List[List[float]]]:

    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def pro_matr(a: List[List[float]], b: List[List[float]]) -> Optional[List[List[float]]]:
    if len(a[0]) != len(a):
        return "Er"

    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result


def tra_matr(a: List[List[float]]) -> List[List[float]]:

    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
