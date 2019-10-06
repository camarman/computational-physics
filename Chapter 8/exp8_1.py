# Eulers method

from math import sin
from numpy import arange
from pylab import plot, show, xlabel, ylabel

x = 0  # inital conditions
t_i = 0  # initial time
t_f = 10  # final time
N = 1000  # step size
h = (t_f - t_i) / N


def f(x, t):
    return -x**3 + sin(t)


t_data = arange(t_i, t_f, h)
x_data = []

for t in t_data:
    x_data.append(x)
    x += h * f(x, t)

plot(t_data, x_data)
xlabel("t")
ylabel("x(t)")
show()
