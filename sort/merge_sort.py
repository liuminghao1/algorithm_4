from utils.sort import merge


def top_merge_sort(_list, low, high):
    middle = low + (high-low) // 2
    if low >= high:
        return

    top_merge_sort(_list, low, middle)
    top_merge_sort(_list, middle+1, high)

    merge(_list, low, middle, high)

