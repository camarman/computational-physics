# 2 body problem

from pylab import plot, show, xlabel, ylabel, legend, grid
from math import sqrt
from numpy import arange, array
from time import perf_counter
start = perf_counter()


G = 6.6738 * 10 ** -11   # m^3kg^-1s^-2
M = 1.9891 * 10 ** 30  # mass of the object-1
m = 5.972 * 10 ** 24  # mass of the object-2

h = 3600  # time step
t_points = arange(0, 4 *365 * 24 * 3600, h)


def f_m(r, t):
    '''The force that acts on the small mass'''
    return (- G * M * r) / dist


def f_M(r, t):
    '''The force that acts on the larger mass'''
    return (- G * m * r) / dist


r_m = array([1.4710 * 10**11, 0])  # position vector of the m (m)
v_m = array([0, 3.0287 * 10**4])  # velocity vector of the m (m/s)

r_M = array([0, 0])  # position vector of the M (m)
v_M = array([40, 100])  # velocity vector of the M (m/s)

R_mx = []
R_my = []
R_Mx = []
R_My = []
V_m = []
V_M = []

U_points = []
T_points = []
E_points = []


def Energy(r, v):
    '''calculates the energy of the small mass m '''
    U = (-G * M * m) / (r[0]**2 + r[1]**2)**(1/2)  # potential energy
    T = 0.5 * m * (v[0]**2 + v[1]**2)  # kinetic energy
    E = U + T  # total energy
    return U, T, E


def avg(xarray):
    return sum(xarray) / len(xarray)


for t in t_points:
    U, T, E = Energy(r_m, v_m)
    U_points.append(U)
    T_points.append(T)
    E_points.append(E)
    dist = (sum([i**2 for i in r_m - r_M]))**(3/2)
    v_m_half, v_M_half = v_m + 0.5 * h * \
        f_m(r_m, t),  v_M + 0.5 * h * f_M(r_M, t)
    r_m_next, r_M_next = r_m + h * v_m_half,  r_M + h * v_M_half
    dist = (sum([i**2 for i in r_m_next - r_M_next]))**(3/2)
    k_m, k_M = h * f_m(r_m_next, t + h), h * f_M(r_M_next, t + h)
    v_m_next, v_M_next = v_m_half + 0.5 * k_m, v_M_half + 0.5 * k_M
    R_mx.append(r_m_next[0])
    R_my.append(r_m_next[1])
    R_Mx.append(r_M_next[0])
    R_My.append(r_M_next[1])
    V_m.append(sqrt(v_m_next[0]**2 + v_m_next[1]**2))
    V_M.append(sqrt(v_M_next[0]**2 + v_M_next[1]**2))
    r_m = r_m_next
    v_m = v_m_next
    r_M = r_M_next
    v_M = v_M_next


plot(R_Mx, R_My, "rs")
plot(R_mx, R_my, "b-.")
xlabel("x axis")
ylabel("y axis")
grid(True)
legend(("M", "m"))
show()

plot(t_points, U_points, "g-.")
plot(t_points, T_points, "r--")
plot(t_points, E_points, "b")
legend(("Potential Energy", "Kinetic Energy", "Total Energy"))
grid(True)
xlabel("Time (s)")
ylabel("Energy (J)")
show()
print("Average Potential energy: ", avg(U_points), "Average Kinetic Energy: ",
      avg(T_points), "Total energy: ", E_points[-1])

end = perf_counter()
print("Time: ", end - start, "second")
