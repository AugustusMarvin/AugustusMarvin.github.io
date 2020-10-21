import numpy as np

A = np.arange(3, 15).reshape((3, 4))
print(A)
#print(' \n')
#按行列检索其中的某一项
print(A[2][3])
print(A[2, 3])
#找某一列
print(A[:,1])
#找某一行
print(A[1,:])
print("\n")
#找某一段元素
#第二行第第一个到第二个
print(A[1,0:2])
#第三列第第一个到第三个
print(A[0:3,3])
print("\n")
#迭代默认为按行
for row in A:
    print(row)
print("\n")
for col in A:
    print(col)
print("\n")
#按列迭代
for column in A.T:
    print(column)
#按元素迭代
print(A.flatten())
for item in A.flat:
    print(item)