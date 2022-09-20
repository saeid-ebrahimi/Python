# Averages each list in in2DList
def two_dim_average_with_pop(in_two_dim_list):
    result = []
    # Repeat until in2DList is empty
    while len(in_two_dim_list) > 0:
        # Remove and assign the last item of in2DList to num_list
        num_list = in_two_dim_list.pop()
        my_sum = 0
        count = 0
        # Repeat until num_list is empty
        while len(num_list) > 0:
            # Remove and save the last item of num_list to number
            number = num_list.pop()
            my_sum += number
            count += 1
        # Insert this average at the beginning of result
        result.insert(0, my_sum / count)
    return result


if __name__ == '__main__':
    my_two_dim_list = [[91, 95, 89, 92, 85],
                       [85, 87, 91, 81, 82],
                       [79, 75, 85, 83, 89],
                       [81, 89, 91, 91, 90],
                       [99, 91, 95, 89, 90]]

    print("Averages:", two_dim_average_with_pop(my_two_dim_list))
    print("my2DList:", my_two_dim_list)
