# Trapezoidal rule until desired accuracy is reached

from math import sin, sqrt


def f(x):
    '''the function'''
    return sin(10 * sqrt(x))**2


def trapezoidal(a, b, N):
    h = (b - a) / N
    return h * ((0.5 * (f(a) + f(b))) + sum([f(a + i * h) for i in range(1, N)]))


N = 1  # step size
error = 1

while error > 10**-6:  # putting desired accuracy as 10^-6
    I_1 = trapezoidal(0, 1, N)
    N *= 2
    I_2 = trapezoidal(0, 1, N)
    error = abs(1/3 * (I_2 - I_1))
    print("the integral is", I_2, "\n the error is", error)
