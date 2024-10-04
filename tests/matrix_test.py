import pytest
from project.matrix import Matrix

def test_matrix_addition():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    result = m1.add(m2)
    assert result.data == [[6, 8], [10, 12]], "Matrix addition failed"

def test_matrix_multiplication():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    result = m1.multiply(m2)
    assert result.data == [[19, 22], [43, 50]], "Matrix multiplication failed"

def test_matrix_transpose():
    m = Matrix([[1, 2], [3, 4]])
    result = m.transpose()
    assert result.data == [[1, 3], [2, 4]], "Matrix transpose failed"

def test_add_invalid_dimensions():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6, 7], [8, 9, 10]])
    with pytest.raises(ValueError, match="Matrices must have the same dimensions for addition"):
        m1.add(m2)

def test_multiply_invalid_dimensions():
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6, 3]])
    with pytest.raises(ValueError, match="Number of columns in the first matrix must be equal to the number of rows in the second matrix."):
        m1.multiply(m2)
