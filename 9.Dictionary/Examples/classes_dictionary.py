

if __name__ == "__main__":
    classes = {"Math": ["David", "Lucy", "Dana"],
               "Physics": ["Addison", "Vrushali", "Bilbo"],
               "Chemistry": ["Sara", "Lugos", "Mireia", "Perle"],
               "Computing": ["Partha", "Venijamin", "Terra", "Sofia"],
               "History": ["Tryphon", "Gevorg", "Raza", "Rein"]}

    print("Students in Computing:", classes["Computing"])
    # Add Francis to History
    classes["History"].append("Francis")
    print("Students in History:", classes["History"])

