import pytest

from project.matrixes import matrix_addition, matrix_multiplication, matrix_transpose


class TestMatrixes:
    @pytest.mark.parametrize(
        "A, B, expected",
        [
            ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[6, 8], [10, 12]]),
            ([[0, 0], [0, 0]], [[1, 2], [3, 4]], [[1, 2], [3, 4]]),
            ([[1, -2], [3, -4]], [[-1, 2], [-3, 4]], [[0, 0], [0, 0]]),
            ([[1]], [[2]], [[3]]),
        ],
    )
    def test_matrix_addition(self, A, B, expected):
        assert matrix_addition(A, B) == expected

    def test_matrix_addition_invalid_size(self):
        with pytest.raises(ValueError):
            matrix_addition([[1, 2]], [[1, 2], [3, 4]])

    @pytest.mark.parametrize(
        "A, B, expected",
        [
            ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[19, 22], [43, 50]]),
            ([[1, 0], [0, 1]], [[2, 3], [4, 5]], [[2, 3], [4, 5]]),
            (
                [[1, 2, 3], [4, 5, 6]],
                [[7, 8], [9, 10], [11, 12]],
                [[58, 64], [139, 154]],
            ),
            ([[1]], [[2]], [[2]]),
        ],
    )
    def test_matrix_multiplication(self, A, B, expected):
        assert matrix_multiplication(A, B) == expected

    def test_matrix_multiplication_invalid_size(self):
        with pytest.raises(ValueError):
            matrix_multiplication([[1, 2]], [[1, 2], [3, 4], [5, 6]])

    @pytest.mark.parametrize(
        "A, expected",
        [
            ([[1, 2], [3, 4]], [[1, 3], [2, 4]]),
            ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
            ([[1]], [[1]]),
            ([[1, -2], [-3, 4]], [[1, -3], [-2, 4]]),
        ],
    )
    def test_matrix_transpose(self, A, expected):
        assert matrix_transpose(A) == expected
