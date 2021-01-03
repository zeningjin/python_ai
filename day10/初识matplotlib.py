from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0,10,1)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
y = 2*x+3
plt.plot(x,y)
plt.xlabel(u"度")
plt.ylabel("sin")
plt.show()