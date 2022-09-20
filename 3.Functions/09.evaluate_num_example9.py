# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def factorial(n):
    if n == 1 or n == 0:
        return 1.0
    else:
        return n*factorial(n-1)


def evaluate_number(num):
    result = 0
    temp = num
    while temp > 0:
        result += factorial(temp % 10)
        temp //= 10
    if num == result:
        return num
    else:
        return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for number in range(100, 1000):
        calc = evaluate_number(number)
        if calc is not None:
            print(evaluate_number(number))
        else:
            pass
