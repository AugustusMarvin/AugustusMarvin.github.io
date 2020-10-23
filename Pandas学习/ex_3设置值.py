import pandas as pd
import numpy as np

datas = pd.date_range('20201022',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=datas,columns=['A','B','C','D'])

df.iloc[2,2] = 1111
df.loc['20201023','B']=2222
print(df)
#将A中>4的数字全部换成0
df[df.A>4]=0
df['E'] = np.nan
df['F'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))
print(df)