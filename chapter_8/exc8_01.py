# Low pass filter

from numpy import arange, floor
from pylab import plot, show, xlabel, ylabel


V_out = 0  # initial condition
t_i = 0    # initial time
t_f = 10   # final time
N = 100000
h = (t_f - t_i) / N

RC_values = [0.01, 0.1, 1]


def f(V_out, t):
    if floor(2 * t) % 2 == 0:
        return (1 - V_out) / RC
    else:
        return (-1 - V_out) / RC

t_points = arange(t_i, t_f, h)
V_out_points = []

for RC in RC_values:
    for t in t_points:
        V_out_points.append(V_out)
        k1 = h * f(V_out, t)
        k2 = h * f(V_out + 0.5 * k1, t + 0.5 * h)
        k3 = h * f(V_out + 0.5 * k2, t + 0.5 * h)
        k4 = h * f(V_out + k3, t + h)
        V_out += 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
    plot(t_points, V_out_points, "go")
    xlabel("Time (t)")
    ylabel("$V_{out}")
    V_out_points = []
    show()
