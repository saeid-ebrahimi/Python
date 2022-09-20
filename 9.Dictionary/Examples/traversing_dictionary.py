

if __name__ == "__main__":
    # Creates myDictionary with sprockets=5, widgets=11, cogs=3, gizmos=15,
    # gadgets=1
    myDictionary = {"sprockets": 5, "widgets": 11, "cogs": 3, "gizmos": 15,
                    "gadgets": 1}
    for value in myDictionary.values():
        if value < 5:
            print("A value less than 5 was found:", value)

    for key in myDictionary.keys():
        value = myDictionary[key]
        if value < 5:
            print(key, "is less than 5:", value)

    for key in myDictionary:
        value = myDictionary[key]
        if value < 5:
            print(key, "is less than 5:", value)

    for (key, value) in myDictionary.items():
        if value < 5:
            print(key, "is less than 5:", value)


