from utils.sort import less, list_exchange


def shell_sort(_list):
    length = len(_list)

    step = 1
    while step < length//3:   # 分成个子数组 起点分别是 1 4 13 40....
        step = step * 3 + 1

    while step >= 1:
        for i in range(step, length):  # 从最后一个数组开始
            for j in range(i, 0, -step):  # 往上一个数比较, 使用插入排序。

                if less(_list[j], _list[j-step]):
                    list_exchange(_list, j, j-step)

        step //= 3  # 切换到前面一个数组
