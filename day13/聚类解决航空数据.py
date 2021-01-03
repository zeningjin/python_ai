from sklearn.cluster import KMeans
import pandas as pd

data = pd.read_csv('cleaned_data.csv')
km = KMeans(n_clusters=5)
km.fit(data)
print(km.cluster_centers_)#展示最后一次迭代的质心
print(km.labels_)# 查看每个样本对应的类别
