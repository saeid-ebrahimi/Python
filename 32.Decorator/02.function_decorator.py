def start_end_decorator(func):

    def warpper():
        print("start of it:")
        func()
        print("end of it:")
    return warpper

@start_end_decorator
def print_name():
    print("hello Alex")

#print_name2 = start_end_decorator(print_name())

print_name()