
from collections import deque

items = deque(['bob', 'mom'])
print(type(items))
print(items)

items.append('bro')
print(len(items))
print(items)

items.append('sis')
print(items)

items.extend(['babe', 'spouse'])
print(items)

'''
#double sided queue chars: 
items.appendleft('bro')
print(items)
items.extendleft(['babe', 'spouse'])
items.pop()
'''

first=items.popleft()
print(first)


if items:
    print(items)
else:
    print("items is empty")
