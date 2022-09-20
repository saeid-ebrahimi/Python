import functools
def start_end_decorator(func):
    @functools.wraps(func)
    def warpper(*args, **kwargs):
        print("start of it:")
        r = func(*args,**kwargs)
        print("end of it:")
        return r
    return warpper

@start_end_decorator
def add5(x):
    return x+5

result = add5(13)
print(result)
print()
print(help(add5))
print(add5.__name__)