
if __name__ == '__main__':
    num_list = []
    in_file = open("read_input_file.txt", "r")
    for line in in_file:
        num_list.append(int(line))
    print(num_list)
    in_file.close()

    name_list1 = []
    name_list2 = []
    in_file = open("file2.txt", "r")
    for line in in_file:
        name_list1.append(line)
        name_list2.append(line.strip('\n').split('\t'))
    in_file.close()
    print(name_list1)
    print(name_list2)
