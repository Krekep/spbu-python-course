import math

def scalar_product(len_a, len_b, angle):
    return abs(len_a) * abs(len_b) * angle


def length_vec(A=(0, 0, 0), B=(0, 0, 0)):
    return math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2 + (B[2] - A[2]) ** 2)


def cos_AB(A=(0, 0, 0), B=(0, 0, 0)):
    chisl = (A[0] *  B[0]) + (A[1] *  B[1]) + (A[2] *  B[2])
    zn = int(math.sqrt(A[0]**2 + A[1]**2 + A[2]**2) * math.sqrt(B[0]**2 + B[1]**2 + B[2]**2))
    return chisl / zn
