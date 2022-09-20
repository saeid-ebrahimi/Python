
from collections import deque

items = deque()

while True:
    ans = input(":")
    if ans == 'n':
        if len(items) > 0:
            elem = items.popleft()
            print(elem)
        else:
            print("the queue is empty!")
        continue
    elif ans == 'x':
        for item in items:
            print(item)
        exit()
    elif ans == 's':
        print(len(items))
        continue
    else:
        items.append(ans)


