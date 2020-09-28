#查找方法
def seq_search(items, key):
    for index in range(len(items)):
        if items[index] == key:
            return index
    return -1

def bin_search(items, key):
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

Shuzu = [1, 4, 5, 6, 8, 10]
print(seq_search(Shuzu, 4))
print(bin_search(Shuzu, 4))