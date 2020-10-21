import numpy as np
A = np.arange(3, 15).reshape((3, 4))
#分割np.split(对象矩阵,分割数目,axis=1按列0按行)
print(np.split(A,2,axis=1))
#按行分为三个矩阵
print(np.split(A,3,axis=0))
#np.split(不可以进行不等的分割
#进行不等的分割应使用np.array_split(
print(np.array_split(A,3,axis=1))
#按行进行分割.vsplit(

print(np.vsplit(A,3))
#按列进行分割.hsplit(
print(np.hsplit(A,2))