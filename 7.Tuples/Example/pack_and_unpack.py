def unpack_and_reverse(my_tuple):
    (var1, var2, var3) = my_tuple[0:3]
    return var3, var2, var1


if __name__ == '__main__':
    print(unpack_and_reverse(("a", "b", "c", "d", "e")))
    print(unpack_and_reverse(("f", "g", "h")))
    print(unpack_and_reverse(("i", "j", "k", "l", "m", "n", "o", "p", "q", "r")))
