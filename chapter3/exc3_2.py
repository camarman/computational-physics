from pylab import plot, show, loadtxt, xlabel, ylabel, title
from numpy import sin, cos, array, pi, linspace, exp

# deltoid curve
theta = linspace(0, 2 * pi, 100)
x = 2 * cos(theta) + cos(2 * theta)
y = 2 * sin(theta) - sin(2 * theta)
plot(x, y, "g-")
show()

# Galilean spiral
theta = linspace(0, 10 * pi, 1000)
r = theta * theta
x = r * cos(theta)
y = r * sin(theta)
plot(x, y)
show()

# Fey’s function
theta = linspace(0, 24 * pi, 1000)
r = exp(cos(theta)) - 2 * cos(4 * theta) + (sin(theta / 12)) ** 5
x = r * cos(theta)
y = r * sin(theta)
plot(x, y)
show()
