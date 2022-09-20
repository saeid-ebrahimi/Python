# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def lcm(a, b):
    mini = a if a < b else b
    for i in range(mini, 1, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    else:
        gcd = 1
    return (a * b)/gcd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("lcm is: ",lcm(2, 5))
