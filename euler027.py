"""
Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39.

However, when n = 40, 40^2 + 40 + 41 is divisible by 41,
and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula n^2 - 79n + 1601 was discovered,
which produces primes for the consecutive values 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b where |a| <= N and |b| <= N

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

Note For this challenge you can assume solution to be unique.

"""

import math
import random
NMAX = 2000
NMIN = 42
maxChain = [-1] * (NMAX + 1)
combos = {(1, 41)}
Primes = {2, 3, 5, 7}
psorted = []


def isPrime(n):
    if n < 2:
        return False
    if n in Primes:
        return True

    q = True
    for i in psorted:
        if i <= math.sqrt(n) and n % i == 0:
            q = False
            break
    if q:
        Primes.add(n)
    return q


def sieveofEratosthenes(n):
    nums = range(2, n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if nums[i - 2] != 0:
            for j in range(i - 2 + i, n - 2 + 1, i):
                nums[j] = 0
    while nums.count(0):
        nums.remove(0)
    return nums


def main():
    N = long(raw_input().strip())
    # N = random.randint(NMIN, NMAX)
    # N = 2000
    psorted.extend(sieveofEratosthenes(N))
    Primes.update(psorted)
    ii = N
    i_old = 0
    for a in range(-ii, ii + 1):
        for b in range(-ii, ii + 1):
            if a % 2 != 0 and b % 2 != 0:
                isValid = True
                i = 0
                while isValid:
                    p = i**2 + a * i + b
                    if isPrime(p):
                        i += 1
                    else:
                        isValid = False
                        if i > i_old:
                            maxChain[ii] = (a, b, i)
                            i_old = i
    print maxChain[N][0], maxChain[N][1]
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
