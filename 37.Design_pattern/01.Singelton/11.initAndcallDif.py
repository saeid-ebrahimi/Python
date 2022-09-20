class A:
    def __init__(self):
        print("init")
    def __call__(self):
        print("call")


a = A()
print()
a()

class B:
    def __init__(self, x, y, z):
        print("init")

b = B(3,5,9)
# print(b(1,4,6)) __call__ called

class C:
    def __call__(self, x, y, z):
        print("call")


# c = C(2,6,8) # __init__ called
c = C() # default __init__ called
print(c(5,99,88))