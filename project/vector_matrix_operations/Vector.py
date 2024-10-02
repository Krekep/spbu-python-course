import numpy as np
from math import acos, sqrt
from typing import Iterable


class Vector:
    """
    A class to represent a mathematical vector and provide basic vector operations.

    Attributes:
    ----------
    vector : np.ndarray
        The array representing the vector.

    Methods:
    -------
    __array__()
        Allows the Vector object to be treated as a NumPy array directly.

    __getitem__(index: int) -> float
        Returns the element at the specified index.

    __len__() -> int
        Returns the length of the vector.

    __mul__(other: "Vector") -> float
        Returns the dot product of the current vector with another vector.

    __xor__(other: "Vector") -> float
        Returns the angle (in radians) between the current vector and another vector.

    norm() -> float
        Returns the norm (magnitude) of the vector.
    """

    def __init__(self, object: Iterable[float | int]):
        """
        Initializes the Vector object with the given elements.

        Parameters:
        ----------
        object : Iterable[float | int]
            An iterable of numbers to form the vector.
        """

        self.vector = np.array(object=object)

    def __array__(self):
        """
        Allows the Vector object to be treated as a NumPy array directly.

        Returns:
        -------
        np.ndarray
            The Vector object as a NumPy array.
        """
        return self.vector

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

        Raises:
        ------
        ValueError
            If vectors are not of the same length.
        """

        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must be of the same length.")

        return sum([x * y for x, y in zip(self.vector, other.vector)])

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
        ValueError
            If vectors are not of the same length.

        ZeroDivisionError
            If one of the vectors has zero magnitude.
        """
        if len(self.vector) != len(other.vector):
            raise ValueError("Vectors must be of the same length.")

        if (self.norm() * other.norm()) == 0:
            raise ZeroDivisionError("None of the vectors must have a zero magnitude")

        return acos((self * other) / (self.norm() * other.norm()))

    def norm(self) -> float:
        """
        Calculates and returns the norm (magnitude) of the vector. By default, this is the Euclidean norm (L2 norm).

        Returns:
        -------
        float
            The norm (magnitude) of the vector.
        """

        return sqrt(self * self)
