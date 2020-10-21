import numpy as np
A = np.arange(3, 15).reshape((3, 4))
print(A)
#简单使用=来进行复制，将会关联两个矩阵，一个矩阵变化将改变其他矩阵
B = A
C = A
D = B
print(A,B,C,D)
print(A[0])
print(A is B)
A[0]  =[1,2,3,4]
print(B[0])
print(D[0])
#deep copy不关联复制
B = A.copy()
A[0]  =[2,3,4,5]
print(B[0])