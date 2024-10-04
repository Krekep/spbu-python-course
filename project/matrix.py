class Matrix:
    def __init__(self, data):
        self.data = data

    def add(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrices must have the same dimensions for addition.")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]
        return Matrix(result)

    def multiply(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError(
                "Number of columns in the first matrix must be equal to the number of rows in the second matrix."
            )
        result = [
            [
                sum(
                    self.data[i][k] * other.data[k][j] for k in range(len(self.data[0]))
                )
                for j in range(len(other.data[0]))
            ]
            for i in range(len(self.data))
        ]
        return Matrix(result)

    def transpose(self):
        result = [
            [self.data[j][i] for j in range(len(self.data))]
            for i in range(len(self.data[0]))
        ]
        return Matrix(result)
