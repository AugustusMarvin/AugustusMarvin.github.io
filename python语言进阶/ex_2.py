def select_sort(items, comp=lambda x, y: x < y):
    #的意思是创建一个函数,带两个参数x和y,返回x<y是否为真
    #简单选择排序
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

def bubble_sort(items, comp=lambda  x, y: x > y):
    "冒泡排序"
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items

def bubblee_sort(items, comp=lambda  x, y: x > y):
    "搅拌排序"
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
            if swapped:
                swapped = False
                for j in range(len(items) - 2 - i, i, -1):
                    if comp(items[j-1], items[j]):
                        items[j], items[j - 1] = items[j - 1], items[j]
                        swapped = True
            if not swapped:
                break
    return items

def merge(items1, items2, comp=lambda x, y: x < y):
    #合并两个有序列表
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items
'''
def _merge_sort(items, comp=lambda x, y: x > y):
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)
'''

def _merge_sort(items):
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid])
    right = _merge_sort(items[mid:])
    return merge(left, right)

Shuzu = [2, 3, 4, 1, 6, 4]
Shuzuu = [1, 3, 4, 6, 8]
Shuzuuu = [2, 6, 8, 10, 14]
Shuzu = select_sort(Shuzu)
Shuzu_1 = bubble_sort(Shuzu)
Shuzu_2 = bubblee_sort(Shuzu)
Shuzu_3 = _merge_sort(Shuzu)
Shuzu_4 = merge(Shuzuu, Shuzuuu)
print(Shuzu)
print(Shuzu_1)
print(Shuzu_2)
print(Shuzu_3)
print(Shuzu_4)