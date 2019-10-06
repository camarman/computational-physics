# Catalan Number
C = 1
for i in range(10 ** 9):
    C *= (4 * i + 2) / (i + 2)
    print(int(C))
