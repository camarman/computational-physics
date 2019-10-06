# The Simpsons Rule


def f(x):
    '''the function'''
    return (x ** 4 - 2*x + 1)


def simpsons_rule(a, b, N):
    h = (b - a) / N
    S1 = 4 * sum([f(a + (2 * i - 1)*h) for i in range(1, N//2 + 1)])
    S2 = 2 * sum([f(a + (2 * i * h)) for i in range(1, N//2)])
    return 1/3 * h * (f(a) + f(b) + S1 + S2)


print(simpsons_rule(0, 2, 10))
