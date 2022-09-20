# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




from collections import deque
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stack = deque()
    while True:
        ans = input(" : ")
        if ans == 'x':
            break
        elif ans == 's':
            print(*stack)
        elif ans == '=':
            print(stack.pop())

        elif ans == '+':
            a = stack.pop ()
            b = stack.pop ()
            stack.append(a+b)
        elif ans == '-':
            a = stack.pop ()
            b = stack.pop ()
            stack.append(a-b)
        elif ans == '*':
            a = stack.pop ()
            b = stack.pop ()
            stack.append(a*b)
        elif ans == '/':
            a = stack.pop ()
            b = stack.pop ()
            stack.append(a/b)
        else:
            stack.append(int(ans))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
