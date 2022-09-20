# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def f1():
    global x
    y = 10
    print("y = ", y)
    x += 10
    print("x = ", x)
    x = x + 1
def main():
    global x, y
    x = 0
    y = 0
    print("x = ", x)
    f1()
    y = y + 1
    print ("y = ", y)
    print ("x = ", x )
    x = x + 1
    x = y = 5


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

