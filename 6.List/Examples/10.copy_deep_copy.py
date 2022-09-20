x = [[1,2,3],['bob','sis','mom'],[(1,3),(2,4)]]

#assignment
y = x
y[0].append(66)
print(x)

#copy
z = x[:]
z[0].append(99)
print(x)

q = x.copy()
q[1].append('bro')
print(x)

#deep copy
from copy import deepcopy
w = deepcopy(x)
w[1].append('babe')
print(x)
