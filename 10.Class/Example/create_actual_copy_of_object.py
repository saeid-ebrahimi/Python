
class Person:
    def __init__(self, name, eye_color, age):
        self.name = name
        self.eye_color = eye_color
        self.age = age


class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


if __name__ == "__main__":
    myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
    myPerson2 = Person(myPerson1.name, myPerson1.eye_color, myPerson1.age)
    myPerson2.eye_color = "blue"
    print(myPerson1.eye_color)
    print(myPerson2.eye_color)
    myPerson2.name.firstname = "Catrin"
    print(myPerson1.name.firstname)
    print(myPerson2.name.firstname)

    myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
    myPerson2 = Person(Name(myPerson1.name.firstname, myPerson1.name.lastname),
                       myPerson1.eye_color, myPerson1.age)
    myPerson2.eye_color = "blue"
    print(myPerson1.eye_color)
    print(myPerson2.eye_color)
    myPerson2.name.firstname = "Catrin"
    print(myPerson1.name.firstname)
    print(myPerson2.name.firstname)
