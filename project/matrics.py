from typing import List, Optional


def sum_matr(a: List[List[float]], b: List[List[float]]) -> Optional[List[List[float]]]:
    """
    Add two matrices

    Parameters:
        a (List[List[float]]): First matrix
        b (List[List[float]]): Second matrix

    Returns:
        Optional[List[List[float]]]: Sum of matrix a and matrix b
    """
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return None
    return [[float(a[i][j] + b[i][j]) for j in range(len(a[0]))] for i in range(len(a))]


def pro_matr(a: List[List[float]], b: List[List[float]]) -> Optional[List[List[float]]]:
    """ "
    Multiplicate two matrices

    Parameters:
        a (List[List[float]]): First matrix
        b (List[List[float]]): Second matrix

    Returns:
        Optional[List[List[float]]]: Product of matrix a and matrix b
    """
    if len(a[0]) != len(b):
        return None

    result = [[0.0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += float(a[i][k] * b[k][j])

    return result


def tra_matr(a: List[List[float]]) -> List[List[float]]:
    """ "
     Transpose a matrix

    Parameters:
        a (List[List[float]]): Matrix

    Returns:
        List[List[float]]: Transposed matrix
    """
    return [[float(a[j][i]) for j in range(len(a))] for i in range(len(a[0]))]
