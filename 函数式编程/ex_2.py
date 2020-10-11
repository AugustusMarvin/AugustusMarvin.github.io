def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

m = lazy_sum(1, 2 , 3, 5)
print(m())

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
f = lambda x, y: x > y
if f(6, 5):
    print("True")
def build(x, y):
    return lambda: x * x + y * y
i  = build(1, 2)
print(i())