import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
input_num = [1, 2, 3, 4, 5]
#plt.plot(x轴坐标, y轴坐标， linewidth=线条粗细)
plt.plot(input_num, squares, linewidth=5)
#设置图标标题，给坐标轴加标签
plt.title("Square Numbers", fontsize=24)
#xlabel、ylabel能够为每一条轴设置标题
#fontsize=能够设置字号
#tick_params能够设置刻度,axis=''指定了其中实参影响的是哪个轴
plt.xlabel("label", fontsize=14)
plt.ylabel("Squre of Value", fontsize=14)
#设置标度大小
plt.tick_params(axis='both', labelsize=14)
plt.show()