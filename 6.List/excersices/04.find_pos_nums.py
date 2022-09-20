# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from functools import reduce


def get_list():
    text = input("enter list of numbers separated by space: ")
    lst = text.strip(" ").split(" ")
    new_lst = []
    for num in lst:
        new_lst.append(int(num))
    return new_lst


def find_pos(lst):
    pos_lst = []
    for num in lst:
        if num > 0:
            pos_lst.append(num)

    return pos_lst


if __name__ == '__main__':
    array = find_pos(get_list())
    print(*array)
