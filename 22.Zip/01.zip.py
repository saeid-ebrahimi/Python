number = [123,56,187]
letters = ('a','b','c')
floates = {12.6,5.6,8.76}
ranges = range(12)
zipped = zip(number,letters)
print(zipped)
print(list(zipped))
z2 = zip(number)
print(*z2)
z3 = zip(letters, number, floates,ranges)
print(*z3)
dic = {k:v for k,v in zip(letters,list(zip(number,floates)))}
print(dic)
d2 = {k:v for v,k in enumerate(letters)}
print(d2)
