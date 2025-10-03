import pytest
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../'))
from project.Task1.vector_operations import dot_product, vector_length, angle_between, Vector

class TestVectorOperations:
    """Test cases for vector operations."""
    
    def test_dot_product(self):
        """Test dot product calculation."""
        assert dot_product([1, 2], [3, 4]) == 11
        assert dot_product([0, 0], [1, 2]) == 0
    
    def test_dot_product_invalid_input(self):
        """Test dot product with invalid inputs."""
        with pytest.raises(ValueError):
            dot_product([1, 2], [1])
    
    def test_vector_length(self):
        """Test vector length calculation."""
        assert vector_length([3, 4]) == 5.0
        assert vector_length([0]) == 0.0
    
    def test_angle_between(self):
        """Test angle between vectors calculation."""
        assert math.isclose(angle_between([1, 0], [0, 1]), math.pi / 2)
        assert angle_between([1, 0], [1, 0]) == 0.0


class TestVectorClass:
    """Test cases for Vector class."""
    
    def test_vector_creation(self):
        """Test Vector object creation."""
        v = Vector([1, 2, 3])
        assert v.components == [1, 2, 3]
    
    def test_vector_dot_product(self):
        """Test dot product using Vector class."""
        v1 = Vector([1, 2])
        v2 = Vector([3, 4])
        assert v1.dot(v2) == 11