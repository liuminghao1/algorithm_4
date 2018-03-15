import random
from sort.select_sort import select_sort
from sort.insert_sort import insert_sort
from sort.shell_sort import shell_sort
from sort.merge_sort import top_merge_sort, low_merge_sort
from utils.sort import merge




_list = [random.randint(0, 49) for i in range(0, 49)]
print(_list, '\ntest before')
low_merge_sort(_list,  len(_list))
print(_list, '\ntest after')
