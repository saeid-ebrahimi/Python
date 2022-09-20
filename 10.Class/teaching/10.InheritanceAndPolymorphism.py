class Animal:
    def __init__(self,eye_color,eye_size,body_size):
        self._eye_color=eye_color
        self._eye_size=eye_size
        self._body_size=body_size

    def __str__(self):
        st=f"eye_size: {self._eye_size},eye_color:{self._eye_color},body_size:{self._body_size}"
        return st

    def move(self):
        return 'moving'

class Pestandar(Animal):
    def __init__(self,eye_color,eye_size,body_size,hand,leg):
        self._leg=leg
        self._hand=hand
        Animal.__init__(self,eye_color,eye_size,body_size)

    def get_eye_color(self):return self._eye_color
    def get_eye_size(self):return self._eye_size
    def get_body_size(self):return self._body_size
    def get_hand(self):return self._hand
    def get_leg(self):return self._leg
    def roam(self):return "roaming"
    def __str__(self):
        st1 = Animal.__str__(self)
        st2= f"hand:{self._hand},leg{self._leg}"
        return st1+st2
class Human(Pestandar):
    def __init__(self,eye_color,eye_size,body_size,hand,leg,decide):
        self._decide=decide
        Pestandar.__init__(self,eye_color,eye_size,body_size,hand,leg)
    def roam(self):
        return "walking"
    def cook(self):
        return "cooking"
    def __str__(self):
        st=f"decide:{self._decide}"
        st2=Pestandar.__str__(self)
        return st2+st

class Person:

    def __init__(self,firstname,lastname,age):
        self._firstname = firstname
        self._lastname = lastname
        self._age = age
    def __str__(self):
        st=f"firstname:{self._firstname},lastname:{self._lastname},age:{self._age}"
        return st
class Student(Person,Human):
    def __init__(self,firstname,lastname,age,eye_color,eye_size,body_size,hand,leg,decide,id):
        self._id=id
        Person.__init__(self,firstname,lastname,age)
        Human.__init__(self,eye_color,eye_size,body_size,hand,leg,decide)
    def __str__(self):
        st=f"id:{self._id}"
        st1=Person.__str__(self)
        st2=Human.__str__(self)
        return st+st1+st2
    def attend(self):
        return "attending in class"









p=Pestandar('blue',2,50,2,2)
print(p)
print(p.move())
print(p.roam())
h=Human('gray',3,200,2,2,75)
print(h)
print(h.roam())
s=Student('ramin','ranaii',20,'brown',3,184,2,2,85,234561)
print(s)
