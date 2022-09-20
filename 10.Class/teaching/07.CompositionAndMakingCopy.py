
class Person:
    def __init__(self, firstname, lastname, eye_color, age):
        self.__name = Name(firstname,lastname)
        self.__eye_color = eye_color
        self.__age = age


    def copy(self):
        return Person(self.__name.get_first_name(), self.__name.get_last_name(),self.__eye_color, self.__age)
        
    def set_age(self,age): self.__age=age
    def get_name(self): return self.__name
    def get_eye_color(self): return self.__eye_color
    def get_age(self): return self.__age
    def __copy__(self):
        return Person(self.__name.get_first_name(), self.__name.get_last_name(),self.__eye_color,self.__age)
    def __deepcopy__(self):
        return Person(self.__name.get_first_name(), self.__name.get_last_name(),self.__eye_color, self.__age)
    def __str__(self):
        s = f"""{self.__name.__str__()}
        eye color: {self.__eye_color}
        age: {self.__age}"""
        return s

class Name:
    def __init__(self, firstname, lastname):
        self.__firstname = firstname
        self.__lastname = lastname
    
    def copy(self, other):
        if isinstance(Name,other):
            self.__firstname = other.get_firstname()
            self.__lastname = other.get_lastname()
        elif other == None:
            self.__firstname = "[unassigned]"
            self.__lastname = "[unassigned]"
        else:
            print("invalid type")
    
    def get_first_name(self): return self.__firstname
    def get_last_name(self): return self.__lastname
    def __copy__(self):
        return Name(self.get_first_name(),self.get_last_name())

    def __deepcopy__(self):
        return Name ( self.get_first_name () , self.get_last_name () )

    def __str__(self):
        s = f"""first name: {self.__firstname}
        last name: {self.__lastname}"""
        return s

from copy import *
if __name__ == "__main__":
    myPerson1 = Person("David", "Joyner", "brown", 30)
    myPerson2 = myPerson1
    # make actual copy
    myPerson3 = Person(myPerson1.get_name().get_first_name(), myPerson1.get_name().get_last_name(),
     myPerson1.get_eye_color(), myPerson1.get_age())
    myPerson4 = myPerson1.copy()
    myPerson5 = copy(myPerson1)
    myPerson1.set_age(18)
    print(myPerson1)
    print(myPerson2)
    print(myPerson3)
    print(myPerson4)
    print(myPerson5)