from recursion import *
from recursion_amok import *
import os

bad_fibonacci(8)
print(factorial(4))
draw_ruler(2, 3)
data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
print(binary_search(data, target=22, low=0, high=len(data)))
disk_usage(os.getcwd())
