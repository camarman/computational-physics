# Bessel Function

from numpy import pi, sin, cos, linspace
from pylab import plot, show, xlabel, ylabel, title, grid, legend, xlim


def J(m, x, theta):
    '''inside of the Bessel function'''
    return cos(m * theta - x * sin(theta))


theta_initial = 0
theta_final = pi
N = 10**4  # step size
h = (theta_final - theta_initial) / N  # the distance between each slice


def Bessel(m, x):
    Sum_1 = 4 * sum([J(m, x, theta_initial + k * h)
                     for k in range(1, N, 2)])  # up to N-1
    Sum_2 = 2 * sum([J(m, x, theta_initial + k * h)
                     for k in range(2, N - 1, 2)])  # up to N-2
    return 1 / pi * (1/3 * h * (J(m, x, theta_initial) + J(m, x, theta_final) + Sum_1 + Sum_2))


J_values = []
for m in range(3):
    J_m = [Bessel(m, x) for x in range(21)]
    J_values.append(J_m)


x_values = linspace(0, 21, 21)
plot(x_values, J_values[0], "b-.", label="$J_0(x)$")
plot(x_values, J_values[1], "g-", label="$J_1(x)$")
plot(x_values, J_values[2], "r--", label="$J_2(x)$")
legend(loc="upper right")
xlabel("x")
ylabel("$J_m(x)$")
xlim(0, 10)
title("Bessel Function for m = 0, 1, 2")
grid(True)
show()
