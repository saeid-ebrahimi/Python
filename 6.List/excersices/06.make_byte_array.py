# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_list():
    text = input("enter list of numbers separated by space: ")
    lst = text.strip(" ").split(" ")
    new_lst = []
    for num in lst:
        new_lst.append(int(num))
    return new_lst


if __name__ == '__main__':
    array = bytearray(get_list())    # number should be in range 0-255
    print(*array)
