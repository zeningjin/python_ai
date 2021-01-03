from day2 import KNN
from day2 import Util


u = Util()
u1 = Util()
#1. 读取数据
X,Y = u.loads(r'E:\AI精英2001\代码\day2\dating.txt')
#2. 对数据进行归一化
X = u.get_X(X)
#3. 对数据进行分割
train_X,test_X,train_Y,test_Y = u.train_test_split(X,Y)
#4. 进行KNN分类或者评估
knn = KNN(4)
# print(knn.classify(X, Y, [1, 2, 3, 4]))
print(knn.score(train_X, test_X, train_Y, test_Y))