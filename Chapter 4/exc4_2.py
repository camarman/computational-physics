# quadratic equation solver
from math import sqrt


a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))


def quadratic_solver(a, b, c):
    delta = (b**2 - 4*a*c)
    root_1 = (-b + sqrt(delta)) / (2 * a)
    root_2 = (-b/a) - root_1
    return root_1, root_2


def quadratic_solver_2(a, b, c):
    delta = (b**2 - 4*a*c)
    root_1 = 2 * c / (-b - sqrt(delta))
    root_2 = 2 * c / (-b + sqrt(delta))
    return root_1, root_2


print(quadratic_solver(a, b, c))
print(quadratic_solver_2(a, b, c))
