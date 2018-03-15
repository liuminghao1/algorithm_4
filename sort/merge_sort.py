from utils.sort import merge


def top_merge_sort(_list, low, high):
    middle = low + (high-low) // 2
    if low >= high:
        return

    top_merge_sort(_list, low, middle)
    top_merge_sort(_list, middle+1, high)

    merge(_list, low, middle, high)


def low_merge_sort(_list, high):
    # high使用len获得，比真实下标多了1。

    step = 1
    for i in range(1, high):  # 子数组长度 1, 2, 4, 8, 16...

        if i == step:  # 暂时没找到好的方法来 输出这种步长的遍历，以后再优化   _step下同：
            _step = 0
            for j in range(0, high):

                if j == _step:

                    merge(_list, j, j+step-1, min(j+step*2-1, high-1))  # 归并排序当前2个数组的

                    _step += step*2  # 下一个循环开始 合并当前2个数组为一个数组
            step *= 2

