

if __name__ == "__main__":
    # 25
    dic1 = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}
    lst2 = dic1['C1']
    lst3 = dic1['C2']
    lst4 = dic1['C3']
    for a, b, c in zip(lst2, lst3, lst4):
        print(a, b, c, sep='\t')

    print(*dic1.keys(), sep='\t')
    for key, value in dic1:
        lst = key + value
        print(*lst)

    for row in zip(*([key] + value for (key, value) in dic1.items())):
        print(*row)

    # 26
    print('#26')
    student = [
        {'id': 1, 'success': True, 'name': 'Lory'},
        {'id': 2, 'success': False, 'name': 'Rabi'},
        {'id': 3, 'success': True, 'name': 'Alex'}]
    s1 = 0
    s2 = 0
    for dic in student:
        s1 += dic['id']
        s2 += dic['success']
    print(s1, s2)
    print(sum([d['id'] for d in student]), end=' ')
    print(sum([d['success'] for d in student]))

    # 27
    print('#27')
    list1 = [1, 2, 8, 5]
    dic3 = dic2 = {}
    for num in list1:
        dic2[num] = {}
        dic2 = dic2[num]
    print(dic3)
    # 28
    print('#28')
    nums = {'c': [2, 3, 1], 'a': [5, 1, 2], 'b': [3, 2, 4]}
    al_sorted = {}
    for key in sorted(nums):
        al_sorted[key] = nums[key]
    print(al_sorted)

    num_sorted = {}
    for key, values in nums.items():
        values.sort()
        num_sorted[key] = values
    print(num_sorted)

    com_sorted = {}
    for key in sorted(nums):
        nums[key].sort()
        com_sorted[key] = nums[key]
    print(com_sorted)
    # 29
    print('# 29')
    dic4 = {}
    student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
    for key in student_list:
        new_key = key.replace(" ", "")
        dic4[new_key] = student_list[key]
    print(dic4)

    print("Original dictionary: ", student_list)
    student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
    print("New dictionary: ", student_dict)

    # 30
    print('#30')
    items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
    items_list = sorted(items, key=items.get, reverse=True)
    new_dic = {}
    for item in items_list:
        new_dic[item] = items[item]
    print(new_dic)

    from heapq import nlargest
    from operator import itemgetter

    items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
    for name, value in nlargest(3, items.items(), key=itemgetter(1)):
        print(name, value)

    # 31
    print('#31')
    nums_dic = {10: 100, 20: 200, 40: 400, 60: 600, 50: 500, 30: 300}
    print('idx', 'key', 'value', sep='\t')
    for index, (key, val) in enumerate(nums_dic.items(), 1):
        print(index, key, val, sep='\t')

    # 32
    print('#32')
    students = {'Aex': {'class': 'V', 'roll_id': 2},
                'Puj': {'class': 'V', 'roll_id': 3}}
    for name, dict1 in students.items():
        print(name+':')
        for item in dict1:
            print('  ', item + ":", dict1[item])

    # 33
    print('#33')
    dic5 = {'name': 'Michel', 'class': 'Math', 'id': 15}
    print(set(dic5.keys()) >= {'name', 'id'})
    print({'class', 'name', 'course'} <= set(dic5.keys()))

    # 34
    print('# 34')
    dic6 = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
    count_dic = {}
    for k in dic6:
        count_dic[k] = len(dic6[k])
    print(count_dic)
    print(sum(count_dic.values()))

    # 35
    print('#35')
    courses_dic = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
    sorted_courses = sorted(courses_dic, key=courses_dic.get, reverse=True)
    dic7 = {}
    for it in sorted_courses:
        dic7[it] = courses_dic[it]
    print(dic7)

    from collections import Counter
    print(dict(Counter(courses_dic)))
    print(Counter(courses_dic).most_common())

    # 36
    print("#36")
    list2 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
    list3 = [1, 2, 2, 3]
    dic8 = {}
    for kk, vv in zip(list2, list3):
        dic8[kk] = vv
    print(dic8)

    from collections import defaultdict
    dic8 = defaultdict(set)
    for kk, vv in zip(list2, list3):
        dic8[kk].add(vv)
    print(dic8)

    # 37
    print('#37')
    student_details = [
        {'id': 1, 'subject': 'math', 'V': 70, 'VI': 82},
        {'id': 2, 'subject': 'math', 'V': 73, 'VI': 74},
        {'id': 3, 'subject': 'math', 'V': 75, 'VI': 86}
    ]
    for stu in student_details:
        mark1 = stu.pop('V')
        mark2 = stu.pop('VI')
        stu['V+VI'] = (mark1+mark2)/2

    print(student_details)

    # 38
    print('#38')
    dic9 = {'key1': 1, 'key2': 3, 'key3': 2}
    dic10 = {'key1': 1, 'key2': 2}
    for key1 in dic9:
        if dic9[key1] == dic10.get(key1):
            print(key1, ':', dic10[key1], 'match in both dictionary')
    # 39
    print("#39")
    dic11 = {
        "students": [
            {"firstName": "Nikki", "lastName": "Royen"},
            {"firstName": "Mervin", "lastName": "Friesland"},
            {"firstName": "Aron ", "lastName": "Wilkins"}],
        "teachers": [
            {"firstName": "Amberly", "lastName": "Calico"},
            {"firstName": "Regine", "lastName": "Agar"}]}
    import json
    file1 = open("dic1.json", 'w')
    json.dump(dic11, file1, indent=4)
    file1.close()

    file1 = open('dic1.json', 'r')
    str1 = json.load(file1)
    file1.close()
    print(str1)

    # 40
    print('#40')
    dic11 = dict(x=list(range(1, 20)), y=list(range(21, 40)), z=list(range(41, 60)))
    print(dic11)
    for key in dic11:
        print(key, 'has values', dic11[key])
    