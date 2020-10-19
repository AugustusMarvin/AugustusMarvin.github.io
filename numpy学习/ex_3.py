import numpy as np
a = np.random.random((2,4))
print(a)
#求和
#所有元素相加
print(np.sum(a))
#按列求和
print(np.sum(a,axis=0))
#按行求和
print(np.sum(a,axis=1))
#其他函数中也可以用axis=
print(np.min(a))
print(np.max(a))
print("-------------")
b = np.arange(2,17).reshape((3,5))
print(b)
#最大值最小值的索引
print(np.argmin(b))
print(np.argmax(b))
#求平均值三方法
print(np.mean(b))
print(b.mean())
print(np.average(b))
#中位数
print(np.median(b))
#生成各元素按顺序累加的矩阵
print(np.cumsum(b))
#生成各元素按顺序累差的矩阵
print(np.diff(b))
#输出非零数
#输出两个一行矩阵，分别为对应元素的行列数
print(np.nonzero(b))
#对矩阵中元素排序
print(np.sort(b))
#转置矩阵
print(np.transpose(b))
print(b.T)
#转置矩阵点乘
print((b.T).dot(b))
#np.clip(截取功能
#np.clip(b, i, j)
#b为目标矩阵
#小于i的数全部置i 
#大于j的数全部置j
print(np.clip(b, 5, 9))