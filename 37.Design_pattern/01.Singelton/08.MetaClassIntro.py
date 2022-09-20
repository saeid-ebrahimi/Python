'''
a = 50
print(type(a))
# int metaclass is type
print(type(int))
'''

class A(object):
    def my_func(self):
        pass

def my_func():
    pass

A_name = "A"
A_parents = (object,)
A_methods = {'my_func': my_func}

type(A_name,A_parents,A_methods)