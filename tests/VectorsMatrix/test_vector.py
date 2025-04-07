import pytest
import project.VectorsMatrix.vector_matrix as vm



def test_scalar_product():
    v1 = vm.Vector([1, 1])
    v2 = vm.Vector([3, 4, 5])

    assert vm.Vector.scalar_product(v1, v2) == 7


def test_sub():
    v1 = vm.Vector([1, 1])
    v2 = vm.Vector([3, 4, 5])
    assert (v2 - v1).coordinates == [2, 3, 5]

def test_add():
    v1 = vm.Vector([1, 1])
    v2 = vm.Vector([3, 4, 5])
    assert (v1 + v2).coordinates == [4, 5, 5]


def test_mul_scalar():
    v = vm.Vector([1, 1])
    assert (v * 2).coordinates == [2, 2]

def test_get_len():
    v = vm.Vector([3, 4])
    assert vm.Vector.get_len(v) == 5


def test_get_angle():
    v1 = vm.Vector([1, 1])
    v2 = vm.Vector([1, -1])
    assert vm.Vector.get_angle(v1, v2) == 90

