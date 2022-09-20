def quotient_and_remainder(dividend, divisor):
    # Returns the tuple of the quotient and remainder
    return dividend // divisor, dividend % divisor


if __name__ == '__main__':
    myTuple1 = (1, 2, 3)
    myTuple2 = (4, 5, 6)
    myTuple3 = (7, 8, 9)

    mySuperTuple = (myTuple1, myTuple2, myTuple3)

    print(mySuperTuple)
    mySuperTuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

    print(mySuperTuple)
    myTuple1 = (1, 2, 3)
    myTuple2 = (4, 5, 6)
    myTuple3 = (7, 8, 9)

    mySuperTuple = (myTuple1, myTuple2, myTuple3)

    # Prints the first item of the second tuple
    print(mySuperTuple[1][0])

    # Returns a tuple containing the quotient and remainder
    myDividend = 11
    myDivisor = 4
    # Assigns the first value of the result to myQuotient and
    # the second to myRemainder
    (myQuotient, myRemainder) = quotient_and_remainder(myDividend, myDivisor)

    print("Quotient:", myQuotient)
    print("Remainder:", myRemainder)
