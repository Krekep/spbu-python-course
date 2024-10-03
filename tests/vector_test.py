import pytest
from project.vector_operations import vector_multiply, vector_length, vector_angle

def test_vector_multiply():
    v1 = [1, 2, 3, 4]
    v2 = [5, 5, 5, 5]
    assert vector_multiply(v1, v2) == 30

    v1 = [95, 100, 4, 1]
    v2 = [0, 0, 0, 0]
    assert vector_multiply(v1, v2) == 0

    v1 = [4, 2]
    v2 = [6, 1, 99, 13]
    with pytest.raises(ValueError):
        vector_multiply(v1, v2)

def test_vector_length():
    v = [0, 0, 0]
    assert vector_length(v) == 0

    v = [4, 0, 3]
    assert vector_length(v) == 5

def test_vector_angle():
    v1 = [0, 1]
    v2 = [1, 0]
    assert pytest.approx(vector_angle(v1, v2), 0.0001) == 1.5708

    v1 = [1, 1, 1]
    v2 = [5, 5, 5]
    assert vector_angle(v1, v2) == 0