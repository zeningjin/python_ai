import pandas as pd
import jieba
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer # 逆文档频率
from sklearn.tree import DecisionTreeClassifier

def get_text(text):
    return jieba.lcut(text)

df = pd.read_csv(r'E:\AI精英2001\代码\day6\新闻分类\val.txt',sep='\t',names=['result','title','url','content'])
X = df.iloc[:,1:]
Y = df.iloc[:,0]
# tokenizer分词器,停用词
with open(r'E:\AI精英2001\代码\day6\新闻分类\中文停用词库.txt',encoding='utf-8') as r:
    stop_words = r.readlines()
tf = TfidfVectorizer(tokenizer=get_text,stop_words=stop_words)
X = tf.fit_transform(df['content'])
train_X,test_X,train_Y,test_Y = train_test_split(X,Y)
tree = DecisionTreeClassifier()
tree.fit(train_X,train_Y)
print(tree.score(test_X,test_Y))