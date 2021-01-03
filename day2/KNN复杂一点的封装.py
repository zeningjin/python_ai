from collections import Counter
import random

class BASE(object):
    def __init__(self,k):
        self.k = k

    # 1. 分类
    def classify(self,X, Y, x):
        # 建立一个列表dis来存储距离
        dis = [sum([(xx[i]-x[i])**2 for i in range(len(xx))])**0.5 for xx in X]
        # dis是通过遍历得来的，dis本身下标和Y就对应，只需要找到new_dis中的元素在dis中对应的下标
        # 就可以找到对应的Y
        return Counter([Y[dis.index(d)] for d in sorted(dis)[:self.k]]).most_common(1)[0][0]

    # 2. 评估
    def score(self,train_X, test_X, train_Y, test_Y):
        counts = 0
        for i, x in enumerate(test_X):
            result = self.classify(train_X, train_Y, x)
            # 判断一下预测结果是否正确,预测的结果是result，正确的结果是test_Y中所对应的元素。
            if result == test_Y[i]:
                counts += 1
        return counts / len(test_Y)

class Util(object):
    # 1. 加载数据

    def loads(self,filepath, sep='\t'):
        # 创建特征矩阵X和目标向量Y
        X = []
        Y = []
        with open(filepath) as r:
            datas = r.readlines()
        for data in datas:
            dd = data.split(sep)
            X.append(list(map(lambda x: float(x), dd[:-1])))
            Y.append(dd[-1].strip())
        return X, Y

    # 2. 归一化
    def get_X(self,X):
        # 最大最小值归一化new=(x-min)/(max-min)
        # 最大最小值归一化new=(x-min)/(max-min)
        # 获得特征数
        new_x = []
        # 遍历列数
        for i in range(len(X[0])):
            l = [x[i] for x in X]
            max1 = max(l)
            min1 = min(l)
            new_x.append([(x - min1) / (max1 - min1) for x in l])
        # new_x变成了[[归一化后的第一列],[归一化后的第二列],[归一化后的第三列]]
        n = []
        # 遍历的是列数
        for i in range(len(new_x[0])):
            r = []
            # 遍历的是行数
            for j in range(len(new_x)):
                r.append(new_x[j][i])
            n.append(r)
        return n

    # 3. 分割数据
    def train_test_split(self,X, Y, test_size=0.2):
        test_X = []
        test_Y = []
        while len(test_X) < len(X) * test_size:
            # 如何选择需要添加的元素？
            index = random.choice(range(len(X)))
            test_X.append(X.pop(index))
            test_Y.append(Y.pop(index))
        return X, test_X, Y, test_Y

