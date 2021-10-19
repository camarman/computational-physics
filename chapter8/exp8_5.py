# Diff Eqn with more than one variable

from numpy import array, arange
from math import sin
from pylab import plot, show

t_i = 0
t_f = 10
w = 1
x = y = 1  # initial conditions
N = 100
h = (t_f - t_i) / N


def f(r, t):
    x = r[0]
    y = r[1]
    fx = x * y - x
    fy = y - x * y + sin(w * t)**2
    return array([fx, fy], float)


tpoints = arange(t_i, t_f, h)
xpoints = []
ypoints = []

r = array([1, 1], float)

for t in tpoints:
    xpoints.append(r[0])  # appending x component
    ypoints.append(r[1])  # appending y component
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)

plot(tpoints, xpoints)
plot(tpoints, ypoints)
show()
