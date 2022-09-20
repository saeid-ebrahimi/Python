# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def evaluate_number(num):
    result1 = 0
    result2 = 0
    temp = num
    counter = 1
    while temp > 0:
        if counter % 2 == 0:
            result1 += (temp % 10)**counter
        else:
            result2 += (temp % 10)**counter
        temp //= 10
        counter += 1
    if result2 == result1:
        return num
    else:
        return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for number in range(1000, 10000):
        calc = evaluate_number(number)
        if calc is not None:
            print(evaluate_number(number))
        else:
            pass