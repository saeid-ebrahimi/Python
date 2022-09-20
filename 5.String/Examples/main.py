# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_string = "My-string-to-split"
    print(my_string)
    my_string_list = my_string.split("-")
    print(my_string_list)
    my_string = "-".join(my_string_list)
    print(my_string)
