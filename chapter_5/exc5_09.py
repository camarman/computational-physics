from gaussxw import gaussxw
from numpy import linspace, exp
from pylab import plot, show, xlabel, ylabel, title, grid


N = 50  # step size
V = 10 ** -3  # m^3 #volume of the box
rho = 6.022 * 10**28  # m^-3 # number density of the atoms
debye_temp = 428  # K
boltzmann_cons = 1.38064852 * 10**-23  # the Boltzmann constant


def f(x):
    return (x**4 * exp(x)) / (exp(x) - 1)**2


def gaussian(a, b):
    x, w = gaussxw(N)
    xp = 0.5 * (b - a) * x + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w
    s = 0
    for k in range(N):
        s += wp[k] * f(xp[k])
    return s


def cv(T):
    return 9 * V * boltzmann_cons * rho * (T / debye_temp)**3 * gaussian(0, debye_temp / T)


x = linspace(5, 500, endpoint=True)
y = cv(x)

plot(x, y)
xlabel("Temperature (K)")
ylabel("Heat capacity of a solid (J / K)")
grid(True)
title("C_v vs K")
show()
