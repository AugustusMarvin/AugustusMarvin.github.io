'''
L = [x * x for x in range(1, 100)]
print(L)
L = (x * x for x in range(1, 100))
print(L)
print(next(L))
for l in L:
    print(l)
'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'

def fib_1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        #print(b)
        a, b = b, a + b
        n += 1
    return 'done'
fib(10)
#fib_1(10)
for f in fib_1(10):
    print(f)