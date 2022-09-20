
if __name__ == '__main__':
    my_int1 = 12
    my_int2 = 23
    my_int3 = 34

    output_file = open("output_file.txt", "w")
    output_file.write(str(my_int1))
    output_file.write(str(my_int2))
    output_file.write(str(my_int3))
    output_file.close()

    output_file = open("output_file.txt", "w")
    output_file.write(str(my_int1) + "\t")
    output_file.write(str(my_int2) + "\t")
    output_file.write(str(my_int3) + "\t")
    output_file.close()
