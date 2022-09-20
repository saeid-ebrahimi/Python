# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def second_greatest_average():
    num_of_students = int(input("Enter number of student :"))
    my_max = 0
    second_greatest_av = -1
    second_greatest_av_id = 0
    for i in range(1, num_of_students+1):
        my_id = int(input("Enter my_id of student number #" + str(i) + " : "))
        average = float(input("Enter average of student number #" + str(i) + " : "))
        if average > my_max:
            second_greatest_av = my_max
            second_greatest_av_id = my_id
            my_max = average
        elif average > second_greatest_av:
            second_greatest_av = average
            second_greatest_av_id = my_id
    print("ID of student with Second greatest average is :", second_greatest_av_id)
    print("Second greatest average is :", second_greatest_av)


def find_number_status():
    user_answer = "yes"
    while user_answer == "yes" and user_answer == "Yes":
        number = int(input("Enter a number :"))
        my_sum = 0
        for i in range(1, number):
            if (number % i) == 0:
                my_sum += i
        if my_sum == number:
            print("inputted number is perfect")
        else:
            print("inputted number is not perfect")
        user_answer = input("enter \"yes\" To continue :")


def fibonacci_series():
    fib1 = 1
    fib2 = 1

    n_num = int(input("Enter which number do you want: "))
    if n_num == 1:
        print(fib1)
    elif n_num == 2:
        print(str(fib1) + " , " + str(fib2))
    else:
        print(fib1, end=" , ")
        print(fib2, end=" , ")
        for i in range(3, n_num+1):
            fib3 = fib2 + fib1
            fib1 = fib2
            fib2 = fib3
            if i < n_num:
                print(fib3, end=" , ")
            else:
                print(fib3, end=" .")


def print_string_with_space():
    my_string = input("Enter an string to show: ")
    for i in my_string:
        print(i, end=" ")


def loan_calc():
    user_answer = "yes"
    while user_answer == "yes":
        loan_amount = int(input("please enter your desire amount of loan: "))
        loan_portion = int(input("please enter the number of mortgagees: "))
        profit = int(input("please enter profit of loan: "))
        final_payment = (12*loan_amount)/(12-loan_portion*(profit/100))
        loan_payment = final_payment / 12
        print("your payment for each portion is : ", loan_payment)
        user_answer = input("Do you want retry procedure for another input ?(enter \"yes\" to retry)")


def calc_your_age():
    day_diff = 0
    month_diff = 0
    year_diff = 0
    birth_year = int(input("Enter your birth year: "))
    birth_month = int(input("Enter your birth month: "))
    birth_day = int(input("Enter your birth day: "))
    current_year = int(input("Enter current year: "))
    current_month = int(input("Enter current month: "))
    current_day = int(input("Enter current day: "))
    if current_year > birth_year:
        day_diff = current_day - birth_day
        if day_diff < 0:
            day_diff += 30
            current_month -= 1
        month_diff = current_month - birth_month
        if month_diff < 0:
            month_diff += 12
            current_year -= 1
        year_diff = current_year - birth_year
    else:
        print("Invalid input!!")
    age_in_day = year_diff * 364 + month_diff * 30 + day_diff
    age_in_hour = age_in_day * 24
    age_in_minute = age_in_hour * 60
    age_in_second = age_in_minute * 60
    print("your age is "+str(year_diff)+" years "+str(month_diff)+" months and "+str(day_diff)+" days")
    print("your age is : ")
    print(age_in_day, " days")
    print("or ", age_in_hour, "hours")
    print("or ", age_in_minute, "minutes")
    print("or ", age_in_second, "seconds.")


def sort_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    if c > b:
        b, c = c, b
    if c > a:
        c, a = a, c
    if b > a:
        a, b = b, a

    print("inputs sorted in value : ", a, b, c)


def calc_salary():
    emp_num = int(input("Enter number of employees: "))
    i = 0
    while i < emp_num:
        employee_id = int(input("Enter employee id here: "))
        total_working_hour = int(input("Enter total working hour here: "))
        payment_per_hour = float(input("Enter employee payment per hour: "))
        if total_working_hour > 40:
            salary = 40 * payment_per_hour + (total_working_hour - 40) * 1.5 * payment_per_hour
        else:
            salary = total_working_hour * payment_per_hour
        print("employee with id #" + str(employee_id) + " salary is : " + str(salary))
        i += 1


def calc_future_price():
    years = int(input("How many years ? "))
    current_price = int(input("Enter item current price: "))
    price_change_rate = int(input("Enter item price change rate in percentage: "))
    i = 0
    future_price = 0
    while i < years:
        future_price += current_price * (1+(price_change_rate/100))
        current_price = future_price
        i += 1
    print("Future Price is : ", future_price)


def calc_series_terms():
    parameter = float(input("Enter variable value in series: "))
    term = 1
    sum_of_terms = 0
    for i in range(0, 10):
        term *= parameter
        sum_of_terms += 1/term
    print("series result: ", sum_of_terms)


def calc_multiplication_via_addition():
    while True:
        first_num = int(input("Enter first number to multiply: "))
        second_num = int(input("Enter second number to multiply: "))
        multiply_result = 0
        if first_num == 0 and second_num == 0:
            break
        for i in range(0, second_num):
            multiply_result += first_num
        print("multiplication result is :", multiply_result)


def evaluate_input():
    number = int(input("Enter a number to evaluate: "))
    temp = number
    new_num = 0
    while temp > 0:
        new_num = temp % 10 + new_num * 10
        temp //= 10
    if number == new_num:
        print("number and its reverse are equal!!")
    else:
        print("number and its reverse are different!!")


def calc_power_via_addition():
    base = int(input("Enter the base for basePow(exp): "))
    exponent = int(input("Enter the exponent: "))
    exponent_result = base
    multiply_result = base
    for i in range(1, exponent):
        for j in range(1, base):
            exponent_result += multiply_result
        multiply_result = exponent_result
        print(exponent_result)
        print("  ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc_power_via_addition()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
