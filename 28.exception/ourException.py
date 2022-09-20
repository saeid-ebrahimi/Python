class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = massage
        self.value = value

    
def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too low", x)
try:
    test_value(200) 
except ValueTooHighError as ex:
    print(ex)
except ValueTooSmallError as ex:
    print(ex.message)
    print(ex.value)