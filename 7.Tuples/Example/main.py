

if __name__ == '__main__':
    # 20
    print('#20')
    tup = (13, 24, 17.5, 'aunt')
    print("there is a tuple {}".format(tup))

    # 21
    print("#21")
    list1 = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
    list1 = [t[:-1]+(120,) for t in list1]
    print(list1)

    lst = []
    for t1 in list1:
        t1 = t1[0:-1]+(80,)
        lst.append(t1)
    print(lst)

    # 22
    print("#22")
    list2 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d',)]
    for i in range(0, list2.count(())):
        list2.remove(())
    print(list2)

    # 23
    print('#23')
    list3 = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    lst2 = [list3[0]]
    for s, num in list3[1:]:
        if num < lst2[0][1]:
            lst2.append((s, num))
        else:
            lst2.insert(0, (s, num))
    print(lst2)
    # 24
    print("#24")
    list4 = [12, 34, 1, 23, (12,), 25]
    cnt = 0
    for item in list4:
        if type(item) is tuple:
            print(cnt)
            break
        else:
            cnt += 1
    # 25
    print('#25')
    tuple1 = ()
    str1 = "python 3 is awesome!"
    for ch in str1:
        tuple1 += (ch,)
    print(tuple1)

