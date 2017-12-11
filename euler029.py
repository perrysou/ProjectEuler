"""
Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5:

2^2=4, 2^3=8, 2^4=16, 2^5=32
3^2=9, 3^3=27, 3^4=81, 3^5=243
4^2=16, 4^3=64, 4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125

If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by a^b for
2 <= a <= N and 2 <= b <= N?
"""

import math
import random
psorted = []
pset = set()
pfcounts = {}
pf = {}


def getPrimeFactors(n):
    if n not in pfcounts:
        pfcounts[n] = {}
        if n == 1 or n in pset:
            return pfcounts[n]
        n_new = n
        for i in psorted:
            ni = 0
            isFactor = False
            while n_new % i == 0:
                isFactor = True
                ni += 1
                n_new /= i
            if isFactor:
                pfcounts[n][i] = ni
            if n_new == 1:
                break
            if i > math.sqrt(n):
                if n_new != n:
                    pfcounts[n][n_new] = 1
                pset.add(n_new)
                break
    return pfcounts[n]


def sieveofEratosthenes(n):
    nums = range(2, n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i - 2] != 0:
            for j in range(i - 2 + i, n - 2 + 1, i):
                nums[j] = 0
    while nums.count(0):
        nums.remove(0)
    return nums


def distinctPowers(n):
    total = (n - 1)**2
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            if len(getPrimeFactors(a)) == 1 or len(getPrimeFactors(b)) != 0:
                print a, b, a**b
            # print len(getPrimeFactors(b))
    return total


def main():
    # n = long(raw_input().strip())
    # n = random.randint()
    n = 5
    psorted.extend(sieveofEratosthenes(320))
    pset.update(psorted)
    print distinctPowers(n)
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'