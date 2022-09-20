class MetaSingleton(type):
    __instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super().__call__(*args,**kwargs)
        return cls.__instance[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1,logger2)