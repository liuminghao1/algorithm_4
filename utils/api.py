

# 2.4.1的 优先队列api

class MaxPQ(object):
    # 最大优先队列

    def __init__(self, max_number=0):
        # 可以初始化一个列表，或者创建一个初始容量为max的优先队列
            self.queue = []
            self.max_number = max_number

    def insert(self, value):
        index = len(self.queue)
        if not self.max_number or self.max_number >= self.size():
            for v in reversed(self.queue):
                if v <= value:
                    break
                index -= 1
            self.queue.insert(index, value)

    def del_max(self):
        if self.queue:
            return self.queue.pop(-1)

    def del_min(self):
        if self.queue:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue)

    def size(self):
        return len(self.queue)



class Transaction(object):
    """一个交易类"""

    def __init__(self, name, date, amount):
        self.name = name
        self.date = date
        self.amount = amount

    def __str__(self):
        return "{0} {1} {2}".format(self.name, self.date, self.amount)

    def __le__(self, other):
        return float(self.amount) <= float(other.amount)


