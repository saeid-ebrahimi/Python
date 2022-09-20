


if __name__ == "__main__":

    dict2 = {'Name' : 'Mahnaz' , 'Age' : 27}
    dict3 = {'Name' : 'Abid' , 'Age' : 27}
    # 1
    dict1 = {'Name' : 'Zara' , 'Age' : 7 , 'Year' : 2020}
    print('#1')
    print(sorted(dict1))
    print(sorted(dict1, reverse=True))

    # 2
    print('#2')
    d = {'Grade':17}
    dict1.update(d)
    dict1['Sex'] = 'female'
    print(dict1)

    # 3
    print('#3')
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    dic4 = {}
    dic4.update(dic1)
    dic4.update(dic2)
    dic4.update(dic3)
    print(dic4)

    # 4
    print('#4')
    print(10 in dic1)

    # 5
    print("#5")
    for key in dic4:
        print(key, ' : ', dic4[key])

    # 6
    print('#6')
    # n = int(input('enter a number: '))
    n = 19
    dic5 = {}
    for i in range(1, n+1):
        dic5[i] = i**2
    print(dic5)
    print(*dic5)

    # 7
    print('#7')
    dic6 = {}
    for i in range(1, 16):
        dic6[i] = i**2
    print(dic6)
    print(*dic6)

    # 8
    print('#8')
    dic7 = dic1.copy()
    dic7.update(dic2)
    print(dic7)

    # 9
    print('#9')
    dic8 = dic2.copy()
    for key in dic8.keys():
        print(key, ": ", dic8[key])

    # 10
    print("#10")
    dic9 = dic8.copy()
    _sum = 0
    for value in dic9.values():
        _sum += value
    print("sum =", _sum)

    # 11
    print('#11')
    _mult = 1
    for value in dic9.values():
        _mult *= value
    print('mult: ', _mult)

    # 12
    dic10 = dic6.copy()
    print('#12')
    print(dic10)
    dic10.pop(5)
    dic10.pop(12)
    print(dic10)

    # 13
    print('#13')
    list1 = ['Mike', 'Rose', 'Mary', 'Nick']
    list2 = [10, 11, 9, 18]
    dic11 = dict(zip(list1, list2))
    print(dic11)

    # 14
    print('#14')
    dic12 = dic11.copy()
    list3 = sorted(dic12)
    list4 = sorted(dic12.values())
    print(list3)
    print(list4)

    # 15
    print('#15')
    max_key = max(dic12)       # maximum key
    max_key2 = max(dic12.keys())   # maximum key
    max_value = max(dic12.values())  # maximum value
    min_key = min(dic12)
    min_key2 = min(dic12.keys())
    min_value = min(dic12.values())
    print(max_value, min_value)

    # 16
    print('#16')

    class MyColor:

        def __init__(self):
            self.red = 164
            self.green = 100
            self.blue = 200


    color_dic = MyColor.__dict__
    print(color_dic)
