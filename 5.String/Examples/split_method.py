# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def numwords(my_string):
    words_list = my_string.split()
    print(words_list)
    return len(words_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_string = "I like shorts!"
    print(numwords(my_string))
