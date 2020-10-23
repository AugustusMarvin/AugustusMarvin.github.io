import pandas as pd
#读取数据
data = pd.read_csv('student.csv')
print(data)
#保存入student文件夹之中
data.to_pickle('student.pickle')