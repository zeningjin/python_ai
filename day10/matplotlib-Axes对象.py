from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure()
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
x1 = np.arange(0,10,1)
x2 = np.arange(0,10,1)
y1 = 2*x1 +3
y2 = np.sin(x2)
ax = fig.add_axes([0,0,1,1])
ax.plot(x1,y1,'sb:')
ax.plot(x2,y2)
ax.legend(labels=('一元一次','sin函数'),loc='center')
plt.show()
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False
# y = 2*x1+3
# plt.plot(x1,y)
# plt.xlabel(u"度")
# plt.ylabel("sin")
