import pytest
import project.VectorsMatrix.vector_matrix as vm



def test_multiplication():
    m_1 = vm.Matrix([[1, 1, 1],
                                [1, 1, 1]])

    m_2 = vm.Matrix([[2, 3],
                                [4, 5],
                                [6, 7]])

    assert vm.Matrix.multiplication(m_1, m_2).elements == [[12, 15], [12, 15]]


def test_add():
    m_1 = vm.Matrix([[1, 1, 1],
                                [1, 1, 1]])

    m_2 = vm.Matrix([[2, 3, 1],
                                [4, 5, 2]])

    assert (m_1 + m_2).elements == [[3, 4, 2], 
                                    [5, 6, 3]]
    
def test_sub():
    m_1 = vm.Matrix([[1, 1, 1],
                                [1, 1, 1]])

    m_2 = vm.Matrix([[2, 3, 1],
                                [4, 5, 2]])

    assert (m_2 - m_1).elements == [[1, 2, 0], 
                                    [3, 4, 1]]

def test_transpose():
    m = vm.Matrix([[2, 3, 1],
                              [4, 5, 2]])
    assert vm.Matrix.transpose(m).elements == [[2, 4],
                                                 [3, 5],
                                                 [1, 2]]


def test_mul_scalar():
    m = vm.Matrix([[2, 3, 1],
                              [4, 5, 2]])
    assert (m * 2).elements == [[4, 6, 2],
                              [8, 10, 4]]

