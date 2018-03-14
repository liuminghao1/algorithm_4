from sort.select_sort import select_sort
from sort.insert_sort import insert_sort
from sort.shell_sort import shell_sort
from sort.merge_sort import top_merge_sort
from utils.sort import merge


_list = [1,2,3,4,5,19, 82,  10, 11, 12,12,13,15, 78,32,62,96,31,100]
top_merge_sort(_list, 0, len(_list)-1)
print(_list)
