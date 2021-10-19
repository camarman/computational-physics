# The lotka-Volterra Eqns

from numpy import array, arange
from pylab import plot, show, xlabel, ylabel

alpha, beta, gamma, delta = 1, 0.5, 0.5, 2

t_i = 0
t_f = 30
N = 200
h = (t_f - t_i) / N


def f(r, t):
    x = r[0]
    y = r[1]
    fx = alpha * x - beta * x * y
    fy = gamma * x * y - delta * y
    return array([fx, fy], float)


tpoints = arange(t_i, t_f, h)
ypoints = []
xpoints = []

r = array([2, 2], float)  # initial condition
for t in tpoints:
    xpoints.append(r[0])  # appending x component
    ypoints.append(r[1])  # appending y component
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)

plot(tpoints, xpoints, "g-.")
plot(tpoints, ypoints, "r--")
xlabel("time")
ylabel("Number of animals (x10^3)")
show()
