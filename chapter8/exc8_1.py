# Low pass filter

from numpy import arange
from math import floor
from pylab import plot, show, xlabel, ylabel

Vout = 0  # inital condition
t_i = 0  # initial time
t_f = 10  # final time
N = 100000
h = (t_f - t_i) / N

RC_values = [0.01, 0.1, 1]


def f(Vout, t):
    if floor(2 * t) % 2 == 0:
        return (1 - Vout) / RC
    else:
        return (-1 - Vout) / RC


t_points = arange(t_i, t_f, h)
Vout_points = []

for RC in RC_values:
    for t in t_points:
        Vout_points.append(Vout)
        k1 = h * f(Vout, t)
        k2 = h * f(Vout + 0.5 * k1, t + 0.5 * h)
        k3 = h * f(Vout + 0.5 * k2, t + 0.5 * h)
        k4 = h * f(Vout + k3, t + h)
        Vout += 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
    plot(t_points, Vout_points, "go")
    xlabel("Time (t)")
    ylabel("$V_{out}")
    Vout_points = []
    show()
