def matrix_addition(m1: list[list[float]], m2: list[list[float]]) -> list[list[float]]:
    """
    Adds two matrices element-wise.

    Args:
        m1 (list[list[float]]): The first matrix.
        m2 (list[list[float]]): The second matrix.

    Returns:
        list[list[float]]: The resulting matrix after element-wise addition.
    """
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(float(m1[i][j] + m2[i][j]))
        result.append(row)
    return result


def matrix_multiplication(
    m1: list[list[float]], m2: list[list[float]]
) -> list[list[float]]:
    """
    Multiplies two matrices.

    Args:
        m1 (list[list[float]]): The first matrix.
        m2 (list[list[float]]): The second matrix.

    Returns:
        list[list[float]]: The resulting matrix after multiplication.
    """
    result = []
    m2_transposed = list(zip(*m2))
    for i in m1:
        row = []
        for j in m2_transposed:
            total = 0.0
            for x, y in zip(i, j):
                total += x * y
            row.append(total)
        result.append(row)
    return result


def transpose_matrix(m: list[list[float]]) -> list[list[float]]:
    """
    Transposes a matrix.

    Args:
        m (list[list[float]]): The matrix to be transposed.

    Returns:
        list[list[float]]: The transposed matrix.
    """
    result = []
    for row in zip(*m):
        result.append(list(row))
    return result
