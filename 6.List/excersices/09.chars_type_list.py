# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def find_upper_and_lower(lst):
    up_lo_other_char_lst = [0, 0, 0]
    for ch in lst:
        if ch.isupper():
            up_lo_other_char_lst[0] += 1
        elif ch.islower():
            up_lo_other_char_lst[1] += 1
        else:
            up_lo_other_char_lst[2] += 1
    return up_lo_other_char_lst


if __name__ == '__main__':
    text = input("enter a text:\n")
    char_count = find_upper_and_lower(text)
    print(f"upper case: {char_count[0]}, lower case: {char_count[1]}, other chars: {char_count[2]} ")
