import math
from typing import List

class Vector:

    def __init__(self, coordintes: List[float]) -> None:
        """Инициализация вектора списком координат"""
        self.coordinates = coordintes

    def copy(v: "Vector") -> "Vector":
        """Создает копию вектора"""
        return Vector(v.coordinates)

    def scalar_product(v_1: "Vector", v_2: "Vector") -> float:
        """
        Вычисляет скалярное произведение двух векторов
        Если векторы разной длины, умножаются только соответствующие компоненты
        """
        len_v_1 = len(v_1.coordinates)
        len_v_2 = len(v_2.coordinates)

        product: float = 0
        if len_v_1 >= len_v_2:
            for i in range(len_v_2):
                product += v_1.coordinates[i] * v_2.coordinates[i]
        else:
            for i in range(len_v_1):
                product += v_1.coordinates[i] * v_2.coordinates[i]

        return product

    def get_len(self) -> float:
        """Вычисляет длину вектора"""
        return math.sqrt(Vector.scalar_product(self, self))

    def get_angle(v1: "Vector", v2: "Vector") -> float:
        """Вычисляет угол между двумя векторами в градусах"""
        return math.degrees(math.acos(Vector.scalar_product(v1, v2) / (Vector.get_len(v1) * Vector.get_len(v2))))

    def __add__(self, v: "Vector") -> "Vector":
        """
        Сложение двух векторов
        Если векторы разной длины, недостающие компоненты считаются нулевыми
        """
        res: List[float] = []
        len_self = len(self.coordinates)
        len_v = len(v.coordinates)
        
        if len_v >= len_self:
            for i in range(len_self):
                res.append(self.coordinates[i] + v.coordinates[i])
            for i in range(len_self, len_v):
                res.append(v.coordinates[i])
        else:
            for i in range(len_v):
                res.append(self.coordinates[i] + v.coordinates[i])
            for i in range(len_v, len_self):
                res.append(self.coordinates[i])
        
        return Vector(res)

    def __mul__(self, scalar: float) -> "Vector":
        """Умножение вектора на скаляр"""
        res: List[float] = []
        for i in range(len(self.coordinates)):
            res.append(self.coordinates[i] * scalar)
        return Vector(res)

    def __sub__(self, v: "Vector") -> "Vector":
        """Вычитание векторов (реализовано через сложение с отрицательным вектором)"""
        return(self + v * (-1))

    def __repr__(self) -> str:
        """Возвращает строковое представление вектора"""
        return f"Vector({self.coordinates})"
    


class Matrix:

    def __init__(self, m: List[List[float]]) -> None:
        """Инициализация матрицы двумерным списком"""
        self.elements = m

    def copy(m: "Matrix") -> "Matrix":
        """Создает копию матрицы"""
        return Matrix(m.elements)

    def __add__(self, m: "Matrix") -> "Matrix":
        """Сложение матриц. Матрицы должны иметь одинаковые размеры"""
        if len(self.elements) != len(m.elements) and len(self.elements[0]) != len(m.elements[0]):
            raise ValueError("Matrices must have the same dimensions")
        return Matrix(
            [
                [self.elements[i][j] + m.elements[i][j] for j in range(len(self.elements[0]))]
                for i in range(len(self.elements))
            ]
        )

    def multiplication(m_1: "Matrix", m_2: "Matrix") -> "Matrix":
        """
        Умножение матриц
        Число столбцов первой матрицы должно равняться числу строк второй матрицы
        """
        if len(m_1.elements) != len(m_2.elements[0]):
            raise ValueError("Matrices must have the same dimensions")
        return Matrix(
            [
                [
                    sum(m_1.elements[i][r] * m_2.elements[r][j] for r in range(len(m_1.elements[0])))
                for j in range(len(m_2.elements[0]))
                ]
                for i in range(len(m_1.elements))
            ]
        )

    def __mul__(self, scalar: float) -> "Matrix":
        """Умножение матрицы на скаляр"""
        return Matrix(
            [
                [self.elements[i][j] * scalar for j in range(len(self.elements[0]))]
                for i in range(len(self.elements))
            ]
        )

    def transpose(self) -> "Matrix":
        """Транспонирование матрицы"""
        return Matrix(
            [[self.elements[i][j] for i in range(len(self.elements))] for j in range(len(self.elements[0]))]
        )

    def __sub__(self, m: "Matrix") -> "Matrix":
        """Вычитание матриц (реализовано через сложение с отрицательной матрицей)"""
        return(self + m * (-1))

    def __repr__(self) -> str:
        """Возвращает строковое представление матрицы"""
        return f"Matrix({self.elements})"