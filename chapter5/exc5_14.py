from gaussxw import gaussxw

sigma = 100  # kg/m^2 sheet density
G = 6.674 * 10**-11  # m^3kg^-1s^-2
L = 10  # m
N = 100  # step size


def f(x, y, z):
    return (x**2 + y**2 + z**2)**(-3/2)


def gaussian(a, b):
    x, w = gaussxw(N)
    xp = 0.5 * (b - a) * x + 0.5 * (b + a)
    wp = 0.5 * (b - a) * w
    s = 0
    for k in range(N):
        s += wp[k] * f(xp[k])
    return s


z = 1
Fz = G * sigma * z * gaussian(-L/2, L/2)
