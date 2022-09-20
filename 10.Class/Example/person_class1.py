class Person:
    # Create a new instance of Person
    def __init__(self):
        # Person's default values
        self.firstname = "[no first name]"
        self.lastname = "[no last name]"
        self.eye_color = "[no eye color]"
        self.age = -1


if __name__ == "__main__":
    # Creates a person 
    myPerson = Person()
    print(myPerson.firstname)
    print(myPerson.lastname)

