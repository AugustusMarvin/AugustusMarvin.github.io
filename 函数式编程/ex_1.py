from functools import reduce
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
def add(x, y):
    return x * y
i = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(i)
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, li)))
#Python strip() 方法
#用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
def not_empty(n):
    return n and n.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter()#初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)#构建新序列
for i in primes():
    if i < 1000:
        #输出1000以内的素数
        print(i)
    else:
        break