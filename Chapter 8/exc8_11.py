# Verlet method
# Orbit of the earth

from math import sqrt
from pylab import plot, show, xlabel, ylabel, legend, grid
from numpy import arange, array
from time import perf_counter

start = perf_counter()


G = 6.6738 * 10 ** -11  # m^3kg^-1s^-2
M = 1.9891 * 10 ** 30  # mass of the sun in kg
m = 5.9772 * 10 ** 24  # mass of the earth in kg

h = 3600  # timsestep in seconds (corresponds to an hour)
t_points = arange(0, 365 * 24 * 3600, h)

r = array([1.4710 * 10**11, 0])  # position vector of the earth
v = array([0, 3.0287 * 10**4])  # velocity vector of the earth

r_points = []
v_points = []
U_points = []
T_points = []
E_points = []


def f(r, t):
    '''a = d^2r/dt^2 = f(r, t)'''
    return (- G * M * r) / (r[0]**2 + r[1]**2)**(3/2)


def Energy(r, v):
    '''calculates the energy of the earth-sun system'''
    U = (-G * M * m) / (r[0]**2 + r[1]**2)**(1/2)  # potential energy
    T = 0.5 * m * (v[0]**2 + v[1]**2)  # kinetic energy
    E = U + T  # total energy
    return U, T, E


def avg(xarray):
    return sum(xarray) / len(xarray)


for t in t_points:
    U, T, E = Energy(r, v)
    U_points.append(U)
    T_points.append(T)
    E_points.append(E)
    v_half = v + 0.5 * h * f(r, t)  # v(t + 0.5h)
    r_next = r + h * v_half
    k = h * f(r_next, t + h)
    v_next = v_half + 0.5 * k
    r_points.append(r_next)
    v_points.append(v_next)
    r = r_next
    v = v_next

R_x = []
R_y = []
for x, y in r_points:
    R_x.append(x)
    R_y.append(y)

end = perf_counter()
print("Time: ", end - start, "second")
plot(R_x, R_y)
xlabel("x")
ylabel("y")
grid(True)
show()
plot(t_points, U_points, "g-.")
plot(t_points, T_points, "r--")
plot(t_points, E_points, "b")
legend(("Potential Energy", "Kinetic Energy", "Total Energy"))
grid(True)
xlabel("Time (s)")
ylabel("Energy (J)")
show()
print("Potential energy: ", avg(U_points), "Kinetic Energy: ",
      avg(T_points), "Total energy: ", E_points[-1])
