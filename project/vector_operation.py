import math


def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))


def vector_length(c):
    return math.sqrt(dot_product(c, c))


def angle_between_vectors(a, b):
    try:
        len_a = vector_length(a)
        len_b = vector_length(b)
        print(f"Длина векторов: a={len_a}, b={len_b}")

        cos_theta = dot_product(a, b) / (len_a * len_b)
        cos_theta = max(-1, min(1, cos_theta))
        angle = math.acos(cos_theta)
        print(f"Косинус угла: {cos_theta}, угол (в радианах): {angle}")
        return angle
    except ZeroDivisionError:
        raise ValueError("Один из векторов является нулевым")
