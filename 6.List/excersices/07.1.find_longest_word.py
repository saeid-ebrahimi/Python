# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_list():
    text = input("enter list of words separated by space: ")
    lst = text.split(" ")
    return lst


def find_longest_word(lst):
    m = 0
    longest_word = ''
    for word in lst:
        word_len = len(word)
        if word_len > m:
            longest_word = word
            m = word_len
    return longest_word


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # byte array can hold values between 0 - 255
    print(find_longest_word(get_list()))

