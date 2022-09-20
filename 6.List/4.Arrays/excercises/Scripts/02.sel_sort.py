from array import *


def read_array(n):
    arr = []
    for i in range(0, n):
        num = int(input("num #{} :".format(i+1)))
        arr.append(num)
    return arr


def sel_sort(arr):
    for i in range(len(arr)):
        maxi = i
        for j in range(i+1, len(arr)):
            if arr[maxi] > arr[j]:
                maxi = j
        arr[i], arr[maxi] = arr[maxi], arr[i]
    return arr


def write_array(arr):
    for el in arr:
        print(el, end=" ")


array = read_array(5)
array = sel_sort(array)
write_array(array)
