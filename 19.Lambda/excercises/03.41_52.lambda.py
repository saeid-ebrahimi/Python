# 41
print("#41")
list1 = ['Red', 'Green', 'Blue', 'White', 'Black']
lst1 = list(map(lambda x: x[::-1], list1))
print(lst1)

# 42
print("#42")
from functools import reduce
list2 = [2.2, 4.12, 6.6, 8.1, 8.3]
ans = reduce(lambda x, y: x*y, list2, 1)
print(ans)

# 43
print("#43")
from functools import reduce
list3 = [12, 34, -10.9, -2.3, -13]
ans2 = reduce(lambda x, y: x*y, list3)
print(ans2)

# 44
print("#44")
from functools import reduce
tup1 = ((10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3))
tup2 = tuple(reduce(lambda x, y: x*y, tu) for tu in tup1)
print(tup2)

# 45
print("45")
tup3 = (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))
tup4 = [tuple(filter(lambda x: x.isdigit() or x.replace('.', '', 1).isdigit(), t)) for t in tup3]
print(tup4)

# 46
print("46")
list4 = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
max_tup = max(enumerate(list4), key=lambda x: x[1])
min_tup = min(enumerate(list4), key=lambda x: x[1])
print(max_tup, min_tup)

# 47
print("#47")
list5 = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
list5.sort(key=lambda x: type(x) == str)
print(list5)

# 48
print("#48")
list6 = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
list6.sort(key=lambda x: int(x))
print(list6)

# 49
print("#49")
list7 = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
dic1 = dict(map(lambda x: (x, list7.count(x)), list7))
print(dic1)

# 50
print("#50")
list8 = ['orange', 'red', 'green', 'blue', 'white', 'black']
list9 = ['orange', 'black']
lst2 = list(filter(lambda x: x not in list9, list8))
print(lst2)

# 51
print("#51")
list10 = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
max1 = max(list10, key=lambda x: x[1])[1]
min1 = min(list10, key=lambda x: x[1])[1]
print(max1, min1)

# 52
print("#52")
list11 = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
lst3 = list(filter(lambda x: x is not None, list11))
print(lst3)
