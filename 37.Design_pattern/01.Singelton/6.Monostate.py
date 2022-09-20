class Book:
    __shared_state = {'name':'origins'}
    # __dic__ : special attribute to save object states

    def __init__(self):
        self.__pages = 150
        self.__dict__ = self.__shared_state

    def set_pages(self,pages):
        self.__pages = pages

    def get_pages(self): return self.__pages


b1 = Book()
b2 = Book()

b1.set_pages(250)

print("book obj 'b1':",b1)
print("book obj 'b2':",b2)
print("obj state 'b1':",b1.__dict__)
print("obj state 'b2':",b2.__dict__)
b2.set_pages(600)
print("obj state 'b1':",b1.__dict__)
print("obj state 'b2':",b2.__dict__)
print( b1.get_pages())