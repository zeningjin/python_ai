import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
# 对于绝大多数的机器学习算法来说，都分为分类器和回归器
from sklearn.linear_model import LarsCV,LassoCV,LogisticRegression
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
df = pd.read_csv(r'E:\AI精英2001\代码\day4\dating.txt',sep='\t',names=['salary','taobao','tv','result'])
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]
s = MinMaxScaler()
s.fit(X)
X = s.transform(X)
train_X,test_X,train_Y,test_Y=train_test_split(X,Y,test_size=0.1)
knn = LogisticRegression(max_iter=10,penalty='l1')
knn.fit(train_X,train_Y)
print(knn.score(test_X,test_Y))