class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("Wana make object..")
        else:
            print("already we have object...")

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s0 = Singleton()
s1 = Singleton()
print("object made",Singleton.getInstance())
s2 = Singleton()
s3 = Singleton()