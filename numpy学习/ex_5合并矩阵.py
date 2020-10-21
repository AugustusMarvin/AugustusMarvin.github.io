import numpy as np

A = np.arange(3, 15).reshape((3, 4))
B = np.arange(16, 28).reshape((3, 4))
#两个矩阵的上下合并
print(np.vstack((A,B))) #vertical stack
C = np.vstack((A,B))
#两个矩阵的左右合并
D = np.hstack((A,B)) #horizontal stack
print(D)
print(A.shape, C.shape)
print(A.shape, D.shape)
E = np.ones((1,5), dtype=np.int16)
F = np.array([1,1,1,1,1])
print(E)
print(E.T)
print(F.T)
#给数列增加一个维度
#[1 1 1 1 1] 
#变为
#[[1 1 1 1 1]]
print(F[np.newaxis,:])
print(F[np.newaxis,:].T)
#多个矩阵的合并.concatenate(
#axis=0上下合并
G = np.concatenate((A,B,B,A),axis=0)
#axis=1左右合并
H = np.concatenate((A,B,B,A),axis=1)
print(G, H)