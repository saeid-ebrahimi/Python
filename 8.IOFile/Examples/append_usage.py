

if __name__ == '__main__':
    name_list = ["David", "Lucy", "Catrin", "Ping",
                 "Natalie", "Dana", "Addison", "Jasmine"]

    num_list = [10, 25, 40, 18, 30, 50, 11, 16]
    output_file = open("file2.txt", "w")
    output_file.writelines("\t".join(name_list))
    output_file.write("\n")
    output_file.writelines("  ".join(str(num_list)))
    output_file.write("\n\n")
    output_file.close()

    output_file = open("file2.txt", "a")
    for i in range(len(num_list)):
        output_file.write(str(name_list[i])+', ')
        print(num_list[i], file=output_file, end='\t')
    print("\n", file=output_file)
    output_file.close()