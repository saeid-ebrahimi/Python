def start_end_decorator(func):

    def warpper():
        print("start of it:")
        func()
        print("end of it:")
    return warpper

def print_name():
    print("hello alex")

print_name2 = start_end_decorator(print_name())

