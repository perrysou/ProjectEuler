"""
"""


import random
import re
import math

maxrecurr = [-1] * (10000 + 1)
lengthofrepetend = [-1] * (10000 + 1)
lengthofrepetend[1] = 0
primes = {2, 3, 5, 7, 11}


def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0 and n != i:
            # lengthofrepetend[n] = -2
            return False
        i += 1
    return True


def getPeriodLength(n):
    if lengthofrepetend[n] == -1:
        npr = n
        while npr % 2 == 0:
            npr /= 2
        while npr % 5 == 0:
            npr /= 5
        if npr != n:
            lengthofrepetend[n] = getPeriodLength(npr)
        else:
            notfound = True
            # if (10**(n - 1) - 1) % n == 0:
            #     lengthofrepetend[n] = n - 1
            #     notfound = False
            mpow = 1
            while notfound:
                if (10**mpow - 1) % n == 0:
                    lengthofrepetend[n] = mpow
                    notfound = False
                mpow += 1
    return lengthofrepetend[n]


def main():
    # t = int(raw_input().strip())
    # t = random.randint(1, 1000)
    t = 1
    k_max = 0
    i_max = 1
    i = 3
    while t:
        # n = long(raw_input().strip())
        # n = long(random.randint(4, 10000))
        n = 5000
        if maxrecurr[n] == -1:
            while i <= n - 1:
                k = getPeriodLength(i)
                if k > k_max:
                    k_max = k
                    i_max = max(i, i_max)
                maxrecurr[i + 1] = i_max
                i += 1
        # print maxrecurr[4:n + 1]
        print lengthofrepetend[n]
        print maxrecurr[n]
        t -= 1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
