import numpy as np

n = int(input('Введите размерность матрицы: '))
a = np.random.randint(10, size = (n, n))
print(a)

sz, sv = np.linalg.eig(a)

print()
for i in range(n):
    print("собственнoе значения {} сooт. ему собственные векторы {}".format(sz[i], sv[:, i]))
