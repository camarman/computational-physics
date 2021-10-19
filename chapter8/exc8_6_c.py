# harmonic and anharmoic oscillator

from numpy import arange, array
from pylab import plot, show, xlabel, ylabel, title

omega = 1
t_i = 0
t_f = 100
N = 1000
h = (t_f - t_i) / N


def f(r, t):
    x = r[0]  # dx/dt = k
    k = r[1]  # dk/dt = -w^2x
    fx = k
    fk = -omega**2 * x**3
    return array([fx, fk], float)


tpoints = arange(t_i, t_f, h)
x_points = []
k_points = []

r = array([0.5, 0], float)

for t in tpoints:
    x_points.append(r[0])
    k_points.append(r[1])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)

plot(x_points, k_points)
xlabel("x")
ylabel("dx/dt")
title("Phase space of an anharmonic oscillator")
show()
