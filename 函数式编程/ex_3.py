def now():
    print('2020-10-11')
f = now
f()

print(now.__name__)
print(f.__name__)