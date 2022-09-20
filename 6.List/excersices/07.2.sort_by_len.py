# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_list():
    text = input("enter list of words separated by space: ")
    lst = text.split(" ")
    return lst


def sort_by_len(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) < len(lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print(sort_by_len(get_list()))
