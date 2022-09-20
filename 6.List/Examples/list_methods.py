

if __name__ == '__main__':
    # A list of the numbers 1 through 20
    myList = [17, 12, 9, 18, 11, 19, 7, 13, 14, 16, 1, 10, 8, 4, 6, 3, 15, 2, 5, 20]
    print(myList, ": Original list")
    myList.sort()
    print(myList, ": After sorting")
    myList.append(21)
    print(myList, ": After appending 21")
    myOtherList = [26, 22, 23, 24]
    myList.extend(myOtherList)
    print(myList, ": After extending with myOtherList")
    myList.insert(15, 25)
    print(myList, ": After inserting 25 at the index 15")
    myList.remove(26)
    print(myList, ": After removing 26")
    myList.sort()
    print(myList, ": After sorting again")
    myList.reverse()
    print(myList, ": After reversing")
    myList.pop()
    print(myList, ": After popping")
    del myList[-5:]
    print(myList, ": After deleting the last five items")
    print(myList.index(23), ": Index of 23")
    print(myList.count(15), ": Count of 15")
    print(4 in myList, ": 4 in myList")
    print(25 in myList, ": 25 in myList")
