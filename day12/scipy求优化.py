import numpy as np
from scipy import optimize
def func(x,a,b):
    return a*x+b

a = 2
b = 3
x = np.arange(-10,10)
y = func(x,a,b)
print(y)
zs = np.random.normal()
print(zs)
y = y+zs
print(y)
result = optimize.curve_fit(func,x,y)[0]
print(result)