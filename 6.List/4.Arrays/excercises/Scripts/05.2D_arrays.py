
from array import *
import numpy
import numpy.matlib as nm
from random import randint


def make_2d_array(n, m):
    a = nm.empty((n, m), dtype='i')
    for i in range(0, n):
        for j in range(0, m):
            a[i, j] = randint(0, 30)
    return a


a = make_2d_array(4, 5)
s = nm.sum(a)
av = nm.average(a)
rmax = nm.amax(a, axis=1)
rmin = nm.amin(a, axis=1)
cmax = nm.amax(a, axis=0)
cmin = nm.amin(a, axis=0)
print("2D array is ", a)
print("it's sqrt is ", nm.sqrt(a))
print("array power 3 is ", nm.power(a, 3))
print("sum is ", s)
print("average is ", av)
print("row max is ", rmax)
print("row min is ", rmin)
print("column max is ", cmax)
print("column min is ", cmin)


