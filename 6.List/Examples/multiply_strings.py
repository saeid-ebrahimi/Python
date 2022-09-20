
def multiply_strings(string_list):
    for index in range(0, len(string_list), 2):
        string_list[index] *= 2
    for index in range(0, len(string_list), 3):
        string_list[index] *= 3
    return string_list


if __name__ == '__main__':
    test_list = ["A", "B", "C", "D", "E", "F", "G"]
    print(multiply_strings(test_list))
