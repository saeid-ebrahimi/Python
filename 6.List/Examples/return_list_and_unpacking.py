

# Returns a list containing the quotient and remainder
def quotient_and_remainder(dividend, divisor):
    return [dividend // divisor, dividend % divisor]


if __name__ == '__main__':
    myDividend = 11
    myDivisor = 4
    # Assigns the first value of the result to myQuotient and the
    # second to myRemainder
    [myQuotient, myRemainder] = quotient_and_remainder(myDividend, myDivisor)

    print("Quotient:", myQuotient)
    print("Remainder:", myRemainder)
