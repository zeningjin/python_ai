import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
import time

time1 = time.time()
df = pd.read_csv(r'E:\AI精英2001\代码\day13\air_data.csv')
# pickle.dump(df,open('test.data','wb'))
# df = pickle.load(open('test.data','rb'))
# print(time.time()-time1)
df = df[['LOAD_TIME','SUM_YR_1','SUM_YR_2','SEG_KM_SUM','LAST_FLIGHT_DATE','avg_discount']]
# 消费时间间隔（观测窗口时间-最后一次飞行的时间）
# 把字符串类型转为日期类型
df['LOAD_TIME'] = pd.to_datetime(df['LOAD_TIME'])
#'2014/2/29  0:00:00'
df = df[df['LAST_FLIGHT_DATE']!='2014/2/29  0:00:00']
df['LAST_FLIGHT_DATE'] = pd.to_datetime(df['LAST_FLIGHT_DATE'])
# 组合新属性
df['SUM'] = df['SUM_YR_1']+df['SUM_YR_2']
df['Consumption_interval'] = (df['LOAD_TIME']-df['LAST_FLIGHT_DATE']).dt.days
df.drop(labels=['LOAD_TIME','SUM_YR_1','SUM_YR_2','LAST_FLIGHT_DATE'],axis=1,inplace=True)
df.dropna(inplace=True)
print(df)
index1 = df['SUM']!=0
index2 = ((df['avg_discount']==0) & (df['SEG_KM_SUM']==0))
data = df[index1 | index2]
s = StandardScaler()
data = s.fit_transform(data)
pd.DataFrame(data).to_csv('cleaned_data.csv',index=False,header=['SEG_KM_SUM','avg_discount','SUM','Consumption_interval'])




