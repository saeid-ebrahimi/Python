
if __name__ == '__main__':
    x = input("exp:")
    print(eval(x))
    # 1
    print('#1')
    with open('department.csv', 'r') as csv1:
        lines3 = []
        for line in csv1:
            lines3.append( line.rstrip( '\n' ) )
    print( lines3 )

    import csv
    lines2 = []
    with open('department.csv', 'r' ) as csv1:
        data = csv.reader(csv1)
        for list1 in list(data):
            lines2.append(', '.join(list1))
        print(lines2)

    # 2
    print('#2')
    csv2 = open('countries.csv', 'r')
    lines3 = []
    for line in csv2:
        lines3.append(line.rstrip('\n'))
    print(lines3)
    csv2.close()

    import csv
    csv2 = open('countries.csv', 'r')
    data = csv.reader(csv2, delimiter='\t')
    lines3 = []
    for el in data:
        lines3.append(', '.join(el))
    print(lines3)
    csv2.close()

    # 3
    print('#3')
    csv3 = open('countries.csv', 'r')
    lines4 = csv3.readlines()
    print(lines4)
    csv3.close()

    csv3 = open('countries.csv', 'r')
    lines4 = list(csv.reader(csv3))
    print(lines4)
    csv3.close()

    # 4
    print('#4')
    import csv
    lines5 = []
    csv4 = open('department.csv', 'r')
    dict_data = csv.DictReader(csv4)
    for dic in dict_data:
        lines5.append(dict(dic))
    print(lines5)
    csv4.close()

    # 5
    print('#5')
    import csv
    lines6 = []
    print('without skip space after delimiter')
    with open('department2.csv', 'r') as csv5:
        data = csv.reader(csv5, skipinitialspace=False)
        for row in data:
            row = ','.join(row)
            print(row)
            lines6.append(row)
        print(lines6)
    print('with skip space after delimiter')
    with open('department2.csv', 'r') as csv5:
        data = csv.reader(csv5, skipinitialspace=True)
        for row in data:
            row = ','.join(row)
            print(row)
            lines6.append(row)
        print(lines6)

    # 6
    print('#6')
    import csv
    csv.register_dialect('csv_dialect1', delimiter='|', skipinitialspace=True, quoting=csv.QUOTE_ALL)
    with open('temp.csv', 'r') as csv6:
        data = csv.reader(csv6, dialect='csv_dialect1')
        print(list(data))

    # 7
    print('#7')
    third_column = []
    with open('department2.csv', 'r') as csv6:
        for line in csv6:
            line_list = line.rstrip('\n').split(',')
            third_column.append(line_list[2])
        third_column_dic = {third_column[0]: third_column[1:]}

        print(third_column_dic)
    with open('department2.csv', 'r') as csv6:
        data_dict = csv.DictReader(csv6)
        department_dic = {'department_id': []}
        for row in data_dict:
            department_dic['department_id'].append(row['department_id'])
    print(department_dic)

    # 8
    print('#8')


