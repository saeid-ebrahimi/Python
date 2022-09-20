import sys
mygenerator = (i for i in range(1000) if i %2 ==0)
print(type(mygenerator))
print(sys.getsizeof(mygenerator))
mylist = [i for i in range(1000) if i %2 ==0]
print(type(mylist))
print(sys.getsizeof(mylist))