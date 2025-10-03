import math


def scalar(a: list, b: list) -> float:
    """
    Вычисляет скалярное произведение двух векторов.

    Args:
        a: Первый вектор (список чисел)
        b: Второй вектор (список чисел)

    Returns:
        Скалярное произведение векторов

    Raises:
        ValueError: Если векторы разной длины
    """
    if len(a) != len(b):
        raise ValueError("Векторы должны иметь одинаковую размерность")
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


def normal(a: list) -> float:
    """
    Вычисляет длину (норму) вектора.

    Args:
        a: Входной вектор (список чисел)

    Returns:
        Длина вектора
    """
    return math.sqrt(sum(x * x for x in a))


def angle(a: list, b: list) -> float:
    """
    Вычисляет угол между двумя векторами в градусах.

    Args:
        a: Первый вектор (список чисел)
        b: Второй вектор (список чисел)

    Returns:
        Угол между векторами в градусах

    Raises:
        ValueError: Если один из векторов нулевой
    """
    if normal(a) == 0 or normal(b) == 0:
        raise ValueError("Нулевой вектор использовать нельзя")
    cos_angle = scalar(a, b) / (normal(a) * normal(b))
    if -1 > cos_angle:
        cos_angle = 1
    if 1 < cos_angle:
        cos_angle = -1
    rad_angle = math.acos(cos_angle)
    angle_deg = rad_angle * (180 / (math.pi))
    return angle_deg


def trans(M: list) -> list:
    """
    Транспонирует матрицу.

    Args:
        M: Исходная матрица (список списков чисел)

    Returns:
        Транспонированная матрица
    """
    row = len(M)  # элементы в первом столбце
    stri = len(M[0])  # элементы в первой строке
    trans_matrix = []
    for i in range(stri):
        new_row = []  # новый столбец новой матрицы
        for j in range(row):
            new_row.append(M[j][i])
        trans_matrix.append(new_row)
    return trans_matrix


def multiplication(M: list, N: list) -> list:
    """
    Умножает две матрицы.

    Args:
        M: Первая матрица (список спиков чисел)
        N: Вторая матрица (список списков чисел)

    Returns:
        Результат умножения матриц

    Raises:
        ValueError: Если матрицы нельзя умножить
    """
    if len(M[0]) != len(N):
        raise ValueError("Несовместимые размеры матриц")
    row_M = len(M)  # строк в M
    stri_M = len(M[0])  # столбцов в M (и строк в N)
    stri_N = len(N[0])  # столбцов в N
    multi = []  # Создаем результирующую матрицу rows_M × cols_N
    for i in range(row_M):
        new_row = []
        for j in range(stri_N):
            sum_val = 0
            for k in range(stri_M):
                sum_val += M[i][k] * N[k][j]
            new_row.append(sum_val)
        multi.append(new_row)
    return multi


def summa(M: list, N: list) -> list:
    """
    Складывает две матрицы.

    Args:
        M: Первая матрица (список списков чисел)
        N: Вторая матрица (список списков чисел)

    Returns:
        Сумма матриц

    Raises:
        ValueError: Если матрицы имеют разные размеры
    """
    if len(M) != len(N) or len(M[0]) != len(N[0]):
        raise ValueError("Матрицы должны иметь одинаковую размерность")
    row = len(M)  # элементы в первом столбце
    stri = len(M[0])  # элементы в первой строке
    suma = []
    for i in range(stri):
        new_stri = []
        for j in range(row):
            k = M[i][j] + N[i][j]
            new_stri.append(k)
        suma.append(new_stri)
    return suma


ALGEBRA_OPERATIONS = ["scalar", "normal", "angle", "trans", "multiplication", "summa"]
