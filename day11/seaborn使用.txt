import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
# sns.set_style(style='ticks')
# sns.set_palette('colorblind')
sns.set_palette(sns.color_palette('deep'))
#{deep:"更深",muted:"更浅",pastel:"更粉嫩",dark:"更黑",bright:"更亮",colorlind:"色盲模式"}
datas = pd.read_csv(r'E:\AI精英2001\代码\day3\dating.txt',sep='\t',names=['salary','taobao','tv','result'])
# datas = MinMaxScaler().fit_transform(X=datas)
# datas = pd.DataFrame(datas,columns=['salary','taobao','tv','result'])
# seaborn.柱状图(x='列名',y='列名',data=dataframe)
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# datas = pd.DataFrame([{'姓名':'马洪顺','年龄':37},{'姓名':'宋琦','年龄':58}])
# datas = pd.DataFrame([{'姓名':'1','年龄':37},{'姓名':'2','年龄':58},{'姓名':'3','年龄':45}])
# sns.barplot(x='姓名',y='年龄',data=datas)
# sns.violinplot(x='result',y='salary',data=datas)
# sns.pointplot(x='姓名',y='年龄',data=datas)
# sns.stripplot(x='result',y='salary',data=datas)
# sns.swarmplot(x='result',y='salary',data=datas)
# sns.kdeplot(data=datas,data2=datas1)
# sns.boxplot(x='result',y='salary',data=datas)
# sns.scatterplot(x='tv',y='salary',data=datas)
sns.pairplot(datas)
# sns.distplot(datas)
# sns.countplot(x='result',data=datas)
# sns.heatmap(data=datas)

plt.show()

