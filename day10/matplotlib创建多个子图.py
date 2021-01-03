from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 挪动x，y轴的位置，也就是图片下边框和左边框的位置
ax.spines['bottom'].set_position(('data', 0))  # data表示通过值来设置x轴的位置，将x轴绑定在y=0的位置
ax.spines['left'].set_position(('axes', 0.5))  # axes表示以百分比的形式设置轴的位置，即将y轴绑定在x轴50%的位置，也就是x轴的中点

x1 = np.arange(0,10,1)
x2 = np.arange(0,10,1)
y1 = 2*x1 +3
x3 = np.arange(10,100,1)
y3 = 5*x3 +5
y2 = np.sin(x2)
plt.subplot(211)
plt.plot(x1,y1)

plt.subplot(414,facecolor='r')
plt.plot(x2,y2)

plt.show()

