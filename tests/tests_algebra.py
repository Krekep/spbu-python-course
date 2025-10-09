import pytest
import numpy as np
from algebra import scalar, normal, angle, trans, multiplication, summa


class TestAlgebra:
    @pytest.mark.parametrize(
        "a,b,expected",
        [
            ([1, 2, 3], [4, 5, 6], 32),
            ([1, 0], [0, 1], 0),
            ([2, 3], [-1, 4], 10),
        ],
    )
    def test_scalar(self, a: list, b: list, expected: float) -> None:
        """
        Test scalar product of vectors.
        
        Args:
            a: First vector
            b: Second vector
            expected: Expected scalar product result
        """
        result = scalar(a, b)
        assert result == expected

    def test_scalar_different_dimensions(self) -> None:
        """
        Test scalar product with vectors of different dimensions.
        """
        a = [1, 2, 3]
        b = [1, 2]
        with pytest.raises(ValueError, match="Vectors must have the same dimension"):
            scalar(a, b)

    def test_normal(self) -> None:
        """
        Test vector norm calculation.
        """
        a = [3, 4]
        expected = 5.0
        result = normal(a)
        assert result == expected

    def test_normal_zero_vector(self) -> None:
        """
        Test norm of zero vector.
        """
        a = [0, 0, 0]
        expected = 0.0
        result = normal(a)
        assert result == expected

    @pytest.mark.parametrize(
        "a,b,expected_angle",
        [
            ([1, 0], [0, 1], 90.0),  # 90 degrees
            ([1, 2, 3], [2, 4, 6], 0.0),  # 0 degrees (parallel vectors)
            ([1, 0], [1, 0], 0.0),  # 0 degrees (same vectors)
        ],
    )
    def test_angle(self, a: list, b: list, expected_angle: float) -> None:
        """
        Test angle between vectors.
        
        Args:
            a: First vector
            b: Second vector
            expected_angle: Expected angle in degrees
        """
        result = angle(a, b)
        assert result == pytest.approx(expected_angle, abs=1e-5)

    def test_angle_zero_vector(self) -> None:
        """
        Test angle calculation with zero vector.
        """
        a = [1, 2, 3]
        b = [0, 0, 0]
        with pytest.raises(ValueError, match="Cannot use zero vector"):
            angle(a, b)

    def test_trans(self) -> None:
        """
        Test matrix transposition.
        """
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        result = trans(matrix)
        assert result == expected

    def test_trans_rectangular(self) -> None:
        """
        Test transposition of rectangular matrix.
        """
        matrix = [[1, 2, 3], [4, 5, 6]]
        expected = [[1, 4], [2, 5], [3, 6]]
        result = trans(matrix)
        assert result == expected

    def test_multiplication(self) -> None:
        """
        Test matrix multiplication.
        """
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]
        result = multiplication(a, b)
        assert result == expected

    def test_multiplication_incompatible_dimensions(self) -> None:
        """
        Test matrix multiplication with incompatible dimensions.
        """
        a = [[1, 2, 3], [4, 5, 6]]  # 2x3
        b = [[1, 2], [3, 4]]  # 2x2
        with pytest.raises(ValueError, match="Incompatible matrix dimensions"):
            multiplication(a, b)

    def test_summa(self) -> None:
        """
        Test matrix addition.
        """
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        result = summa(a, b)
        assert result == expected

    def test_summa_different_dimensions(self) -> None:
        """
        Test matrix addition with different dimensions.
        """
        a = [[1, 2], [3, 4]]
        b = [[1, 2, 3], [4, 5, 6]]
        with pytest.raises(ValueError, match="Matrices must have the same dimensions"):
            summa(a, b)

    @pytest.mark.parametrize(
        "operation_name",
        [
            "scalar",
            "normal", 
            "angle",
            "trans",
            "multiplication",
            "summa",
        ],
    )
    def test_algebra_operations_import(self, operation_name: str) -> None:
        """
        Test that all algebra operations are properly imported and available.
        
        Args:
            operation_name: Name of the operation to test
        """
        assert operation_name in ALGEBRA_OPERATIONS
