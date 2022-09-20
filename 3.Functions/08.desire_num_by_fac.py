# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)


def find_desire_num():
    for i in range(1, 1000):
        number = i
        s = 0
        while number > 0:
            s += fact(number % 10)
            number //= 10
        if s == i:
            print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_desire_num()
