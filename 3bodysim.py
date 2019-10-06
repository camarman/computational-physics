from math import sqrt
from numpy import arange, array
from pylab import plot, show, xlabel, ylabel, legend, grid, title
from time import perf_counter

start = perf_counter()

G = 6.6738 * 10 ** -11   # m^3kg^-1s^-2

dt = 3600  # time - step
time_range = arange(0, 365 * 24 * 3600, dt)


m1 = 1.9891 * 10 ** 30  # mass of the object-1
# position vector of the m2 (m) #I set to values (1,1) otherwise the energy calculations give inf
r1 = array([1, 1])
v1 = array([0, 0])  # velocity vector of the m2 (m/s)

m2 = 5.972  * 10 ** 24  # mass of the object-2
r2 = array([1.4710 * 10**11, 0])  # position vector of the m1 (m)
v2 = array([0, 3.0287 * 10**4])  # velocity vector of the m1 (m/s)

m3 = 0.07346 * 10 ** 24 # in kg
r3 = array([1.4710 * 10**11 + 3.844 * 10**8 , 0 ])  
v3 = array([0, 1023.056]) 

def f_m1(r1, r2, r3, t):
    '''The force that acts on the m1'''
    dist12 = (sum([i**2 for i in r1 - r2]))**(3/2)
    dist13 = (sum([i**2 for i in r1 - r3]))**(3/2)
    return (- G * m2 * (r1 - r2)) / dist12 + (- G * m3 * (r1 - r3)) / dist13

def f_m2(r1, r2, r3, t):
    '''The force that acts on the m2'''
    dist21 = (sum([i**2 for i in r2 - r1]))**(3/2)
    dist23 = (sum([i**2 for i in r2 - r3]))**(3/2)
    return (- G * m1 * (r2 - r1)) / dist21 + (- G * m3 * (r2 - r3)) / dist23


def f_m3(r1, r2, r3, t):
    '''The force that acts on the m3'''
    dist31 = (sum([i**2 for i in r3 - r1]))**(3/2)
    dist32 = (sum([i**2 for i in r3 - r2]))**(3/2)
    return (- G * m1 * (r3 - r1)) / dist31 + (- G * m2 * (r3 - r2)) / dist32

R_x1 = []  # x component of the position vector of the m1
R_y1 = []  # y component of the position vector of the m1
R_x2 = []  # x component of the position vector of the m2
R_y2 = []  # y component of the position vector of the m2
R_x3 = []  # y component of the position vector of the m3
R_y3 = []  # y component of the position vector of the m3
V1 = []  # storing velocity values of the m1
V2 = []  # storing velocity values of the m2
V3 = [] # storing velocity values of the m3

for t in time_range:
    v1_half, v2_half, v3_half = v1 + 0.5 * dt * f_m1(r1, r2, r3, t),  v2 + 0.5 * dt * f_m2(r1, r2, r3, t), v3 + 0.5 * dt * f_m3(r1, r2, r3, t)
    r1_next, r2_next, r3_next = r1 + dt * v1_half,  r2 + dt * v2_half, r3 + dt * v3_half
    k1, k2, k3 = dt * f_m1(r1_next, r2_next, r3_next, t + dt), dt * f_m2(r1_next, r2_next, r3_next, t + dt), dt * f_m3(r1_next, r2_next, r3_next, t + dt) 
    v1_next, v2_next, v3_next = v1_half + 0.5 * k1, v2_half + 0.5 * k2, v3_half + 0.5 * k3
    R_x1.append(r1_next[0])
    R_y1.append(r1_next[1])
    R_x2.append(r2_next[0])
    R_y2.append(r2_next[1])
    R_x3.append(r3_next[0])
    R_y3.append(r3_next[1])
    V1.append(sqrt(v1_next[0]**2 + v1_next[1]**2))
    V2.append(sqrt(v2_next[0]**2 + v2_next[1]**2))
    V3.append(sqrt(v3_next[0]**2 + v3_next[1]**2))
    r1 = r1_next
    v1 = v1_next
    r2 = r2_next
    v2 = v2_next
    r3 = r3_next
    v3 = v3_next

plot(R_x1, R_y1, "rs")
plot(R_x2, R_y2, "b-.")
plot(R_x3, R_y3, "g--")
xlabel("x axis")
ylabel("y axis")
grid(True)
legend(("m1", "m2", "m3"))
show()

