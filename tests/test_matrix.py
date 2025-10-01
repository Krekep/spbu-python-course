import pytest

from project.matrix import Matrix


def test_shape_and_indexing():
    A = Matrix([[1, 2], [3, 4], [5, 6]])
    assert A.shape == (3, 2)
    assert list(A[0]) == [1.0, 2.0]
    assert list(A[2]) == [5.0, 6.0]


def test_addition():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    C = A + B
    assert [list(r) for r in C] == [[6.0, 8.0], [10.0, 12.0]]


def test_scalar_multiplication():
    A = Matrix([[1, -2], [3, 0]])
    B = 2 * A
    C = A * 0.5
    assert [list(r) for r in B] == [[2.0, -4.0], [6.0, 0.0]]
    assert [list(r) for r in C] == [[0.5, -1.0], [1.5, 0.0]]


def test_matrix_multiplication():
    A = Matrix([[1, 2, 3], [4, 5, 6]])  # 2x3
    B = Matrix([[1, 2], [3, 4], [5, 6]])  # 3x2
    C = A * B  # 2x2
    assert [list(r) for r in C] == [[22.0, 28.0], [49.0, 64.0]]


def test_transpose():
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    AT = A.T
    assert AT.shape == (3, 2)
    assert [list(r) for r in AT] == [[1.0, 4.0], [2.0, 5.0], [3.0, 6.0]]


def test_invalid_construction_and_ops():
    with pytest.raises(ValueError):
        _ = Matrix([])
    with pytest.raises(ValueError):
        _ = Matrix([[1, 2], [3]])
    A = Matrix([[1, 2, 3]])
    B = Matrix([[1, 2]])
    with pytest.raises(ValueError):
        _ = A + B
    with pytest.raises(ValueError):
        _ = A * B
