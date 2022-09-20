from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person1.fromBirthYear('ali',2001)
person2 = Person.fromBirthYear('mayank', 1996)
print (person1.age)
print (person2.age)
print (Person.isAdult(22))
