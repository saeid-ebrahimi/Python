# 32
print('#32')
tup=((1, 2, 6), (2, 3, -6), (13, 7))
lst=[]
for t in tup:
	sum=0
	for num in t:
		sum+=num
	lst.append(sum)
print(lst)

#33
print('#33')
list7=[(1, 2, 6), (2, 3, -6), (13, 7)]
lst=[]
for tup in list7:
	lst.append(list(tup))
print(lst)