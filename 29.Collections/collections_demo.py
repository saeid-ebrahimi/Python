import collections_demo
a = "alireza haghighi"
d = collections_demo.Counter(a)
print(d)
print(d.most_common(4)[1][0])
print(*d.elements())

Point = collections_demo.namedtuple('Point', 'x,y,z')
pt = Point(12.5,18.89,9)
print(*pt)
print(pt.x,pt.y)

d={}
print(type(d))

od = collections_demo.OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print(od)
print(od['c'])

dc1 = collections_demo.defaultdict(int)
dc1['a']=3
print(dc1['b'])
dc2 = collections_demo.defaultdict(float)
dc2['a']=3
print(dc2['b'])
dc3 = collections_demo.defaultdict(str)
dc3['a']=3
print(dc3['b'])
dc4 = collections_demo.defaultdict(bool)
dc4['a']=3
print(dc4['b'])

dq = collections_demo.deque()
dq.append("goli")
dq.appendleft(23)
dq.insert(1,"gholmorad")

dq.popleft()
dq.popleft()
dq.extendleft([12,45,89.9,(4,34)])
print(dq)
dq.rotate(2)
print(dq)
dq.rotate(-3)
print(dq)




