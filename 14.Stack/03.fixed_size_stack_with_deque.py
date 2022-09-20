# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




from collections import deque
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stack = deque([], maxlen=4)
    stack.append("joy")
    stack.append("fun")
    stack.append('excitement')
    stack.append("happiness")
    print(*stack)
    stack.append('passion')
    stack.append('love')
    print(*stack)
    while stack:
        item = stack.pop()
        print(item)
        print(*stack)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
