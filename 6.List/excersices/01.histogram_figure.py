# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_histogram(num_list):
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    print("histogram figure: ")
    for num in num_list:
        print('*' * num)


def get_list():
    lst = []
    size = int(input("size of list: "))
    for i in range(size):
        num = int(input(f'element #{i+1}: '))
        lst.append(num)
    return lst


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_histogram(get_list())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
