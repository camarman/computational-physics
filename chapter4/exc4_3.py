# Calculating derivatives


def f(x):
    return x * (x - 1)


def derivative_f(x, e):
    return (f(x + e) - f(x)) / e


for i in range(2, 16, 2):
    print(derivative_f(1, 10**-i))
