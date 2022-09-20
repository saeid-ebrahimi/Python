

class Name:
    def __init__(self) :
        self.firstname = "[no first name]"
        self.lastname = "[no last name]"


if __name__ == "__main__":
    # Define the class Name

    # Define dictionaries with keys firstname and lastname
    myNameDict = {"firstname": "David", "lastname": "Joyner"}

    # Define instances of Name
    myNameInst = Name()
    myNameInst.firstname = "David"
    myNameInst.lastname = "Joyner"

    print("Dictionary: " + myNameDict["firstname"])
    print("Instance: " + myNameInst.firstname)


