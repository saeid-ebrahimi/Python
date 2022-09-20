

if __name__ == "__main__":
    # Creates myDictionary with sprockets=5, widgets=11, cogs=3, and gizmos=15
    myDictionary = {"sprockets": 5, "widgets": 11, "cogs": 3, "gizmos": 15}
    print(myDictionary)

    # Creates the new key "gadgets" with value 1
    myDictionary["gadgets"] = 1
    print(myDictionary)
    del myDictionary["gadgets"]
    print(myDictionary)

    # Creates myDictionary with David=4045551234, Lucy=4045555678,
    # Vrushali=4045559101
    myDictionary = {"David": "4045551234", "Lucy": "4045555678",
                    "Vrushali": "4045559101"}
    print(myDictionary)

    # Checks if "David" is a key in the dictionary
    if "David" in myDictionary:
        print("David is already in myDictionary!")
        myDictionary["David2"] = "4045551121"
    else:
        myDictionary["David"] = "4045551121"
    print(myDictionary)
    # Dana key doesn't exist so we get KeyError
    print(myDictionary["Dana"])
