

class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother


if __name__ == "__main__":
    # Write your code here!
    father_p = Person("Mr. Burdell", 53)
    mother_p = Person("Mrs. Burdell", 53)
    george_p = Person("George P. Burdell", 25, father_p, mother_p)

    print(george_p.name)
    print(george_p.mother.name)
    print(george_p.father.name)
