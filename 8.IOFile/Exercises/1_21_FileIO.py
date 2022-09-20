

if __name__ == '__main__':

    # 1
    print('# 1')
    file1 = open('test1.txt', 'r')
    content = file1.read()
    print(content)
    file1.close()

    # 2
    print("# 2")
    n = 4
    file2 = open("test1.txt", "r")
    lines = file2.readlines()[0:4]
    for line in lines:
        print(line)
    file2.close()

    # 3
    print('#3')
    with open('test2.txt', "a") as file3:
        str1 = "If you need a dash of inspiration, " \
               "explore these short love messages and quotes about love for a" \
               " little help with telling your beloved just how much you care!\n"
        file3.write(str1)
    with open('test2.txt', 'r') as file4:
        print(file4.read())

    # 4
    print('#4')
    n = 3
    file5 = open('test2.txt', 'r')
    lines = file5.readlines()
    for line in lines[-n:]:
        print(line)
    file5.close()
    # 5
    print('#5')
    with open('test2.txt', 'r') as file5:
        lines = file5.readlines()
    print(lines)

    # 6
    print('#6')
    with open('test2.txt', 'r') as file6:
        lines = file6.readline()
        print(lines)

    # 7
    print('#7')
    with open('test2.txt', 'r') as file7:
        content = file7.read()
        words = content.split(' ')
        words.sort(key=len, reverse=True)
    print(words)

    # 8
    print('#8')
    with open('test2.txt', 'r') as file8:
        arr = []
        for line in file8:
            arr.append(line)
        print(*arr)

    # 9
    print('#9')
    with open('test2.txt', 'r') as file9:
        lines = file9.readlines()
        print(len(lines))

    # 10
    print("#10")
    file10 = open('test2.txt', 'r')
    file_content = file10.read()
    print(file_content.count('a'))
    file10.close()

    # 11
    print('#11')
    from os import stat
    with open('test2.txt', 'r') as file11:
        file_content = file11.read()
        print(len(file_content))
        print(stat('test2.txt').st_size)

    # 12
    print('#12')
    my_list = [12, [24, 55], (23, 45, 11), {'a': 12, 'c': 14}]
    file12 = open('test3.txt', 'w')
    file12.write(str(my_list)+'\n')
    for el in my_list:
        file12.write(str(el)+'\n')
    file12.close()

    # 13
    print('# 13')
    file13 = open('test3_copy.txt', 'w')
    file14 = open('test3.txt', 'r')
    file_content = file14.read()
    file13.write(file_content)
    file13.close()
    file14.close()

    # 14
    print('#14')
    file15 = open('test3_copy.txt', 'r')
    file16 = open('test3.txt', 'r')
    lines1 = file15.readlines()
    lines2 = file16.readlines()
    min_lines = min(lines1, lines2, key=len)
    max_lines = max(lines1, lines2, key=len)
    lines3 = max_lines.copy()
    print(lines3)
    for i in range(0, len(min_lines)):
        lines3[i] = min_lines[i] + max_lines[i]
    print(lines3)

    # 15
    print('#15')
    file17 = open('test2.txt', 'r')
    lines = file17.readlines()
    from random import randint
    idx = randint(0, len(lines))
    print(idx)
    print(lines[idx])

    # 16
    print('#16')
    with open('test1.txt', 'r') as file18:
        print(file18.closed)
    print(file18.closed)

    # 17
    print('#17')
    file19 = open('test2.txt', 'r')
    new_lines = []
    for line in file19:
        new_lines.append(line.rstrip('\n'))
    print(new_lines)
    file19.close()

    # 18
    print('#18')
    file20 = open('test2.txt', 'r')
    file_content = file20.read()
    words = file_content.split(' ')
    print(len(words))
    file20.close()

    # 19
    print('#19')
    from glob import glob
    files_list = glob('*.txt')
    content_list = []
    print(files_list)
    for file_name in files_list:
        with open(file_name, 'r') as file21:
            content = file21.read()
            chars_list = list(content)
            print(chars_list)
            content_list.append(content)
    print(content_list)

    # 20
    import os
    import string
    dir_name = 'letter_files'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    letters = string.ascii_uppercase
    for letter in letters:
        with open(dir_name+'/'+letter+'.txt', 'w') as file22:
            file22.write(letters)

    # 21
    print('#21')
    import string
    st = 4
    with open('words.txt', 'w') as file23:
        alphabets = string.ascii_letters
        for idx in range(0, len(alphabets), st):
            word = alphabets[idx: idx+st]
            file23.writelines(word + '\n')
