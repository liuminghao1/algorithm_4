from utils.sort import partition, list_exchange


def quick_sort(_list, low, high):
    if low >= high:
        return
    target = partition(_list, low, high)
    # print(target, 'target')
    quick_sort(_list, low, target-1)
    quick_sort(_list, target+1, high)


def quick_3way(_list, low, high):
    if low >= high:
        return
    left = low
    middle = low + 1
    right = high
    target = _list[middle]

    while middle <= high:

        if _list[middle] < target:  # 把比切分元素小的数放到中下标左边, 坐下标和中下标右移一位，获得新未知数, 下次再比较
            list_exchange(_list, left, middle)
            left += 1
            middle += 1
        elif _list[middle] > target:  # 把比切分元素大的数放到中下标右边，中下标的数获得原右下标的未知数，右小标左一一位，获得新未知数。
            list_exchange(_list, middle, right)
            right -= 1
        else:
            middle += 1  # 相等 中下标右移一位

    quick_sort(_list, low, middle-1)
    quick_sort(_list, right+1, high)

