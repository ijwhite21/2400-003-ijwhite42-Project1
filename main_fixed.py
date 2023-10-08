# File: main_fixed.py
# Author: Israel White
# Date: 10/2/2023
# Class: 2400 003
# Description: The 1st part of this script will perform the Euclid's Extended Algorith which takes in 2 inputs, and returns
# 2 coefficients for the inputs so that when they are multiplied by the coefficients and added together,
# they equal the greatest common divisor of the 2 numbers.

# The 2nd part will just find the greatest common divisor using the consecutive integer algorithm

# The 3rd part will find the GCD of 2 integers using the middle school procedure

# import the math library so we can use the floor and sqrt functions
import math

# intermediate formula for finding the "Extended" Algorithm coefficients a and b such that ax + by = gcd(x, y)
# this takes in the arrays from the Extended Algorithm function that form the
# equation 'y = mx + b'. z is the gcd, xi and yi are the original inputs, and neg_x, and neg_y (1 or -1) are whether or not
# we had to use abs() on each input (for flipping the sign of the coefficients at the end)
def formula(yy, mm, xx, bb, z, xi, yi, neg_x, neg_y):
    #pop all the input arrays since we don't need the last value in them
    yy.pop()
    mm.pop()
    xx.pop()
    bb.pop()

    # set i to the length of the arrays (they're all the same length)
    if len(yy) > 0:
        # we start at the end of the arrays and iterate to 0
        i = len(yy)-1
        x = yy[i]
        xcoef = 1
        y = mm[i]
        ycoef = xx[i]
        # this will shift all of the values over and adjust the ycoef accordingly.
        # since Euclid's Algorithm turns (x, y) into (y, x % y), we need to do some algebra to shift
        # the values in 'y = mx + b' while not simplifying.
        while i > 0:
            # the following 2 lines of code are where the bulk of the work is done to get these coefficients
            # we are essentially backtracking each iteration in the Euclid's algorithm and simplifying the equations
            # to eventually get 2 coefficients a and b such that ax + by = gcd(x, y)
            x, y = yy[i-1], x
            xcoef, ycoef=ycoef, ycoef*xx[i-1]+xcoef
            i = i-1
    else:
        xcoef = 0
        ycoef = 1

    # this prints the output in the form xi(xcoef) + yi(ycoef) = z
    # also note that we had to take the absolute value of the inputs to find the gcd, here we are finally
    # utilizing the neg_x and neg_y values (1 or -1) to make everything print as the original inputs (as they may have been negative)
    return "{}({}) + {}({}) = {}".format(xi*neg_x, xcoef*neg_x, yi*neg_y, ycoef*neg_y, z)

