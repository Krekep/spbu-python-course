import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from project.vector_operations import (
    coordinates_vectors,
    vector_length,
    angle_between_vectors,
)


def test_coordinates_vectors():
    assert coordinates_vectors([1, 2, 3], [4, 5, 6]) == 32


def test_vector_length():
    assert vector_length([3, 4]) == 5


def test_angle_between_vectors():
    assert (
        pytest.approx(angle_between_vectors([1, 0], [0, 1]), 0.0001) == 1.5708
    )  # π/2 radians
