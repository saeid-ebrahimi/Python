
from array import *


def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
    return num


def find_all_primes(num):
    primes = array('i',[])
    for i in range(2, num):
        p = prime(i)
        if p != 0:
            primes.append(p)
    return primes


def find_desire_nums(num):
    ans = []
    primes = find_all_primes(num)
    for idx in range(0, len(primes)):
        for i in range(idx+1, len(primes)):
            if primes[idx] + primes[i] == num:
                ans.append([primes[idx], primes[i]])
    return ans
ans = ""
while ans != 'exit':
    num = int(input("enter an even number greater than 6: "))
    if num > 6 and num % 2 == 0:
        print(*find_desire_nums(num))
    else:
        print("invalid entered number")
    ans = input("continue?(enter exit to finish!) ")
