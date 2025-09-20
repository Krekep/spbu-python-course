
from typing import List, Union, Any
import math

# This function add matrix1 and matrix2
def matrix_addition(matrix1: List[List[Union[int, float]]], matrix2: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    
    if len(matrix1) != len(matrix2) or any(len(row1) != len(row2) for row1, row2 in zip(matrix1, matrix2)):
        raise ValueError("The matrices must be the same size")
    
    return [
        [x + y for x, y in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]

# This function multiplies matrix1 and matrix2
def matrix_multiplication(matrix1: List[List[Union[int, float]]], matrix2: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("the number of columns in a matrix must be equal to the number of rows in another matrix")
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(element)
        result.append(row)
    
    return result

# This function transpose matrix
def matrix_transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    
    return [list(row) for row in zip(*matrix)] # '*' - unpacks the matrix

# This function produces a scalar product of two vectors
def dot_product(vector1: List[Union[int, float]], vector2: List[Union[int, float]]) -> Union[int, float]:
    if len(vector1) != len(vector2):
        raise ValueError("The vectors must be the same length.")
    return sum(x * y for x, y in zip(vector1, vector2))

# This function calculates the length of the vector
def vector_length(vector: List[Union[int, float]]) -> float:
    return math.sqrt(sum(x * x for x in vector))

# This function finds the angle between two vectors
def angle_between_vectors(vector1: List[Union[int, float]], vector2: List[Union[int, float]]) -> float:
    if len(vector1) != len(vector2):
        raise ValueError("The vectors must be the same length.")
    
    dot = dot_product(vector1, vector2)
    length1 = vector_length(vector1)
    length2 = vector_length(vector2)
    
    if length1 == 0 or length2 == 0:
        raise ValueError("the vectors should not be null")
    
    cos_angle = dot / (length1 * length2)
    # Обеспечиваем, чтобы значение было в допустимом диапазоне для arccos
    cos_angle = max(-1.0, min(1.0, cos_angle))
    
    return math.acos(cos_angle)