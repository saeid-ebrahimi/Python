# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_string = "This is my text. It has thirteen "\
                "words. It also has three sentences."
    print(my_string.split())
    print(my_string.split("."))
    print(my_string.split(". "))
    names = input("enter a list of names: ")
    print(names.split(","))
    my_string = "this is MY test string!!!!"
    print(my_string)
    print(my_string.capitalize())
    print(my_string.lower())
    print(my_string.upper())
    print(my_string.title())
    print(my_string.strip("!"))
    print(my_string.replace("MY", "YOUR"))
    my_list = my_string.split()
    print("-".join(my_list))
    print(my_string)
    my_string = "My-string-to-split"
    print(my_string)
    my_string_list = my_string.split("-")
    print(my_string_list)
    my_string = "-".join(my_string_list)
    print(my_string)
