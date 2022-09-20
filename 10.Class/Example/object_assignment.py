

class Person:
    def __init__(self, name, eyecolor, age):
        self.name = name
        self.eye_color = eyecolor
        self.age = age


class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


if __name__ == "__main__":
    myPerson1 = Person(Name("David", "Joyner"), "brown", 30)
    myPerson2 = myPerson1
    myPerson2.eye_color = "blue"
    print("myPerson1's eye color: " + myPerson1.eye_color)
    print("myPerson2's eye color: " + myPerson2.eye_color)



