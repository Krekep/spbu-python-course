import pytest
import math

from project.vectors import vector_length, scalar_product, angle_vectors


class TestVectors:
    def test_vector_length_basic(self):
        assert vector_length([1, 2]) == pytest.approx(math.sqrt(5))

    @pytest.mark.parametrize(
        "vec, expected",
        [
            ([3, 4], 5),
            ([6, 8], 10),
            ([0, 0, 0], 0),
            ([1, 9], math.sqrt(82)),
            ([1, 3, 4], math.sqrt(26)),
        ],
    )
    def test_vector_length_parametrize(self, vec, expected):
        assert vector_length(vec) == pytest.approx(expected)

    @pytest.mark.parametrize(
        "vec1, vec2, expected",
        [
            ([1, 2], [3, 4], 11),
            ([1, 1], [2, 2], 4),
            ([0, 0], [5, 7], 0),
            ([-1, 2], [3, -4], -11),
        ],
    )
    def test_scalar_product(self, vec1, vec2, expected):
        assert scalar_product(vec1, vec2) == expected

    def test_scalar_product_invalid_length(self):
        with pytest.raises(ValueError):
            scalar_product([1, 2], [1, 2, 3])

    @pytest.mark.parametrize(
        "vec1, vec2, expected",
        [
            ([1, 0], [0, 1], math.pi / 2),
            ([10, 0], [20, 0], 0),
            ([1, 0], [-1, 0], math.pi),
            ([1, 1], [1, -1], math.pi / 2),
        ],
    )
    def test_angle_vectors(self, vec1, vec2, expected):
        assert angle_vectors(vec1, vec2) == pytest.approx(expected)

    def test_angle_vectors_zero_vector(self):
        with pytest.raises(ValueError):
            angle_vectors([0, 0], [1, 0])
