import math

# Euclid's Algorithm for greatest common divisor "Not Extended"
def gcd(x, y):
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

#intermediate formula for finding the "Extended" Algorithm coefficients
def formula(yy, mm, xx, bb, z, xi, yi):
    yy.pop()
    mm.pop()
    xx.pop()
    bb.pop()
    # print(yy, mm, xx, bb)

    # set i to the length of the arrays (they're all the same length)
    if len(yy) > 0:
        i = len(yy)-1
        x = yy[i]
        xcoef = 1
        y = mm[i]
        ycoef = xx[i]
        # print("{}({})+{}({})".format(x, xcoef, y, ycoef))
        while i > 0:
            x, y = yy[i-1], x
            xcoef, ycoef=ycoef, ycoef*xx[i-1]+xcoef
            # print("{}({})+{}({})".format(x,xcoef,y,ycoef))
            i = i-1
    else:
        xcoef = 0
        ycoef = 1
    # print(xcoef, ycoef)
    # return xcoef, ycoef
    return "{}({}) + {}({}) = {}".format(xi, xcoef, yi, ycoef, z)

# Euclid's "Extended" Algorithm for greatest common divisor
def euclid_extended(x, y):
    # undefined for negative numbers
    if x < 0 or y < 0:
        return "Undefined"
    xi = x
    yi = y
    #These arrays will store each value in the formula y = mx + b
    # used for finding the coefficients
    yy = []
    mm = []
    xx = []
    bb = []

    # make sure the inputs are in descending order
    if y > x:
        x, y = y, x
    # the whole Euclid algorithm happens in this while loop
    while x != 0 or y != 0:
        # at any point if x or y = 0 then we just return the other number
        if x == 0:
            # return y
            return formula(yy, mm, xx, bb, y, xi, yi)
        elif y == 0:
            # return x
            return formula(yy, mm, xx, bb, x, xi, yi)
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
    # undefined for negative numbers
    if x < 0 or y < 0:
        return "Undefined"
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
    # print(gcd(31415, 14142))
    # print(consecutive_integer_gcd(31415, 14142))
    print("-Euclid's Extended Algorithm-")
    print(euclid_extended(int(input("Please type the first integer:")), int(input("Please type the second integer:"))))
    print("-Consecutive Integer Algorithm-")
    print(consecutive_integer_gcd(int(input("Please type the first integer:")),int(input("Please type the second integer:"))))
