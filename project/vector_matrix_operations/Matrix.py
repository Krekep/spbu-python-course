import numpy as np


class Matrix:
    """
    A class to represent a mathematical matrix and provide basic matrix operations.

    Attributes:
    ----------
    matrix : np.ndarray
        The 2D array representing the matrix.

    Methods:
    -------
    __array__(self)
        Allows the Matrix object to be treated as a NumPy array directly.

    __repr__(self) -> str
        Provides a detailed string representation of the Matrix object for debugging.

    __str__(self) -> str
        Provides a clean, user-friendly string representation of the Matrix.

    __getitem__(self, indices: tuple) -> float
        Allows access to matrix elements using mat[i, j].

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

        self.matrix = np.array(object)

    def __array__(self):
        """
        Allows the Matrix object to be treated as a NumPy array directly.

        Returns:
        -------
        np.ndarray
            The Matrix object as a NumPy array.
        """
        return self.matrix

    def __repr__(self) -> str:
        """
        Provides a detailed string representation of the Matrix object for debugging.

        Returns:
        -------
        string
            The string representation for debugging.
        """

        return f"Matrix({self.matrix.tolist()})"

    def __str__(self) -> str:
        """
        Provides a clean, user-friendly string representation of the Matrix.

        Returns:
        -------
        string
            The string representation.
        """

        return str(self.matrix)

    def __getitem__(self, indices: tuple) -> float:
        """
        Allows access to matrix elements using mat[i, j].

        Parameters:
        ----------
        indices : tuple
            A tuple representing the indices (i, j) to access the matrix.

        Returns:
        -------
        float
            The value at the specified index.
        """
        return self.matrix[indices]

    @property
    def data(self):
        """
        Provides access to the underlying matrix without directly exposing matrix.
        """
        return self.matrix

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

        Raises:
        ------
        ValueError
            If matrices are not of the same shape.
        """

        if self.matrix.shape != other.matrix.shape:
            raise ValueError("Matrices must be of the same shape")

        res = np.zeros(shape=self.matrix.shape)
        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):
                res[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return Matrix(res)

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

        Raises:
        ------
        ValueError
            If the matrix shapes are not compatible for multiplication
        """

        if self.matrix.shape[1] != other.matrix.shape[0]:
            raise ValueError("Matrix shapes are not compatible for multiplication")

        res = np.zeros(shape=(self.matrix.shape[0], other.matrix.shape[1]))

        for i in range(self.matrix.shape[0]):
            for j in range(other.matrix.shape[1]):
                res[i][j] = sum(
                    [
                        self.matrix[i][k] * other.matrix[k][j]
                        for k in range(self.matrix.shape[1])
                    ]
                )

        return Matrix(res)

    def T(self) -> "Matrix":
        """
        Returns the transpose of the current matrix.

        Returns:
        -------
        Matrix
            The transposed matrix.
        """
        res = np.zeros(shape=(self.matrix.shape[1], self.matrix.shape[0]))
        for i in range(self.matrix.shape[1]):
            for j in range(self.matrix.shape[0]):
                res[i][j] = self.matrix[j][i]

        return Matrix(res)
