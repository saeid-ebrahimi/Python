def save(filename, in_list):
    out_file = open(filename, 'w')
    for item in in_list:
        print(item, file=out_file)
    out_file.close()


def load(filename):
    in_list = []
    in_file = open(filename, 'r')
    for line in in_file:
        in_list.append(line.strip())
    in_file.close()
    return in_list


if __name__ == '__main__':
    myList = ["David", "Lucy", "Catrin", "Ping", "Natalie",
              "Dana", "Addison", "Jasmine"]
    save("io_file.txt",  myList)
    temp_list = load("io_file.txt")
    print(temp_list)
