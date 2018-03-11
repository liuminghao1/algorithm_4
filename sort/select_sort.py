
from utils.sort import less, list_exchange


def select_sort(_list):
    length = len(_list)

    for i in range(0, length):
        minimum = i
        for j in range(i+1, length):
            if less(_list[j], _list[minimum]):
                minimum = j
        list_exchange(_list, i, minimum)  # 把最少的值放到左边


if __name__ == "__main__":
    _list = [0, 9, 2, 8, 3, 7, 4, 5, 6]
    select_sort(_list)
    print(_list)



