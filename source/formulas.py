# В данном файле определены основные математичекие операции, необходимые для проведения исследования

from math import sqrt, pi, exp
from random import randint, gauss
import numpy as np

from source.constants import M, I0, k, z, b, x1, aa, bb, x2  # Импортируем константы, определенные в файле constants


# Example
def pow_2(x):
    return x ** 2


# Возращает массив из N равномерно распределеных на интервале [0,M-1] точек
def make_ravn_dist(N):
    types_count = np.zeros(M)

    for i in range(N):
        type_number = randint(0, M - 1)
        types_count[type_number] += 1

    return types_count


# Возращает массив из N нормально распределеных на интервале [0,M-1] точек
def make_norm_dist(mean, diff, N):
    types_count = np.zeros(M)

    for i in range(N):
        curr_r = int(gauss(mean, diff))
        if 0 < curr_r < 100:
            types_count[int(curr_r)] += 1
        else:
            i -= 1

    return types_count


# Формула для вычисления первого дифракционного минимума
def func_of_Imin(x, q, N, e):
    return I0 * N * 1 * (1 / (2 * k * z)) ** 2 * (2 * b) ** 2 * q ** 4 * (
            (1 + 2 * e ** 2) - (2 * (1 + e) ** 2 * x1 / (q * x)) + (1 + e ** 2 / 3) * (x1 / (q * x)) ** 2)


# Формула для вычисления максимума
def func_of_Imax(x, q, N, e):
    return I0 * N * 1 * (q ** 2 / (2 * k * z)) ** 2 * (2 * aa / (q * x)) ** 2 * (
            1 + (e ** 2) / 3 + (1 + 2 * e ** 2) * bb * (q * x) ** 2 / aa - 2 * (
            1 + e ** 2) * bb * x2 * q * x / aa + (1 + (e ** 2) / 3) * x2 ** 2 * bb / aa)
