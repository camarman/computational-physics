# Relativistic travel time calculator for a distant planet

from math import sqrt

c = 1  # since we are tkaing v as a fraction of c

x_0 = float(input("Enter the distance to a planet in light years: "))
v = float(input("Enter the speed of the spaceship as a fraction of c: "))


t_0 = x_0 / v  # units in year
gamma = 1 / sqrt(1 - (v/c)**2)

t = gamma * (t_0 - (v * x_0 / c**2))  # lorentz transformation for time

print("Time it takes to an observer on Earth:", "%0.3f" % t_0, " years")
print("Time it takes to an observer on spaceship:", "%0.3f" % t, "years")
