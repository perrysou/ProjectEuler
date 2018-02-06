"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through N pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import math
import random
import itertools

uniques = {}


def getPandigital(n):
    if n == 4:
        xand = [0]
        xer = [1]
        prod = [2]
    elif n == 5:
        xand = [0]
        xer = [1]
        prod = [3]
    elif n == 6:
        xand = [0]
        xer = [1]
        prod = [3]
    elif n == 7:
        xand = [0, 0]
        xer = [1, 2]
        prod = [4, 4]
    elif n == 8:
        xand = [0, 0]
        xer = [1, 2]
        prod = [4, 4]
    elif n == 9:
        xand = [0, 0]
        xer = [1, 2]
        prod = [5, 5]
    sums = 0
    for i in range(len(xand)):
        for p in itertools.permutations(range(1, n + 1)):
            mand = mer = pro = 0
            for j, d in enumerate(p[xand[i]:xer[i]][::-1]):
                mand += d * 10**j
            for j, d in enumerate(p[xer[i]:prod[i]][::-1]):
                mer += d * 10 ** j
            for j, d in enumerate(p[prod[i]:][::-1]):
                pro += d * 10 ** j
            if mand * mer == pro:
                if pro not in uniques:
                    uniques[pro] = n
                    sums += pro
    return sums


def main():
    n = long(raw_input().strip())
    # n = random.randint(9, 9)
    print getPandigital(n)


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
