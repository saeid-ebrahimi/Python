

if __name__ == "__main__":
    my_dictionary = {"rambo": 2.3, "avengers": 5.6, "justice league": 6.35}
    print(my_dictionary)
    my_dictionary["rambo"] = 3.5
    my_dictionary["batman"] = 4.5
    my_dictionary["justice league"] += 1.6
    print(my_dictionary)
    del my_dictionary["batman"]
    print(my_dictionary)
    print(my_dictionary["rambo"])
