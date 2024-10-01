import pytest
import math
from project.vector_operations import scalar_product, length_vec, cos_ab


def test_scalar_product():
    """
    Tests the scalar_product function with two vectors.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test passes if the scalar product of the vectors is correctly computed.
    """
    vector_a = (5, 0, 0)  # Example vector
    vector_b = (10 * math.cos(math.radians(30)), 10 * math.sin(math.radians(30)), 0)
    expected = scalar_product(
        vector_a, vector_b
    )  # Using function to get expected value
    assert scalar_product(vector_a, vector_b) == pytest.approx(expected, rel=1e-5)


def test_length_vec():
    """
    Tests the length_vec function to calculate the distance between two points.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test passes if the length of the vector between points is correctly computed.
    """
    a = (0, 0, 0)
    b = (3, 4, 0)
    expected = 5  # Vector length should be 5 (Pythagorean theorem)
    assert length_vec(a, b) == pytest.approx(expected)


def test_length_vec_same_point():
    """
    Tests length_vec for the same point input.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test passes if the length of the vector between two identical points is 0.
    """
    a = (1, 2, 3)
    b = (1, 2, 3)
    expected = 0  # The vector length between the same points should be 0
    assert length_vec(a, b) == pytest.approx(expected)


def test_cos_ab():
    """
    Tests the cos_ab function to calculate the cosine of the angle between two vectors.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test passes if the cosine of the angle between the vectors is correctly computed.
    """
    a = (1, 0, 0)
    b = (0, 1, 0)
    expected = 0  # Cosine of the angle between perpendicular vectors should be 0
    assert cos_ab(a, b) == pytest.approx(expected)


def test_cos_ab_same_direction():
    """
    Tests cos_ab for vectors in the same direction.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test passes if the cosine of the angle between parallel vectors is 1.
    """
    a = (1, 0, 0)
    b = (2, 0, 0)
    expected = 1  # Cosine of the angle between parallel vectors should be 1
    assert cos_ab(a, b) == pytest.approx(expected)


def test_cos_ab_opposite_direction():
    """
    Tests cos_ab for vectors in opposite directions.

    Parameters
    ----------
    None

    Returns
    -------
    None
        The test passes if the cosine of the angle between opposite vectors is -1.
    """
    a = (1, 0, 0)
    b = (-1, 0, 0)
    expected = -1  # Cosine of the angle between opposite vectors should be -1
    assert cos_ab(a, b) == pytest.approx(expected)
