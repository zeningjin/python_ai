# 1. 不同类别的女生，是否存在一些区别？ 有
# 2. 不同类别的女生的区别在哪儿？区别一定是在salary、taobao、tv上，这三个全部都有关系。
# 3. 最主要是因为特征值的不同。
# 4. 新给一个女生的数据，可以找这个女生的闺蜜，她闺蜜是什么样的人，他大概率就是什么样的人。
# 5. 直接把该女生分为该类。
from collections import Counter
import random
# 1. 加载数据，加载成特征矩阵和目标向量
#CSV文件，就是以\t为数据分隔符的
def loads(filepath,sep='\t'):
    # 创建特征矩阵X和目标向量Y
    X=[]
    Y=[]
    with open(filepath) as r:
        datas = r.readlines()
    for data in datas:
        dd = data.split(sep)
        X.append(list(map(lambda x:float(x),dd[:-1])))
        Y.append(dd[-1].strip())
    return X,Y

def get_X(X):
    # 最大最小值归一化new=(x-min)/(max-min)
    # 最大最小值归一化new=(x-min)/(max-min)
    # 获得特征数
    new_x = []
    # 遍历列数
    for i in range(len(X[0])):
        l = [x[i] for x in X]
        max1 = max(l)
        min1 = min(l)
        new_x.append([(x-min1)/(max1-min1) for x in l])
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

# 2. 给定新数据，算距离数据最近的前K个样本，K的取值：“凭经验”，一般来说，3-15，不超过20，计算的时候使用欧氏距离。
# 3. 统计前K个样本所对应的类别，然后将出现次数最多的类别作为输出。
def classify(X,Y,x,k):
    # 建立一个列表dis来存储距离
    dis = [sum([(xx[i]-x[i])**2 for i in range(len(xx))])**0.5 for xx in X]
    # dis是通过遍历得来的，dis本身下标和Y就对应，只需要找到new_dis中的元素在dis中对应的下标
    # 就可以找到对应的Y
    return Counter([Y[dis.index(d)] for d in sorted(dis)[:k]]).most_common(1)[0][0]

def train_test_split(X,Y,test_size=0.2):
    test_X = []
    test_Y = []
    while len(test_X) < len(X)*test_size:
        # 如何选择需要添加的元素？
        index = random.choice(range(len(X)))
        test_X.append(X.pop(index))
        test_Y.append(Y.pop(index))
    return X,test_X,Y,test_Y

def score(train_X,test_X,train_Y,test_Y,k):
    counts = 0
    for i, x in enumerate(test_X):
        result = classify(train_X, train_Y, x, k)
        # 判断一下预测结果是否正确,预测的结果是result，正确的结果是test_Y中所对应的元素。
        if result == test_Y[i]:
            counts += 1
    return counts / len(test_Y)

if __name__ == '__main__':
    X,Y = loads(r'E:\AI精英2001\代码\day2\dating.txt')
    print(X)
    X = get_X(X)
    # 切割训练集和测试集，一开始默认一般使用0.2，具体如何分割：“凭经验”
    train_X,test_X,train_Y,test_Y = train_test_split(X,Y,test_size=0.1)
    s = score(train_X,test_X,train_Y,test_Y,4)
    print(s)