import itertools
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09 
}
#用股票价格大于100元的股票再创建一个新的字典
prices_2 = {key: value for key, value in prices.items() if value > 100}
print(prices_2)

#产生ABCD的全排列
a = itertools.permutations('ABCD')
for i in a:
    print(i)
#产生ABCDE的5选3组合
b = itertools.combinations('ABCDE', 3)
for i in b:
    print(i)
#产生ABCD和123的笛卡尔积
c = itertools.product('ABCD', '123')
for i in c:
    print(i)
#产生ABC的无限循环序列
d = itertools.cycle(('A', 'B', 'C'))
#for i in d:
    #print(i)


names = ['guan', 'zhang', 'zhao', 'ma', 'huang']
courses = ['math', 'chinese', 'english']
scores = [[None] * len(courses) for i in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)

