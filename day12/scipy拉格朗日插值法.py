import pandas as pd
from scipy.interpolate import lagrange

df = pd.read_excel(r'E:\AI精英2001\代码\day12\catering_sale.xls')
df1 = df.iloc[9:20,:]
new_df = df1.dropna()
df['销量'][14] = lagrange(x=list(new_df.index),w=list(new_df['销量']))(14)
print(df)
df['日期'] = df['日期'].dt.date.apply(str)
df.to_excel(r'E:\AI精英2001\代码\day12\new_catering_sale.xls',index=False)