# Second order RK method

from math import sin
from numpy import arange
from pylab import plot, show

x = 0       # initial conditions
t_i = 0     # initial time
t_f = 10    # final time
N = 100     # step size
h = (t_f - t_i) / N


def f(x, t):
    return -x**3 + sin(t)


t_points = arange(t_i, t_f, h)
x_points = []

for t in t_points:
    x_points.append(x)
    k1 = h * f(x, t)
    k2 = h * f(x + 0.5 * k1, t + 0.5 * h)
    x += k2

plot(t_points, x_points)
show()
