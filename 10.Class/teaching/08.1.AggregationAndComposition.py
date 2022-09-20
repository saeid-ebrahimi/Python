class Hand:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_width(self): return self.__width

    def get_height(self): return self.__length

    def __str__(self):
        st = f"hand length is {self.__length} and its width is {self.__width}"
        return st


class Sword:
    def __init__(self, length, power):
        self.__length = length
        self.__power = power

    def get_length(self): return self.__length

    def get_power(self): return self.__power

    def __str__(self):
        st = f"sword length is {self.__length} and its power is {self.__power}"
        return st


class Person:
    def __init__(self, name, age, length, width, sword):
        self.__name = name
        self.__age = age
        self.__hand = Hand(length, width)
        self.__sword = sword

    def get_hand(self): return self.__hand

    def get_sword(self): return self.__sword

    def __str__(self):
        st2 = f"my name is {self.__name}, I'm {self.__age} years old. I have a hand and  {self.__hand.__str__()}. I got a sword, {self.__sword}"
        return st2


s = Sword(50,20)
p1 = Person("ali", 15, 14, 18,s)
print(p1.get_hand().get_width())
print(p1.get_sword().get_length())
print(p1)
del p1
print(s)