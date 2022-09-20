# 1
print("#1")
y = lambda x: x + 15
print(y(15))

# 2
print('#2')
import random

def weired(n):
	return lambda x: x*n


times = 2
result = weired(times)
num = 18
print(f"{times} times number {num} is {result(num)}")


time = 4
result = weired(time)
num = 20
print(f"{time} times number {num} is {result(num)}")

# 3
print('#3')
list1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
list1.sort(key=lambda x: x[1])
print(list1)

# 4
print("#4")
list1 = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
list1.sort(key=lambda x:x["color"])
print(list1)

# 5
print("#5")
list2 = [12, 19, 17, 26, 13]
list2 = list(filter(lambda x: x % 2 == 0, list2))
print(list2)

# 6
print("#6")
list3 = [12, 15, 21, 8, 10]
list3 = list(map(lambda x: x*x, list3))
print(list3)

# 7
print('#7')
ch = 'l'
y = lambda x: x[0] == ch
print(y('lambda'))

# 8
print('#8')
from datetime import datetime
current = datetime.now()
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()
print(year(current))
print(month(current))
print(day(current))
print(time(current))

# 9
print('#9')
num = lambda x: x.replace('.','',1).isdigit()
check_num = lambda x: x[1:] if x[0]=='-' else x
inp = '-12.34'
print(num(check_num(inp)))
inp2 = '2.344'
print(num(check_num(inp2)))
inp3 = '1578'
print(num(check_num(inp3)))
inp4 = 'r3.34'
print(num(check_num(inp4)))

# 10
print('#10')
from functools import reduce
fibonacci = lambda n: reduce(lambda x, y: x+[x[-1] + x[-2]], range(n-2), [1, 1])
print(fibonacci(6))
print(fibonacci(12))

# 11
print("#11")
list4 = [12, 15, 27, 18, 30, 21]
list5 = [12, 18, 44, 32, 45]
list6 = list(filter(lambda x: x in list4, list5))
print(list6)
list7 = list(set(list4) & set(list5))
print(list7)

# 12
print("#12")
list8 = [12, 3, 14, 5, -2, -20, -10]
list8.sort(key=lambda x: 0 if x == 0 else 1/x)
print(list8)

# 13
print("#13")
list9 = [12, 15, 27, 18, 30, 21, 33]
even = len(list(filter(lambda x: x % 2 == 0, list9)))
odd = len(list(filter(lambda x: x % 2 == 1, list9)))
print(even, odd)

# 14
print('#14')
names = ["Gholi", "Goli", "Golam", "Ghanbar", "Changiz", "Jamshid", "Kamran"]
cnt = len(list(filter(lambda x: len(x) == 6, names)))
print(cnt)

# 15
print("#15")
nums1 = [12, 15, 27, 18, 30]
nums2 = [12, 18, 44, 32, 45]
list10 = list(map(lambda x, y: x + y, nums1, nums2))
print(list10)

# 16
'''
print("#16")
number = int(input("number of students: "))
students = []
for i in range(number):
	stu_name = input("Enter name of student: ")
	mark = float(input("enter student mark: "))
	students.append([stu_name, mark])

students.sort(key=lambda x: x[1])
for lst in students:
	if lst[1] != students[0][1]:
		sec_min = lst
		break
print(sec_min)
'''
# 17
print("#17")
lst2 = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
new_list = list(filter(lambda x: (x % 19 == 0) or (x % 13 == 0),lst2))
print(new_list)

# 18
print('#18')
lst3 = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
lst4 = list(filter(lambda x: x == ''.join(reversed(x)), lst3))
print(lst4)

# 19
print("#19")
from collections import Counter
lst5 = ["bcda", "abce", "cbda", "cbea", "adcb"]
str1 = 'abcd'
lst6 = list(filter(lambda x: Counter(x) == Counter(str1), lst5))
print(lst6)

# 20
print("#20")
str2 = "sdf -23 safs8 5.64 sdfsd8 sdfs 56 21sfs 20 5"
words = str2.split(" ")
lst7 = list(filter(lambda x:x.replace('.', '', 1).isdigit() or x.replace('.','',1 )[1:].isdigit(), words))
print(lst7)
