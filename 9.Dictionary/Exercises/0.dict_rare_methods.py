


if __name__ == "__main__":
    dict1 = {'Name' : 'Zara' , 'Age' : 7}
    dict2 = {'Name' : 'Mahnaz' , 'Age' : 27}
    dict3 = {'Name' : 'Abid' , 'Age' : 27}
    dict4 = {'Name' : 'Zara' , 'Age' : 7}
    seq = ('name' , 'age' , 'sex')

    dict1 = dict1.fromkeys(seq)
    print(dict1)

    dict2 = dict1.fromkeys(seq, [13, 14])
    print(dict2)

    dict3.update(dict2)
    print(dict3)

    dict4.pop('Name')
    print(dict4)

    dict4.setdefault('Name', 'Cameron')
    print(dict4)