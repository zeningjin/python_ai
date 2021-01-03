# 1. 不同类别的女生，是否存在一些区别？ 有
# 2. 不同类别的女生的区别在哪儿？区别一定是在salary、taobao、tv上，这三个全部都有关系。
# 3. 最主要是因为特征值的不同。
# 4. 新给一个女生的数据，可以找这个女生的闺蜜，她闺蜜是什么样的人，他大概率就是什么样的人。
# 5. 直接把该女生分为该类。
from collections import Counter



# 1. 加载数据，加载成特征矩阵和目标向量
def loads(filepath):
    # 创建特征矩阵X和目标向量Y
    X=[]
    Y=[]
    with open(filepath) as r:
        datas = r.readlines()
    for data in datas:
        dd = data.split('\t')
        X.append(list(map(lambda x:float(x),dd[:-1])))
        Y.append(dd[-1].strip())
    return X,Y



# 2. 给定新数据，算距离数据最近的前K个样本，K的取值：“凭经验”，一般来说，3-15，不超过20，计算的时候使用欧氏距离。
# 3. 统计前K个样本所对应的类别，然后将出现次数最多的类别作为输出。
def classify(X,Y,x,k):
    # 建立一个列表dis来存储距离
    dis = []
    for xx in X:
        dis.append(((xx[0]-x[0])**2+(xx[1]-x[1])**2+(xx[2]-x[2])**2)**0.5)
    new_dis = sorted(dis)[:k]
    # dis是通过遍历得来的，dis本身下标和Y就对应，只需要找到new_dis中的元素在dis中对应的下标
    # 就可以找到对应的Y
    ys = []
    for d in new_dis:
        i = dis.index(d)
        ys.append(Y[i])
    return Counter(ys).most_common(1)[0][0]

if __name__ == '__main__':
    X,Y = loads(r'E:\AI精英2001\代码\day2\dating.txt')
    # 切割训练集和测试集，一开始默认一般使用0.1，具体如何分割：“凭经验”
    train_X=X[:800]
    test_X=X[800:]
    train_Y=Y[:800]
    test_Y=Y[800:]
    counts = 0
    for i,x in enumerate(test_X):
        result = classify(train_X,train_Y,x,4)
        # 判断一下预测结果是否正确,预测的结果是result，正确的结果是test_Y中所对应的元素。
        if result==test_Y[i]:
            counts += 1
    print(counts/198)