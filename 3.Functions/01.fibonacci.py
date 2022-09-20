# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def fibonacci_series(term_num):
    if term_num == 1 or term_num == 2:
        return 1
    else:
        return fibonacci_series(term_num - 1) + fibonacci_series(term_num-2)


def main1():
    series_term = int(input("Enter number of series term: "))
    print("fibonacci series terms from 1 to "+str(series_term))
    for i in range(1, series_term+1):
        fibonacci_result = fibonacci_series(i)
        if i == series_term:
            print(fibonacci_result, end=" .")
        else:
            print(fibonacci_result, end=" , ")
    print(" ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main1()
