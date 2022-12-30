# Differential equation with more than one variable

from numpy import array, arange, sin
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


t_points = arange(t_i, t_f, h)
x_points = []
y_points = []

r = array([1, 1], float)

for t in t_points:
    x_points.append(r[0])  # appending x component
    y_points.append(r[1])  # appending y component
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)

plot(t_points, x_points)
plot(t_points, y_points)
show()
