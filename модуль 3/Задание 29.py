#Заменить в массиве все отрицательные элементы на 0.
from numpy import *
a = array([-1, 0, 28, -9032, 3, 9, -1, -6])
n = len(a)
i = 0
while i < n:
    if a[i]<0:
        a[i] = 0
    i += 1

print(a)
