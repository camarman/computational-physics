# nonlinear pendulum
# not sure that code works properly

from numpy import arange, array
from math import sin
from pylab import plot, show, xlabel, ylabel, title

l = 0.1  # in m, length of the pendulum
g = 9.81  # m/s^2

t_i = 0
t_f = 100
N = 1000
h = (t_f - t_i) / N


def f(r, t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = (-g / l) * sin(theta)
    return array([ftheta, fomega], float)


tpoints = arange(t_i, t_f, h)
theta_points = []

r = array([179, 0], float)

for t in tpoints:
    theta_points.append(r[0])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)

plot(tpoints, theta_points)
xlabel("Time (t)")
ylabel("$\theta$")
title("Nonlinear Pendulum")
show()
