import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
# def func(x):
#     return x*x+x
# # x*x+x = 0,x=0,x=-1
# x = np.arange(-10,10,0.1)
# result = optimize.fsolve(func,x0=[1,-1])
# print(result)
# plt.plot(x,func(x))

def func1(x):
    return np.sin(x)

def func2(x):
    return 0.05*x-0.5

def func3(x):
    return func2(x)-func1(x)

result = optimize.fsolve(func3,x0=[-9,-7,-3,0,2,7,10])
print(result)
x = np.arange(-10,10,0.1)
plt.plot(x,func1(x))
plt.plot(x,func2(x))
plt.plot(result,func1(result),'ro')

plt.show()

plt.show()