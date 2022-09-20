def append_to_file(file_name, value):
    output_file = open(file_name, 'a')
    output_file.write(str(value) + '\n')
    output_file.close()


if __name__ == '__main__':
    append_to_file("AppendToFileOutput.txt", 1301)
