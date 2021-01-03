# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 11:37
# @Author  : xx
# @File    : ML.py
# @Software: PyCharm
import random


class Base(object):
    def __new__(cls, *args, **kwargs): # 在这里检查子类的方法中有没有自己的score

        if 'score' in cls.__dict__.keys() and cls!=Base: # 判断类对象不是父类，且有score方法
            raise ImportError('该方法不能被覆盖')
        # 没有该方法的子类还需要正常创建
        return super().__new__(cls)

    def classify(self, X, Y, x):
        raise NotImplementedError('{}.classify callback is not defined'.format(self.__class__.__name__))

    def score(self, train_X, test_X, train_Y, test_Y):
        counts = 0
        for i, x in enumerate(test_X):
            result = self.classify(train_X, train_Y, x)
            # 判断一下预测结果是否正确,预测的结果是result，正确的结果是test_Y中所对应的元素。
            if result == test_Y[i]:
                counts += 1
        return counts / len(test_Y)

class Util(object):
    # 1. 加载数据

    def loads(self, filepath, sep='\t'):
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
    def get_X(self, X):
        # 最大最小值归一化new=(x-min)/(max-min)
        # 最大最小值归一化new=(x-min)/(max-min)
        # 获得特征数
        new_x = []
        # 遍历列数
        for i in range(len(X[0])):
            l = [x[i] for x in X]
            new_x.append([(x - min(l)) / (max(l) - min(l)) for x in l])
        # new_x变成了[[归一化后的第一列],[归一化后的第二列],[归一化后的第三列]]
        return [[new_x[j][i] for j in range(len(new_x))] for i in range(len(new_x[0]))]

    # 3. 分割数据
    def train_test_split(self, X, Y, test_size=0.2):
        test_X = []
        test_Y = []
        while len(test_X) < len(X) * test_size:
            # 如何选择需要添加的元素？
            index = random.choice(range(len(X)))
            test_X.append(X.pop(index))
            test_Y.append(Y.pop(index))
        return X, test_X, Y, test_Y

def main(filepath,ojb):
    util = Util()
    X, Y = util.loads(filepath)
    X = util.get_X(X)
    tarin_x, test_x, train_y, test_y = util.train_test_split(X, Y)
    return ojb.score(tarin_x, test_x, train_y, test_y)