# 矩阵的加减法
# A = [[1,2],[3,4],[5,6]]
# B = [[1,2],[3,4]]
# 加减法对位元素相加减。
# C = A+B
# 加法
# C = []
# for i in range(len(A)):
#     r = []
#     for j in range(len(A[i])):
#         r.append(A[i][j]+B[i][j])
#     C.append(r)
# print(C)
# 减法
# C = []
# for i in range(len(A)):
#     r = []
#     for j in range(len(A[i])):
#         r.append(A[i][j]-B[i][j])
#     C.append(r)
# print(C)

# 矩阵的转置
# 矩阵原本的形状为m * n
# 矩阵转置生成一个新矩阵形状为n * m
# C = []
# #  取列
# for i in range(len(A[0])):
#     r = []
#     for j in range(len(A)):
#         # r.append(A[i][j]-B[i][j])
#         r.append(A[j][i])
#     C.append(r)
# print(C)

A = [[1,2,3],[4,5,6]]
B = [[2,3],[5,6],[4,6]]
C = []
# 乘法
# 遍历第一个矩阵的行
# 生成的新矩阵的行：第一个矩阵的行
# for i in range(len(A)):
#     # 遍历第二个矩阵的列
#     r = []
#     # 生成新矩阵的列：第二个矩阵的列
#     for j in range(len(B[0])):
#         # 遍历第二个矩阵的行
#         sums = 0
#         # 求和：用A的列数或者B的行数来控制求和次数
#         for n in range(len(B)):
#             sums += A[i][n]*B[n][j]
#         r.append(sums)
#     C.append(r)
# print(C)