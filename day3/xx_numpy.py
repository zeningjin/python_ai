import numpy as np
import time
# 创建一个一维数组，传入列表或者元组
# n = np.array([1,2,3])
# 创建一个二维数组，传入列表嵌套或者元组嵌套
# n = np.array([[1,2,3],[4,5,6]])
# n = np.array(range(100000000))
# 根据range对象去创建一个ndarray
# n = np.arange(10)
# 创建一个全是1的数组，如果传入的是一个数，那么创建的是一维的，如果传的是两个数就是二维的。
# n = np.ones((3,3))
# 创建一个全是1的数组，这个数组的形状和传入数组的形状一致。
# n = np.ones_like([[1,2,3],[4,5,6]])
# n = np.zeros((3,3))
# n = np.zeros_like([[1,2,3],[4,5,6]])
# print(n)
# print(n)
# n = np.full((3,3),66666)
# n = np.full_like([[1,2,3],[4,5,6]],666)
# n = np.random.randn(3,3)
# print(n)
# 属性
# 1. shape返回数组的形状
# print(n.shape)
# 2. ndim返回数组的维度
# print(n.ndim)
# size返回所有的元素个数
# print(n.size)
# dtype
# print(n.dtype)
# numpy操作
# 可以直接在ndarray后面进行运算，对ndarray中的所有元素，进行运算
a = np.arange(10)
b = np.arange(10)
# 重新规范形状,在重新规范形状的时候，必须保证前后矩阵形状相同
# print(a)
# a= a.reshape(2,5)
# print(a)
# 加减乘除
# 加：将矩阵中所有元素全部加一
# print(a+1)
# 将两个数组中的对位元素相加
# print(a+b)
# 减:将矩阵中所有元素全部减一
# print(a-1)
# 将两个数组中的对位元素相减
# print(a-b)
# 乘法:将矩阵中所有元素全部乘二
# print(a*2)
# 将两个数组中的对位元素相乘
# print(a*b)
# 除法:将矩阵中所有元素全部乘二
# print(a/2)
# 将两个数组中的对位元素相除
# print(a/b)
# 有两个列表分别是a、b，a = [若干个数的平方],b=[若干个数的立方组成的列表]，得出一个C，求两个列表对位元素的和
# 复杂运算
# np.sum可以求所有元素之和
a = np.array([1,2,3,4,5,6,7,8,9])
# print(np.sum(a))
# np.prod所有元素的乘积
# print(np.prod(a))
# np.max & np.min求最大值最小值
# print(np.max(a))
# print(np.min(a))
# np.mean求平均值
# print(np.mean(a))
#np.var求方差
# print(np.var(a)**0.5)
# np.std求标准差
# print(np.std(a))
# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# print(a.T)
# print(a[1][2])
# def python_sum(n):
#     a = []
#     b = []
#     for i in range(n):
#         a.append(i**2)
#         b.append(i**3)
#     c = []
#     for i in range(n):
#         c.append(a[i]+b[i])
#     return c
#
# def numpy_sum(n):
#     a = np.arange(n)**2
#     b = np.arange(n)**3
#     return a+b
#
# if __name__ == '__main__':
#     time1 = time.time()
#     for i in range(999999):
#         python_sum(10)
#     print(time.time()-time1)
#     #0.000997304916381836
#     time1 = time.time()
#     for i in range(999999):
#         numpy_sum(10)
#     print(time.time() - time1)