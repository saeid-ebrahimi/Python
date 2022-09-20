def name_counts(my_list):
    my_dict = {}
    for full_name in my_list:
        first_name = full_name.split()[0]
        if first_name not in my_dict:
            my_dict[first_name] = 0
        my_dict[first_name] += 1
    return my_dict


if __name__ == "__main__":
    name_list = ["David Joyner", "David Zuber", "Brenton Joyner",
                  "Brenton Zuber", "Nicol Barthel", "Shelba Barthel",
                  "Shelba Crowley", "Shelba Fernald", "Shelba Odle",
                  "Shelba Fry", "Maren Fry"]
    print(name_counts(name_list))