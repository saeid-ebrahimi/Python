
from array import *
from numpy import matlib as ml
import numpy as nm


def read_array(n, m):
    arr = ml.zeros((n, m))
    for i in range(0, n):
        for j in range(m):
            arr[i, j] = int(input(f"enter element [{i}][{j}]: "))
    return arr


def max_in_row(arr):
    rows = arr.shape[0]
    cols = arr.shape[1]
    a = []
    for i in range(rows):
        a.append(0)
        for j in range(cols):
            if a[i] < arr[i, j]:
                a[i] = arr[i, j]
    return a


my_arr = read_array(4, 4)

print(*max_in_row(my_arr))


