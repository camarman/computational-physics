def f(x):
    '''the function'''
    return (x ** 4 - 2*x + 1)


def trapesozidal(a, b, N):
    h = (b - a) / N
    return h * ((0.5 * (f(a) + f(b))) + sum([f(a + i * h) for i in range(1, N)]))


I_1 = trapesozidal(0, 2, 10)
I_2 = trapesozidal(0, 2, 20)

print("I_1 is ", I_1)
print("I_2 is ", I_2)

error = 1/3 * (I_2 - I_1)
act_error = 4.4 - I_2
print("computed error is", error)
print("actual error", act_error)