# Euclid's "Extended" Algorithm for greatest common divisor
# This function will take in 2 integers (input by user) and will use euclid's algorithm to find the GCD
# At the end of the function, it will call the 'formula' function and send every intermediate value found in order
# for the formula function to calculate the 2 coefficients a and b such that ax + by = gcd(x, y)
def euclid_extended(x, y):
    # these variables will be used when finding the 2 coefficients at the end. If the input is negative,
    # the coefficient's sign will need to be flipped
    neg_x = 1
    neg_y = 1
    # take absolute value of both numbers so that negative numbers work also
    if x < 0:
        x = abs(x)
        # here we keep track of if we needed to flip the sign for when we find the coefficient at the end
        neg_x = -1
    if y < 0:
        y = abs(y)
        # here we keep track of if we needed to flip the sign for when we find the coefficient at the end
        neg_y = -1
    # make sure the inputs are in descending order
    if y > x:
        x, y = y, x
        # also swap the negative coefficients so they line up at the end
        neg_x, neg_y = neg_y, neg_x

    # if x is 0 but y isn't, return y as gcd
    if x == 0:
        if y != 0:
            return "{}({}) + {}({}) = {}".format(x, 1, y*neg_y, neg_y, y)
    # if y is 0 but x isn't, return x as gcd
    if y == 0:
        if x != 0:
            return "{}({}) + {}({}) = {}".format(x*neg_x, neg_x, y, 1, x)

    xi = x
    yi = y
    #These arrays will store each value in the formula y = mx + b
    # used for finding the coefficients a and b such that ax + by = gcd(x, y)
    yy = []
    mm = []
    xx = []
    bb = []


    # the whole Euclid algorithm (not extended yet) happens in this while loop
    while x != 0 or y != 0:
        # at any point if x or y = 0 then we just return the other number
        if x == 0:
            # return y
            # here we are sending all of the intermediate values for y = mx + b as lists to the formula function
            # to get the coefficients a and b such that ax + by = gcd(x, y)
            return formula(yy, mm, xx, bb, y, xi, yi, neg_x, neg_y)
        elif y == 0:
            # return x
            # here we are sending all of the intermediate values for y = mx + b as lists to the formula function
            # to get the coefficients a and b such that ax + by = gcd(x, y)
            return formula(yy, mm, xx, bb, x, xi, yi, neg_x, neg_y)
        # if neither number = 0 then we run the loop again using y and x mod y as the inputs
        else:
            # append each value in the equation y = mx + b where y is x, m is y, x is the integer division of x and y
            # essentially and b is the remainder after division. These values will be passed into the formula function
            # and some simple algebra will be applied to reduce down to the 2 needed coefficients
            bb.append(x % y)
            yy.append(x)
            mm.append(y)
            xx.append(-math.floor(x / y))
            x, y = (y, x % y)
    # we can only get to this line of code if both x and y = 0, then it's undefined
    return "Undefined"

# this function will take the smaller of the 2 inputs and check every lower number until it hits the gcd
def consecutive_integer_gcd(x, y):
    neg_x = 1
    neg_y = 1
    # take absolute value of both numbers so that negative numbers work also
    if x < 0:
        x = abs(x)
        neg_x = -1
    if y < 0:
        y = abs(y)
        neg_y = -1
    #this is just to preserve the input order for when the results print
    xi = x
    yi = y
    #make sure the 2 inputs are in ascending order
    if y > x:
        x, y = y, x
        neg_x, neg_y = neg_y, neg_x

    # if x is 0 but y isn't, return y
    if x == 0:
        if y != 0:
            # in the output, neg_y (1 or -1) is multiplied by y to show the user's original input value
            return "GCD({}, {}) = {}".format(x, y*neg_y, y)
    # if y is 0 but x isn't, return x
    if y == 0:
        if x != 0:
            # in the output, neg_x (1 or -1) is multiplied by x to show the user's original input value
            return "GCD({}, {}) = {}".format(x*neg_x, y, x)

    # return undefined if both inputs are 0
    if x == 0 and y == 0:
        return "Undefined"
    # return x if y = 0
    if y == 0:
        s = x
        #this will return the values in the desired format
        return "gcd({}, {}) = {}".format(xi*neg_x, yi, s)
    #make variable 's' equal to the smaller of the 2 numbers
    s = min(x, y)
    #if s>0 or the remainder of each input divided by s is not 0, subtract 1 from s
    while s > 0 and (x%s != 0 or y%s != 0):
        s = s-1
    #if s is 0 then y is the gcd
    if s == 0:
        s = y
        # in the output, neg_x and neg_y (1 or -1) are multiplied by x and y respectively to show the user's original input values
        return "gcd({}, {}) = {}".format(xi*neg_x, yi*neg_y, s)
    #if not, then s is the gcd
    else:
        # in the output, neg_x and neg_y (1 or -1) are multiplied by x and y respectively to show the user's original input values
        return "gcd({}, {}) = {}".format(xi*neg_x, yi*neg_y, s)

# this function checks if a number x is prime
def is_prime(x):
    # iterate from 2 to the square root of the input + 1
    for i in range(2, math.floor(math.sqrt(x))+1):
        # if the input is divisible by any number with no remainder, return False
        if x % i == 0:
            return False
    # if it hasn't returned False up to this point, then return True
    return True

