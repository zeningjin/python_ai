from sklearn.cluster import KMeans,DBSCAN
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

text={
    '今天天气很好',#宋：0 0
    '我今天考上了清华大学',#宋：1 1
    '清华大学很好',#宋：1 0
    '我今天心情很好',#宋：0 0
    '清华大学今天让我进去了'#宋：1 1
}

for t in text:
    print(jieba.lcut(t))
tid = TfidfVectorizer(tokenizer=lambda w:jieba.lcut(w))
X = tid.fit_transform(text)
print(X)
kmeans=DBSCAN(eps=1,min_samples=1)
print(kmeans.fit_predict(X))