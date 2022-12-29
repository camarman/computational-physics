a = 0
b = 2
N = 10
h_c = 10**-6
h = (b - a)/10


def f(x):
    '''the function'''
    return x**4 - 2*x + 1


f_a_prime = (f(a + h_c) - f(a - h_c)) / (2 * h_c)
f_b_prime = (f(b + h_c) - f(b - h_c)) / (2 * h_c)

S_1 = (1/12) * (h_c**2) * (f_a_prime - f_b_prime)

S_2 = h * (0.5 * f(a) + 0.5 * f(b) + sum([f(a + i * h) for i in range(1, N)]))

print("The result of the integral:", S_1 + S_2)
