# @property能够将一个方法变为属性进行调用
def main():
    items = list(map(int, input().split()))
    overall = partial = items[0]
    for i in range(1, len(items)):
        partial = max(items[i], partial + items[i])
        overall = max(partial, overall)
    print(overall)

if __name__ == '__main__':
    main()