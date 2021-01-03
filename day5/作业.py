import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LarsCV,LassoCV,LogisticRegression
#1. 读数据
# 对哪些列做动态字符串映射{键：值}
def transform_data(datas,cols):
    # 遍历每一列
    for c in cols:
        # 遍历每一列不重复的值
        for i,item in enumerate(datas[c].drop_duplicates()):
            datas[c][datas[c].str.strip()==item.strip()]=i+1
    return datas

def drop(datas):
    for c in datas.columns:
        datas[c][datas[c]==" ?"]=np.NAN
    datas.dropna(inplace=True)
    return datas

datas = pd.read_csv(r'E:\AI精英2001\代码\day5\adult.txt',names=range(15))
datas = drop(datas)
datas = transform_data(datas, [1, 3, 5, 6, 7, 8, 9, 13, 14])

X = datas.iloc[:,:-1]
Y = datas.iloc[:,-1]
Y = Y.astype(int)
s = MinMaxScaler()
s.fit(X)
X = s.transform(X)
for i in range(10):
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.1)
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(train_X, train_Y)
    print(knn.score(test_X, test_Y))
