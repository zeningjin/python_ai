# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 17:40
# @Author  : hbw
# @File    : sss.py
# @Software: PyCharm
from collections import Counter
from scrapy import Spider
from ML import Base,main



class KNN(Base):
    def __init__(self, k=5):
        self.k = k
    # 1. 分类
    def classify(self, X, Y, x):
        # 建立一个列表dis来存储距离
        dis = [sum([(xx[i] - x[i]) ** 2 for i in range(len(xx))]) ** 0.5 for xx in X]
        # dis是通过遍历得来的，dis本身下标和Y就对应，只需要找到new_dis中的元素在dis中对应的下标
        # 就可以找到对应的Y
        return Counter([Y[dis.index(d)] for d in sorted(dis)[:self.k]]).most_common(1)[0][0]

class KNN2(Base):
    def classify(self, X, Y, x):
        return '2'

class KNN3(Base):
    pass

class KNN1(Base):
    def classify(self, X, Y, x):
        return '1'

    def score(self, train_X, test_X, train_Y, test_Y):
        return 1



if __name__ == '__main__':
    filepath= r'E:\数据集\dating.txt'
    knn=KNN()
    print(main(filepath,knn))