

if __name__ == "__main__":
    ta_info = [("Joshua", "Georgia"),
               ("Jackie", "Vermont"),
               ("Marguerite", "Tennessee")]
    my_dictionary = {"Joshua": "Georgia", "Jackie": "Vermont",
                     "Marguerite": "Tennessee"}
    print(my_dictionary)
    my_dictionary2 = {}
    for my_tuple in ta_info:
        for i in range(0, len(my_tuple), 2):
            my_dictionary2[my_tuple[i]] = my_tuple[i+1]
    print(my_dictionary2)
    josh_val = my_dictionary["Joshua"]
    jack_val = my_dictionary["Jackie"]
    marg_val = my_dictionary["Marguerite"]
    print(josh_val)
    print(jack_val)
    print(marg_val)
