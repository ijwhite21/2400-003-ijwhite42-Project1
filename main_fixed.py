# Israel White
# 10/2/2023
# 2400 003
# The 1st part of this script will perform the Euclid's Extended Algorith which takes in 2 inputs, and returns
# 2 coefficients for the inputs so that when they are multiplied by the coefficients and added together,
# they equal the greatest common divisor of the 2 numbers.
# The 2nd part will just find the greatest common divisor using the consecutive integer algorithm

# import the math library so we can use the floor function
import math

# Euclid's Algorithm for greatest common divisor "Not Extended"
def gcd(x, y):
    # take absolute value of both numbers so that negative numbers work also
    x = abs(x)
    y = abs(y)
    # make sure the inputs are in descending order
    if y > x:
        x, y = y, x
    # the whole algorithm happens in this while loop
    while x != 0 or y != 0:
        # at any point if x or y = 0 then we just return the other number
        if x == 0:
            return y
        elif y == 0:
            return x
        # if neither number = 0 then we run the loop again using y and x mod y as the inputs
        else:
            x, y = (y, x % y)
    # we can only get to this line of code if both x and y = 0, then it's undefined
    return None

# intermediate formula for finding the "Extended" Algorithm coefficients
# this takes in the arrays from the Extended Algorithm function that form the
# equation 'y = mx + b'. z is the gcd, xi and yi are the original inputs, and nex_x, and neg_y are whether or not
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
            x, y = yy[i-1], x
            xcoef, ycoef=ycoef, ycoef*xx[i-1]+xcoef
            i = i-1
    else:
        xcoef = 0
        ycoef = 1
    # here we need to flip the signs of xi and xcoef if the first input was negative
    if neg_x:
        xi = xi * -1
        xcoef = xcoef * -1
    # here we need to flip the signs of yi and ycoef if the first input was negative
    if neg_y:
        yi = yi * -1
        ycoef = ycoef * -1
    # this prints the output in the form xi(xcoef) + yi(ycoef) = z
    return "{}({}) + {}({}) = {}".format(xi, xcoef, yi, ycoef, z)

# Euclid's "Extended" Algorithm for greatest common divisor
def euclid_extended(x, y):
    # make sure the inputs are in descending order
    if y > x:
        x, y = y, x
    # these booleans will be used when finding the 2 coefficients at the end. If the input we negative
    # the coefficient's sign will need to be flipped
    neg_x = False
    neg_y = False
    # take absolute value of both numbers so that negative numbers work also
    if x < 0:
        x = abs(x)
        # here we keep track of if we needed to flip the sign for when we find the coefficient at the end
        neg_x = True
    if y < 0:
        y = abs(y)
        # here we keep track of if we needed to flip the sign for when we find the coefficient at the end
        neg_y = True
    xi = x
    yi = y
    #These arrays will store each value in the formula y = mx + b
    # used for finding the coefficients
    yy = []
    mm = []
    xx = []
    bb = []


    # the whole Euclid algorithm happens in this while loop
    while x != 0 or y != 0:
        # at any point if x or y = 0 then we just return the other number
        if x == 0:
            # return y
            return formula(yy, mm, xx, bb, y, xi, yi, neg_x, neg_y)
        elif y == 0:
            # return x
            return formula(yy, mm, xx, bb, x, xi, yi, neg_x, neg_y)
        # if neither number = 0 then we run the loop again using y and x mod y as the inputs
        else:
            bb.append(x % y)
            yy.append(x)
            mm.append(y)
            xx.append(-math.floor(x / y))
            x, y = (y, x % y)
    # we can only get to this line of code if both x and y = 0, then it's undefined
    return "Undefined"

# this function will take the smaller of the 2 inputs and check every lower number until it hits the gcd
def consecutive_integer_gcd(x, y):
    # take absolute value of both numbers so that negative numbers work also
    x = abs(x)
    y = abs(y)
    #this is just to preserve the input order for when the results print
    xi = x
    yi = y
    #make sure the 2 inputs are in ascending order
    if y > x:
        x, y = y, x
    # return None if both inputs are 0
    if x == 0 and y == 0:
        return "Undefined"
    # return x if y = 0
    if y == 0:
        s = x
        #this will return the values in the desired format
        return "gcd({}, {}) = {}".format(xi, yi, s)
    #make variable 's' equal to the smaller of the 2 numbers
    s = min(x, y)
    #if s>0 or the remainder of each input divided by s is not 0, subtract 1 from s
    while s > 0 and (x%s != 0 or y%s != 0):
        s = s-1
    #if s is 0 then y is the gcd
    if s == 0:
        s = y
        return "gcd({}, {}) = {}".format(xi, yi, s)
    #if not, then s is the gcd
    else:
        return "gcd({}, {}) = {}".format(xi, yi, s)

# def middle_school_gcd(x, y):
#     return x

if __name__ == '__main__':
    print("-Euclid's Extended Algorithm-")
    print(euclid_extended(int(input("Please type the first integer:")), int(input("Please type the second integer:"))))
    print("-Consecutive Integer Algorithm-")
    print(consecutive_integer_gcd(int(input("Please type the first integer:")),int(input("Please type the second integer:"))))
    input("Press ENTER to quit...")
