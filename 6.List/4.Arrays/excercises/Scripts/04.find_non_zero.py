from array import *


def read_array():
    arr = array('i', [])
    n = int(input("enter number of elements: "))
    for cnt in range(0, n):
        num = int(input("enter num #{} :".format(cnt+1)))
        arr.append(num)
    return arr


def operation(nums):
    mid = len(nums) // 2
    if nums[mid] != 0:
        nums /= nums[mid]
        return nums
    else:
        idx = 1
        sign = 1
        for i in range(mid+1):
            num = nums[mid + sign * idx]
            if num != 0:
                d_num = array('f', [])
                for c in range(len(nums)):
                    d_num.append(nums[c]/num)
                return d_num
            if sign == 1:
                idx += 1
            sign *= -1
        print("all elements are zero!")
        return array('i', [])


print(*operation(read_array()))
