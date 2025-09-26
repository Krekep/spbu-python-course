"""
Test module for vector operations.

Contains unit tests for vector functions: scalar product, length calculation, angle between vectors.
"""

import sys
import os
import math

# Add project directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "project"))

from vector import Scalar, Lenth, Angle


def test_scalar():
    """
    Test scalar product calculation with various cases.
    """
    # Test with positive numbers
    v1 = [1.0, 2.0, 3.0]
    v2 = [4.0, 5.0, 6.0]
    expected = 1.0 * 4.0 + 2.0 * 5.0 + 3.0 * 6.0
    assert Scalar(v1, v2) == expected

    # Test with zero vector
    v3 = [0.0, 0.0, 0.0]
    v4 = [1.0, 2.0, 3.0]
    assert Scalar(v3, v4) == 0.0

    # Test with negative numbers
    v5 = [-1.0, 2.0, -3.0]
    v6 = [4.0, -5.0, 6.0]
    expected = (-1.0) * 4.0 + 2.0 * (-5.0) + (-3.0) * 6.0
    assert Scalar(v5, v6) == expected


def test_lenth():
    """
    Test vector length calculation with various cases.
    """
    # Test with 2D vector
    v1 = [3.0, 4.0]
    expected = 5.0
    assert Lenth(v1) == expected

    # Test with unit vector
    v2 = [1.0, 0.0, 0.0]
    assert Lenth(v2) == 1.0

    # Test with single element vector
    v3 = [5.0]
    assert Lenth(v3) == 5.0

    # Test with zero vector
    v4 = [0.0, 0.0, 0.0, 0.0]
    assert Lenth(v4) == 0.0


def test_angle():
    """
    Test angle calculation between vectors with various cases.
    """
    # Test standard angles
    v7 = [1.0, 1.0]
    v8 = [1.0, 0.0]
    expected_45 = math.pi / 4.0
    assert abs(Angle(v7, v8) - expected_45) < 0.0001

    v9 = [1.0, math.sqrt(3)]
    v10 = [2.0, 0.0]  #
    expected_60 = math.pi / 3.0
    assert abs(Angle(v9, v10) - expected_60) < 0.0001

    # Test perpendicular vectors
    v1 = [1.0, 0.0]
    v2 = [0.0, 1.0]
    expected = math.pi / 2.0
    assert abs(Angle(v1, v2) - expected) < 0.0001

    # Test parallel vectors
    v3 = [1.0, 2.0]
    v4 = [2.0, 4.0]  # v4 = 2 * v3
    assert abs(Angle(v3, v4)) < 0.0001

    # Test opposite vectors
    v5 = [1.0, 0.0]
    v6 = [-1.0, 0.0]
    expected = math.pi
    assert abs(Angle(v5, v6) - expected) < 0.0001
