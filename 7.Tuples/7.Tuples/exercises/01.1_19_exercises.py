

if __name__ == '__main__':
    # 1
    tup1 = (12, 45, 11)
    print(tup1)
    # 2
    tup2 = 'rose', (23, 14), 45, ['a', 'c']
    print(tup2)
    # 3
    print(tup1[0:2])
    # 4
    name, tup, num, list1 = tup2
    print(list1)
    # 5
    tup1 = tup1 + tup2[1] + (12,)
    print(tup1)
    # 6
    str1 = str(tup2)
    print(str1)
    # 7
    print(tup1[3], tup1[-4])
    # 8
    tup3 = tup2
    print(tup3)
    # 9
    rep = tup3.count(14)
    print(rep)
    # 10
    for idx in range(len(tup1)):
        for i in range(idx+1, len(tup1)):
            if tup1[idx] == tup1[i]:
                print(tup1[idx])
    # 11
    print(13 in tup1)
    # 12
    print(list(tup2))
    # 13
    if 14 in tup1:
        ls = list(tup1)
        ls.remove(14)
        tup1 = tuple(ls)
    print(tup1)
    t2 = tup1
    t = ()
    for item in t2:
        if item != 12:
            t = t + (item,)
    t2 = t
    print(t2)

    # 14
    print(tup1.index(11))
    # 15
    print(len(tup2))
    # 16
    t = ('a', 34), ('al', 31), (20, 'kk')
    d = dict((x, y) for x, y in t)
    dd = {}
    for x, y in t:
        dd[x] = y
    print("#16: ")
    print(d)
    print(dd)

    # 17
    lst = [(12, 4), (14, "rose"), ('mike', 40)]
    lstt = list(zip(*lst))
    print("#17:")
    print(lstt)
    t1 = ()
    t2 = ()
    for x, y in lst:
        t1 = t1 + (x,)
        t2 = t2 + (y,)
    lstt = [t1, t2]
    print(lstt)
    # 18
    print("#18:")
    t3 = tup2
    t3 = t3[::-1]
    print(t3)
    # 19
    print('#19:')
    lst2 = [(12, 4), (14, "rose"), ('mike', 40)]
    d2 = dict((x, y) for x, y in lst2)
    print(d2)
    d3 = {}
    for (x, y) in lst2:
        d3[x] = y