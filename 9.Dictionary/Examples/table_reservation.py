

if __name__ == "__main__":
    seatingChart = {"David": 3, "Lucy": 3, "Dana": 2,
                    "Addison": 2, "Vrushali": 1, "Bilbo": 3,
                    "Sara": 1, "Lugos": 1, "Mireia": 1,
                    "Partha": 2, "Venijamin": 1, "Terra": 2,
                    "Tryphon": 3, "Gevorg": 1, "Raza": 3,
                    "Rein": 3, "Sofia": 2, "Perle": 2}

    for (name, table_number) in seatingChart.items():
        print(name, "seating at table #", table_number)
    print()
    for i in range(1, 4):
        print("table #", i, " is reserved for:", sep="", end=" ")
        for (name, table) in seatingChart.items():
            if table == i:
                print(name, end=", ")
        print()
    print()