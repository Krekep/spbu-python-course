import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))
from project.Task1.matrix_operations import matrix_add, matrix_multiply, matrix_transpose, Matrix

class TestMatrixOperations:
    """Test cases for matrix operations."""
    
    def test_matrix_add(self):
        """Test matrix addition."""
        result = matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        assert result == [[6, 8], [10, 12]]
    
    def test_matrix_add_invalid_dimensions(self):
        """Test matrix addition with invalid dimensions."""
        with pytest.raises(ValueError, match="Matrices must have the same dimensions"):
            matrix_add([[1, 2]], [[3, 4, 5]])
    
    def test_matrix_multiply(self):
        """Test matrix multiplication."""
        result = matrix_multiply([[1, 2], [3, 4]], [[2, 0], [1, 2]])
        assert result == [[4, 4], [10, 8]]
        
        # Test identity matrix multiplication
        identity = [[1, 0], [0, 1]]
        matrix = [[1, 2], [3, 4]]
        result = matrix_multiply(matrix, identity)
        assert result == matrix
    
    def test_matrix_multiply_invalid_dimensions(self):
        """Test matrix multiplication with invalid dimensions."""
        with pytest.raises(ValueError):
            matrix_multiply([[1, 2]], [[3, 4, 5]])
    
    def test_matrix_transpose(self):
        """Test matrix transposition."""
        result = matrix_transpose([[1, 2, 3], [4, 5, 6]])
        assert result == [[1, 4], [2, 5], [3, 6]]
        
        # Test square matrix transpose
        result = matrix_transpose([[1, 2], [3, 4]])
        assert result == [[1, 3], [2, 4]]


class TestMatrixClass:
    """Test cases for Matrix class."""
    
    def test_matrix_creation(self):
        """Test Matrix object creation."""
        m = Matrix([[1, 2], [3, 4]])
        assert m.data == [[1, 2], [3, 4]]
        assert m.rows == 2
        assert m.cols == 2
    
    def test_matrix_creation_invalid(self):
        """Test Matrix creation with invalid data."""
        with pytest.raises(ValueError, match="All rows must have the same length"):
            Matrix([[1, 2], [3, 4, 5]])
    
    def test_matrix_addition(self):
        """Test matrix addition using Matrix class."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        result = m1.add(m2)
        expected = Matrix([[6, 8], [10, 12]])
        assert result == expected
    
    def test_matrix_multiplication(self):
        """Test matrix multiplication using Matrix class."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[2, 0], [1, 2]])
        result = m1.multiply(m2)
        expected = Matrix([[4, 4], [10, 8]])
        assert result == expected
    
    def test_matrix_transpose_method(self):
        """Test matrix transposition using Matrix class."""
        m = Matrix([[1, 2, 3], [4, 5, 6]])
        result = m.transpose()
        expected = Matrix([[1, 4], [2, 5], [3, 6]])
        assert result == expected
    
    def test_matrix_repr(self):
        """Test Matrix string representation."""
        m = Matrix([[1, 2], [3, 4]])
        assert repr(m) == "Matrix([[1, 2], [3, 4]])"
    
    def test_matrix_equality(self):
        """Test Matrix equality comparison."""
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[1, 2], [3, 4]])
        m3 = Matrix([[5, 6], [7, 8]])
        assert m1 == m2
        assert m1 != m3
        assert m1 != "not a matrix"