# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def read_data():
    foot = float(input("How many foot? "))
    inch = float(input("How many inch? "))
    return [foot, inch]


def convert_units(foot, inch):
    foot_to_meter = foot * 0.3048
    inch_to_meter = inch * 0.3048 / 12
    foot_to_centimeter = foot_to_meter * 100
    inch_to_centimeter = inch_to_meter * 100
    return [foot_to_meter, foot_to_centimeter, inch_to_meter, inch_to_centimeter]


def write_data(foot_to_meter, foot_to_centimeter, inch_to_meter, inch_to_centimeter):
    print("convert from foot to meter :", foot_to_meter)
    print("convert from foot to centimeter :", foot_to_centimeter)
    print("convert from inch to meter :", inch_to_meter)
    print("convert from inch to meter :", inch_to_centimeter)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    [my_foot, my_inch] = read_data()
    [my_foot_to_meter, my_foot_to_centimeter, my_inch_to_meter, my_inch_to_centimeter]\
        = convert_units(my_foot, my_inch)
    write_data(my_foot_to_meter, my_foot_to_centimeter, my_inch_to_meter, my_inch_to_centimeter)
