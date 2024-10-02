import pytest
from project.operation_vector import scalar, length, angle

def test_scalar():
    assert scalar([1, 6, 9], [-5, 0, 7]) == 58.0

    with pytest.raises(ValueError):
        scalar([1, 2], [1])

def test_length():
    assert length([3, 4]) == pytest.approx(5.0)
    assert length([1, 0, 0]) == 1.0
    
    assert length([-3, -4]) == pytest.approx(5.0)

def test_angle():
    assert pytest.approx(angle([1, 0], [0, 1]), 0.1) == 0.0

    assert pytest.approx(angle([1, 0], [1, 0]), 0.1) == 1.0
