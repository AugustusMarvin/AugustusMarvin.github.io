import pandas as pd
import numpy as np

datas = pd.date_range('20201022',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=datas,columns=['A','B','C','D'])

df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)
#丢掉含有nan的行
print(df.dropna(axis=0,how='any')) #how={'any','all'}
#只有一行全为nan时才舍弃
print(df.dropna(axis=0,how='all')) #how={'any','all'}
#在A中至少有一个是nan时才会返回true
print(np.any(df.isnull()) == True) #how={'any','all'}
#在nan中填入0
print(df.fillna(value=0)) #how={'any','all'}