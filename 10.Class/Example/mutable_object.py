
class Person:
    def __init__(self, name, eye_color, age):
        self.name = name
        self.eye_color = eye_color
        self.age = age


class Name:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


def capitalize_name(name):
    name.firstname = name.firstname.upper()
    name.lastname = name.lastname.upper()


def capitalize_string(in_string):
    in_string = in_string.upper()


if __name__ == "__main__":
    myPerson = Person(Name("David", "Joyner"), "brown", 30)

    capitalize_string(myPerson.name.firstname)
    capitalize_string(myPerson.name.lastname)
    print(myPerson.name.firstname)
    print(myPerson.name.lastname)

    capitalize_name(myPerson.name)
    print(myPerson.name.firstname)
    print(myPerson.name.lastname)
