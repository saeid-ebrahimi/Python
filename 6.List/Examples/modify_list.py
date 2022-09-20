def modify_list(my_list):
    my_list.sort()
    my_list.reverse()
    del my_list[-3:]
    if 7 in my_list:
        my_list.remove(7)
    my_list[0] *= 2
    my_list[2] *= 2
    return my_list


if __name__ == '__main__':
    import math
    print(modify_list([7, 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e]))

    print(7 in [ 4, 3, 2.0, 81, 37.5, 89, math.pi, -2, math.e])
