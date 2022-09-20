
if __name__ == '__main__':
    input_file = open("file1.txt", "r")
    print(input_file)
    input_file.close()

    input_file = open("read_input_file.txt", "r")
    # read a line from file
    print(input_file.readline())
    print(input_file.readline())
    print(input_file.readline())
    input_file.close()

    input_file = open("read_input_file.txt", "r")
    print(input_file.readline().strip())
    print(input_file.readline().strip())
    print(input_file.readline().strip())
    input_file.close()

    print("\n")
    input_file = open("read_input_file.txt", "r")
    my_int1 = int(input_file.readline())
    print(my_int1)
    my_int2 = int(input_file.readline())
    print(my_int2)
    # read n character or n Byte form a line
    my_int3 = int(input_file.readline(3))
    print(my_int3)
    input_file.close()
