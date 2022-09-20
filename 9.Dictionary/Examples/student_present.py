def students_present(stu_dict):
    list_of_keys = []
    for (name, value) in stu_dict.items():
        if value == "Present" or value == "Here":
            list_of_keys.append(name)
        else:
            pass
    return list_of_keys


if __name__ == "__main__":
    student_list = {"David": "Here", "Marguerite": "Here",
                    "Jackie": "", "Joshua": "Present",
                    "Erica": "Here", "Daniel": ""}
    print(students_present(student_list))
