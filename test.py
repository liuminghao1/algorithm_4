import random
from sort.select_sort import select_sort
from sort.insert_sort import insert_sort
from sort.shell_sort import shell_sort
from sort.merge_sort import top_merge_sort, low_merge_sort
from utils.sort import merge
from sort.quick_sort import quick_sort




_list = [random.randint(0, 49) for i in range(0, 49)]
# _list = [0,2,1]
print(_list, 'test before')
quick_sort(_list, 0, len(_list)-1)
print(_list, 'test after')
