class MyInt(type):
    # call and used for making object from existed class
    def __call__(cls, *args, **kwargs):
        print("Int ijad shode:", args)
        return type.__call__(cls, *args, **kwargs)

class int(metaclass=MyInt):
    def __init__(self,x,y):
        self.x = x
        self.y = y

a = int(20,60)
