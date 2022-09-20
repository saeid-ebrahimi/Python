# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def digit_repeat_counter(number, digit):
    cnt = 0
    while number > 0:
        if number % 10 == digit:
            cnt += 1
        number //= 10
    return cnt


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num = int(input("Enter a number: "))
    dig = int(input("Enter a digit: "))
    print("number of repetition of entered digit is : ", digit_repeat_counter(num, dig))
