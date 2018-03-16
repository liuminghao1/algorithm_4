

def less(a, b):
    return a < b


def list_exchange(_list, a, b):
    _list[a], _list[b] = _list[b], _list[a]


def merge(_list, low, middle, high):
    copy_list = [i for i in _list]  # 比较浪费空间 后面看看怎么优化

    left = low
    right = middle + 1

    for i in range(low, high+1):

        if left > middle:
            _list[i] = copy_list[right]
            right += 1
        elif right > high:
            _list[i] = copy_list[left]
            left += 1
        elif copy_list[left] > copy_list[right]:
            _list[i] = copy_list[right]
            right += 1
        else:
            _list[i] = copy_list[left]
            left += 1


def partition(_list, low, high):

    left = low
    right = high
    target = _list[low]  # 把第一个元素作为 切分元素
    while left < right:
        while _list[left] <= target:  # 左边开始查找一个大于 target 的元素
            left += 1
            if left == high:
                break

        while _list[right] >= target:  # 右边开始查找一个小于等于 target 的元素

            right -= 1
            if right == low:
                break
        if left >= right:
            break
        list_exchange(_list, left, right)  # 没到切分元素前 左右的数互相交换

    list_exchange(_list, low, right)  # right=left  把最后比较的数 和 切分元素 替换。

    return right

