# The Lorenz Eqn

from numpy import array, arange
from pylab import plot, show, xlabel, ylabel

sigma, r, b = 10, 28, 8/3

t_i = 0
t_f = 50
N = 10000
h = (t_f - t_i) / N


def f(v, t):
    x = v[0]
    y = v[1]
    z = v[2]
    fx = sigma * (y - x)
    fy = r * x - y - x * z
    fz = x * y - b * z
    return array([fx, fy, fz], float)


tpoints = arange(t_i, t_f, h)
xpoints = []
ypoints = []
zpoints = []

v = array([0, 1, 0], float)  # initial conditions
for t in tpoints:
    xpoints.append(v[0])  # appending x component
    ypoints.append(v[1])  # appending y component
    zpoints.append(v[2])  # appending z component
    k1 = h * f(v, t)
    k2 = h * f(v + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(v + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(v + k3, t + h)
    v += 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)

plot(tpoints, ypoints, "r")
show()
plot(xpoints, zpoints)
show()
