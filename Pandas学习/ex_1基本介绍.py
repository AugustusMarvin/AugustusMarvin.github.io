import pandas as pd
import numpy as np
#pd生成一个列表
s = pd.Series([1,3,6, np.nan, 44, 1])
print(s)
#生成矩阵
#生成行索引
datas = pd.date_range('20201022',periods=6)
print(datas)
#pd.DataFrame(生成矩阵
# 列索引columns=['a','b','c','d'] index=datas行索引
df = pd.DataFrame(np.random.randn(6,4),index=datas,columns=['a','b','c','d'])
print(df)
# 列索引 行索引默认为数字从0开始
df_1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df_1)
#几种在矩阵中输入数据的方法
df_2 = pd.DataFrame({'A':1.,
    'B':pd.Series([1,3,6,1]),
    'C':np.array([3]*4,dtype='int32'),
    'D':pd.Timestamp('20201022'),
    'E':pd.Series(1,index=list(range(4)),dtype='float32'),
    'F':'Zero'})
print(df_2)
print(df_2.dtypes)
print(df_2.index)
print(df_2.columns)
print(df_2.values)
print(df_2.describe())
print(df_2.T)
#倒序排序
#列倒序
print(df_2.sort_index(axis=1, ascending=False))
#行倒序
print(df_2.sort_index(axis=0, ascending=False))
#对某一列行里的值进行排序
print(df_2.sort_values(by='B'))