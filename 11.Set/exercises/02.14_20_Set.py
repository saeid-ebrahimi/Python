# 14
print("#14")
set1= {14, 16, 19}
print(max(set1))
print(min(set1))

# 15
print("#15")
print(len(set1))

# 16
print("#16")
print( 17 in set1)

# 17
set2 = {16,18,11}
print("#17")
print(set1.isdisjoint(set2))

# 18
print('#18')
print(set1.issuperset(set1))
print(set1.issuperset(set2))

#19
print('#19')
print(set1.difference(set2))
print(set1 - set2)

#20
print('#20')
set3 = set1.copy()
set1 -= set2
print(set1)
set3.difference_update(set2)
print(set3)
