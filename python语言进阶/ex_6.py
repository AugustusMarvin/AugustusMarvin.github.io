def quick_sort(items, comp=lambda x, y: x <= y):
    items = list(items)[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items

def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        print("pos" + str(items[pos]))
        #print(pos)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        #不比pivot元素大才触发
        #将第i,j两个元素交换
        if comp(items[j], pivot):
            i += 1
            print(str(items[i]) + "," + str(items[j]))
            items[i], items[j] = items[j], items[i]
            print(items)
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1

nums = [2, 3, 4, 6, 3, 1, 11, 8]
n_nums = quick_sort(nums)
print(n_nums)