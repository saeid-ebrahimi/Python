

# Defines the class Person
class Person:
    def __init__(self, name, eye_color, age):
        self.name = name
        self.eye_color = eye_color
        self.age = age


# Defines the class Name
class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


if __name__ == "__main__":
    # Creates a person with eye_color "brown", age 30, and
    # a name with firstname "David", lastname "Joyner",
    myPerson = Person(Name("David", "Joyner"), "brown", 30)
    print(myPerson.name.firstname)
    print(myPerson.name.lastname)
    print(myPerson.eye_color)
    print(myPerson.age)
