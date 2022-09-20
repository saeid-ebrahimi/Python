#1
print('#1')
set1={'Mike', 'Rose', 'Artemis', 14, 10, 2021}
print(set1)

# 2
print('#2')
for item in set1:
	print(item)
	
# 3
print('#3')
set1.add((12,6))
print(*set1)

# 4
print('#4')
if 'Rose' in set1:
	set1.remove('Rose')
print(set1)

# 5
print('#5')
set1.discard('Mike')
print(set1)

#6
print('#6')
set2 = {'Artemis',  'Saeid', 'Mike',2020}
print(set1.intersection(set2))
print(set1 & set2)
#7
print('#7')
print(set1.union(set2))
print(set1 | set2)

#8
print('#8')
print(set1.difference(set2))
print(set1 - set2)

#9
print('#9')
print(set1.symmetric_difference(set2))
print(set1 ^ set2)

#10 
print('#10')
print(set1.issubset(set2))
print(set1 < set2)
print(set1 <= set2)

print(set1.issuperset(set2))
print(set1> set2)
print(set1>= set2)

#11
print('#11')
set3 = set1.copy()
set3.add('zara')
print (set1, set3, sep='\n')

#12
print('#12')
set3.clear()
print(set3)

#13
print('#13')
set4=frozenset(set1) 
#set4.discard('saeid') #attribute error
#set4.clear() #attribute error
print(set4 | set2)

#14 
print('#14')
set5= {12, 15, 20, 14, 60}
