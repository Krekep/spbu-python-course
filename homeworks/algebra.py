import numpy as np

def Scalar(a, b): #скалярное произведение
    if a.shape != b.shape:
        raise ValueError("Векторы должны иметь одинаковую размерность")
    return np.dot(a, b)

def Normal(a):  #длина
    return len(a)

def Angle(a, b): # угол между векторами
    if Normal(a) == 0 or Normal(b) == 0:
        raise ValueError("Нулевой вектор использовать нельзя")
    cos_angle = Scalar(a, b) / (Normal(a) * Normal(b))
    protected_cos = np.clip(cos_angle, -1, 1)
    angle_rad = np.arccos(protected_cos)
    angle_deg = np.degrees(angle_rad)
    return angle_deg

def Trans(M): # транспонирование
    return M.T
  
def Multiplication(M, N): # умножение матриц
    if N.shape != B.shape:
        raise ValueError("Матрицы должны иметь одинаковую размерность")
    return np.dot(M, N)

def Summa(M, N): # сложение
    if N.shape != B.shape:
        raise ValueError("Матрицы должны иметь одинаковую размерность")
    return M + N

ALGEBRA_OPERATIONS = ['Scalar','Normal','Angle','Trans','Multiplication','Summa']
