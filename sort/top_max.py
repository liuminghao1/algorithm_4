import sys, re
from utils.api import MaxPQ, Transaction


def top_max():
    m = int(sys.argv[1])
    max_pq = MaxPQ(m)
    if not sys.stdin.isatty():
        for line in sys.stdin:
            line = list(filter(lambda x: x, line.strip().split(' ')))

            # ['Hoare', '2/10/2005', '4050.20'] 转为列表格式,  python3 filter 返回一个filter对象，用list转换为列表
            transaction = Transaction(line[0], line[1], line[2])
            max_pq.insert(transaction)

            if max_pq.size() > m:
                max_pq.del_min()

    # 书里还有个stack操作的，太麻烦了，直接输出吧
    while max_pq.is_empty():
        sys.stdout.write(str(max_pq.del_max()) + '\n')








