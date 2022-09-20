# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def calc_gravity(mass1, mass2, distance):
    gravity_constant = 6.693e-6
    gravity = (mass1 * mass2) * gravity_constant / distance**2
    return gravity


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m1 = float(input("Enter mass of first item in kilogram: "))
    m2 = float(input("Enter mass of second item in kilogram: "))
    d = float(input("Enter distance of items in meter: "))
    print("Gravity between items is "+str(calc_gravity(m1, m2, d))+" N")