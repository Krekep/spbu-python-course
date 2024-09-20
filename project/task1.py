import numpy as np
from math import acos
from collections.abc import Sequence


class Vector:
    """
    A class to represent a mathematical vector and provide basic vector operations.

    Attributes:
    ----------
    vector : np.ndarray
        The array representing the vector.

    Methods:
    -------
    __getitem__(index: int) -> float
        Returns the element at the specified index.

    __len__() -> int
        Returns the length of the vector.

    __mul__(other: "Vector") -> float
        Returns the dot product of the current vector with another vector.

    __xor__(other: "Vector") -> float
        Returns the angle (in radians) between the current vector and another vector.

    norm(ord: int = 2) -> float
        Returns the norm (magnitude) of the vector.
    """

    def __init__(self, object):
        """
        Initializes the Vector object with the given elements.

        Parameters:
        ----------
        object : iterable
            An iterable of numbers to form the vector.
        """

        self.vector = np.array(object=object)

    def __getitem__(self, index: int) -> float:
        """
        Returns the element at the specified index.

        Parameters:
        ----------
        index : int
            The index of the element to return.

        Returns:
        -------
        float
            The element at the specified index.
        """

        return self.vector[index]

    def __len__(self) -> int:
        """
        Returns the dimensionality (number of elements) of the vector.

        Returns:
        -------
        int
            The number of elements in the vector.
        """

        return len(self.vector)

    def __mul__(self, other: "Vector") -> float:
        """
        Calculates and returns the dot product of this vector with another vector.

        Parameters:
        ----------
        other : Vector
            Another vector to calculate the dot product with.

        Returns:
        -------
        float
            The dot product of the two vectors.
        """

        return np.dot(self.vector, other.vector)

    def __xor__(self, other: "Vector") -> float:
        """
        Calculates and returns the angle (in radians) between this vector and another vector.
        If one of the vectors has zero magnitude, raises a ZeroDivisionError.

        Parameters:
        ----------
        other : Vector
            Another vector to calculate the angle with.

        Returns:
        -------
        float
            The angle between the two vectors in radians.

        Raises:
        ------
        ZeroDivisionError
            If one of the vectors has zero magnitude.
        """

        if (self.norm() * other.norm()) == 0:
            raise ZeroDivisionError

        return acos(np.dot(self.vector, other.vector) / (self.norm() * other.norm()))

    def norm(self, ord: int = 2) -> float:
        """
        Calculates and returns the norm (magnitude) of the vector. By default, this is the Euclidean norm (L2 norm).

        Parameters:
        ----------
        ord : int, optional
            The order of the norm (default is 2, which is the Euclidean norm).

        Returns:
        -------
        float
            The norm (magnitude) of the vector.
        """

        return float(np.linalg.norm(self.vector, ord=ord))


class Matrix:
    """
    A class to represent a mathematical matrix and provide basic matrix operations.

    Attributes:
    ----------
    matrix : np.ndarray
        The 2D array representing the matrix.

    Methods:
    -------
    __add__(other: "Matrix") -> "Matrix"
        Returns the result of matrix addition with another matrix.

    __matmul__(other: "Matrix") -> "Matrix"
        Returns the result of matrix multiplication with another matrix.

    T() -> "Matrix"
        Returns the transpose of the matrix.
    """

    def __init__(self, object):
        """
        Initializes the Matrix object with the given elements.

        Parameters:
        ----------
        object : iterable
            A 2D iterable (list of lists or array-like) to form the matrix.
        """

        self.matrix = np.array(object)  # Changed to np.array

    def __add__(self, other: "Matrix") -> "Matrix":
        """
        Adds the current matrix to another matrix.

        Parameters:
        ----------
        other : Matrix
            The matrix to be added.

        Returns:
        -------
        Matrix
            The resulting matrix after addition.
        """

        return Matrix(self.matrix + other.matrix)

    def __matmul__(self, other: "Matrix") -> "Matrix":
        """
        Multiplies the current matrix with another matrix.

        Parameters:
        ----------
        other : Matrix
            The matrix to multiply with.

        Returns:
        -------
        Matrix
            The resulting matrix after multiplication.
        """

        return Matrix(np.matmul(self.matrix, other.matrix))  # Changed to np.matmul

    def T(self) -> "Matrix":
        """
        Returns the transpose of the current matrix.

        Returns:
        -------
        Matrix
            The transposed matrix.
        """

        return Matrix(self.matrix.T)
