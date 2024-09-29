def get_row_matrix(A=()):
    return len(A)


def get_cols_matrix(A=()):
    t = get_row_matrix(A)
    return len(A[0]) if t > 0 else 0


def sum_matrix(A=(), B=()):
    row_a = get_row_matrix(A)
    cols_a = get_cols_matrix(A)

    row_b = get_row_matrix(B)
    cols_b = get_cols_matrix(B)

    if (row_a != row_b) or (cols_a != cols_b):
        print('ERROR SIZE')
        return -1
    else:
        res = [[0] * cols_a for _ in range(row_a)]
        for i in range(row_a):
            for j in range(cols_a):
                res[i][j] = A[i][j] + B[i][j]
        return res


def product_matrix(A=(), B=()):
    row_a = get_row_matrix(A)
    cols_a = get_cols_matrix(A)

    row_b = get_row_matrix(B)
    cols_b = get_cols_matrix(B)

    if (cols_a != row_b):
        print('ERROR SIZE')
        return -1

    res = [[0] * cols_b for _ in range(row_a)]

    for i in range(row_a):
        for j in range(cols_b):
            for k in range(cols_a):
                res[i][j] += A[i][k] * B[k][j]
    return res


def transponir_matrix(A=()):
    row = get_row_matrix(A)
    cols = get_cols_matrix(A)

    res = [[0] * row for _ in range(cols)]

    for i in range(row):
        for j in range(cols):
            res[j][i] = A[i][j]
    return res
