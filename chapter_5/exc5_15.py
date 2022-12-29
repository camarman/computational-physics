# Central difference derivative for sample points

from numpy import linspace, tanh, cosh
from pylab import plot, show

h = 10**-5
x_initial = -2
x_final = 2

x = linspace(x_initial, x_final, int((x_final - x_initial) / h), endpoint=True)
y = 1 + 0.5 * tanh(2 * x)

analytic_equation = 1 / cosh(2 * x)**2

derivative = []
for i in range(1, len(x) - 1):
    derivative.append((y[i+1] - y[i-1]) / (2 * h))

plot(x, analytic_equation, "go")
plot(x[1:-1], derivative, "b--")

show()
