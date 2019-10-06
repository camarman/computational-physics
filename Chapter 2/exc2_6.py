from math import sqrt, pi

l_1 = float(input("Enter the distance of perihelion: "))
v_1 = float(input("Enter the velocity of the object at the perhelion: "))

G = 6.6738e-11  # m^3/kgs^2
M = 1.9891e30  # mass of the sun in kg


def eqn_solver(l_1, v_1):
    '''takes input as y and returns the larger root of the ax^2 + bx + c = 0'''
    a = 1
    b = - (2 * G * M / v_1 * l_1)
    c = - v_1 ** 2 + (2 * G * M / l_1)
    delta = sqrt(b**2 - 4*a*c)
    root_1 = (-b - delta) / (2 * a)
    root_2 = (-b + delta) / (2 * a)
    return max(root_1, root_2)


l_2 = l_1 * v_1 / eqn_solver(l_1, v_1)

a = 1/2 * (l_1 + l_2)  # semi-major axis of ellipse
b = sqrt(l_1 * l_2)  # semi-minor axis

T = 3.17098e-8 * (2 * pi * a * b) / (l_1 * v_1)  # orbital period in years
e = (l_2 - l_1) / (l_2 + l_1)  # orbital eccentricity

print("Orbital period of the object is", "%0.4f" % T)
print("eccentricity:", "%0.4f" % e)
