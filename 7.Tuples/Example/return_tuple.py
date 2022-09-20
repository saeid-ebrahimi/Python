def string_length(my_string):
    my_tuple = (my_string, len(my_string))
    return my_tuple


if __name__ == '__main__':
    my_str = "My name is Saeid."
    print(string_length(my_str))
    print(string_length("Hello, world!"))
    print(string_length("CS1301"))
    print(string_length("Some people pronounce it 'toople'."
                        " Others pronounce it 'tuhple'. Either is correct."))
