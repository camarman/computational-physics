# Quantum step potential

from math import sqrt

m = 9.11e-31  # mass of electron in kg
h_bar = 1.054e-34

E = float(input("Enter the kinetic energy in eV: "))  # eV
V = float(input("Enter the potential in eV: "))  # eV

k_1 = sqrt(2 * m * E) / h_bar
k_2 = sqrt(2 * m * (E - V)) / h_bar

T = 4 * k_1 * k_2 / (k_1 + k_2) ** 2
R = (k_1 - k_2) ** 2 / (k_1 + k_2) ** 2

print("Transmission probability :", "%0.3f" % T)
print("Reflection probability:", "%0.3f" % R)
