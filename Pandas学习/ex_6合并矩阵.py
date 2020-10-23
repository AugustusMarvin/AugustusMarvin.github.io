import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
print(df1)
print(df2)
print(df3)
print('\n')
#合并三个矩阵
#纵向合并
res1 = pd.concat([df1,df2,df3],axis=0)
print(res1)
#将索引重新排序
res2 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(res2)
#join,['inner','outer']
df4 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df5 = pd.DataFrame(np.ones((3,4))*1,columns=['c','d','e','f'],index=[2,3,4])
#默认join模式'outer'，将在没有元素的位置填充nan
res3 = pd.concat([df4,df5])
print(res3)
res4 = pd.concat([df4,df5],join='outer',axis=0,ignore_index=True)
print(res4)
#自然连接，合并两个矩阵中共有的索引部分
res5 = pd.concat([df4,df5],join='inner',axis=0,ignore_index=True)
print(res5)
#自然连接，合并两个矩阵中共有的索引部分，新版pandas不能用
#res6 = pd.concat([df4,df5], axis=1, join_axes=[df4.index])
#print(res6)
df6 = df1.copy() 
print(df6)
#利用append合并矩阵
df6 = df6.append([df2,df3],ignore_index=True)
print(df6)
#添加一行矩阵
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res6 = df6.append(s1,ignore_index=True)
print(res6)