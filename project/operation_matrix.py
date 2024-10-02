from typing import List

def add(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:

    """
    Add two matrices

    A = the first matrix
    B = the second matrix

    Return -> matrix addition

    ValueError = matrices of different dimensions
    """
    
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("!Matrices have different dimensions!")

    res = [[0.0] * len(A[0]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            res[i][j] = A[i][j] + B[i][j]
    return res

def mul(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:

    """
    Multiply two matrices

    A = the first  matrix
    B = the second matrix

    Returns -> matrix multiplication 

    ValueError = the number of columns in the first matrix don't match the number of rows in the second matrix.
        
    """
    
    if len(A[0]) != len(B):
        raise ValueError("!Matrices cannot be multiplied!")

    res = [[0.0] * len(B[0]) for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                res[i][j] += A[i][k] * B[k][j]

    return res

def transpose(A: List[List[float]]) -> List[List[float]]:

    """
    Transpose a matrix

    A = The  matrix 

    Returns ->  matrix transposition
    
    """

    res = [[0.0] * len(A) for i in range(len(A[0]))]

    for i in range(len(A[0])):
        for j in range(len(A)):
            res[i][j] = A[j][i]

    return res
