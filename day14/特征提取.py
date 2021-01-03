from PIL import Image
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import os
import numpy as np
import pickle

dir_path = r'E:\AI精英2001\代码\day14\cut_images'

# 需要构建特征矩阵和目标向量
Y = []
datas = []
# for file in os.listdir(dir_path):
# Y.append(file.split('_')[0])
img = Image.open(os.path.join(r'E:\AI精英2001\代码\day14\cut_images\1_8.jpg'))
data = np.array(img)
print(data)
print(data.shape)
# x,y,z = data.shape
# datas.append(data.reshape(x*y*z))
# datas = np.array(datas)
# Y = np.array(Y)
# s = StandardScaler()
# X = s.fit_transform(datas)
# train_x,test_x,train_y,test_y = train_test_split(X,Y)
# svm = SVC()
# svm.fit(train_x,train_y)
# pickle.dump(s,open('StandardScaler.model','wb'))
# pickle.dump(svm,open('SVM.model','wb'))
# svm = pickle.load(open('SVM.model','rb'))
# score = svm.score(test_x,test_y)
# print(score)