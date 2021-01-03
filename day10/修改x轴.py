from matplotlib import pyplot as plt
import numpy as np


x = np.arange(-5,5,0.01)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
ax = plt.gca()
print(ax.spines['top'].set_color('none'))
print(ax.spines['right'].set_color('none'))
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('axes',0.5))
y = np.sin(x)
plt.plot(x,y)
plt.xlabel(u"度")
plt.ylabel("sin")
plt.show()