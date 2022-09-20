
# Define the class Person
class Person:
    # Create a new instance of Person
    def __init__(self, firstname="[no first name]", lastname="[no last name"):
        self.firstname = firstname
        self.lastname = lastname
        self.eye_color = "[no eye color]"
        self.age = -1


if __name__ == "__main__":
    myPerson1 = Person()
    print(myPerson1.firstname)
    myPerson2 = Person(firstname="David")
    print(myPerson2.firstname)
    myPerson3 = Person("Catrin")
    print(myPerson3.firstname)
    my_person4 = Person("David", "Joyner")
