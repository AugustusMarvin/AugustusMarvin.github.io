import numpy as np
a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(a, b)
c = b**2
d = 10*np.sin(a)
e = b < 3
f = array_3 = np.array([
    [1, 2],
    [2, 3]
])
g = np.arange(4).reshape((2,2))
print(c)
print(d)
print(e)
#元素各自相乘
print(g*f)
#点乘
print(np.dot(g,f))
print(g.dot(f))
