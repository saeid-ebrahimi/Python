

if __name__ == "__main__":
    # 17
    print('#17')
    student_data = {'id1':
                        {'name': ['Sara'],
                         'class': ['V'],
                         'subject_integration': ['english, math, science']
                         },
                    'id2':
                        {'name': ['David'],
                         'class': ['V'],
                         'subject_integration': ['english, math, science']
                         },
                    'id3':
                        {'name': ['Sara'],
                         'class': ['V'],
                         'subject_integration': ['english, math, science']
                         },
                    'id4':
                        {'name': ['Surya'],
                         'class': ['V'],
                         'subject_integration': ['english, math, science']
                         },
                    }

    dic = {}
    for key, val in student_data.items():
        if val not in dic.values():
            dic[key] = val

    print(dic)

    # 18
    dic2 = {}

    print("#18")
    if len(dic2) > 0:
        print("non empty dictionary")
    else:
        print("empty dictionary")

    if dic2:
        print('non empty dictionary')
    else:
        print("empty dictionary")

    # 19
    from collections import Counter
    print('#19')
    dic3 = {'a': 100, 'b': 200, 'c': 300}
    dic4 = {'a': 300, 'b': 200, 'd': 400}
    dic5 = dict(Counter(dic3) + Counter(dic4))
    print(dic5)

    dic6 = {}
    keys = set(dic3.keys()) | set(dic4.keys())
    for key in keys:
        dic6[key] = dic4.get(key, 0) + dic3.get(key, 0)
    print(dic6)

    # 20
    print('#20')
    list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
             {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    unique_values = set(val for dic in list1 for val in dic.values())
    print(unique_values)

    unique_values2 = []
    for d in list1:
        for value in d.values():
            unique_values2.append(value)
    unique_values2 = set(unique_values2)
    print(unique_values2)

    # 21
    print("#21")
    dic7 = {'1': ['a', 'b', 'c'], '2': ['d', 'e', 'f', 'g']}
    list4 = []
    list2 = list(dic7.values())
    for i in range(0, len(list2)):
        for k in range(i+1, len(list2)):
            for j in range(0, len(list2[i])):
                for m in range(0, len(list2[k])):
                    list4.append(list2[i][j]+list2[k][m])

    print(list4)
    print([x+y for x in list2[0] for y in list2[1]])
    from itertools import product
    for tup in product(*[value2 for value2 in dic7.values()]):
        print(''.join(tup), end=' ')
    list5 = list2.copy()
    print()
    # help(product())

    # 22
    print('#22')
    dic8 = {'a': 500, 'b': 5877, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
    lst = sorted(dic8, key=dic8.get)
    print(lst[:-4:-1])

    from heapq import nlargest
    print(nlargest(3, dic8, dic8.get))

    # 23
    print('#23')
    dic9 = {}
    list6 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
             {'item': 'item4', 'amount': 750}, {'item': 'item1', 'amount': 750},
             {'item': 'item3', 'amount': 700}, {'item': 'item2', 'amount': 650}]

    for dd in list6:
        if dd['item'] not in dic9:
            dic9[dd['item']] = 0
        dic9[dd['item']] += dd['amount']

    print(dic9)

    # 24
    print('#24')
    str1 = 'pycharm is awesome ide in world'
    dic10 = {}
    for ch in str1:
        if ch not in dic10:
            dic10[ch] = str1.count(ch)
    print(dic10)
