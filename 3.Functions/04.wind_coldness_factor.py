# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def calc_wind_coldness_factor(velocity, temperature):
    from math import sqrt
    term = 10 * sqrt(velocity)-velocity + 10.5
    term *= 33-temperature
    wind_factor = 33 - term/23.1
    return wind_factor


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    temp = float(input("Enter temperature in centigrade: "))
    vel = float(input("Enter velocity of wind in meter per seconds: "))
    print("wind coldness factor is "+str(calc_wind_coldness_factor(vel, temp)))
