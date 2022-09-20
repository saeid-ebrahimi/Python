import sys 
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums 

def firstn_generator(n):
    num = 0
    while num < n:
        yield num 
        num += 1

print(sum(firstn(999)))
print(sum(firstn_generator(999)))

print(sys.getsizeof(firstn(999)))
print(sys.getsizeof(firstn_generator(999)))
