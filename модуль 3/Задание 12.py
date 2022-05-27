#Вычислите норму ||a||1 вектора.

from numpy import *
v = array([1, -7, 9, 13, 81])
norm = nanmax(linalg.norm(v))
print('%.6f'%norm)
