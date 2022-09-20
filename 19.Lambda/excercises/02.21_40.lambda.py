
# 21
print("#21")
list1 = [13, 14, 16, 18]
mul = 13
lst1 = list(map(lambda x: x * mul, list1))
print(*lst1)

# 22
print('#22')
list2 = ['php', 'w3r', 'Python', 'absolute', 'Java', 'aaa']
filtered_seq = filter(lambda el: el[0].isupper() and el[1:].islower(), list2)
# print(len(''.join(filtered_seq)))

sum1 = sum(list(map(lambda x: len(x), filtered_seq)))
print(sum1)

# 23
print('#23')
list3 = [-13, 14.5, -15.7, 134.7, 10, -100]
pos_sum = sum(list(filter(lambda x: x > 0, list3)))
neg_sum = sum(list(filter(lambda x: x < 0, list3)))
print(pos_sum)
print(neg_sum)

# 24
print('#24')
nums = range(12, 120)
lst2 = [num for num in nums if not any(map(lambda n: int(n) == 0 or num % int(n) != 0, str(num)))]
print(lst2)

# 25
print('#25')


def rearrange_bigger(n):
    # Break the number into digits and store in a list
    nums = list(str(n))
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False


print(rearrange_bigger(1302))

# 26
print('#26')
list4 = [[0], [1, 3, 12], [5, 7], [9, 11, 13, 55], [13, 15, 17]]
list5 = list(map(lambda x: len(x), list4))
list4.sort(key=len)
list5.sort()
list6 = list(zip(list5, list4))
maxi = max(list6, key=lambda x: len(x[1]))
mini = min(list6, key=lambda x: len(x[1]))
print(maxi)
print(mini)

# 27
print('#27')
list7 = [['orange', 'green'], ['white', 'black'], ['white', 'black', 'orange']]
list8 = list(map(lambda lst: sorted(lst), list7))
print(list8)

# 28
print('#28')
list9 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
print(sorted(list9, key=lambda x: len(x)))

# 29
print('#29')
list_val = ['Python', 3, 2, 4, 5, 'version']
lst3 = list(filter(lambda x: type(x) == int or type(x) == float, list_val))
print(max(lst3))

# 30
print("#30")
matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = sorted(matrix1, key=lambda l: sum(l))
print(matrix2)

# 31
print('#31')
list11 = ['Python', 'list', 'exercises', 'practice', 'solution']
desire_len = 6
lst4 = list(filter(lambda s: len(s) == desire_len, list11))
print(lst4)

# 32
print('#32')
list10 = [1, 'abc', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
print(len(list(filter(lambda el: type(el) == float, list10))))

# 33
print("#33")
str1 = "W3resource"
# help('any')
cond1 = any([let.islower() for let in str1])
cond2 = any([let.isupper() for let in str1])
cond3 = any([let.isdigit() for let in str1])
if cond3 and cond2 and cond1:
    print("valid")
else:
    print("invalid")

# 34
print('#34')
dict1 = {'Sara Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kira Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
lst5 = list(filter(lambda key: dict1[key][0] >= 6 and dict1[key][1] <= 70, dict1.keys()))
print(lst5)

# 35
print("#35")
list12 = [1, 2, 4, 6, 8, 10, 12, 14, 18, 16]
ans = not any(list(filter(lambda el1: el1[0] != el1[1], zip(list12, sorted(list12)))))
print(ans)

# 36
print("#36")
list13 = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knot', 91, 94), ('Beau Turnbull', 94, 98)]
n = 1
lst5 = list(map(lambda x: x[n], list13))
print(lst5)

# 37
print("#37")
list14 = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knot', 91, 94), ('Beau Turnbull', 94, 98)]
n2 = 1
list14.sort(key=lambda x: x[n2])
print(list14)

# 38
print("38")
list15 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list16 = [5, 8, 3]
lst5 = list(filter(lambda x: x not in list16, list15))
print(lst5)

# 39
print("39")
list17 = ['red', 'blue', 'black', 'white', 'green', 'orange']
str2 = 'g'

lst6 = list(filter(lambda x: str2 in x, list17))
print(lst6)

# 40
print("#40")
list18 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
list19 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
lst7 = [list(filter(lambda x:x in list19, lst)) for lst in list18]
print(lst7)
