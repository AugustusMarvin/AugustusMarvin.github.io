import numpy as np

array = np.array(
    [[1,2,3],
    [2,3,4]]
)
print(array)
#行列数
print("行列数" + str(array.shape))
#维数
print("维数" + str(array.ndim))
#元素数
print("size" + str(array.size))
#type的定义：dtype=np.int 
array_1 = np.array([2, 32, 4], dtype=np.int)
array_2 = np.array([2, 32, 4], dtype=np.float)
print(array_1)
print(array_2)
#生成多行矩阵
array_3 = np.array([
    [1, 23, 5],
    [2, 3, 56]
])
print(array_3)
#生成指定类型的矩阵
#array_4 = np.zeros((5,5), dtype=np.int16)
#零矩阵
array_4 = np.zeros((5,5))
print(array_4)
#全1矩阵
array_5 = np.ones((5,5), dtype=np.int16)
print(array_5)
#全空矩阵
array_6 = np.empty((5,5))
print(array_6)
#按顺序排列指定步长矩阵
array_7 = np.arange(10, 20, 2)
print(array_7)
#.reshape((4,4))可设置行列
array_8 = np.arange(12, 28).reshape((4,4))
print(array_8)
#生成线段
#np.linspace(起始位置, 终结位置, 点数)
array_9 = np.linspace(1, 20, 5)
print(array_9)
array_9 = np.linspace(1, 20, 4).reshape((2, 2))
print(array_9)