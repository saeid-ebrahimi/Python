
from array import *


def prime(n):
    a = array('i', [])
    for num in range(2, n + 1):
        cnt = 0
        for i in range(1, num + 1):
            if num % i == 0:
                cnt += 1
            if cnt > 2:
                cnt = 0
                break
        else:
            a.append(num)
    return a


arr = prime(100)
print(arr)
print(type(arr))
for idx in range(0, len(arr)):
    print(arr[idx], end=" ")
