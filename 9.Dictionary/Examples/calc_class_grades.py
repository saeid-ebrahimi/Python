

if __name__ == "__main__":
    answer_key = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "A"}

    students = {}
    students["David"] = {"1": "A", "2": "B", "3": "A", "4": "B", "5": "C"}
    students["Terra"] = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "A"}
    students["Catrin"] = {"1": "A", "2": "C", "3": "C", "4": "D", "5": "A"}
    for (name, answers) in students.items():
        grade = 0
        for (question, answer) in answers.items():
            if answer_key[question] == answer:
                grade += 1
        print(name, "grade is :", grade)
        students[name]["grade"] = grade
    print(students)