
from array import *


def calc_fine():
    a = []

    car_id = input("enter car id: ")
    a.append(car_id)
    fine_table = array('i', [1000, 2000, 12000, 4000, 8000, 9000, 6000, 40000, 20000, 30000])
    fine = 0
    fine_counter = 0
    for i in range(0, 10):
        occ = int(input(f"enter occurrences for fine code #{i}"))
        fine += occ * fine_table[i]
        fine_counter += occ

    a.append(fine_counter)
    a.append(fine)

    return a


ans = ' '
while ans != 'exit':
    ar = calc_fine()
    print(f"car with id {ar [ 0 ]} has {ar [ 1 ]} crime in total and it's fine is {ar [ 2 ]}")
    ans = input("another car id to calc?(enter 'exit' to finish): ")
