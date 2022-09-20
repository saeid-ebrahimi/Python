# Averages the numbers in a list
# Averages each list in in2DList
def two_dim_average(in_two_dim_list):
    result = []
    # For each list in the list of lists
    for numList in in_two_dim_list:
        list_num = 0
        # For each number in the current list
        for number in numList:
            list_num += number
        # Append this list's average to result
        result.append(list_num / len(numList))
    return result


if __name__ == '__main__':
    my_two_dim_List = [[91, 95, 89, 92, 85],
                       [85, 87, 91, 81, 82],
                       [79, 75, 85, 83, 89],
                       [81, 89, 91, 91, 90],
                       [99, 91, 95, 89, 90]]
    print("Averages:", two_dim_average(my_two_dim_List))
