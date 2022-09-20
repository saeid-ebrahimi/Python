def tup_to_dict(list_of_tuples):
    my_dic = {}
    for name_tuple in list_of_tuples:
        my_dic[name_tuple[0]] = name_tuple[1]
    return my_dic

if __name__ == "__main__":
    print(tup_to_dict([("Turquoise", "#40E0D0"), ("Red", "#990000")]))
