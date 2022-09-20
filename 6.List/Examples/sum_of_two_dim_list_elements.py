def sum_lists(two_dim_list):
    list_sum = 0
    for num_list in two_dim_list:
        for num in num_list:
            list_sum += num
    return list_sum


if __name__ == '__main__':
    list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(sum_lists(list_of_lists))
