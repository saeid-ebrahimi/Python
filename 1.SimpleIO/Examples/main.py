# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def area_calculator():
    base = float(input("Please enter the base : "))
    height = float(input("Please enter the height: "))
    area = 0.5 * height * base
    print("Area is " + str(area))
    return None


def calc_cylinder():
    radius = float(input("Enter the cylinder radius :"))
    height = float(input("Enter the height :"))
    pi = 3.14
    volume = pi * radius**2 * height
    print("volume is :"+str(volume))
    area = (2*pi*radius*height) + 2*(pi*radius**2)
    print("area is :"+str(area))


def calc_sphere():
    radius = float(input("Please enter radius :"))
    pi = 3.14
    volume = (4/3)*pi*radius**3
    surf_area = 4*pi*radius*radius
    print("sphere volume is :"+str(volume)+" and it's surface area is : "+str(surf_area))


def polygon_area_calculator():
    from math import tan, pi
    num_of_sides = int(input("please enter number of sides: "))
    side = float(input("please enter the polygon sides value : "))
    area = (num_of_sides*(side**2))/(4 + tan(pi/num_of_sides))
    print("the polygon area is : "+str(area))


def calc_wind_chill():
    velocity = float(input("Enter a value for velocity: "))
    temp = float(input("Enter a value for temperature: "))
    wind_chill = 13.12+0.6215*temp-11.37*(velocity**0.16)+0.3965*temp*(velocity**0.16)
    print("wind chill = " + str(wind_chill))


def repeat_string():
    input_string = input("enter a phrase or number to repeat: ")
    _times = int(input("How many times repeat input ? "))
    print(input_string*_times)


def show_in_complex():
    real_part = float(input("Enter number real part: "))
    imaginary_part = float(input("Enter number imaginary part: "))
    print("complex style of num :", complex(real_part, imaginary_part))


def num_of_molecules():
    volume = float(input(" Enter volume of water:"))
    per_litre_weight = 950
    per_molecules_weight = 3.0e-23
    molecules = volume * per_litre_weight / per_molecules_weight
    print("number of molecules is : " + str(molecules))


def age_in_seconds():
    age = int(input("Enter your age : "))
    age_in_sec = age * 3.156e7
    print("your age in seconds is", age_in_sec)


def calc_pure_income():
    income = float(input("Enter your income : "))
    insurance = income * .07
    tax = income * .1
    pure_income = income - insurance - tax
    print("Reminded income is:", pure_income)


def calc_next_year_price():
    last_year_price = float(input("Enter item last year price: "))
    current_price = float(input("Enter item current price: "))
    price_change_rate = (current_price - last_year_price) / last_year_price
    next_year_price = current_price * (1+price_change_rate)
    print("next year item price is : ", next_year_price)


if __name__ == '__main__':
    calc_next_year_price()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
