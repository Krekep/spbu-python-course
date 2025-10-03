import math


def scalar(a, b):  # скалярное произведение
    if len(a) != len(b):
        raise ValueError("Векторы должны иметь одинаковую размерность")
    for i in range(len(a)):
            scalar = a[i]*b[i]
    return scalar


def normal(a):  # длина
    return len(a)


def angle(a, b):  # угол между векторами
    if normal(a) == 0 or normal(b) == 0:
        raise ValueError("Нулевой вектор использовать нельзя")
    cos_angle = scalar(a, b) / (normal(a) * normal(b))
    if -1 > cos_angle:
        cos_angle = 1
    if 1 < cos_angle:
        cos_angle = -1
    rad_angle = math.acos(cos_angle)
    angle_deg = rad_angle*(180/(math.pi))
    return angle_deg


def trans(M): # транспонирование
    row = len(M) # элементы в первом столбце
    stri = len(M[0]) # элементы в первой строке 
    trans_matrix = []
    for i in range(stri):
        new_row = [] # новый столбец новой матрицы
        for j in range(row):
            new_row.append(M[j][i])
        trans_matrix.append(new_row)
    return trans_matrix


def multiplication(M, N):  # умножение матриц
    if len(M) != len(N) or len(M[0]) != len(N[0]):
        raise ValueError("Матрицы должны иметь одинаковую размерность")
    row_M = len(M)      # строк в M
    stri_M = len(M[0])   # столбцов в M (и строк в N)
    stri_N = len(N[0])   # столбцов в N
    multi = [] # Создаем результирующую матрицу rows_M × cols_N
    for i in range(row_M):
        new_row = []
        for j in range(stri_N):
            sum = 0   # Вычисляем элемент [i][j]
            for k in range(stri_M):
                sum += M[i][k] * N[k][j]
            new_row.append(sum)
        result.append(new_row)  
    return result


def summa(M, N):  # сложение
    if len(M) != len(N) or len(M[0]) != len(N[0]):
        raise ValueError("Матрицы должны иметь одинаковую размерность")
    row = len(M) # элементы в первом столбце
    stri = len(M[0]) # элементы в первой строке
    suma = []
    for i in range(stri):
        new_stri = []
        for j in range(row):
            k = M[i][j] + N[i][j]
            new_stri.append(k)
        suma.append(new_stri)    
    return suma


ALGEBRA_OPERATIONS = ["scalar", "normal", "angle", "trans", "multiplication", "summa"]
