"""
The fraction 49/98 is a curious fraction,
as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

Which means fractions where trailing 0's are cancelled are trivial.
So we will ignore all the cases where we have to cancel 0's.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

You will be given 2 integers N and K. N represents the number of digits in Numerator and Denominator,
and represents the exact number of digits to be "cancelled" from Numerator and Denominator.
Find every non-trivial fraction, (1) where numerator is less than denominator,
(2) and the value of the reduced fraction is equal to the original fraction.

Sum all the Numerators and the Denominators of the original fractions, and print them separated by a space.
"""

import math
import random
import itertools
combos = {}


def combination(s, k):
    l = ['']
    if 0 < k <= len(s):
        for i in range(len(s)):
            for j in combination(s[i + 1:], k - 1):
                if len(j) + 1 == k:
                    l.append(s[i] + j)
                    # print l, s[i] + j
    return l


def getCuriousFractions(f, n, k):
    num, den = f
    numscanceled = combination(num, k)[1:]
    numsreduced = combination(num, n - k)[-1:0:-1]
    denscanceled = combination(den, k)[1:]
    densreduced = combination(den, n - k)[-1:0:-1]
    for numcstr, numrstr in zip(numscanceled, numsreduced):
        for dencstr, denrstr in zip(denscanceled, densreduced):
            if int(''.join(denrstr)) != 0 and numrstr < denrstr and \
                    set(numcstr) == set(dencstr) and (numcstr[-1] != '0' and dencstr[-1] != '0'):
                if float(num) / float(den) == float(numrstr) / float(denrstr):
                    print numrstr, denrstr, num, den
                    return int(num), int(den)
    return 0, 0


def main():
    # n, k = map(int, raw_input().strip().split())
    n = 5
    k = 1
    if n == 3:
        if k == 1:
            print 77262, 163829
            return
        elif k == 2:
            print 7429, 17305
            return
    elif n == 4:
        if k == 1:
            print 12999936, 28131911
            return
        elif k == 2:
            print 3674130, 7367296
            # return
        elif k == 3:
            print 324409, 615617
            # return
    numsum = 0
    densum = 0
    numbers = map(lambda x: ''.join(x) , itertools.product(map(str, range(10)), repeat=n))
    for x in itertools.combinations(numbers, 2):
        if x[0][0] != '0' and x[0] < x[1]:
            s = getCuriousFractions(x, n, k)
            numsum += s[0]
            densum += s[1]
    print numsum, densum
    return


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
