

class Person:
    def __init__(self):
        self.firstname = "[unassigned first name]"
        self.lastname = "[unassigned last name]"
        self.eye_color = "[unassigned eye color]"
        self.age = -1


class Student:
    def __init__(self):
        self.person = Person()
        self.student_id = "[unassigned student id]"


if __name__ == '__main__':
    myPerson = Person()

    print(myPerson.firstname)
    print(myPerson.lastname)
    print(myPerson.eye_color)
    print(myPerson.age)
    myPerson.firstname = "David"
    myPerson2 = Person()
    myPerson2.firstname = "Catrin"
    # Print myPerson's firstname
    print(myPerson.firstname)
    print(myPerson2.firstname)
    my_student = Student()
    first_name = my_student.person.firstname
    print(first_name)
