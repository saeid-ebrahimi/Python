

if __name__ == '__main__':
    my_list = ["David", "Lucy", "Catrin", "Ping",
               "Natalie", "Dana", "Addison", "Jasmine"]

    output_file = open("file1.txt", "w")
    for i in range(len(my_list)):
        output_file.write(my_list[i]+"\t")
    output_file.write("\n")
    for i in range(len(my_list)):
        print(my_list[i], file=output_file, end="\t")
    print("\n\n", file=output_file)
    for name in my_list:
        output_file.write(name + "\t")
    output_file.write("\n")
    for name in my_list:
        print(name, file=output_file, end="\t")
    print("\n\n", file=output_file)
    output_file.writelines(my_list)
    output_file.write("\n")
    output_file.writelines("\t".join(my_list))
    output_file.write("\n")

    output_file.close()