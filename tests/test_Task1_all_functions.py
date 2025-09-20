import pytest
import math
import project.operations_on_vectors_and_matrix as vm

class Test_Vector_Operations:
    def test_dot_product(self):
        assert vm.dot_product([1, 2, 3], [4, 5, 6]) == 32
        assert vm.dot_product([0, 0], [0, 0]) == 0
        
        assert vm.dot_product([-1, 2], [3, -4]) == -11
        
        assert abs(vm.dot_product([0.1, 0.2], [0.3, 0.4]) - 0.11) < 0.0001
        
        with pytest.raises(ValueError):
            vm.dot_product([1, 2], [1, 2, 3])  # different lenght

    def test_vector_length(self):
        assert vm.vector_length([3, 4]) == 5.0
        assert vm.vector_length([0, 0]) == 0.0
        assert vm.vector_length([-3, -4]) == 5.0
        assert abs(vm.vector_length([1, 2, 2]) - 3.0) < 0.0001

    def test_angle_between_vectors(self):
        assert vm.angle_between_vectors([1, 0], [2, 0]) == pytest.approx(0.0)
        assert vm.angle_between_vectors([1, 0], [0, 1]) == pytest.approx(math.pi/2)
        
        assert vm.angle_between_vectors([1, 0, 0], [0, 1, 0]) == pytest.approx(math.pi/2)
        
        with pytest.raises(ValueError):
            vm.angle_between_vectors([0, 0], [1, 2])  # nool vector
        with pytest.raises(ValueError):
            vm.angle_between_vectors([1, 2], [1, 2, 3])  # Different lenght

class Test_Matrix_Operations:
    def test_matrix_addition(self):

        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        assert vm.matrix_addition(matrix1, matrix2) == expected
        
        matrix1 = [[-1, 2], [3, -4]]
        matrix2 = [[5, -6], [-7, 8]]
        expected = [[4, -4], [-4, 4]]
        assert vm.matrix_addition(matrix1, matrix2) == expected
        
        with pytest.raises(ValueError):
            vm.matrix_addition([[1, 2]], [[1]])  # different size of matrix

    def test_matrix_multiplication(self):

        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        assert vm.matrix_multiplication(matrix1, matrix2) == expected
        
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[7, 8], [9, 10], [11, 12]]
        expected = [[58, 64], [139, 154]]
        assert vm.matrix_multiplication(matrix1, matrix2) == expected
        
        with pytest.raises(ValueError):
            vm.matrix_multiplication([[1, 2, 3]], [[1, 2]])  # incompatible sizes

    def test_matrix_transpose(self):

        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        assert vm.matrix_transpose(matrix) == expected
        
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        assert vm.matrix_transpose(matrix) == expected
        
        matrix = [[1, 2, 3]]
        expected = [[1], [2], [3]]
        assert vm.matrix_transpose(matrix) == expected
