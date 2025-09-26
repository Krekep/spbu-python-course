import pytest
import numpy as np
from algebra import*

class TestAlgebra:
  @pytest.mark.parametrize('a,b,expected', [
    (np.array([1, 2, 3]), np.array([4, 5, 6]), 32),
    (np.array([1, 0]), np.array([0, 1]), 0),
    (np.array([2, 3]), np.array([-1, 4]), 10),
  ])

  def test_Scalar(self, a, b, expected): #скалярное произведение
    result = Scalar(a, b)
    np.testing.assert_array_equal(result, expected)

  def test_Normal(self):
    a = np.array([0, 1]) #длина вектора
    expected = 5.0
    result = Normal(a)
    np.testing.assert_array_equal(result, expected)

  def test_Angle(self):
    a = np.array([1, 0]) # 90 градусов
    b = np.array([0, 1])
    assert Angle(a, b) == pytest.approx(90.0, abs = 1e-5)

    a = np.array([1, 2, 3]) # 0 градусов
    b = np.array([2, 4, 6])
    assert Angle(a, b) == pytest.approx(0.0, abs=1e-5)

  def test_Trans(self): #транспонирование
    M = np.array([[1, 2], [3,4]])
    expected = np.array([[1,3],[2,4]])
    result = Trans(M)
    np.testing.assert_array_equal(result, expected)
    
  def test_Multiplication(self): #умножение матриц
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    expected = np.array([[19, 22], [43, 50]])
    result = Multiplication(A, B)
    np.testing.assert_array_equal(result, expected)

  def test_Summa(self): #сумма матриц
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    expected = A + B
    result = Summa(A, B)
    np.testing.assert_array_equal(result, expected)
