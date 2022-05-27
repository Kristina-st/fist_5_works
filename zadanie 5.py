from sympy import *
from sympy.abc import*
from sympy.plotting import*

# 1.2
x = Symbol('x')
y = limit((3*x*x + 2*x + 1)/(2*x*x*x - x),x,0)
print("limit = ",y,"\n")


#2.2
print("Symma: ")
pprint(summation(1/n/n, (n, 1, oo)))
print(" ")

#3.2
m, n, a, b = symbols('m n a b')
znach = log(a, x)
rez = diff(znach, x, 2)
print("Производная  = ",rez,"\n")

# 4.1
p = Symbol('p')
f = x**p
z = integrate(f,x)
pprint(z,use_unicode=True)

#5.4
X = Symbol('X')
e = solve(X**7 + 7*X**5 + 3*X**4 + 5*X**3 + 26*X*X - 10*X + 40,X, dict=True)
pprint(e, use_unicode=True)

#6.1
yr = x*x*x/2 + 1 - cos(2 - x)
plot(yr, -2.5, 2.5)
