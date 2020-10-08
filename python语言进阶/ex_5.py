'''
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
'''
class Thing(object):
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    
    @property
    def value(self):
        #价格重量比
        return self.price / self.weight

def input_thing():
    #输入物品信息
    #split()
    #通过指定分隔符对字符串进行切片
    #并返回分割后的字符串列表（list）
    print("输入物品信息:")
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)

def main():
    '''
    第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。
    把函数依次作用在list中的每一个元素上，得到一个新的list并返回。注意，map不改变原list，而是返回一个新list。
    '''
    max_weight = input("max weight")
    number_of_things = input("number of things")
    all_things = []
    for _ in range(0, int(number_of_things)):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print("小偷拿走了" + thing.name)
            total_weight += thing.weight
            total_price += thing.price
    print("总价值" + total_price)

if __name__ == '__main__':
    main()