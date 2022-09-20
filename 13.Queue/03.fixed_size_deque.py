
from collections import deque

items = deque([],maxlen= 4)
print(type(items))
print(*items)
print(items.maxlen)

items.append('bro')
print(len(items))
print(*items)

items.append('sis')
print(*items)

items.extend(['babe', 'spouse'])
print(*items)

items.append('grandma') #remove first item
print(*items)

items.append('grandpa') #remove first item 
print(*items)

first=items.popleft()
print(first)


if items:
    print(*items)
else:
    print("items is empty")
