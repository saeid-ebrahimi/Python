# Generators are memory efficient for large data
def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
#print(sorted(g,reverse=True))
#print(sum(g))

'''
value = next(g)
print(value)
value = next(g)
print(value)

value = next(g)
print(value)
value = next(g)
print(value)
'''
'''
for i in g:
    print(i)
'''