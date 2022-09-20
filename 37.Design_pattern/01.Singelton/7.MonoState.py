class Book:
    __shared_state = {}
    # args helps us to add any new attribute
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


b1 = Book()
b2 = Book()
b3 = Book()
b1.pages = 200
b2.color = "colorful"
b2.pages = 400
b3.size = 30
print("book obj 'b1':",b1)
print("book obj 'b2':",b2)
print("book obj 'b3':",b3)
print("obj state 'b1':",b1.__dict__)
print("obj state 'b2':",b2.__dict__)
print("obj state 'b3':",b3.__dict__)