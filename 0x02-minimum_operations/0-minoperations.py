#!/usr/bin/env python3

def minOperations(n):
    """
    # check if n is less than or equal to 1
    # return 0
    # create a list to store the factors
    # loop through the range of 2 to n
    # check if n is divisible by i
    # append i to the list of factors
    # return the sum of the factors
    """
    if n <= 1:
        return 0
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n = n / i
    return sum(factors)