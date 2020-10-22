import pandas as pd
import numpy as np
datas = pd.date_range('20201022',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=datas,columns=['A','B','C','D'])
#输出某一列
print(df['A'])
print(df.A)
#输出某几行
print(df[0:3])  #前三行
print(df['20201022':'20201023'])    #前两行

#select by label:loc
#按照标签进行输出
print(df.loc['20201022'])
print(df.loc[:,['A','B']])
print('\n')
print(df.loc['20201022',['A','B']])
#select by label:iloc
#输出某部分 1-2行，1-2列
print(df.iloc[1:3,1:3])
#跳着输出
print(df.iloc[[1,3,5],1:3])
#Boolean indexing按照 是\否 输出
print(df)
#筛选df中元素大于8的
print(df[df.A>8])