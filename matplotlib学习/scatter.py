import matplotlib.pyplot as plt
from random import choice
#使用scatter(函数来创建散点图
'''
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.scatter(2, 4, s=200)
plt.show()
'''
#通过给x\y轴各一个列表，来让scatter()函数创建含有多个点的散点图
'''
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=200)
plt.show()
'''
'''
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
x_values = list(range(1,100))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=200)
plt.show()
'''
#在plt.scatter(中传递实参edgecolor='none'，来删除散点图中各点的轮廓
#在plt.scatter(中传递实参c='颜色'，来将各点设置为自己想要的颜色
#也可以给实参c赋予rgb颜色，取值范围0-1
'''
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
x_values = list(range(1,1000))
y_values = [x**2 for x in x_values]
#plt.scatter(x_values, y_values, edgecolor='none', c='red', s=200)
plt.scatter(x_values, y_values, edgecolor='none', c=(0, 0, 0.9), s=200)
plt.show()
'''
#使用颜色映射  c=y_values, cmap=plt.cm.Blues
#使用.savefig函数来保存图表
#实参bbox_inchs='tight'将自动删除掉图表多余的空白
'''
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
x_values = list(range(1,1000))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=200)
plt.show()
plt.savefig("scatter.png", bbox_inchs='tight')
'''
'''
#创建一个随机漫步类
class RandomWalk():
    def __init__(self, ran_num=5000):
        #ran_num设定随机漫步多少个点
        self.ran_num = ran_num
        #所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        while len(self.x_values) < self.ran_num:
            x_direction = choice([1, -1])
            y_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4, 5])
            y_distance = choice([1, 2, 3, 4, 5])
            x_step = x_direction * x_distance
            y_step = y_direction * y_distance
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            #self.x_values[-1]为获取列表中最后一位的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)
def main():
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=20)
    plt.show()
while __name__ == "__main__":
    main()
'''
#创建一个随机漫步类
class RandomWalk():
    def __init__(self, ran_num=5000):
        #ran_num设定随机漫步多少个点
        self.ran_num = ran_num
        #所有随机漫步都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        while len(self.x_values) < self.ran_num:
            x_direction = choice([1, -1])
            y_direction = choice([1, -1])
            x_distance = choice([1, 2, 3, 4, 5])
            y_distance = choice([1, 2, 3, 4, 5])
            x_step = x_direction * x_distance
            y_step = y_direction * y_distance
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            #self.x_values[-1]为获取列表中最后一位的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

def main():
    #可以在创建类时赋值来改变创建点的数量
    rw = RandomWalk(50000)
    rw.fill_walk()
    pointnum = list(range(rw.ran_num))
    #在函数scatter(中传递实参c='red', edgecolors='none'来给点着色
    plt.scatter(rw.x_values, rw.y_values, c=pointnum, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    #使用.axes().get_xaxis().set_visible(False)和.axes().get_yaxis().set_visible(False)来选择x\y轴的坐标轴是否可见
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
while __name__ == "__main__":
    main()
