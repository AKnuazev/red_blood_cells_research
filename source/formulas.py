# Here you can write your functions formulas

from math import sqrt, pi, exp, fabs


# Example
def pow_2(x):
    return x ** 2


# Нормальное распределение
def norm_dist(sygma_r, j):
    M = 100  # По условию M=100
    r = 2 * sqrt(3) * sygma_r / M
    return (1 / (sygma_r * sqrt(2 * pi))) * exp(-1 * ((r * j) ** 2) / (2 * sygma_r ** 2))


# Формула для вычисления первого дифракционного минимума
def first_difr_min(teta, ro, N, epsilon):  # TODO ro = k*r
    I_zero = 1
    a = 1           # alpha
    k = 9.92*10**6
    z = 0.1
    b = 0.4         # beta
    e = epsilon     # epsilon
    x1 = 3.82

    in_module = (1+2*e**2)-2*(1+e**2)*(x1/(ro*teta))+(1+(e**2/3)*(x1**2/(ro*teta)**2))
    I = I_zero*N*a**2*(1/(2*k*z))**2*(2*b)**2*ro**4 * (in_module)