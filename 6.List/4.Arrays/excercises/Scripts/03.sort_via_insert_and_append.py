from array import *

def read_array_sorted(n):
    arr = array('i',[])
    for i in range(0, n):
        num = int(input("num #{} :".format(i+1)))
        for idx in range(len(arr)):
            if arr[idx] > num:
                arr.insert(idx, num)
                break
        else:
            arr.append(num)
    return arr


print(*(read_array_sorted(5)))
