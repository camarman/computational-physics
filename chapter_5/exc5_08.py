# Simpsons rule until desired accuracy reached

from math import sin, sqrt


def f(x):
    '''the function'''
    return sin(10 * sqrt(x))**2


def simpsons_rule(a, b, N):
    h = (b - a) / N
    S1 = 4 * sum([f(a + (2 * i - 1)*h) for i in range(1, N//2 + 1)])
    S2 = 2 * sum([f(a + (2 * i * h)) for i in range(1, N//2)])
    return 1/3 * h * (f(a) + f(b) + S1 + S2)


N = 2  # step size
error = 1

while error > 10**-6:  # putting desired accuracy as 10^-6
    I_1 = simpsons_rule(0, 1, N)
    N *= 2
    I_2 = simpsons_rule(0, 1, N)
    error = abs(1/15 * (I_2 - I_1))
    print("the integral is", I_2, "\n the error is", error)
