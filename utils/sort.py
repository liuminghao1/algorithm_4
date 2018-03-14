

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
