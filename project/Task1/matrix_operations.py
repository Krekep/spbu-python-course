def matrix_add(matrix1, matrix2):
    """
    Add two matrices element-wise.

    Args:
        matrix1 (list): First matrix as list of lists.
        matrix2 (list): Second matrix as list of lists.

    Returns:
        list: Resulting matrix after addition.

    Raises:
        ValueError: If matrices have different dimensions.
    """
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")
    
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]


def matrix_multiply(matrix1, matrix2):
    """
    Multiply two matrices.

    Args:
        matrix1 (list): First matrix.
        matrix2 (list): Second matrix.

    Returns:
        list: Resulting matrix after multiplication.

    Raises:
        ValueError: If number of columns in first matrix doesn't match 
                   number of rows in second matrix.
    """
    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "Number of columns in first matrix must equal "
            "number of rows in second matrix"
        )
    
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for k in range(len(matrix2)):
            for j in range(len(matrix2[0])):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


def matrix_transpose(matrix):
    """
    Transpose a matrix (swap rows and columns).

    Args:
        matrix (list): Input matrix.

    Returns:
        list: Transposed matrix.
    """
    return [list(row) for row in zip(*matrix)]


class Matrix:
    """
    A class representing a mathematical matrix.
    
    Attributes:
        data (list): Matrix data as list of lists.
    """
    
    def __init__(self, data):
        """
        Initialize a matrix with given data.
        
        Args:
            data (list): Matrix data as list of lists.
            
        Raises:
            ValueError: If rows have inconsistent lengths.
        """
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same length")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
    
    def add(self, other):
        """
        Add another matrix to this matrix.
        
        Args:
            other (Matrix): Another matrix.
            
        Returns:
            Matrix: Result of addition.
        """
        return Matrix(matrix_add(self.data, other.data))
    
    def multiply(self, other):
        """
        Multiply with another matrix.
        
        Args:
            other (Matrix): Another matrix.
            
        Returns:
            Matrix: Result of multiplication.
        """
        return Matrix(matrix_multiply(self.data, other.data))
    
    def transpose(self):
        """
        Transpose the matrix.
        
        Returns:
            Matrix: Transposed matrix.
        """
        return Matrix(matrix_transpose(self.data))
    
    def __repr__(self):
        return f"Matrix({self.data})"
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return self.data == other.data