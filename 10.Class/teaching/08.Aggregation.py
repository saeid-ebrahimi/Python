

class Person:
    def __init__(self, name:str, age:int, father=None, mother=None):
        assert isinstance(name,str), f"name type is {type(name)} and should be str"
        assert isinstance(age, int), f"age type is {type(age)} and should be int"
        assert age>=0,f"age {age} is not greater than 0"
        assert isinstance(father, Person) or father==None, f"father object {father} is not a Person instance"
        assert isinstance(mother, Person) or mother == None, f"mother object {mother} is not a Person instance"
        self.__name = name
        self.__age = age
        self.__father = father
        self.__mother = mother

    def set_age(self,age): self.__age=age
    def get_name(self): return self.__name
    def get_age(self): return self.__age
    def get_father(self): return self.__father
    def get_mother(self): return self.__mother
    def __copy__(self):
        return Person(self.__name.get_first_name(), self.__name.get_last_name(),self.__eye_color,self.__age)
    def __deepcopy__(self):
        return Person(self.__name.get_first_name(), self.__name.get_last_name(),self.__eye_color, self.__age)
    def __str__(self):
        s = f"""{self.__name}
        age: {self.__age}
        father: {self.__father}
        mother: {self.__mother}"""
        return s

import datetime

if __name__ == "__main__":
    # Write your code here!
    father_p = Person("Mr. Burdell", 58)
    mother_p = Person("Mrs. Burdell", 53)
    george_p = Person("George P. Burdell", 25, father_p, mother_p)
    print(george_p)
    print(george_p)
    print(george_p)
