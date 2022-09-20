
from array import *
from numpy import matlib as ml
import numpy as nm


def make_zeros_arr():
    n = int(input("enter size of table"))
    a = ml.zeros((n, n))
    return a


def check_idx(i, j, n):
    if i > n:
        i = 0
    if i < 0:
        i = n
    if j > n:
        j = 0
    if j < 0:
        j = n
    return [i, j]


def put_num(arr):
    i = 0
    n = arr.shape[0]
    j = (n-1) // 2
    arr[i, j] = 1
    for num in range(2, n**2 + 1):
        i1 = i-1  # up
        j1 = j-1  # left
        [i1, j1] = check_idx(i1, j1, n - 1)
        if arr[i1, j1] != 0:
            i1 = i+1  # down
            j1 = j
            [i1, j1] = check_idx(i1, j1, n - 1)
        arr[i1, j1] = num
        i = i1
        j = j1
    return arr


def print_table(arr):
    for x in range(arr.shape[0]):
        for y in range(arr.shape[1]):
            print(int(arr[x, y]), end='  ')
        print()


print(put_num(make_zeros_arr()))
print_table(put_num(make_zeros_arr()))
