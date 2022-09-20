class SigletonObject(object):
    class __SingletonObject:
        def __init__(self):
            self.val = None 

        def __str__(self):
            return "{0!r} {1}".format(self,self.val)

    instance = None

    @classmethod
    def __new__(cls): 
        if not SigletonObject.instance:
            SigletonObject.instance = SigletonObject.__SingletonObject()
        return SigletonObject.instance

    def __getattribute__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)





obj1 = SigletonObject
obj1.val  =" Obj value 1"
print("printing obj1:",obj1)

obj2 = SigletonObject
obj2.val = "Obj value 2"
print("printing obj1:",obj1)
print("printing obj2:",obj2)