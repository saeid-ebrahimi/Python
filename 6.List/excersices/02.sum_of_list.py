# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def calc_sum(num_list):
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    s = 0
    for num in num_list:
        s += num
    return s


def get_list():
    text = input("enter list of numbers separated by space: ")
    lst = text.strip(" ").split()
    num_list = []
    for num in lst:
        num_list.append(int(num))
    return num_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calc_sum(get_list()))
    print(sum(get_list()))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
