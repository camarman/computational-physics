from pylab import plot, show, xlabel, ylabel, title, grid
from numpy import linspace, exp


def E(x):
    '''the function'''
    return exp(-x ** 2)


def simpsons_rule(a, b, N):
    h = 0.1
    S1 = 4 * sum([E(a + (2 * i - 1)*h) for i in range(1, N//2 + 1)])
    S2 = 2 * sum([E(a + (2 * i * h)) for i in range(1, N//2)])
    return 1/3 * h * (E(a) + E(b) + S1 + S2)

print(simpsons_rule(0, 3, 100))  # the integral value from 0 to 3

x_values = linspace(-10, 10, 100)
y_values = list(map(E, x_values))
plot(x_values, y_values)
xlabel("x")
ylabel("E(x)")
title("E(x) vs x")
grid(True)
show()
