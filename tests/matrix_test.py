from project.matrix_operations import matrix_multiply, matrix_sum, matrix_transpose

def test_matrix_multiply():
    mat1 = [[5, 5], [9, 1]]
    mat2 = [[3, 4], [8, 2]]
    assert matrix_multiply(mat1, mat2) == [[55, 30], [35, 38]]

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[0, 0], [0, 0]]
    assert matrix_multiply(mat1, mat2) == [[0, 0], [0, 0]]

    mat1 = [[12, 54, 77, 3], [5, 0, 46, 52]]
    mat2 = [[32, 11], [90, 2], [45, 18], [13, 87]]
    assert matrix_multiply(mat1, mat2) == [[8748, 1887], [2906, 5407]]

def test_matrix_sum():
    mat1 = [[4, 2, 7], [8, 7, 9], [0, 4, 5]]
    mat2 = [[13, 6, 8], [32, 55, 0], [4, 21, 5]]
    assert matrix_sum(mat1, mat2) == [[17, 8, 15], [40, 62, 9], [4, 25, 10]]

    mat1 = [[9, 8], [4, 5]]
    mat2 = [[-5, 0], [6, -15]]
    assert matrix_sum(mat1, mat2) == [[4, 8], [10, -10]]

def test_matrix_transpose():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert matrix_transpose(mat) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    mat = [[11, 5], [97, 43], [1, 0]]
    assert matrix_transpose(mat) == [[11, 97, 1], [5, 43, 0]]
    