import pytest
from project.vector import Vector
import math


@pytest.fixture
def vector1():
    return Vector(1, 2, 3)


@pytest.fixture
def vector2():
    return Vector(4, 5, 6)


@pytest.fixture
def vector_zero():
    return Vector(0, 0, 0)


def test_dot(vector1, vector2):
    assert vector1.dot(vector2) == 32
    assert vector1.dot(vector1) == 14


def test_length(vector1, vector2, vector_zero):
    assert vector1.length() == math.sqrt(14)
    assert vector2.length() == math.sqrt(77)
    assert vector_zero.length() == 0


def test_angle(vector1, vector2):
    assert math.isclose(vector1.angle(vector2), 12.933154491899135)


def test_angle_zero_vector(vector1, vector_zero):
    with pytest.raises(ValueError):
        vector1.angle(vector_zero)


def test_invalid_dot(vector1):
    vector3 = Vector(1, 2)
    with pytest.raises(ValueError):
        vector1.dot(vector3)
