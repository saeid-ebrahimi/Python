def find_coffee(filename):
    in_file = open(filename, "r")
    for line in in_file:
        if line.strip() == "coffee":
            return True
    return False


if __name__ == '__main__':
    print(find_coffee("Scripts\coffee_ful.txt"))
    print(find_coffee("Scripts\coffee_less.txt"))
