import pandas as pd

# l = [[1,2],[3,4]]
# df = pd.DataFrame(l)
# print(df)

X = pd.read_csv(r'E:\AI精英2001\代码\day3\dating.txt',sep='\t',names=['淘宝','tv'],usecols=[1,2])
Y = pd.read_csv(r'E:\AI精英2001\代码\day3\dating.txt',sep='\t',names=['薪资','taobao','tv','result'],usecols=[3])
# print(X)
# print(Y)
# 可以进行转置
# print(X.T)
# 元素个数
# print(X.size)
# 矩阵形状
# print(X.shape)
# 输出数据类型，不要求全部一致


# 将DataFrame转为numpy的ndarray
# print(X.values)
# print(type(X.values))


# 方法
# 求最大值，axis为0的时候返回列的最大值，为1的时候返回行的最大值
# print(X.max(axis=1))
# print(X.min(axis=0))
# print(X.mean())
# print(X.sum(axis=1))
# print(X.std())

# pandas独特独有的方法
# print(X['taobao'])
# 返回一列不重复的值
# print(X['taobao'].duplicated())
# 还可以对数据进行筛选
# print(X)
# print(X[X['taobao']==6.382129])
# 按行切片，一般来说给一个范围
# print(X[:4])
# print(X[' 淘宝'])
# print(X.taobao)
# print(X.tv)
# print(X.淘宝)