from utils.sort import partition


def quick_sort(_list, low, high):
    if low >= high:
        return
    target = partition(_list, low, high)
    # print(target, 'target')
    quick_sort(_list, low, target-1)
    quick_sort(_list, target+1, high)



