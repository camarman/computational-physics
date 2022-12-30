# Exercise 2.2 : Altitude of a satellite

from math import pi


G = 6.67e-11  # m^3/ kgs^2
M_earth = 5.97e24  # mass of the earth
R = 6371  # radius of the earth in km

T = float(input("Enter the period of the satellite: "))
h = ((G * M_earth * T ** 2) / (4 * pi**2))**(1 / 3) / 10 ** 3 - R  # in km
print("The altitude of the satellite is", "%0.2f" % h, "km")
