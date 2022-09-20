import itertools
a = [1,2,4,677,80]
b = [23,65]
c = [20,70]
pro = tuple(itertools.product(a,b,c))
print(pro)
pro2 = list(itertools.product(b,c,repeat=4))
print(pro2)

per = tuple(itertools.permutations(a)) # all formations with different order
per = tuple(itertools.permutations(a,3))
print(per)
from pprint import *
com = itertools.combinations(a,3) # all possible combination with determined length without repeatation
pprint(list(com))
com_wr = itertools.combinations_with_replacement(a,3) # all possible combination with determined length with repeatation
pprint(list(com_wr))

ac = list(itertools.accumulate(a))
print(ac)
import operator
acc = list(itertools.accumulate(a,func=operator.mul))
print(acc)
acc = list(itertools.accumulate(a,func=max))
print(acc)
a = [3,1,2,6,9]
gb = itertools.groupby(a,key=lambda x: x < 3)
for k, val in gb:
    print(k, list(val))

b = [{'name': 'Tim', 'age': 25},
     {'name':'Mary', 'age': 30},
     {'name': 'Tom', 'age': 20},
     {'name':'rose', 'age': 25}]
gb2 = itertools.groupby(b, lambda x: x['age'] > 25)
for key, val in gb2:
    print(key,list(val))

for i in itertools.count(20,2):
    print(i, 'jim')
    if i == 70:
        break

a = [12, 45, 6, 88]
for i in itertools.cycle(a):
    print(i)

for i in itertools.repeat(1, 5):
    print(i)

for i in itertools.repeat(20, 5):
    print(i)