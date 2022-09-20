# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    days_set = set(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
    print("days: ", days_set)
    month_set = frozenset(['Jan', 'Feb', 'Mar', 'Apr'])
    print("months: ", *month_set)
    Dates = {21, 10, 2020}

    for day in days_set:
        print(day)

    days = {'Sat', 'Sun', 'mon'}
    days.add('Fri')
    print(days)
    days.remove('Sat')
    #days.remove('sat') #KeyError
    print(days)
    days.discard('sat')
    print(days)

    print(days | days_set)
    print(days & days_set)
    print(days_set - days)
    print(days < days_set)
    print(days ^ days_set)
    print('fri' in days_set)
    print("Fri" in days_set)
    print(len(days_set))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
