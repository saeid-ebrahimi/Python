# 26
print('#26')
tup = (4, 3, 2, 2, 1, 18)
acc =1
for num  in tup:
    acc *= num
print(acc)

# 27
print('#27')
lst= []
acc2 = 0
tup2 = ((10, 12, 24, 66), (34, 26, 13), (1, 10, 14))
for t in tup2:
    for items in t:
       acc2 += items
    lst.append(acc2/len(t))
print(lst)

# 28
tup4 = ()
print('#28')
tup3 = (('234','11'),('24','453','11'))
for t in tup3:
    tp = ()
    for st in t:
        tp = tp + (int(st),)
    tup4 += (tp,)
print(tup4)

# 29
print('#29')
st = ''
tup5 = (10, 12, 24, 66)
for num in tup5:
    st += str(num)
num = int(st)
print(num)

# 30
print('#30')
tup6 = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
for t in tup6:
    for color in t:
        if color == 'Pink':
            print('Finded')

# 31
print('#31')
lst3 = [(1, 2, 3, 4), (3, 5, 2, 1), (2, 2, 3, 1)]
list6 = [0,0,0,0]
for tup in lst3:
    for i in range(0,len(tup)):
        list6[i] += tup[i]
print(tuple(list6))
    

