"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math
import copy


# check if n (n>=2) is a prime number
def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        else:
            i += 1
            continue
    return True


def getPrimeFactors(n):
    # a dictionary {prime#1 : count1, prime#2: count2, ...}, 2 <= prime#i <= n
    primeCount = {}
    # every integer x (x <= n) in the sequence
    for x in range(2, n + 1):
        if isPrime(x):
            primeCount[x] = 1  # first appearance of a prime#, add to the dictionary
        else:
            # loop through prime numbers i in the dictionary (i <= x)
            for i in primeCount.iterkeys():
                temp = 0
                while x % i == 0:
                    temp += 1
                    x /= i
                # keep increasing the counter for i until x is not divisible by i
                else:
                    primeCount[i] = max(temp, primeCount[i])  # update the counter in the dictionary
                    continue
    return primeCount


def main():
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        primeCount = getPrimeFactors(n)
        product = 1
        for p in primeCount.iterkeys():
            product *= p ** primeCount[p]
        print product

if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
