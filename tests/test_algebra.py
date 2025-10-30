import pytest
from project.algebra import scalar, normal, angle, trans, multiplication, summa


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
        """Test scalar product of vectors."""
        result = scalar(a, b)
        assert result == expected

    def test_normal(self) -> None:
        """Test vector norm calculation."""
        a = [3, 4]
        expected = 5.0
        result = normal(a)
        assert result == expected

    def test_angle(self) -> None:
        """Test angle between vectors."""
        # 90 degrees
        a = [1, 0]
        b = [0, 1]
        assert angle(a, b) == pytest.approx(90.0, abs=1e-5)

        # 0 degrees
        a = [1, 2, 3]
        b = [2, 4, 6]
        assert angle(a, b) == pytest.approx(0.0, abs=1e-5)

    def test_trans(self) -> None:
        """Test matrix transposition."""
        matrix = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        result = trans(matrix)
        assert result == expected

    def test_multiplication(self) -> None:
        """Test matrix multiplication."""
        a = [[1.0, 2.0], [3.0, 4.0]]
        b = [[5.0, 6.0], [7.0, 8.0]]
        expected = [[19.0, 22.0], [43.0, 50.0]]
        result = multiplication(a, b)
        assert result == expected

        """Test 2x3 * 3x2 multiplication"""
        a1 = [[1, 2, 3], [4, 5, 6]]
        b1 = [[7, 8], [9, 10], [11, 12]]
        expected1 = [[58, 64], [139, 154]]
        result1 = multiplication(a1, b1)
        assert result1 == expected1

        """Test 3x2 * 2x3 multiplication"""
        a2 = [[1, 2], [3, 4], [5, 6]]
        b2 = [[7, 8, 9], [10, 11, 12]]
        expected2 = [[27, 30, 33], [61, 68, 75], [95, 106, 117]]
        result2 = multiplication(a2, b2)
        assert result2 == expected2

    def test_summa(self) -> None:
        """Test matrix addition."""
        a = [[1, 2], [3, 4]]
        b = [[5, 6], [7, 8]]
        expected = [[6, 8], [10, 12]]
        result = summa(a, b)
        assert result == expected
