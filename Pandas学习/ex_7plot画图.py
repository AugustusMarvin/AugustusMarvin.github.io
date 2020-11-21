import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plot data

#Series 随机生成1000个数据
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
#把数据进行累加
data = data.cumsum()
#DataFrame
#生成了四组数据,分别命名为ABCD
data_1 = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list("ABCD"))
data_1 =data_1.cumsum()
#data_1.plot()
#plt.show()

#数据点
#plot methods:
#'bar',hist,box,kde,area,scatter,hexbin,pie
ax = data_1.plot.scatter(x='A',y='B',color='DarkBlue',label='Class 1')
data_1.plot.scatter(x='A',y='C',color='DarkGreen',label = 'Class 2',ax=ax)
plt.show()
'''
data.plot()
plt.show()
'''