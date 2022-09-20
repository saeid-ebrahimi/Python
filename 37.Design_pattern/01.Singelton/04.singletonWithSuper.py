
class Singleton():
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

s1 = Singleton()
print("obj created ",s1)
s2 = Singleton()
print("obj created ", s2)