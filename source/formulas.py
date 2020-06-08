# Here you can write your functions formulas

from math import sqrt, pi, exp, fabs
import numpy as np

# константы:
I0 = 1
k=2*3.14*1000000/0.633
z=0.1
b=0.4
#q=k*R
#e=dR
x1=3.82
aa=0.346
bb=0.4
x2=5.32

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
    I = I_zero*N*a**2*(1/(2*k*z))**2*(2*b)**2*ro**4 *in_module
    return I


def strange_func_of_Imin (x, q, N, e):
    return I0*N*1*(1/(2*k*z))**2*(2*b)**2*q**4*((1+2*e**2)-(2*(1+e)**2*x1/(q*x)) + (1 + e**2/3)*(x1/(q*x))**2)



# A1=x1/q
# Imin11 = I0*N*1*(1/(2*k*z)**2*(2*b)**2*q**4*((1+2*e**2)-(2*(1+e)**2*x1/(q*A1)) + (1 + e**2/3)*(x1/(q*A1))**2) #общий вид мин
# #считаем нужное число


# Общий вид макс
# def first_difr_max():
#     Imax = I0*N*1*(q**2/(2*k*z))**2*(2*aa/(q*x))**2*(1+(e**2)/3+(1+2*e**2)*bb*(q*x)**2/aa-2*(1+e**2)*bb*x2*q*x/aa+(1+(e**2)/3)*x2**2*bb/aa)
#     return Imax

# A2=x2/q
# #нужное число
# Imax11 = I0*N*1*(q**2/(2*k*z))**2*(2*aa/(q*A2))**2*(1+(e**2)/3+(1+2*e**2)*bb*(q*A2)**2/aa-2*(1+e**2)*bb*x2*q*A2/aa+(1+(e**2)/3)*x2**2*bb/aa)

# #пробежать е от 0 до 0,3
# vid = (Imax11-Imin11)/(Imax11+Imin11)
# vid1 = 1-2*(e**2)*(b*x2)**2/(3*aa**2)
# vid2 = 1-8*(b*e)**2/3