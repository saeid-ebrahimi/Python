# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def calc_coefficient(x, n):
    if n == 0:
        return 1.0
    else:
        return x * calc_coefficient(x, n - 1)


def calc_quotient(n):
    if n == 1:
        return 1
    else:
        return n * calc_quotient(n-1)


def generate_terms(x, n):
    coefficient = calc_coefficient(x, n)
    quotient = calc_quotient(n)
    return coefficient / quotient


def calc_sin(radian, precision):
    n = 2 * precision + 1
    result = 0
    sign = 1
    for i in range(1, n+1, 2):
        result += generate_terms(radian, i) * sign
        sign *= -1
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_radian = float(input("Enter x argument for sin(x) in radian: "))
    my_precision = int(input("Enter number of terms for sin function equivalent series: "))
    print("sin of entered parameter is", calc_sin(my_radian, my_precision))

