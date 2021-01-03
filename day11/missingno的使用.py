import missingno as msn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
datas = pd.read_csv(r'E:\AI精英2001\代码\day11\adult.txt',sep=',',names=range(15))
for c in datas.columns:
    datas[c][datas[c] == ' ?'] =np.NAN
msn.heatmap(datas)
plt.show()