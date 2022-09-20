
from array import *


def read_array(n):
    arr = array('i', [])
    for i in range(1, n+1):
        arr.append(int(input(f"enter num #{i}: ")))
    return arr


def reverse(arr):
    n = len(arr)
    for i in range(0, n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr


size = int(input("size of array: "))
a = read_array(size)
print(*reverse(a))

