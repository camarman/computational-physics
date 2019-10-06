# 2 body problem

from math import sqrt
from numpy import arange, array
from pylab import plot, show, xlabel, ylabel, legend, grid, title
from time import perf_counter

start = perf_counter()

G = 6.6738 * 10 ** -11   # m^3kg^-1s^-2

dt = 3600  # time - step
time_range = arange(0, 20 * 365 * 24 * 3600, dt)


m1 = 1.9891 * 10 ** 25  # mass of the object-1
r1 = array([1, 1])  # position vector of the m2 (m) #I set to values (1,1) otherwise the energy calculations give inf
v1 = array([0, 10000])  # velocity vector of the m2 (m/s)

m2 = 1.9891 * 10 ** 25  # mass of the object-2
r2 = array([740.52 * 10**6, 0])  # position vector of the m1 (m)
v2 = array([0, -10000])  # velocity vector of the m1 (m/s)


def f_m1(r1, r2, t):
    '''The force that acts on the m1'''
    dist = (sum([i**2 for i in r1 - r2]))**(3/2)
    return (- G * m2 * (r1 - r2)) / dist


def f_m2(r1, r2, t):
    '''The force that acts on the m2'''
    dist = (sum([i**2 for i in r2 - r1]))**(3/2)
    return (- G * m1 * (r2 - r1)) / dist


R_x1 = []  # x component of the position vector of the m1
R_y1 = []  # y component of the position vector of the m1
R_x2 = []  # x component of the position vector of the m2
R_y2 = []  # y component of the position vector of the m2
V1 = []  # storing velocity values of the m1
V2 = []  # storing velocity values of the m1

U1_data = []  # storing potential energy of m1
T1_data = []  # storing kinetic energy of m1
E1_data = []  # stroing total energy of m1

U2_data = []  # storing potential energy of m2
T2_data = []  # storing kinetic energy of m2
E2_data = []  # stroing total energy of m2


def energy(r1, v1, r2, v2):
    '''calculates the energy for a given object '''
    U1 = (-G * m1 * m2) / (r1[0]**2 + r1[1]**2)**(1/2)  # potential energy
    T1 = 0.5 * m1 * (v1[0]**2 + v1[1]**2)  # kinetic energy
    E1 = U1 + T1  # total energy
    U2 = (-G * m1 * m2) / (r2[0]**2 + r2[1]**2)**(1/2)  # potential energy
    T2 = 0.5 * m2 * (v2[0]**2 + v2[1]**2)  # kinetic energy
    E2 = U2 + T2  # total energy
    U1_data.append(U1)
    T1_data.append(T1)
    E1_data.append(E1)
    U2_data.append(U2)
    T2_data.append(T2)
    E2_data.append(E2)
    return None


def avg(xarray):
    return sum(xarray) / len(xarray)


for t in time_range:
    W = energy(r1, v1, r2, v2)
    v1_half, v2_half = v1 + 0.5 * dt * \
        f_m1(r1, r2, t),  v2 + 0.5 * dt * f_m2(r1, r2, t)
    r1_next, r2_next = r1 + dt * v1_half,  r2 + dt * v2_half
    k1, k2 = dt * f_m1(r1_next, r2_next, t + dt), dt * \
        f_m2(r1_next, r2_next, t + dt)
    v1_next, v2_next = v1_half + 0.5 * k1, v2_half + 0.5 * k2
    R_x1.append(r1_next[0])
    R_y1.append(r1_next[1])
    R_x2.append(r2_next[0])
    R_y2.append(r2_next[1])
    V1.append(sqrt(v1_next[0]**2 + v1_next[1]**2))
    V2.append(sqrt(v2_next[0]**2 + v2_next[1]**2))
    r1 = r1_next
    v1 = v1_next
    r2 = r2_next
    v2 = v2_next


plot(R_x1, R_y1, "rs")
plot(R_x2, R_y2, "b-.")
xlabel("x axis")
ylabel("y axis")
grid(True)
legend(("M", "m"))
show()

plot(time_range, U1_data, "g-.")
plot(time_range, T1_data, "r--")
plot(time_range, E1_data, "b")
legend(("Potential Energy", "Kinetic Energy", "Total Energy"))
grid(True)
xlabel("Time (s)")
ylabel("Energy (J)")
title("Energy vs Time for m1")
show()
print("For m1; \nAverage Potential Energy: ", avg(U1_data), "\nAverage Kinetic Energy: ",
      avg(T1_data), "\nTotal energy: ", avg(E1_data))

plot(time_range, U2_data, "g-.")
plot(time_range, T2_data, "r--")
plot(time_range, E2_data, "b")
legend(("Potential Energy", "Kinetic Energy", "Total Energy"))
grid(True)
xlabel("Time (s)")
ylabel("Energy (J)")
title("Energy vs Time for m2")
show()
print("----------------------------")
print("For m2; \nAverage Potential Energy: ", avg(U2_data), "\nAverage Kinetic Energy: ",
      avg(T2_data), "\nTotal energy: ", avg(E2_data))

end = perf_counter()
print("Run time:", end - start)

