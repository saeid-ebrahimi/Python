# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sum_of_list(list1):
    if len(list1) == 1:
        return list1[0]
    else:
        return list1[0] + sum_of_list(list1[1:])


def convert_to_str(num, base):
    conver_tString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num < base:
        return conver_tString[num]
    else:
        return conver_tString[num % base] + convert_to_str(num//base, base)

def sum_of(list2):
    _sum = 0
    for item in list2:
        if type(item) == list:
            _sum += sum_of(item)
        else:
            _sum += item
    return _sum


def fact(num):
    if 0 <= num < 2:
        return 1
    else:
        return num * fact(num-1)


def fibonacci(num):
    if 0 < num <= 2:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)


def sum_of_digits(num):

    if num < 10:
        return num % 10
    else:

        return num % 10 + sum_of_digits(num//10)


def sum_of_nums(num):
    if num >= 0:
        return num + sum_of_nums(num - 2)
    else:
        return 0


def harmonic_sum(num):
    if num <= 1:
        return 1
    else:
        return 1/num + harmonic_sum(num-1)


def geometric_sum(num):
    if num < 0:
        return 0
    else:
        return 1/(2**num) + geometric_sum(num-1)


def rec_pow(base, exp):
    if base == 1:
        return 1
    elif exp == 0:
        return 1
    else:
        return base*rec_pow(base, exp - 1)


def rec_gcd(num1, num2):
    min_num = min(num2, num1)
    max_num = max(num2, num1)
    if min_num == 0:
        return max_num
    elif min_num == 1:
        return 1
    else:
        return rec_gcd(min_num, max_num % min_num)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # 1
    print('#1')
    nums1 = [2, 4, 5, 6, 7, 16, 78]
    print(sum_of_list(nums1))
    # 2
    print('#2')
    print(convert_to_str(1000, 16))
    # 3
    print('#3')
    nums2 = [1, [2, 8], [[3, 4], [5, 6, 7]]]
    print(sum_of(nums2))
    # 4
    print('#4')
    print(fact(11))
    # 5
    print('#5')
    print(fibonacci(10))
    # 6
    print('#6')
    print(sum_of_digits(1465))
    # 7
    print('#7')
    print(sum_of_nums(16))
    # 8
    print('#8')
    print(harmonic_sum(12))
    # 9
    print('#9')
    print(geometric_sum(10))
    # 10
    print('#10')
    print(rec_pow(2, 10))
    # 11
    print('#11')
    print(rec_gcd(52, 26))
    