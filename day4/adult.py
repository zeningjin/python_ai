import pandas as pd

df = pd.read_csv(r'E:\AI精英2001\代码\day4\adult.txt',names=['年龄','工作种类','Fnlwgt','教育情况','受教育年限','婚姻状态','职业情况','亲属情况','种族肤色','性别','资本盈利','资本损失','每周工作时间','国籍','收入'
])
salary=df['收入']
salary[df['收入']==' <=50K']=1
salary[df['收入']==' >50K']=0
print(df)