# this function will find the prime factorization of an input x
def prime_factorization(x):
    # this list name 'factors' holds all the factors. 1 is a factor of all numbers
    factors = [1]
    # while x is even, add 2 to the factors list and divide by 2
    # check if x is even
    while x % 2 == 0:
        # if so, add 2 to the factors list
        factors.append(2)
        # divide x by 2
        x = x / 2
    # now checking by 2's, iterate from 3 to sqrt(x) + 1
    # this is checking odd numbers
    for i in range(3, int(math.sqrt(x))+1, 2):
        # check if x is divisible y i
        while x % i == 0:
            # if so, add i to the list
            factors.append(int(i))
            # divide x by i
            x = x / i
    # if x is larger than 2, add to the list
    if x > 2:
        factors.append(int(x))
    # this outputs the list of prime factors
    return factors

# This function will take in 2 lists and output a list of all common values (including duplicates) between the 2 lists
def matching_factors(x: list, y: list):
    # z is the output list
    z = []
    # iterate through the first list x, then compare each element against each element of the 2nd list y
    # if a match is found, push the element onto z and pop y. also break the inner loop
    for i in range(len(x)):
        for j in range(len(y)):
            if y[j] == x[i]:
                z.append(y[j])
                y.pop(j)
                break
    # by this point we have all the common factors in the z list so we output them
    return z

# middle school procedure for finding the gcd of 2 integers
def middle_school_gcd(x, y):
    # if both are 0, return undefined
    if x == 0 and y == 0:
        return "Undefined"

    # these coefficients will preserve the inputs for the end as they cannot be negative while finding the gcd
    neg_x = 1
    neg_y = 1

    # take absolute value of x and y
    if x < 0:
        x = abs(x)
        # if x was negative, neg_x will keep track of that
        neg_x = -1
    if y < 0:
        y = abs(y)
        # if y was negative, neg_y will keep track of that
        neg_y = -1

    # if x is 0 but y isn't, return y
    if x == 0:
        if y != 0:
            return "GCD({}, {}) = {}".format(x, y*neg_y, y)
    # if y is 0 but x isn't, return x
    if y == 0:
        if x != 0:
            return "GCD({}, {}) = {}".format(x*neg_x, y, x)

    # put x and y in descending order
    if y > x:
        x, y = y, x
        # if we swap x and y, we need to swap neg_x and neg_y
        neg_x, neg_y = neg_y, neg_x

    # call the prime_factorization function to get the prime factors of x
    x_primes = prime_factorization(x)
    # call the prime_factorization function to get the prime factors of y
    y_primes = prime_factorization(y)

    # call the matching_factors function to get the matching factors of x and y
    common_factors = matching_factors(x_primes, y_primes)

    # z is the actual gcd of x and y (or will be at the end)
    z = 1
    # this will multiply all the matching factors of x and y together
    for i in common_factors:
        z = z * i

    # this prints the format GCD(x, y) = z
    # neg_x and neg_y (1 or -1) are multiplied to
    return "GCD({}, {}) = {}".format(x*neg_x, y*neg_y, z)

# in main, we will print each algorithm's title, then take in 2 inputs for each (from the user) and print the respective outputs
if __name__ == '__main__':
    # Euclid's Extended Algorithm (taking 2 inputs from the user)
    print("-Euclid's Extended Algorithm-")
    print(euclid_extended(int(input("Please type the first integer:")), int(input("Please type the second integer:"))))
    # Consecutive Integer Algorithm (this will take 2 inputs from the user)
    print("-Consecutive Integer Algorithm-")
    print(consecutive_integer_gcd(int(input("Please type the first integer:")),int(input("Please type the second integer:"))))
    # Middle School GCD (this will take 2 inputs from the user)
    print("-Middle School GCD-")
    print(middle_school_gcd(int(input("Please type the first integer:")), int(input("Please type the second integer:"))))
    # require the user to press ENTER to close the program
    input("Press ENTER to quit...")
