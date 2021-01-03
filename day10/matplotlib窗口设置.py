from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1,10,1)
y = 2*x+1

fig = plt.figure(figsize=(10,10),dpi=100,edgecolor='red',linewidth=10)
plt.plot(x,y)
plt.show()