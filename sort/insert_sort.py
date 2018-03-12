from utils.sort import less, list_exchange


def insert_sort(_list):
    length = len(_list)
    for i in range(1, length):
        for j in range(i, 0, -1):
            if less(_list[j], _list[j-1]):
                list_exchange(_list, j, j-1)
            else:
                break
