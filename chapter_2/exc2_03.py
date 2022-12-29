# Cartesian to polar coordinate transformation

from math import sqrt, atan, pi

x, y = (input("Enter the coordinates in the form of x,y: ")).split(",")
x, y = float(x), float(y)
r = sqrt(x ** 2 + y ** 2)
tangent_theta = y / x
theta = atan(tangent_theta) * 180 / pi
print("r:", "%0.3f" % r, "theta:", "%0.3f" % theta)
